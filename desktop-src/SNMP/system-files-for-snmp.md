---
title: System Files for SNMP
description: The following table describes the principal files that relate to the SNMP service.
ms.assetid: 513d7c75-2f68-4d7d-897f-493089f045cd
ms.topic: article
ms.date: 05/31/2018
---

# System Files for SNMP

The following table describes the principal files that relate to the SNMP service.



| Filename     | Description                                                                                                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DHCPMIB.DLL  | Extension agent DLL that implements the Microsoft-defined DHCP MIB. Installed only on DHCP servers.                                                                                                                                 |
| EVNTAGNT.DLL | SNMP DLL that translates event logs into SNMP traps; also known as the SNMP event translator.                                                                                                                                       |
| HOSTMIB.DLL  | Extension agent DLL that implements the Host Resources MIB.                                                                                                                                                                         |
| LMMIB2.DLL   | Extension agent DLL that implements LAN Manager MIB-II.                                                                                                                                                                             |
| MGMTAPI.DLL  | Microsoft SNMP Management API library. This API allows SNMP manager applications to "listen" for SNMP manager requests, and send requests to and receive responses from SNMP agents.                                                |
| MIB.BIN      | Compiled MIB information used by MGMTAPI.DLL.                                                                                                                                                                                       |
| SNMP.EXE     | SNMP service. This is the master agent that receives SNMP requests and delivers them to the appropriate extension agent DLL.                                                                                                        |
| SNMPAPI.DLL  | SNMP utilities DLL used by SNMP extension agent DLLs and manager applications. This DLL contains a framework for developing extension agent DLLs.                                                                                   |
| SNMPSNAP.DLL | SNMP configuration application that is a Microsoft Management Console (MMC) snap-in component. The snap-in adds several pages to the SNMP Service Properties sheet. For more information, see the online help for the SNMP service. |
| SNMPTRAP.EXE | SNMP trap service. Receives SNMP traps and forwards them to SNMP manager applications.                                                                                                                                              |
| WINSMIB.DLL  | Extension agent DLL that implements the Microsoft-defined WINS MIB. Installed only on WINS servers.                                                                                                                                 |
| WSNMP32.DLL  | Microsoft [WinSNMP API](winsnmp-api.md) library. This API allows SNMP manager applications to "listen" for SNMP manager requests, and send requests to and receive responses from SNMP agents.                                     |



 

For additional information, see [The SNMP Management Information Base (MIB)](the-snmp-management-information-base-mib-.md). (You can also refer to the Windows 2000 Resource Kit.)

 

 




