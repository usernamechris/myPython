
# -*- coding: utf-8 -*-

import httplib
import json
import unittest
import logging


class sky_scanner(unittest.TestCase):

    def test_connection(self):
        logging.basicConfig(level=logging.DEBUG)

        conn = httplib.HTTPConnection('partners.api.skyscanner.net')
        self.assertIsNotNone(conn)

        contry = "KR"
        currency = "USD"
        locale = "en-US"
        query = "TYOA-sky"
        apiKey = "br275383206339467238375786905151"

        request_query = "/apiservices/autosuggest/v1.0/%s/%s/%s?query=%s&apiKey=%s" % (contry, currency, locale, query, apiKey)
        '''
        request_query = "/apiservices/reference/v1.0/locales?apiKey=%s" % apiKey
        '''
        logging.debug(request_query)

        '''
        conn.request(
            "GET",
            "/apiservices" +
            "/autosuggest/v1.0/" + contry + ""
            "apiKey=br275383206339467238375786905151"
        )
        '''

        conn.request("GET", request_query)

        res = conn.getresponse()
        self.assertIsNotNone(res)
        logging.debug(res.status)
        logging.debug(res.read())
        conn.close()
        '''
        contents = json.loads(res.read())

        self.assertIsNone(contents)
        '''



if __name__ == '__main__':
    unittest.main()