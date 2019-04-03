#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import json
import os
import re
import sys
import urllib
from datetime import datetime
import LibWaakii.IpInfo as IpInfo
import LibWaakii.AppLoggerLite as AppLogger
import LibWaakii.AppGlobal as AppGlobal
import LibWaakii.AppConfig as AppConfig
import json
import LibWaakii.AliYunDns as DDNS

def main():
    AppGlobal.setAppPath(os.path.split(os.path.realpath(__file__))[0])

    oIpAddress = IpInfo.IpAddress()
    print(oIpAddress.getGatewayIp())
    AppLogger.StandLogger.debugLog('debug-log')
    AppLogger.StandLogger.infoLog('info-log')
    AppLogger.StandLogger.warningLog('warning-log')

    data = {
        'interval':'60',
        'last_ip':'',
    }

    oAppConfig = AppConfig.JsonConf()
    #oAppConfig.store(data)
    loadConfig = oAppConfig.load()
    print(loadConfig)
    #oAppConfig.set({'last_ip':'114.114.114.114'})
    
    oDNSWorker = DDNS.DNSWorker("solab.com.cn",loadConfig['access_key_id'],loadConfig['access_Key_secret'],'cn-hangzhou')
    print(oDNSWorker.getAliyunDnsRecord())
    # print(oDNSWorker.get_record_id())
    print(oDNSWorker.get_record_id_all())
    #print(oDNSWorker.get_record_value())

if __name__ == '__main__':
    main()