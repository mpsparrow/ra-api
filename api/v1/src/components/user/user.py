from sanic.views import HTTPMethodView

class User(HTTPMethodView):
    async def post(self, request):
        """
        Create new user
        """
        return {"status": "complete"}

    async def get(self, request):
        """
        /user/id 
        """
        return {"user": "potato"}

