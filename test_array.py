
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

        country = "KR"
        currency = "krw"
        #locale = "ko-KR"
        locale = "en-US"
        place_id = "SELA-sky"
        query= "서울"
        apiKey = "br275383206339467238375786905151"

        #request_query = "/apiservices/autosuggest/v1.0/%s/%s/%s?id=%s&apiKey=%s" % (country, currency, locale, place_id, apiKey)
        #request_query = "/apiservices/autosuggest/v1.0/%s/%s/%s?id=%s&apiKey=%s" % ('US', 'USD', 'en-US', place_id, apiKey)
        request_query = "/apiservices/autosuggest/v1.0/%s/%s/%s?query=%s&apiKey=%s" % (country, currency, locale, query, apiKey)
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
        contents = res.read()
        logging.debug(contents)
        dict = json.loads(contents)
        logging.debug(dict['Places'][0]['PlaceName'])
        conn.close()
        '''
        contents = json.loads(res.read())

        self.assertIsNone(contents)
        '''



if __name__ == '__main__':
    unittest.main()