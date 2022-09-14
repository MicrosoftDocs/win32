---
title: Multiple Trap Registrations
description: Several options are available when a WinSNMP application registers a WinSNMP session for traps or notifications.
ms.assetid: 76a4095f-ab5c-4f7a-9b60-a383a632fd65
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Trap Registrations

Several options are available when a WinSNMP application registers a WinSNMP session for traps or notifications. Because of this, an application can call the [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister) function multiple times, in effect defining a custom filter for the reception of traps and notifications. For example, you can register for one type of trap or notification, or for all traps and notifications, depending on the value of the *notification* parameter. Additionally, the application can specify values in other parameters to the **SnmpRegister** function to further define the traps and notifications that should reach an application. For more information, see [Managing Traps and Notifications](managing-traps-and-notifications.md).

Following are instances in which multiple calls to **SnmpRegister** are redundant. In these instances **SnmpRegister** returns SNMPAPI\_SUCCESS if the function completes successfully, but the redundant registration is ineffective.

1.  A call to the [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister) function requesting filtered delivery of traps and notifications to the session, after a previous call to **SnmpRegister** requesting delivery of all traps and notifications (unfiltered delivery). This call is redundant because the session is already receiving all traps and notifications, including the single type defined by the filter.
2.  A duplicate call to **SnmpRegister**, or one in which the parameter list is identical to the parameter list in a previous call to **SnmpRegister** for the session.
3.  A call to the [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister) function requesting filtered delivery of traps and notifications based on an object identifier (OID) whose prefix is an OID specified in a previous call to **SnmpRegister**. For example, you can specify "1.3.6.1.4.1.311" in the *notification* parameter to receive notifications originating from any Microsoft SNMP agent entity. If you call **SnmpRegister** again and specify "1.3.6.1.4.1.311.1", the second call is redundant because the session is already receiving all traps and notifications that contain the OID prefix "1.3.6.1.4.1.311".

To unregister the session, you must match each unique registration call to the [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister) function. Call **SnmpRegister** to unregister the session, and ensure that the first five parameters to **SnmpRegister** are identical to those in the initial registration call. The only difference between the initial call and the unregistering call is that when registering you must specify the value SNMPAPI\_ON in the *status* parameter, and when you call the function to unregister, you must specify SNMPAPI\_OFF. You do not need to match redundant registration calls to the **SnmpRegister** function. You need only match the first unique registration call.

To change filtering criteria, it may be necessary for an application to first unregister and disable delivery of certain traps or notifications. Then the application can create a new filter by calling [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister), passing appropriate values.

 

 




