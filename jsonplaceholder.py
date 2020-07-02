import http.client
import logging
import json
from urllib.parse import urlencode

class Jsonplaceholder():
    """
    This module is developed as example to consume jsonplaceholder.typicode.com 
    """    
    def __init__( self,
                  host = None,
                  ssl  = None,
                  port = None,
                  conn_timeout = None,
                  debug_level = None
                ):

        self.host = host or "jsonplaceholder.typicode.com"
        self.ssl = ssl or True
        self.port = port or 443
        self.debug_level = debug_level or 0
        self.conn_timeout = conn_timeout or 10

        self.conn = None 

    def __hit_api__( self, params=None, body=None, headers={}, encode_chunked=False, method="GET", url="/" ):
        """
        This private method sends request to the API.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """
        try:
            self.conn.request( 
                               method=method, 
                               url=url, 
                               body=body, 
                               headers=headers,
                               encode_chunked=encode_chunked
                            )
            
            response = self.conn.getresponse()

            result = {}
            result["status"] = response.status
            result["reason"] = response.reason
            result["headers"] = response.getheaders()
            result["body"] = json.loads( response.read() )
            return result

        except Exception as e:
            logging.error( e )
            return None

    def __get_user__( self, params=None, body=None, headers={}, encode_chunked=False ):
        """
        Manages API requests for /users calling __hit_api__ method.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """
        url = "/users"

        if params is not None and "email" in params:
            url = url + "?" + urlencode(params, safe='@')
        elif params is not None:
            url = url + "?" + urlencode(params)
        return self.__hit_api__( url=url, method="GET" )

    def __get_post__( self, params=None, body=None, headers={}, encode_chunked=False ):
        """
        Manages API requests for /posts calling __hit_api__ method.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """        
        url = "/posts"

        if params is not None:
            url = url + "?" + urlencode(params)            
        return self.__hit_api__( url=url, method="GET" )

    def __get_album__( self, params=None, body=None, headers={}, encode_chunked=False ):
        """
        Manages API requests for /albums calling __hit_api__ method.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """              
        url = "/albums"

        if params is not None :
            url = url + "?" + urlencode(params)            
        return self.__hit_api__( url=url, method="GET" )

    def __get_photo__( self, params=None, body=None, headers={}, encode_chunked=False ):
        """
        Manages API requests for /photos calling __hit_api__ method.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """           
        url = "/photos"

        if params is not None :
            url = url + "?" + urlencode(params)            
        return self.__hit_api__( url=url, method="GET" )

    def connect (self):
        """
        Create the initial connection and return HTTPConnection object.
        Return True if it is successful and False if fails.
        """           
        try:
            if self.ssl :
                self.conn = http.client.HTTPSConnection( host=self.host, port=self.port, timeout = self.conn_timeout)
            else:
                self.conn = http.client.HTTPConnection( host=self.host, port=self.port, timeout = self.conn_timeout )
            self.conn.set_debuglevel( self.debug_level )
            return True
        except Exception as e:
            logging.error( e )
            return False

    def get_connection(self):
        """
        Return a connection object. It is not used by this example.
        """                 
        return self.conn    
    
    def set_debug_level(self, l ):
        """
        Set debug level for HTTPConnection object. It is not used by this example.
        """
        self.conn.set_debuglevel( l )
        return True 

    def get_users( self ):
        """
        Get all the users registered in the API server. It is not used by this example.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """        
        return self.__get_user__()

    def get_user_by_email( self, email ):
        """
        Get an user by its email address.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: <dict> }
        """   
        result = self.__get_user__( params={ "email":email } )
        
        if result is not None and len(result["body"]) > 0 :
            result["body"] = result["body"][0]
            return result
        else:
            return None

    def get_user_by_id( self, id ):
        """
        Get an user by its id identifier.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: <dict> }
        """           
        result = self.__get_user__( params={ "id":id } )
        
        if result is not None and len(result["body"]) > 0 :
            result["body"] = result["body"][0]
            return result
        else:
            return None

    def get_posts( self ):
        """
        Get all the posts registered in the API server. It is not used by this example.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """                
        return self.__get_post__()

    def get_post_by_id( self, id ): 
        """
        Get a post by its id identifier. It is not used by this example.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: <dict> }
        """                 
        result = self.__get_post__( params={ "id":id } )

        if result is not None and len(result["body"]) > 0 :
            result["body"] = result["body"][0]
            return result
        else:
            return None         

    def get_posts_by_user_id( self, u_id ):
        """
        Get a all posts filtered by user id.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """           
        return self.__get_post__( params={ "userId":u_id } )

    def get_albums( self ):
        """
        Get all the albums registered in the API server. It is not used by this example.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """             
        return self.__get_album__()

    def get_albums_by_user_id( self, u_id ):
        """
        Get all the albums filtered by userId.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """
        return self.__get_album__( params={ "userId":u_id } )

    def get_album_by_id( self, id ):
        """
        Get an album filtered by albumId.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: <dict> }
        """        
        result = self.__get_album__( params={ "id":id } )

        if result is not None and len(result["body"]) > 0 :
            result["body"] = result["body"][0]
            return result
        else:
            return None  

    def get_album_by_title( self, title ):
        """
        Get an album filtered by album title. It is not used by this example.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: <dict> }
        """                
        result = self.__get_album__( params={ "title":title } )    

        if result is not None and len(result["body"]) > 0 :
            result["body"] = result["body"][0]
            return result
        else:
            return None  

    def get_photos( self ):
        """
        Get all the photos available in the API server. It is not used by this example.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """           
        return self.__get_photo__()

    def get_photos_by_album_id( self, a_id ):
        """
        Get photos filtered by album id.
        Return a dictionary : { status:<int> , reason: <string>, headers: [<( header, value )>], body: [<dict>] }
        """
        return self.__get_photo__( params={ "albumId":a_id } )
    
    def get_user_report_from_email( self, email ):
        """
        Create a report with user information and all the posts,album and photos created by the user.
        Return a dictionary : { userInfo:<dict> , userPosts: [<dict>], userAlbums: [<dict>], photos: [<dict>] }
        """
        result = {}

        try:
            user = self.get_user_by_email ( email )
            if user:
                user_info = user["body"]
            
                posts = self.get_posts_by_user_id( user_info["id"] )
                posts_info = posts["body"]

                albums = self.get_albums_by_user_id( user_info["id"] )
                albums_info = albums ["body"]

                photos = []

                for album in albums_info:
                    photos_by_album = self.get_photos_by_album_id(album["id"])
                    photos = photos + photos_by_album["body"] 

                result["userInfo"] = user_info
                result["userPosts"] = posts_info
                result["userAlbums"] = albums_info
                result["photos"] = photos

                return result
        except Exception as e:
            logging.error( e )
            return None            