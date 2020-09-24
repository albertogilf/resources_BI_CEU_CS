import mysql.connector
from populations import Population
from animals import Mouse, EnumsMouse
from families import Family, NormalFamily, PoligamicFamily
from datetime import date
from datetime import datetime

cnx = mysql.connector.connect(
    host = "localhost",
    user= "root",
    passwd = "Marta22berruezo",
    database = "conjunto_ratones"
)


def getIdNewPopulation():
    """
    Esta función devuelve la referencia de la ultima poblacion.
    """
    cursor = cnx.cursor()

    cursor.execute("SELECT max(reference) FROM population")
    reference = 1
    record = cursor.fetchone()          
    if record[0]:
        reference = int(record[0]) + 1
    cursor.close()
    return reference


def getIdNewMouse():
    """
    Esta función devuelve la referencia del último ratón.
    """
    cursor = cnx.cursor()

    cursor.execute("SELECT max(reference) FROM mouse")
    reference = 1
    record = cursor.fetchone()
    if record[0]:
        reference = int(record[0]) + 1
    cursor.close()
    return reference


def getIdNewFamily():
    """
    Esta función devuelve la referencia de la ultima familia.
    """
    cursor = cnx.cursor()

    cursor.execute("SELECT max(id) FROM family")
    reference = 1
    record = cursor.fetchone()
    if record[0]:
        reference = int(record[0]) + 1
    cursor.close()
    return reference



def closeConexion():
    """
    Esta funcion cierra la conexion con la terminal.
    """
    try:
        cnx.close()
    except Exception:
        print("no se puede cerrar la conexión")



def insertPopulation(population, commit = False):  
    """
    Esta función inserta una poblacion en memoria
    Parámetros:
        -poblacion: poblacion que se quiere insertar en memoria
    """
    cursor = cnx.cursor()

    insert_into_population = "INSERT INTO population(name,researcher,start_date,num_days) VALUES (%s,%s,%s,%s)"
    start_date = str(population.get_start_date())                                                                       #la paso a string que recoge sql, o como es un date la puedo pasar a date directamente
    values_population = (population.get_name(), population.get_researcher(), start_date, population.get_num_days())   #obtengo los valores que ha creado
    cursor.execute(insert_into_population, values_population )                                                          #cuando los obtengo los llevo a la base de datos
    if commit:
        cnx.commit()                                                                                                        #o se hace todo o no se hace nada 
    cursor.close()
    


def insertMouse(population, mouse, commit = False):   
    """
    Esta función inserta un raton en memoria, según la poblacion en la que este
    Parámetros:
        -poblacion: poblacion que se quiere insertar el raton en memoria
        -mouse: raton que se quiere insertar
        -commit: por defecto true
    """
    cursor = cnx.cursor()

    insert_into_mouse = "INSERT INTO mouse(name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    birthdate = str(mouse.get_birthdate())
    id_population = population.get_reference()
    gender_mouse = str(mouse.get_gender())
    chromosome1 = str(mouse.get_chromosome1())
    chromosome2 = str(mouse.get_chromosome2())
    values_mouse = ( mouse.get_name(), birthdate, mouse.get_weight(), gender_mouse , mouse.get_temperature(), mouse.get_description(), chromosome1, chromosome2, id_population)
    cursor.execute(insert_into_mouse, values_mouse )
    if (commit):
        cnx.commit()
    cursor.close()



def insertPopulationWithSize(population):   
    """
    Esta función inserta una poblacion en memoria
    Parámetros:
        -poblacion: poblacion que se quiere insertar en memoria
    """
    try:
        insertPopulation(population, commit = False)
        for mouse in (population.get_animal_list()):
            insertMouse(population, mouse, commit = False)
        cnx.commit()
    except Exception:
        cnx.rollback()




def deleteMouse(population, reference_mouse, commit = False):          
    """
    Esta función elimina un raton en memoria
    Parámetros:
        -poblacion: poblacion donde se encuentra el raton que se quiere eliminar en memoria
        -reference_mouse: referencia del raton que se quiere eliminar
    """
    cursor = cnx.cursor()

    delete_mouse = "DELETE FROM mouse WHERE reference = %s and id_population = %s"
    id_population = population.get_reference()
    cursor.execute(delete_mouse, (reference_mouse, id_population))
    if commit:
        cnx.commit()
    cursor.close()



