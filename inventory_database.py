import pymysql
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['inputs']['host']
user = config['inputs']['user']
password = config['inputs']['password']
dtbz = config['inputs']['db']


class Database:
    def __init__(self):
        self.conn = pymysql.connect(host=host, user=user, password=password, db=dtbz)
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS inventory (rowId INT AUTO_INCREMENT PRIMARY KEY, `date` datetime, `partNumber` '
            'VARCHAR(30), '
            'description VARCHAR( '
            '40) NOT NULL, `quantityReceived` INT  NOT NULL, quantityDelivered INT NOT '
            'NULL) ENGINE=InnoDB')
        self.conn.commit()

    def fetch(self):
        """returns row values"""
        self.cur.execute("SELECT `rowId`,`partNumber`, `description`, `quantityReceived`, "
                         "`quantityDelivered` FROM "
                         "inventory")
        rows = self.cur.fetchall()
        return rows

    def insert(self, partNumber, description, quantityReceived, quantityDelivered):
        """inserts value into table"""
        self.cur.execute("INSERT INTO `inventory` (`date`, `partNumber`, `description`, `quantityReceived`, "
                         "`quantityDelivered`) VALUES (now(), %s, %s, %s, %s)",
                         (partNumber, description, quantityReceived, quantityDelivered))
        self.conn.commit()

    def remove(self, rowId):
        """removes table row with reference to rowID"""
        self.cur.execute("DELETE FROM inventory WHERE rowId=%s", (rowId,))
        self.conn.commit()

    def update(self, rowId, partNumber, description, quantityReceived, quantityDelivered):
        """updates row entires"""
        self.cur.execute("UPDATE inventory SET partNumber = %s, description =  %s, quantityReceived = %s, "
                         "quantityDelivered = %s WHERE rowId = %s",
                         (partNumber, description, quantityReceived, quantityDelivered, rowId))
        self.conn.commit()

    def __del__(self):
        """deletes values"""
        self.conn.close()


# object of class
data = Database()

# data.insert('xyz', 'metal', 10,0)
# data.insert('jkl', 'valve seal', 0, 3)
# data.insert('mno', 'ring', 0, 2)
