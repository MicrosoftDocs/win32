---
title: Software Requirements for the WinSNMP API
description: A WinSNMP application must access the WinSNMP API through the dynamic-link library WSNMP32.DLL.
ms.assetid: ba0b9443-3fcf-41e2-993e-54e042f9d785
ms.topic: article
ms.date: 05/31/2018
---

# Software Requirements for the WinSNMP API

A WinSNMP application must access the WinSNMP API through the dynamic-link library WSNMP32.DLL.

The following files are required to support the functionality of the WinSNMP API.



| Filename     | Description                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| WSNMP32.LIB  | WinSNMP Library                                                                              |
| WSNMP32.DLL  | Provides WinSNMP interface                                                                   |
| WINSNMP.H    | WinSNMP header file                                                                          |
| SNMPTRAP.EXE | Receives SNMP traps and forwards them to MGMTAPI.DLL, the Microsoft SNMP Manager API library |
| SNMPAPI.DLL  | Provides SNMP utilities                                                                      |



 

 

 




