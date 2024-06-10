from flask_appbuilder import IndexView


class HomeView(IndexView):
    index_template = 'index.html'
