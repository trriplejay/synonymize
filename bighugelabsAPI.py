import json
import urllib
"""
python 2.7 API info for bighugelabs.com thesaurus

Keep API key in a separate file (named secret_key.py), and add it to
.gitignore, then import API_KEY from it.
"""


class BigHugeLabAPI(object):

    def __init__(secret_key=None, reqtype=None):
        # get API key by creating an account on words.bighugelabs.com
        self.secret_key = secret_key
        self.reqtype = reqtype



    def get_word(self, word, reqtype=None):

        """
        if user provided reqtype in the call, use that, otherwise
        use self.reqtype. if neither exist, return an error
        """
        if reqtype is None:
            if self.reqtype is not None:
                reqtype = self.reqtype
            else:
                return "need to specify a request type"
        if self.secret_key is not None:
            if reqtype == 'json':
                return get_json(word)

            elif reqtype == 'plain':
                return get_plain(word)

            elif reqtype == 'xml':
                return get_xml(word)

            elif reqtype == 'php':
                return get_php(word)

            else:
                return "bad reqtype"
        else:
            return "no API key specified"

    """
    provide specific calls for users who prefer these less abstract methods
    """
    def get_json(self, word):
        return json.load(urllib.urlopen(
            'http://words.bighugelabs.com/api/2/',
            + self.secret_key+'/'+word+'/json'
        ))

    def get_plain(self, word):
        pass

    def get_xml(self, word):
        pass

    def get_php(self, word):
        pass
