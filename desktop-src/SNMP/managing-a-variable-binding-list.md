---
title: Managing a Variable Binding List
description: The SnmpGetVb function retrieves variable binding information from a variable binding list. The function retrieves the variable name and the variables associated value from the variable binding entry specified by the WinSNMP application.
ms.assetid: 357aebd6-171a-4221-b12a-712702f9d9c6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing a Variable Binding List

The [**SnmpGetVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetvb?branch=master) function retrieves variable binding information from a variable binding list. The function retrieves the variable name and the variable's associated value from the variable binding entry specified by the WinSNMP application.

To update variable binding entries in a variable binding list, call the [**SnmpSetVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetvb?branch=master) function. The **SnmpSetVb** function also appends new variable binding entries to an existing variable binding list.

The WinSNMP application must call the [**SnmpDeleteVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpdeletevb?branch=master) function to remove entries from a variable binding list.

To retrieve, modify or delete a variable binding entry, the WinSNMP application must specify the position of the entry in the variable binding list.

A call to the [**SnmpSetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetpdudata?branch=master) function associates a variable binding list with a PDU. A call to the [**SnmpGetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetpdudata?branch=master) function retrieves a variable binding list from a PDU. An individual variable binding is not directly associated with a PDU, but it is indirectly associated through its inclusion in a variable binding list.

 

 