def updateMouse(population, reference, name, weight, temperature, description, commit = False):            
    """
    Esta función modifica un raton en memoria
    Parámetros:
        -poblacion: poblacion donde se encuentra el raton que se quiere modificar y que se encuentra en memoria
        -reference: referencia del raton que se quiere modificar
        -name: el nuevo nombre modificado
        -weight: el nuevo peso modificado
        -temperature: la nueva temperatura modificada
        -description: la nueva descripcion modificada
    """
    cursor = cnx.cursor()

    update_mouse = "UPDATE mouse SET name = %s, weight=%s,temperature=%s, description=%s WHERE reference = %s"
    value_mouse = (name, weight, temperature, description, reference)
    cursor.execute(update_mouse, value_mouse)
    if commit:
        cnx.commit()
    cursor.close()


def createFamily(population, family, commit = False):
    """
    Esta función inserta una familia en memoria
    Parámetros:
        -poblacion: poblacion donde se quiere insertar la familia en memoria
        -family: familia que se quiere insertar
        -commit: por defecto true
    """
    cursor = cnx.cursor()
  
    create_family = "INSERT INTO family(id,id_father,id_population) VALUES (%s,%s,%s)"
    id_family = family.get_reference()
    mouse_father = family.get_parent()
    reference_father =  mouse_father.get_reference()
    id_population = population.get_reference()
    values_family = (id_family, reference_father, id_population)
    cursor.execute(create_family, values_family)

    update_mouses = "UPDATE mouse SET id_population = NULL WHERE reference = (%s)"
    values_father = (reference_father,)
    cursor.execute(update_mouses,values_father)
    if commit:
        cnx.commit()
    


def createNormalFamily(family, commit = False):
    """
    Esta función inserta una familia normal en memoria
    Parámetros:
        -family: familia normal que se quiere insertar
        -commit: por defecto true
    """
    cursor = cnx.cursor()

    create_normal_family = "INSERT INTO normal_family(id,id_normal_mother) VALUES (%s,%s)"
    mouse_mother = family.get_mother()
    reference_mother = mouse_mother.get_reference()
    values_normal_family = (family.get_reference(), reference_mother)
    cursor.execute(create_normal_family, values_normal_family)

    update_mouses = "UPDATE mouse SET id_population = NULL WHERE reference = (%s)"
    values_mother = (reference_mother,)
    cursor.execute(update_mouses,values_mother)
    if commit:
        cnx.commit()


def createPolygamicFamily(family, commit = False):
    """
    Esta función inserta una familia poligamica en memoria
    Parámetros:
        -family: familia poligamica que se quiere insertar
        -commit: por defecto true
    """
    cursor = cnx.cursor()

    create_polygamic_family = "INSERT INTO polygamous_family (id) VALUES (%s)"
    values_polygamic_family = (family.get_reference(), )
    cursor.execute(create_polygamic_family, values_polygamic_family)
    
    create_mother = "UPDATE mouse SET id_polygamous_mother=%s WHERE reference = %s"
    for mother in family.get_mothers():
        reference_mother = mother.get_reference()
        values_polygamic_mother = (family.get_reference(), reference_mother)
        cursor.execute(create_mother, values_polygamic_mother)

        update_mouses = "UPDATE mouse SET id_population = NULL WHERE reference = (%s)"
        values_mother = (reference_mother,)
        cursor.execute(update_mouses,values_mother)
    if commit:
        cnx.commit()


def insertFamily(population):                       
    """
    Esta función inserta una familia, que puede ser una familia normal y una familia poligamica en memoria
    Parámetros:
        -poblacion: poblacion donde se quiere insertar la familia en memoria
    """
    try:
        for family in  population.get_families_list():
            createFamily(population, family, commit = False)
            #print(str(family))

            if isinstance(family, NormalFamily.NormalFamily):
                createNormalFamily(family, commit = False)
            elif isinstance(family, PoligamicFamily.PoligamicFamily):
                createPolygamicFamily(family, commit = False)
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()


        
def createChildren(mouse, family, commit = False):
    """
    Esta función modifica ratones en memoria para que sean hijos.
    Parámetros:
        -poblacion: poblacion donde se quiere modificar los ratones en memoria para que sean hijos
        -mouse: raton que se quiere modificar para que sea hijo
        -family: familia donde se encuentra el raton
        -commit: por defecto true
    """
    cursor = cnx.cursor()

    create_mother = "UPDATE mouse SET id_son = (%s) WHERE reference = (%s)"
    reference_family = family.get_reference()
    reference_mouse = mouse.get_reference()
    values_children = (reference_family, reference_mouse)
    cursor.execute(create_mother, values_children)
    if commit:
        cnx.commit()


def reproduceFamilies(population):          
    """
    Esta función crea hijos en memoria.
        -poblacion: poblacion donde se quiere crear hijos en memoria.
    """
    try:
        for family in population.get_families_list():
            for children in family.get_children():
                insertMouse(population, children, commit = False)
                createChildren(children, family, commit = False)
        cnx.commit()
    except Exception:
        cnx.rollback()
        



