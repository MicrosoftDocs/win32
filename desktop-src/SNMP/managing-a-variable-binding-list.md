---
title: Managing a Variable Binding List
description: The SnmpGetVb function retrieves variable binding information from a variable binding list. The function retrieves the variable name and the variable's associated value from the variable binding entry specified by the WinSNMP application.
ms.assetid: '357aebd6-171a-4221-b12a-712702f9d9c6'
---

# Managing a Variable Binding List

The [**SnmpGetVb**](snmpgetvb.md) function retrieves variable binding information from a variable binding list. The function retrieves the variable name and the variable's associated value from the variable binding entry specified by the WinSNMP application.

To update variable binding entries in a variable binding list, call the [**SnmpSetVb**](snmpsetvb.md) function. The **SnmpSetVb** function also appends new variable binding entries to an existing variable binding list.

The WinSNMP application must call the [**SnmpDeleteVb**](snmpdeletevb.md) function to remove entries from a variable binding list.

To retrieve, modify or delete a variable binding entry, the WinSNMP application must specify the position of the entry in the variable binding list.

A call to the [**SnmpSetPduData**](snmpsetpdudata.md) function associates a variable binding list with a PDU. A call to the [**SnmpGetPduData**](snmpgetpdudata.md) function retrieves a variable binding list from a PDU. An individual variable binding is not directly associated with a PDU, but it is indirectly associated through its inclusion in a variable binding list.

 

 




