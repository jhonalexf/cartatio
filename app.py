
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app = Flask(_name_, static_url_path='/static')

platos = {
     "ENCEBOLLADOS Y ALGO MÁS...": [
            
           
            {
                "nombre": "Encebollado Dumbo",
                "descripcion": "Unico y auténtico guayaco... es una receta tradicional desde los astilleros de nuestro puerto guayaquileño, disfrútelo con canguil, chifle y limón.",
                "precio": 3.00,
                "imagen": "encebollado_dumbo.png"
            },
            {
                "nombre": "Encebollado con Camarones",
                "descripcion": "Acompañado con canguil y chifle.",
                "precio": 4.90,
                "imagen": "encebollado_camaron.png"
            },
            {
                "nombre": "El Maná",
                "descripcion": " Con las 3B, Bueno, Bonito y Barato, para que vengan siempre en familia o con esa persona especial para degustar la conchitas Asadas de los manglares de Esmeraldas, y tampoco se puede quedar solo porque lo acompañamos conarroz blanco, encurtido y patacones.",
                "precio": 7.90,
                "imagen": "el_mana.png"
            },
            {
                "nombre": "Encebollado con Conchitas",
                "descripcion": "Con Conchitas Prietas, canguil y chifle.",
                "precio": 5.90,
                "imagen": "encebollado_conchitas.png"
            },
            {
                "nombre": "Encebollado Mixto",
                "descripcion": "Para un gusto espectacular con Conchitas y Camarones, acompañado con canguil, chifle y limón.",
                "precio": 8.50,
                "imagen": "encebollado_mixto.png"
            },
            {
                "nombre": "Maremoto",
                "descripcion": "Un rico plato de Encebollado con Camarones, Conchitas, Calamares, Almejas y Mejillones.",
                "precio": 10.90,
                "imagen": "maremoto.png"
            }
        ],

         "CEVICHES": [
            {
                "nombre": "Ceviche de Concha",
                "descripcion": "Disfrute de la Concha Prieta con canguil y chifle.",
                "precio": 10.90,
                "imagen": "cevicheconcha.png"
            },
            {
                "nombre": "Ceviche de Camarones",
                "descripcion": "Acompañado con canguil, chifle y limón.",
                "precio": 8.90,
                "imagen": "ceviche_camarones.png"
            },
            {
                "nombre": "Ceviche Mixto",
                "descripcion": "Un dual de Conchitas y Camarones con canguil y chifle.",
                "precio": 9.90,
                "imagen": "ceviche_mixto.png"
            }
        ],

         "ARROZ": [
            {
                "nombre": "Arroz con Camarones",
                "descripcion": "Un deleite a su paladar de un delicioso arroz con camarones, papitas fritas y maduros.",
                "precio": 8.90,
                "imagen": "arroz_camarones.png"
            },
         
            {
                "nombre": "Arroz Mixto",
                "descripcion": "Arroz meloso con Conchitas, Camarones, maduros fritos y tapitas de Conchitas Asadas.",
                "precio": 8.90,
                "imagen": "arroz_mixto.png"
            },
             
            {
                "nombre": "Arroz con Conchas",
                "descripcion": "Para los amantes de la concha Prieta acompañada de una giarnición de maduros fritos y Conchitas Asadas.",
                "precio": 10.90,
                "imagen": "arroz_conchas.png"
            },
            {
                "nombre": "La Costeñita ",
                "descripcion": "Una delicia con papas fritas a gozar un rico filete de pescado, ceviche de camarones, arroz blanco y encurtido.",
                "precio": 8.90,
                "imagen": "costeñita.png"
            },
            {
                "nombre": "Corvina Frita",
                "descripcion": " Un hermoso filete de corvina rosada, la propia corvina para disfrutar con una guarnición de papas fritas, arroz blanco y ensalada.",
                "precio": 9.90,
                "imagen": "corvinafrita.png"
            },
             {
                "nombre": "Camarones Apanados",
                "descripcion": "Para disfrutarlo con papas fritas, arroz blanco, salsa rosada y ensalada.",
                "precio": 8.90,
                "imagen": "camaronesapanados.png"
            },
            {
                "nombre": "Camarones al Ajillo",
                "descripcion": "Para el jefe del hogar, para esa persona trabajadora: unos ricos camarones de Pedernales(Manabi), cocidos en una exquisita salsa picante, con una guarnición de papas fritas, arroz blanco y ensalada.",
                "precio": 9.90,
                "imagen": "camaronesajillo.png"
            },
            
            

        ],
        
        " ... Y PARA ALGUIEN ESPECIAL ": [

            {    
                "nombre": "Conchitas Asadas",
                "descripcion": "simplemente las mejores y autenticas CONCHITAS ASADAS, pruébalas aquí con una guirnición de encurtido y patacones.",
                "precio": 11.90,
                "imagen": "conchasasadas.png"
            },
            {
                "nombre": "Conchitas Asadas con queso ",
                "descripcion": "una ricura para disfrutar con patacones y queso.",
                "precio": 9.90,
                "imagen": "conchasconqueso.png"
            },
            {
                "nombre": "Arroz con Mariscos",
                "descripcion": "Disfrute de un potaje en un mismo plato de arroz meloso con Camarones, Almejas, Mejillones, Cangrejo, Calamar y Conchitas Asadas, y para completar un Filete de Pescado con una guarnición de maduros fritos.",
                "precio": 16.50,
                "imagen": "arroz_mariscos.png"
            },
            {
                "nombre": "Encocado Mixto",
                "descripcion": " Una delicia salsa de coco con camarones y filete de pescado, arroz blanco, ensalada y maduros fritos.",
                "precio": 8.90,
                "imagen": "encocado_mixto.png"
            },
            {
                "nombre": "Corvina en Salsa de Mariscos",
                "descripcion": "Un rico Filete de Pescado bañado en una suculenta salsa compuesta de Mariscos (Conchitas, Camarones, Almejas, Mejillones y Calamar), con arroz blanco y una guarnición de papas fritas.",
                "precio": 16.50,
                "imagen": "corvina_salsa_mariscos.png"
            },
            {
                "nombre": "La Banderita",
                "descripcion": "Una combinacion de cecihes de conchas, camarones, pescado y la infaltable guatita, lo acompañamos tambien con una guarnicion de arroz blanco y maduros fritos.",
                "precio": 9.90,
                "imagen": "banderita.png"
            },
            {
                "nombre": "Sopa 7 Mariscos",
                "descripcion": "A base de un rico fumet de Pescado y donde UD, pueda disfrutar de Camarones, Alemejas, Mejillones, Conchas, Calamares y Cangrejo, y para saborearlo con una porción de arroz blanco.",
                "precio": 16.50,
                "imagen": "sopa_7_mariscos.png"
            },
            
            {
                "nombre": "La Costeñita 2",
                "descripcion": "Algo especial y bonito... de una mezcla perefecta de mariscos en una bandeja donde usted puede degustar de un hermoso filete de pescado y de una porcion de arroz con mariscos, que lleva Camarones, Almejas, Mejillones y Calamares, para degustarlo con un Cevichito Mixto(Conchitas-Camarones) y a esto súmele una guarnición de maduros fritos y ensalada.",
                "precio": 14.50,
                "imagen": "la_costenita_2.png"
            },
            {
                "nombre": "Mi Planchita",
                "descripcion": "Algo especial unas Conchitas Asadas y un Filete de Lomo de falda para saborearlo con papitas firtas y patacones ",
                "precio": 11.50,
                "imagen": "mi_planchita.png"
            },
            {
                "nombre": "Mar y Tierra",
                "descripcion": " Un delicioso lomo de falda con una guarnición de papas fritas, Ceviche de Camarones, arroz blanco, ensalda y patacones",
                "precio": 11.90,
                "imagen": "mar_y_tierra.png"
            },
            {
                "nombre": "Lomito y Camarones",
                "descripcion": "Unos ricos Camarones a la Plancha y picantitos y un Filete de Lomo de Falda, en una plancha con papitas ritas y patacones.",
                "precio": 11.90,
                "imagen": "lomito_camarones.png"
            },
            {
                "nombre": "El Plato del TikTok",
                "descripcion": "Para la persona que quiere festejar su dia especial. nada mejor que hacerlo con un Filete de Lomo de Falda, unas Conchitas Asadas y un Ceviche de Camarón, para saborearlo con arroz y con una guarnición de papas fritas, patacones y ensalada.",
                "precio": 14.90,
                "imagen": "plato_tiktok.png"
            },
            {
                "nombre": "Banquete de los Manglares",
                "descripcion": "Una delicia, una parrilla con Conchitas Asadas y Camarones para degustarlo con papitas fritas y patacones",
                "precio": 14.90,
                "imagen": "banquete_manglares.png"
            },
            {
                "nombre": "Parillada de Mariscos",
                "descripcion": "Para disfrutar de un potaje de mariscos; de Conchitas Asadas, de Camarones, de Almejitas, de Mejillones, de Filete de Pescado, y calamares ....con una guarnición de patacones y una porción de arroz.",
                "precio": 19.90,
                "imagen": "parilla.png"
            }, 
            {
                "nombre": " Una rica piña con Mariscos",
                "descripcion": "Camarones, Calamares, Almejas, Mejillones y Quesito derretido... con una guarnición de patacones y Conchitas Asadas.",
                "precio": 16.50,
                "imagen": "pina_mariscos.png"
            },
            {
                "nombre": "A la Costa",
                "descripcion": "Una bandeja con riquisimos Mariscos que contiene un Filete de Pescado, una porción de Arroz con Mariscos, Conchitas Asadas, Ceviche Mixto, encurtido y maduros fritos.",
                "precio": 14.50,
                "imagen": "a_la_costa.png"
            }
        ],

    
         "BEBIDAS": [
         
            {
                "nombre": "Vaso de Limonada",
                "descripcion": "Bebida refrescante natural.",
                "precio": 1.25,
                "imagen": "vaso_limonada.png"
            },
    
            {
                "nombre": "Jarra de Limonada",
                "descripcion": "Jarra familiar de limonada.",
                "precio": 4.50,
                "imagen": "jarra_limonada.png"
            },
         
            {
                "nombre": "Vaso de Frutos Rojos",
                "descripcion": "Bebida frutal fresca.",
                "precio": 1.90,
                "imagen": "vaso_frutos_rojos.png"
            },
    
             {
                "nombre": "Jarra de Frutos Rojos",
                "descripcion": "Ideal para compartir.",
                "precio": 5.90,
                "imagen": "jarra_frutos_rojos.png"
            }
        ],

    
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', platos=platos)

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