#EJERCICIO1
def selectPopulations():
    """
    Esta funcion selecciona las referencias de poblaciones.
    Devuelve:
        -las referencias de una poblacion
    """
    cursor = cnx.cursor()

    cursor.execute("SELECT reference FROM population")
    population  = cursor.fetchall()             #recoger todos los datos
    reference_population =[]
    for i in population:
        numero = int(i[0])
        reference_population.append(numero)
    return reference_population



def selectOneMouse(reference_mouse):
    """
    Esta función selecciona de memoria un raton y lo crea, a partir de una referencia
    Parametros:
        -reference_mouse: referencia de un raton
    Devuelve:
        -un raton
    """
    cursor = cnx.cursor()

    mouse = "SELECT * FROM mouse WHERE reference = %s"
    value_value = (reference_mouse,)
    cursor.execute(mouse, value_value)
    for information in cursor.fetchall():
        reference = int(information[0])
        if (reference <= 0):
            raise ValueError("The references of the mouses should be > 0")

        name = str(information[1])

        birthdate = datetime.strptime(str(information[2]),'%Y-%m-%d').date()

        weight = float(information[3])
        if (weight <= 0):
            raise ValueError("The weight of the mouses should be > 0")

        try:
            gender = EnumsMouse.Gender.from_str(str(information[4]))
        except NotImplementedError as nie: 
            print(str(nie))
            raise ValueError("The gender should be Male or female")

        temperature = float(information[5])
        if (temperature <= 0):
            raise ValueError("The temperature of the mouses should be > 0")
        
        description = str(information[6])

        try:
            chromosome1 = EnumsMouse.Chromosome.from_str(information[7])
        except NotImplementedError: 
            raise ValueError("The chromosome should be X, Y, X_MUTATED or Y_MUTATED")

        try:
            chromosome2 = EnumsMouse.Chromosome.from_str(information[8])
        except NotImplementedError: 
            raise ValueError("The chromosome should be X, Y, X_MUTATED or Y_MUTATED")
    
    mouse = Mouse.Mouse(reference = reference, name = name, birthdate = birthdate, weight = weight, gender = gender, temperature = temperature, description = description, chromosome1 = chromosome1, chromosome2 = chromosome2 )
    cursor.close()
    return mouse


def selectAllMousesOfPopulation(reference_population):
    """
    Esta función selecciona todos los ratones de una poblacion a partir de la referencia de la poblacion
    Parametros:
        -reference_population: la referencia de una poblacion 
    Devuelve:
        -una lista de ratones de una poblacion
    """
    cursor = cnx.cursor()

    selectMouse = "SELECT reference FROM mouse WHERE id_population = %s"
    value = (reference_population,)
    cursor.execute(selectMouse, value)
    mouses_list = []
    for reference in cursor.fetchall():
        mouse = selectOneMouse(reference[0])
        mouses_list.append(mouse)
    return mouses_list



def selectNormalFamily(reference_population):
    """
    Esta función selecciona de memoria una familia normal y la crea, a partir de la referencia de la poblacion
    Parametros:
        -reference_population: es la referencia de la poblacion 
    Devuelve:
        -una lista con familias normales
    """
    cursor = cnx.cursor()
    select_normal_family = "SELECT nf.id FROM family as f\
                            INNER JOIN normal_family as nf\
                            on f.id = nf.id\
                            WHERE f.id_population = %s"
    values_normal_family = (reference_population,)
    cursor.execute(select_normal_family, values_normal_family)
    normal_families_list = []
    for data in cursor.fetchall():                 
        id_family = (data[0],)
        
        select_father = "SELECT id_father FROM family WHERE id = %s"
        cursor.execute(select_father, id_family)
        reference_father = cursor.fetchall()
        final_reference_father = reference_father[0][0]
        father = selectOneMouse(final_reference_father)

        select_mother = "SELECT id_normal_mother FROM normal_family WHERE id = %s"
        cursor.execute(select_mother, id_family)
        reference_mother = cursor.fetchall()
        final_reference_mother = reference_mother[0][0]
        mother = selectOneMouse(final_reference_mother)


        select_son = "SELECT reference FROM mouse WHERE id_son = %s"
        cursor.execute(select_son, id_family)
        son_list = []
        for reference in cursor.fetchall():                 #con hijos lo hago distinto porque puede haber varios hijos
            son = selectOneMouse(reference[0])
            son_list.append(son)
        
        family = NormalFamily.NormalFamily(parent = father , mother = mother, reference= id_family, children = son_list)
        normal_families_list.append(family)
  
    return normal_families_list


