# flask-SQLAlchemy

# a savoir

 - le projet contient un template
 
 - python-dotenv est installé pour un environnment de développement


# Objectif du projet

- Créer une base de donnée (sqlachemy)

- Créer un nom

- Afficher ce nom sur la page Home


# Créer un nom dans la base de donnée

- flask shell

- from app import db, Students

- db.create_all()

- student = Students(name='toto')

- db.session.add()

- db.session.commit()
