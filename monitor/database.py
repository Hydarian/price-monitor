import sqlite3

class MonitorPriceDatabase:
    def __init__(self, db_path="monitor.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        self.creating_table_products()
        self.creating_price_table()


    def price_change(self, url):
        """
            Returns the price difference and percentage change
            compared to the previous price.
        """
        
        self.cursor.execute(
            "SELECT id FROM products WHERE url = ?",
            (url,)
        )

        product_id = self.cursor.fetchone()

        if product_id is None:
            return None

        self.cursor.execute("""
        SELECT price
        FROM prices
        WHERE product_id = ?
        ORDER BY id DESC
        LIMIT 2
        """, (product_id[0],))

        rows = self.cursor.fetchall()

        if len(rows) < 2:
            return None
        else:
            old_price = rows[1][0]
            new_price = rows[0][0]
            if old_price == 0:
                return None
            difference = new_price - old_price
            percent = (difference / old_price) * 100
            return difference, percent


    def creating_table_products(self):
        '''
            create the table and check if exist or not.
        '''

        table_creation_query = '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE
        );
        '''

        self.cursor.execute(table_creation_query)
        self.connection.commit()


    def creating_price_table(self):
        table_creation_query = '''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(id)
        );
        '''

        self.cursor.execute(table_creation_query)
        self.connection.commit()


    def saving_data_products(self, url, title):
        '''
            Save a product to the database.

            If the product already exists, no new record is inserted.

            Args:
                url: product url
                title: product title
        '''
        self.cursor.execute(
            "SELECT id FROM products WHERE url = ?",
            (url,)
        )

        product = self.cursor.fetchone()

        if product is None:
            self.cursor.execute('INSERT INTO products (title, url) VALUES (?, ?)',
                                (title, url)
                                )

        self.connection.commit()


    def saving_price_data(self, url, price):
        self.cursor.execute('SELECT id FROM products WHERE url = ?',
                            (url,)
                            )
        row = self.cursor.fetchone()
        if row:
            product_id = row[0]
            self.cursor.execute('INSERT INTO prices (product_id, price) VALUES (?, ?)',
                                (product_id, price))

        self.connection.commit()