import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS reminder(
            id Integer Primary Key,
            date text,
            time text,
            remadetail text,
            mobno text,
            email text,
            alerttime text    
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self,date, time, remadetail, mobno, email, alerttime):
        self.cur.execute("insert into reminder values (NULL,?,?,?,?,?,?)",
                         (date, time, remadetail, mobno, email, alerttime))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from reminder")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from reminder where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, date, time, remadetail, mobno, email, alerttime):
        self.cur.execute(
            "update reminder set id=?, date=?, time=?, remadetail=?, mobno=?, email=?, alerttime=?,",
            (date, time, remadetail, mobno, email, alerttime))
        self.con.commit()
