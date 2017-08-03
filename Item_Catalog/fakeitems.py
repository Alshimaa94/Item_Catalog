from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///CatalogApp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Programming
category1 = Category(name="Programming", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Software applications developer", user_id=1, description="Design or customize computer applications software, Modify existing software to optimize operational efficiency or correct errors, Evaluate software requirements and user needs to determine software feasibility", category=category1)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Computer systems analyst", user_id=1,  description="Analyze data processing problems to improve computer systems, Develop and test system design procedures, Enhance system compatibility so information can be shared easily", category=category1)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Network systems administrator", user_id=1, description="Install and support an organization network system, Examine website functions to ensure performance without interruption, Perform data backups and disaster recovery operations", category=category1)
session.add(item3)
session.commit()

# Items for Business 
category2 = Category(name="Business", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Financial Advisor", user_id=1, description="financial advisors meet with clients and counsel them on their finances. This could mean sitting down and creating budgets to firming up retirement plans to giving advice about investing", category=category2)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Operations Research Analyst", user_id=1,  description="Operations research analysts are high-level problem-solvers who use advanced techniques, such as optimization, data mining, statistical analysis and mathematical modeling, to develop solutions that help businesses and organizations operate more efficiently and cost-effectively", category=category2)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Accountant", user_id=1, description="an accountant is a person who keeps or inspects financial records. They're numbers people who excel at organization and detail-oriented work", category=category2)
session.add(item3)
session.commit()

# Items for Law
category3 = Category(name="Law", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Solicitor", user_id=1, description="You'll be a confidential adviser that has direct contact with clients, combining expertise and people skills to provide legal guidance and assistance. Once qualified, you can work in private practice, in-house for a commercial or industrial organisation, in local or central government or in the court service.", category=category3)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Barrister", user_id=1, description="From providing specialist legal advice to representing clients in court, your tasks will vary depending on your area of expertise. Generally, you: advise clients on the law and the strength of their case; hold conferences with clients to discuss their situation and provide legal advice; represent clients in court by presenting the case, examining witnesses and giving reasons why the court should support the case; and negotiate settlements with the other side.", category=category3)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Chartered legal executive", user_id=1, description="As a qualified lawyer you'll have your own client files and, as a fee-earner in private practice, your work is charged directly to the client. This is an important difference between chartered legal executives and other legal support staff.", category=category3)
session.add(item3)
session.commit()

print "added menu items!"