def selectPoligamicFamily(reference_population):
    """
    Esta función selecciona de memoria una familia poligamica y la crea, a partir de la referencia de la poblacion
    Parametros:
        -reference_population: es la referencia de la poblacion 
    Devuelve:
        -una lista con familias poligamicas
    """
    cursor = cnx.cursor()
    select_poligamic_family = "SELECT pf.id FROM family as f\
                            INNER JOIN polygamous_family as pf\
                            on f.id = pf.id\
                            WHERE f.id_population = %s"
    values_poligamic_family = (reference_population,)
    cursor.execute(select_poligamic_family, values_poligamic_family)
    poligamic_families_list = []
    for data in cursor.fetchall():                 
        id_family = (data[0],)
        
        select_father = "SELECT id_father FROM family WHERE id = %s"
        cursor.execute(select_father, id_family)
        reference_father = cursor.fetchall()
        final_reference_father = reference_father[0][0]
        father = selectOneMouse(final_reference_father)

        select_mother = "SELECT reference FROM mouse WHERE id_polygamous_mother = %s"
        cursor.execute(select_mother, id_family)
        mother_list = []
        for reference in cursor.fetchall():
            mother = selectOneMouse(reference[0])
            mother_list.append(mother)
    

        select_son = "SELECT reference FROM mouse WHERE id_son = %s"
        cursor.execute(select_son, id_family)
        son_list = []
        for reference in cursor.fetchall():             
            son = selectOneMouse(reference[0])
            son_list.append(son)
    
        family = PoligamicFamily.PoligamicFamily(parent = father , mothers = mother_list, reference= id_family, children = son_list)
        poligamic_families_list.append(family)
    return poligamic_families_list

def selectAllFamilies(reference_population):
    """
    Esta función junta todas las familias que hay, a partir de la referencia de una población
    Parametros:
        -reference_population: es la referencia de la poblacion 
    Devuelve:
        -una lista con familias tanto normales como poligamicas
    """
    families_list = []
    normal_families = selectNormalFamily(reference_population)
    poligamic_families = selectPoligamicFamily(reference_population)
    for normal_family in normal_families:
        families_list.append(normal_family)
    for poligamic_family in poligamic_families:
        families_list.append(poligamic_family)
    return families_list
    



def selectOnePopulation(reference_population):
    """
    Esta función selecciona de memoria una poblacion y la crea, a partir de la referencia de la poblacion
    Parametros:
        -reference_population: es la referencia de la poblacion 
    Devuelve:
        -una poblacion
    """
    cursor = cnx.cursor()

    select_population = "SELECT * from population WHERE reference = %s"
    value_reference = (reference_population,)
    cursor.execute(select_population,value_reference)
    population  = 0 
    for data in cursor.fetchall():
        name = str(data[1])
        researcher = str(data[2])
        start_date = datetime.strptime(str(data[3]),'%Y-%m-%d').date()
        num_days = int(data[4])
        if (num_days <= 0):
            raise ValueError("Num days of the experiment should be > 0")

    mouses_list = selectAllMousesOfPopulation(reference_population)
    families_list = selectAllFamilies(reference_population)

    population = Population.Population(reference = reference_population, name = name, researcher = researcher, start_date = start_date,  num_days = num_days, animal_list = mouses_list, families_list = families_list)
    cursor.close()
    return population
    



def main():
    #prueba="hola"
    #id_population = getIdNewPopulation()
    #id_mouse = getIdNewMouse()
    #print(id)
    #id_mouse = getIdNewMouse()
    #poblacion = Population.Population(reference = id_population, name="nombre", researcher="researcher", start_date=date.today(), num_days=270, animal_list=None, families_list=[])
    #poblacion = Population.Population(reference = id_population, name="nombre", researcher="researcher", start_date=date.today(), num_days=270, animal_list=None, families_list=[])
    #insertPopulation(poblacion)
    #mouse = Mouse.Mouse(reference=id_mouse, name="nombre", birthdate=date.today(), weight=70, gender=EnumsMouse.Gender.MALE, temperature=37, description="", chromosome1=EnumsMouse.Chromosome.X, chromosome2=EnumsMouse.Chromosome.Y)
    #mouse = Mouse.Mouse(reference = id_mouse, name = "nombre", probabilityMutation = 0.3)
    #insertMouse(poblacion, mouse)
    #deleteMouse(poblacion, mouse.get_reference())
    #print(hola, "se ejecuto")

    #num = getIdNewPopulation()
    #print(num)
    #num = selectPopulations()
    #num = selectOnePopulation(1)
    num = selectOnePopulation(1)
    print(num)
    
    #closeConexion()
    #if(cnx.is_connected()): 
        #print ("connection still open. Check connection")



if __name__=="__main__":
    main()
