from database.DB_connect import DBConnect
from model.__init__ import Vendita, Prodotto

class products_DAO  ():
    def __init__(self):
        pass

    def get_colori(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Database non trovato")
            return
        else:
            cursor = cnx.cursor()
            cursor.execute("select distinct Product_color from go_products gp ")
            for row in cursor:
                result.append(row[0])
        cnx.close()
        return result
    def get_prodotti_colori(self,colore):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Database non trovato")
            return
        else:
            cursor = cnx.cursor()
            cursor.execute("""SELECT * from go_products gp 
                        where Product_color = %s
                        """, (colore,))
            for row in cursor:
                result.append(Prodotto(row[0], row[1], row[2],
                                       row[3],row[4], row[5],
                                       row[6]))
        cnx.close()
        return result

class vendite_DAO():

    def get_vendite(self, colore, anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Database non trovato")
            return
        else:
            cursor = cnx.cursor()
            cursor.execute("""SELECT Product_number, Date, Retailer_code  
                FROM go_daily_sales gds 
                WHERE EXTRACT(YEAR FROM Date) = %s
                and Product_number in (select Product_number from go_products gp 
                where Product_color = %s);
                """, (anno, colore))
            for row in cursor:
                result.append(Vendita(row[0],row[1],row[2]))
        cnx.close()
        return result

