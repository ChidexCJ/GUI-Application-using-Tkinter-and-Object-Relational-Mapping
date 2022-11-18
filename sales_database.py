#import dependencies
import pymysql
import configparser

# read config.ini file to pull stored values
config = configparser.ConfigParser()
config.read('config.ini')

# declare variables for config values
host = config['inputs']['host']
user = config['inputs']['user']
password = config['inputs']['password']
dtbz = config['inputs']['db']


class Database:
    def __init__(self):
        self.conn = pymysql.connect(host=host, user=user, password=password, db=dtbz)
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS sales (rowId INT AUTO_INCREMENT PRIMARY KEY, `date` datetime, `partNumber` '
            'VARCHAR(30), '
            'description VARCHAR( '
            '40) NOT NULL, '
            'customerName VARCHAR(30) NOT NULL, location VARCHAR(30) NOT NULL, `unitPrice` INT  NOT NULL, '
            'quantity INT NOT '
            'NULL) ENGINE=InnoDB')
        self.conn.commit()

    def fetch(self):
        """returns row values"""
        self.cur.execute("SELECT `rowId`,`partNumber`, `description`, `customerName`, `location`, `unitPrice`, "
                         "`quantity` FROM "
                         "sales")
        rows = self.cur.fetchall()
        return rows

    def insert(self, partNumber, description, customerName, location, unitPrice, quantity):
        """inserts value into table"""
        self.cur.execute("INSERT INTO `sales` (`date`, `partNumber`, `description`, `customerName`, `location`, "
                         "`unitPrice`, "
                         "`quantity` "
                         ") VALUES (now(), %s, %s, %s, %s, %s, %s)",
                         (partNumber, description, customerName, location, unitPrice, quantity))
        self.conn.commit()

    def remove(self, rowId):
        """removes table row with reference to rowID"""
        self.cur.execute("DELETE FROM sales WHERE rowId=%s", (rowId,))
        self.conn.commit()

    def update(self, rowId, partNumber, description, customerName, location, unitPrice, quantity):
        """updates row entires"""
        self.cur.execute("UPDATE sales SET partNumber = %s, description =  %s,customerName = %s, location = %s, "
                         "unitPrice = %s, "
                         "quantity = %s WHERE rowId = %s",
                         (partNumber, description, customerName, location, unitPrice, quantity, rowId))
        self.conn.commit()

    def __del__(self):
        """deletes values"""
        self.conn.close()


#object of class
data = Database()


# data.insert('xyz', 'metal', 'john', 'aba', 10000, 20)
# data.insert('jkl', 'valve seal', 'ken', 'kano', 1000, 50)
# data.insert('mno', 'ring', 'obi', 'onitsha', 25000, 10)
# data.insert('abc', 'fuel pump', 'john', 'lagos', 5000, 20)
# data.insert('def', 'piston', 'peter', 'kaduna', 60000, 10)
# data.insert('fgh', 'gear knob', 'Denni', 'enugu', 5500, 10)
# data.insert('pqr', 'oil pump', 'Matt', 'jos', 35000, 5)
