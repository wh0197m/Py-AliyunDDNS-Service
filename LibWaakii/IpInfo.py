#-*- coding:utf-8 -*-

import requests
import re
import LibWaakii.AppLoggerLite as AppLogger
import time
import LibWaakii.AppConfig as AppConfig

class IpAddress(object):
    # 获取外网IP
    def parseOutIp(self,content):
        try:
            if content != None:
                ip = content
                
                # AppLogger.StandLogger.infoLog('取得外网IP成功,ip地址为(' + ip + ')')

                AppConfig.JsonConf().set({'last_ip':ip})
                
                return ip
            else:
                # AppLogger.StandLogger.warningLog('取得外网IP失败，可能原因（网络未连接）')
                return None
        except:
            return None

    def getIpServiceContent(self, url = 'https://ifconfig.me/ip'):
        try:
            r = requests.get(url)
            return r.text
        except:
            return None

    def getGatewayIp(self):
        return self.parseOutIp(self.getIpServiceContent())
