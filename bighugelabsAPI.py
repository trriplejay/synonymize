import json
import urllib
"""
python 2.7 API info for bighugelabs.com thesaurus

Keep API key in a separate file (named secret_key.py), and add it to
.gitignore, then import API_KEY from it.
"""


class BigHugeLabAPI(object):

    def __init__(self, secret_key=None, reqtype=None):
        # get API key by creating an account on words.bighugelabs.com
        self.secret_key = secret_key
        self.reqtype = reqtype



    def get_word(self, word, reqtype=None):

        """
        if user provided reqtype in the call, use that, otherwise
        use self.reqtype. if neither exist, return an error
        """
        if type(word) != str:
            raise TypeError("invalid word passed in")
        else:
            if reqtype is None:
                if self.reqtype is not None:
                    reqtype = self.reqtype
                else:
                    raise TypeError("No request type specified")

            if self.secret_key is not None:
                if reqtype == 'json':
                    return self.get_json(word)

                elif reqtype == 'plain':
                    return self.get_plain(word)

                elif reqtype == 'xml':
                    return self.get_xml(word)

                elif reqtype == 'php':
                    return self.get_php(word)

                else:
                    raise TypeError("bad request type")
            else:
                raise ValueError("no API key specified")

    """
    provide specific calls for users who prefer these less abstract methods
    """
    def get_json(self, word):
        result = json.load(urllib.urlopen(
            'http://words.bighugelabs.com/api/2/'+self.secret_key+'/'+word+'/json'
        ))
        # need to do some checking in case we get a bad return from http
        return result

    def get_plain(self, word):
        pass

    def get_xml(self, word):
        pass

    def get_php(self, word):
        pass
