---
title: Receiving SNMP Messages
description: The WinSNMP application must call the SnmpRecvMsg function to retrieve the response to an SnmpSendMsg request.
ms.assetid: '323a5565-a8a5-4efd-aa4e-e4623b581d09'
---

# Receiving SNMP Messages

The WinSNMP application must call the [**SnmpRecvMsg**](snmprecvmsg.md) function to retrieve the response to an [**SnmpSendMsg**](snmpsendmsg.md) request.

The [**SnmpCreateSession**](snmpcreatesession.md) function passes an application window handle and a notification message identifier to the Microsoft WinSNMP implementation. When the application window receives this message, it signals the application to call the [**SnmpRecvMsg**](snmprecvmsg.md) function using the session handle returned by [**SnmpCreateSession**](snmpcreatesession.md).

The [**SnmpRecvMsg**](snmprecvmsg.md) function returns two entity handles, a context handle, and the handle to a PDU. It is recommended that the WinSNMP application free these resources using the [**SnmpFreeEntity**](snmpfreeentity.md), [**SnmpFreeContext**](snmpfreecontext.md), and [**SnmpFreePdu**](snmpfreepdu.md) functions.

For additional information about managing the time between a call to the [**SnmpSendMsg**](snmpsendmsg.md) function and the receipt of the corresponding response, see [About Retransmission](about-retransmission.md). For additional information about using the **request\_id** PDU field to match a response PDU with its request PDU, see [Matching Response and Request PDUs](matching-response-and-request-pdus.md).

 

 




