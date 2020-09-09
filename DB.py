import psycopg2

def connection_db():
    '''
    Coneccion con base de datos
    '''
    # conn = psycopg2.connect(user="orion",
    #                         password="12345",
    #                         host="ec2-35-172-38-7.compute-1.amazonaws.com",
    #                         port="5432",
    #                         database="ocr")
    conn = psycopg2.connect(user="intertelcoluisr",
                            password="Exito!2019",
                            host="localhost",
                            port="5432",
                            database="eventdata")
    return conn

def fill_ef_segments(segment):
    '''
    Llenar tabla de segmentos
    '''
    try:
        conn = connection_db()
        cur = conn.cursor()

        # query = "INSERT INTO events (url,classname,text) VALUES ('" + segment + "');"
        query = "INSERT INTO events (date,time,base_uri,class_name,text_content,inner_html,inner_text,node_name,node_value,button,from_element,current_target,relate_target,time_stamp) VALUES ( CURRENT_DATE, CURRENT_TIME,'" + segment[0] + "','"+segment[1]+"','"+segment[2]+"','"+segment[3]+"','"+segment[4]+"','"+segment[5]+"','"+segment[6]+"','"+segment[7]+"','"+segment[8]+"','"+segment[9]+"','"+segment[10]+"','"+segment[11]+"');"
        print(query)
        cur.execute(query)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
