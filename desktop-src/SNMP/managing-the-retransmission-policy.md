---
title: Managing the Retransmission Policy
description: The WinSNMP application can request that the Microsoft WinSNMP implementation execute the application's retransmission policy. When the implementation manages retransmission, it uses the time-out period and the retry count values in its database.
ms.assetid: 1f1a9589-3566-4d90-ac4d-7acf69f34676
ms.topic: article
ms.date: 05/31/2018
---

# Managing the Retransmission Policy

The WinSNMP application can request that the Microsoft WinSNMP implementation execute the application's retransmission policy. When the implementation manages retransmission, it uses the time-out period and the retry count values in its database.

The implementation identifies the default retransmission mode in a return value from the [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup) function during initialization. The mode can be one of the following values.



| Value        | Meaning                                                                      |
|--------------|------------------------------------------------------------------------------|
| SNMPAPI\_ON  | The implementation is executing the application's retransmission policy.     |
| SNMPAPI\_OFF | The implementation is not executing the application's retransmission policy. |



 

A WinSNMP application can retrieve at any time the current retransmission mode in effect for the implementation by calling the [**SnmpGetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetretransmitmode) function. The WinSNMP API provides other [database functions](winsnmp-functions.md) that simplify management of the retransmission policy.

At any time during program execution, the WinSNMP application can adjust execution of the policy by performing one of the following steps:

-   Request that the implementation start or stop executing the retransmission policy by calling the [**SnmpSetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretransmitmode) function. For more information, see [Turning Retransmission On and Off](turning-retransmission-on-and-off.md).
-   Modify the time-out period and retry count values in the implementation's database. For more information, see [Changing the Retransmission Policy](changing-the-retransmission-policy.md).
-   Call the [**SnmpCancelMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcancelmsg) function to cancel the retransmission cycle and release internal data structures associated with a single SNMP message request. For more information, see [Canceling Retransmission](canceling-retransmission.md).

The application can execute its own retransmission policy. In this case, execution may or may not be based on the values in the database.

 

 




