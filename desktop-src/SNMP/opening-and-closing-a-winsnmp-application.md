---
title: Opening and Closing a WinSNMP Application
description: The WinSNMP application must call the SnmpStartup function successfully before it calls any other WinSNMP function.
ms.assetid: 'ff2b99c9-c2fd-4bb7-8fd5-799e72c4560d'
---

# Opening and Closing a WinSNMP Application

The WinSNMP application must call the [**SnmpStartup**](snmpstartup.md) function successfully before it calls any other WinSNMP function. The **SnmpStartup** function enables the Microsoft WinSNMP implementation to perform initialization procedures. The function also returns to the application the version of the WinSNMP API that the implementation supports, the level of SNMP communications it supports, and the implementation's default translation and retransmission modes.

The WinSNMP application must call the [**SnmpCleanup**](snmpcleanup.md) function when the application no longer requires the implementation's services. Even though **SnmpCleanup** enables the implementation to deallocate all resources allocated to the application, it is recommended that the application first call the [**SnmpClose**](snmpclose.md) function once for each open WinSNMP session, to maximize the implementation's performance. The WinSNMP application must call [**SnmpCleanup**](snmpcleanup.md) as the last WinSNMP function before it terminates.

 

 




