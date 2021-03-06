from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

whiskey = User(first_name='Whiskey', last_name='Kake', image_url='https://images.unsplash.com/photo-1544208757-ddbaebce244e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80')
bowser = User(first_name='Bowser', last_name='Pilip', image_url ='https://images.unsplash.com/photo-1507668077129-56e32842fceb?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2134&q=80')
spike = User(first_name='Spike', last_name="porcupine", image_url = 'https://images.unsplash.com/photo-1478147427282-58a87a120781?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80')

post1 = Post(title='first title', content='first content', user_id=2)
post2 = Post(title='second title', content='second content', user_id=1)
post3 = Post(title='third title', content='third content', user_id=3)

db.session.add_all([whiskey, bowser, spike])

db.session.commit()

db.session.add_all([post1, post2, post3])

db.session.commit()
