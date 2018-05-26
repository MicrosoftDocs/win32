---
title: Receiving SNMP Messages
description: The WinSNMP application must call the SnmpRecvMsg function to retrieve the response to an SnmpSendMsg request.
ms.assetid: 323a5565-a8a5-4efd-aa4e-e4623b581d09
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiving SNMP Messages

The WinSNMP application must call the [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) function to retrieve the response to an [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master) request.

The [**SnmpCreateSession**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master) function passes an application window handle and a notification message identifier to the Microsoft WinSNMP implementation. When the application window receives this message, it signals the application to call the [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) function using the session handle returned by [**SnmpCreateSession**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master).

The [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) function returns two entity handles, a context handle, and the handle to a PDU. It is recommended that the WinSNMP application free these resources using the [**SnmpFreeEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreeentity?branch=master), [**SnmpFreeContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreecontext?branch=master), and [**SnmpFreePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreepdu?branch=master) functions.

For additional information about managing the time between a call to the [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master) function and the receipt of the corresponding response, see [About Retransmission](about-retransmission.md). For additional information about using the **request\_id** PDU field to match a response PDU with its request PDU, see [Matching Response and Request PDUs](matching-response-and-request-pdus.md).

 

 




