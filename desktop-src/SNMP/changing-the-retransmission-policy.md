---
title: Changing the Retransmission Policy
description: The Microsoft WinSNMP implementation provides retransmission policy support by storing a time-out value and a retry count for the WinSNMP application in a database.
ms.assetid: 9ab45adc-12b7-40b1-8fec-40bf04302f64
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Retransmission Policy

The Microsoft WinSNMP implementation provides retransmission policy support by storing a time-out value and a retry count for the WinSNMP application in a database. The implementation stores values for individual destination entities. The implementation initially supplies default values for these elements, but an application can add or modify values for individual entities.

A call to the [**SnmpGetTimeout**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgettimeout) and [**SnmpGetRetry**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetretry) functions returns the time-out and retry count values for a specific destination entity. To change the time-out value, a WinSNMP application must call the [**SnmpSetTimeout**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettimeout) function. To change the retry count value the application must call the [**SnmpSetRetry**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretry) function. The updated settings affect new SNMP message requests to the destination entity.

 

 




