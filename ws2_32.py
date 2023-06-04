## ###
#  IP: GHIDRA
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#       http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##
# Set names of ordinals for WS2_32.dll
# @category: Examples.Python

from ghidra.program.model.symbol.SourceType import *

# table from: https://github.com/phracker/HopperScripts/blob/master/WS2_32.dll%20Ordinals%20to%20Names.py

ordinals = {'Ordinal_1' : 'accept',
'Ordinal_2' : 'bind',
'Ordinal_3' : 'closesocket',
'Ordinal_4' : 'connect',
'Ordinal_5' : 'getpeername',
'Ordinal_6' : 'getsockname',
'Ordinal_7' : 'getsockopt',
'Ordinal_8' : 'htonl',
'Ordinal_9' : 'htons',
'Ordinal_10' : 'ioctlsocket',
'Ordinal_11' : 'inet_addr',
'Ordinal_12' : 'inet_ntoa',
'Ordinal_13' : 'listen',
'Ordinal_14' : 'ntohl',
'Ordinal_15' : 'ntohs',
'Ordinal_16' : 'recv',
'Ordinal_17' : 'recvfrom',
'Ordinal_18' : 'select',
'Ordinal_19' : 'send',
'Ordinal_20' : 'sendto',
'Ordinal_21' : 'setsockopt',
'Ordinal_22' : 'shutdown',
'Ordinal_23' : 'socket',
'Ordinal_24' : 'GetAddrInfoW',
'Ordinal_25' : 'GetNameInfoW',
'Ordinal_26' : 'WSApSetPostRoutine',
'Ordinal_27' : 'FreeAddrInfoW',
'Ordinal_28' : 'WPUCompleteOverlappedRequest',
'Ordinal_29' : 'WSAAccept',
'Ordinal_30' : 'WSAAddressToStringA',
'Ordinal_31' : 'WSAAddressToStringW',
'Ordinal_32' : 'WSACloseEvent',
'Ordinal_33' : 'WSAConnect',
'Ordinal_34' : 'WSACreateEvent',
'Ordinal_35' : 'WSADuplicateSocketA',
'Ordinal_36' : 'WSADuplicateSocketW',
'Ordinal_37' : 'WSAEnumNameSpaceProvidersA',
'Ordinal_38' : 'WSAEnumNameSpaceProvidersW',
'Ordinal_39' : 'WSAEnumNetworkEvents',
'Ordinal_40' : 'WSAEnumProtocolsA',
'Ordinal_41' : 'WSAEnumProtocolsW',
'Ordinal_42' : 'WSAEventSelect',
'Ordinal_43' : 'WSAGetOverlappedResult',
'Ordinal_44' : 'WSAGetQOSByName',
'Ordinal_45' : 'WSAGetServiceClassInfoA',
'Ordinal_46' : 'WSAGetServiceClassInfoW',
'Ordinal_47' : 'WSAGetServiceClassNameByClassIdA',
'Ordinal_48' : 'WSAGetServiceClassNameByClassIdW',
'Ordinal_49' : 'WSAHtonl',
'Ordinal_50' : 'WSAHtons',
'Ordinal_51' : 'gethostbyaddr',
'Ordinal_52' : 'gethostbyname',
'Ordinal_53' : 'getprotobyname',
'Ordinal_54' : 'getprotobynumber',
'Ordinal_55' : 'getservbyname',
'Ordinal_56' : 'getservbyport',
'Ordinal_57' : 'gethostname',
'Ordinal_58' : 'WSAInstallServiceClassA',
'Ordinal_59' : 'WSAInstallServiceClassW',
'Ordinal_60' : 'WSAIoctl',
'Ordinal_61' : 'WSAJoinLeaf',
'Ordinal_62' : 'WSALookupServiceBeginA',
'Ordinal_63' : 'WSALookupServiceBeginW',
'Ordinal_64' : 'WSALookupServiceEnd',
'Ordinal_65' : 'WSALookupServiceNextA',
'Ordinal_66' : 'WSALookupServiceNextW',
'Ordinal_67' : 'WSANSPIoctl',
'Ordinal_68' : 'WSANtohl',
'Ordinal_69' : 'WSANtohs',
'Ordinal_70' : 'WSAProviderConfigChange',
'Ordinal_71' : 'WSARecv',
'Ordinal_72' : 'WSARecvDisconnect',
'Ordinal_73' : 'WSARecvFrom',
'Ordinal_74' : 'WSARemoveServiceClass',
'Ordinal_75' : 'WSAResetEvent',
'Ordinal_76' : 'WSASend',
'Ordinal_77' : 'WSASendDisconnect',
'Ordinal_78' : 'WSASendTo',
'Ordinal_79' : 'WSASetEvent',
'Ordinal_80' : 'WSASetServiceA',
'Ordinal_81' : 'WSASetServiceW',
'Ordinal_82' : 'WSASocketA',
'Ordinal_83' : 'WSASocketW',
'Ordinal_84' : 'WSAStringToAddressA',
'Ordinal_85' : 'WSAStringToAddressW',
'Ordinal_86' : 'WSAWaitForMultipleEvents',
'Ordinal_87' : 'WSCDeinstallProvider',
'Ordinal_88' : 'WSCEnableNSProvider',
'Ordinal_89' : 'WSCEnumProtocols',
'Ordinal_90' : 'WSCGetProviderPath',
'Ordinal_91' : 'WSCInstallNameSpace',
'Ordinal_92' : 'WSCInstallProvider',
'Ordinal_93' : 'WSCUnInstallNameSpace',
'Ordinal_94' : 'WSCUpdateProvider',
'Ordinal_95' : 'WSCWriteNameSpaceOrder',
'Ordinal_96' : 'WSCWriteProviderOrder',
'Ordinal_97' : 'freeaddrinfo',
'Ordinal_98' : 'getaddrinfo',
'Ordinal_99' : 'getnameinfo',
'Ordinal_101' : 'WSAAsyncSelect',
'Ordinal_102' : 'WSAAsyncGetHostByAddr',
'Ordinal_103' : 'WSAAsyncGetHostByName',
'Ordinal_104' : 'WSAAsyncGetProtoByNumber',
'Ordinal_105' : 'WSAAsyncGetProtoByName',
'Ordinal_106' : 'WSAAsyncGetServByPort',
'Ordinal_107' : 'WSAAsyncGetServByName',
'Ordinal_108' : 'WSACancelAsyncRequest',
'Ordinal_109' : 'WSASetBlockingHook',
'Ordinal_110' : 'WSAUnhookBlockingHook',
'Ordinal_111' : 'WSAGetLastError',
'Ordinal_112' : 'WSASetLastError',
'Ordinal_113' : 'WSACancelBlockingCall',
'Ordinal_114' : 'WSAIsBlocking',
'Ordinal_115' : 'WSAStartup',
'Ordinal_116' : 'WSACleanup',
'Ordinal_151' : '__WSAFDIsSet',
'Ordinal_500' : 'WEP'
}

# Get imports
sm = currentProgram.getSymbolTable()
symb = sm.getExternalSymbols()
number_of_symbols = len(symb)
monitor.initialize(number_of_symbols)
for i in range():
    monitor.incrementProgress(1) # update the progress
    symbol = symb[i]
    parent_namespace = symbol.getParentNamespace().getName()
    symbol_name = symbol.getName()
    monitor.checkCanceled() # check to see if the user clicked cancel
    monitor.setMessage("Working on {}".format(symbol_name)) # update the status message
    # symbol matches "WS2_32.DLL::Ordinal_.*"
    if parent_namespace.find("WS2_32.DLL") != -1:
        if symbol_name.find("Ordinal_") == 0:
            new_name = ordinals[symbol_name]
            print("{}:{}".format(symbol_name, new_name))
            symbol.setName(new_name, USER_DEFINED)