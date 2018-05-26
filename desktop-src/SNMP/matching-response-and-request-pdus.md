---
title: Matching Response and Request PDUs
description: The order in which the WinSNMP application receives SNMP responses may not match the order in which the application submits SNMP operation requests.
ms.assetid: cd09cc4b-2ef6-4d2f-8f0f-b83d8df8599a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Matching Response and Request PDUs

The order in which the WinSNMP application receives SNMP responses may not match the order in which the application submits SNMP operation requests. To match the response with the request, the application must use the request identifier field (the **request\_id**) of the response.

The **request\_id** field is a unique numeric value that identifies the PDU. Applications can assign request identifiers by calling the [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master) function or the [**SnmpSetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetpdudata?branch=master) function. Call the [**SnmpGetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetpdudata?branch=master) function to retrieve a PDU's **request\_id**.

 

 




