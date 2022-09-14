---
title: Turning Retransmission On and Off
description: An application can set the retransmission mode with a call to the SnmpSetRetransmitMode function. The new retransmission mode applies to subsequent calls to the SnmpSendMsg function.
ms.assetid: 0e167014-2703-4942-91f0-c60a5c0d8e12
ms.topic: article
ms.date: 05/31/2018
---

# Turning Retransmission On and Off

An application can set the retransmission mode with a call to the [**SnmpSetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretransmitmode) function. The new retransmission mode applies to subsequent calls to the [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) function.

When the application calls **SnmpSetRetransmitMode** with the retransmission mode value SNMPAPI\_ON, the Microsoft WinSNMP implementation begins execution of the application's retransmission policy. The new retransmission mode does not affect outstanding SNMP messages. An outstanding message is one that has no response at the time the application changes the retransmission mode.

When the WinSNMP application calls the [**SnmpSetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretransmitmode) function with the retransmission mode value SNMPAPI\_OFF, the implementation stops executing the retransmission policy. The implementation cancels retransmission attempts for outstanding SNMP messages. This is because it may not be possible for the implementation to handle all outstanding SNMP requests and operations plus new requests, before an application time-out or retry counter signals an event.

 

 




