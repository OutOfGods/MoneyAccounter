import unittest
from io import StringIO, BytesIO

import pickle_serialization
import json_serialization
import yaml_serialization
import accounter as ac


class SerializationTest(unittest.TestCase):
    acc = ac.Accounter()
    acc.add_new_data(123, "test", "20170404")
    acc.add_new_data(321, "test1", "20170404")

    def test_pickle_save(self):
        outfile = BytesIO()
        pickle_serialization.serialize(self.acc, outfile)
        content = outfile.getvalue()
        self.assertEqual(content, b'\x80\x03cpandas.core.frame\nDataFrame\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00'
                                  b'\x00_dataq\x03cpandas.core.internals\nBlockManager\nq\x04)\x81q\x05(]q'
                                  b'\x06(cpandas.indexes.base\n_new_Index\nq\x07cpandas.indexes.base\nIndex'
                                  b'\nq\x08}q\t(X\x04\x00\x00\x00dataq\ncnumpy.core.multiarray\n_reconstruct'
                                  b'\nq\x0bcnumpy\nndarray\nq\x0cK\x00\x85q\rC\x01bq\x0e\x87q\x0fRq\x10(K\x01K'
                                  b'\x03\x85q\x11cnumpy\ndtype\nq\x12X\x02\x00\x00\x00O4q\x13K\x00K\x01\x87q'
                                  b'\x14Rq\x15(K\x03X\x01\x00\x00\x00|q\x16NNNJ\xff\xff\xff\xffJ\xff\xff\xff'
                                  b'\xffK?tq\x17b\x89]q\x18(X\x07\x00\x00\x00commentq\x19X\x04\x00\x00\x00dateq'
                                  b'\x1aX\x05\x00\x00\x00valueq\x1betq\x1cbX\x04\x00\x00\x00nameq\x1dNu\x86q\x1eRq'
                                  b'\x1fh\x07cpandas.indexes.range\nRangeIndex\nq }q!(h\x1dNX\x05\x00\x00\x00startq"K'
                                  b'\x00X\x04\x00\x00\x00stopq#K\x02X\x04\x00\x00\x00stepq$K\x01u\x86q%Rq&e]q\'(h'
                                  b'\x0bh\x0cK\x00\x85q(h\x0e\x87q)Rq*(K\x01K\x01K\x02\x86q+h\x15\x89]q,(X\x04\x00'
                                  b'\x00\x00testq-X\x05\x00\x00\x00test1q.etq/bh\x0bh\x0cK\x00\x85q0h\x0e\x87q1Rq2(K'
                                  b'\x01K\x01K\x02\x86q3h\x12X\x02\x00\x00\x00M8q4K\x00K\x01\x87q5Rq6(K\x04X\x01\x00'
                                  b'\x00\x00<q7NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00}q8(C\x02nsq9K\x01K\x01K'
                                  b'\x01tq:\x86q;tq<b\x89C\x10\x00\x00T\xfa\xb4\x08\xb2\x14\x00\x00T\xfa\xb4\x08\xb2'
                                  b'\x14q=tq>bh\x0bh\x0cK\x00\x85q?h\x0e\x87q@RqA(K\x01K\x01K\x02\x86qBh\x12X\x02\x00'
                                  b'\x00\x00i8qCK\x00K\x01\x87qDRqE(K\x03h7NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK'
                                  b'\x00tqFb\x89C\x10{\x00\x00\x00\x00\x00\x00\x00A\x01\x00\x00\x00\x00\x00'
                                  b'\x00qGtqHbe]qI(h\x07h\x08}qJ(h\nh\x0bh\x0cK\x00\x85qKh\x0e\x87qLRqM(K\x01K\x01'
                                  b'\x85qNh\x15\x89]qOh\x19atqPbh\x1dNu\x86qQRqRh\x07h\x08}qS(h\nh\x0bh\x0cK\x00'
                                  b'\x85qTh\x0e\x87qURqV(K\x01K\x01\x85qWh\x15\x89]qXh\x1aatqYbh\x1dNu\x86qZRq[h'
                                  b'\x07h\x08}q\\(h\nh\x0bh\x0cK\x00\x85q]h\x0e\x87q^Rq_(K\x01K\x01\x85q`h\x15'
                                  b'\x89]qah\x1batqbbh\x1dNu\x86qcRqde}qeX\x06\x00\x00\x000.14.1qf}qg(X\x04\x00'
                                  b'\x00\x00axesqhh\x06X\x06\x00\x00\x00blocksqi]qj(}qk(X\x06\x00\x00\x00valuesqlh*X'
                                  b'\x08\x00\x00\x00mgr_locsqmcbuiltins\nslice\nqnK\x00K\x01K\x01'
                                  b'\x87qoRqpu}qq(hlh2hmhnK\x01K\x02K\x01\x87qrRqsu}qt(hlhAhmhnK\x02K\x03K\x01'
                                  b'\x87quRqvueustqwbX\x04\x00\x00\x00_typqxX\t\x00\x00\x00dataframeqyX'
                                  b'\t\x00\x00\x00_metadataqz]q{ub.')

    def test_json_save(self):
        outfile = StringIO()
        json_serialization.serialize(self.acc, outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertEqual(content, "[{\"comment\": \"test\", \"date\": \"2017-04-04 00:00:00\", \"value\": 123}, {"
                                  "\"comment\": \"test1\", \"date\": \"2017-04-04 00:00:00\", \"value\": 321}]")

    def test_yaml_save(self):
        outfile = StringIO()
        yaml_serialization.serialize(self.acc, outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertEqual(content, "- {comment: test, date: '2017-04-04 00:00:00', value: 123}"
                                  "\n- {comment: test1, date: '2017-04-04 00:00:00', value: 321}\n")

    def test_pickle_load(self):
        outfile = BytesIO()
        pickle_serialization.serialize(self.acc, outfile)
        outfile.seek(0)
        content = pickle_serialization.deserialize(outfile)
        self.assertEqual(str(content), str(self.acc))

    def test_json_load(self):
        outfile = StringIO()
        json_serialization.serialize(self.acc, outfile)
        outfile.seek(0)
        content = json_serialization.deserialize(outfile)
        self.assertEqual(str(content), "  comment      date  value\n"
                                       "0    test  20170404    123\n"
                                       "1   test1  20170404    321")

    def test_yaml_load(self):
        outfile = StringIO()
        yaml_serialization.serialize(self.acc, outfile)
        outfile.seek(0)
        content = yaml_serialization.deserialize(outfile)
        self.assertEqual(str(content), "  comment      date  value\n"
                                       "0    test  20170404    123\n"
                                       "1   test1  20170404    321")

