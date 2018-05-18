---
title: Changing the Retransmission Policy
description: The Microsoft WinSNMP implementation provides retransmission policy support by storing a time-out value and a retry count for the WinSNMP application in a database.
ms.assetid: '9ab45adc-12b7-40b1-8fec-40bf04302f64'
---

# Changing the Retransmission Policy

The Microsoft WinSNMP implementation provides retransmission policy support by storing a time-out value and a retry count for the WinSNMP application in a database. The implementation stores values for individual destination entities. The implementation initially supplies default values for these elements, but an application can add or modify values for individual entities.

A call to the [**SnmpGetTimeout**](snmpgettimeout.md) and [**SnmpGetRetry**](snmpgetretry.md) functions returns the time-out and retry count values for a specific destination entity. To change the time-out value, a WinSNMP application must call the [**SnmpSetTimeout**](snmpsettimeout.md) function. To change the retry count value the application must call the [**SnmpSetRetry**](snmpsetretry.md) function. The updated settings affect new SNMP message requests to the destination entity.

 

 




