---
title: About Traps and Notifications
description: One type of message an SNMP agent application can send to a WinSNMP application is an asynchronous message that informs the application of a significant event.
ms.assetid: 5249c5a5-9260-4a67-b00f-a12214012bb3
ms.topic: article
ms.date: 05/31/2018
---

# About Traps and Notifications

One type of message an SNMP agent application can send to a WinSNMP application is an asynchronous message that informs the application of a significant event. An example of a significant event is when a network link shuts down or when an authentication failure occurs.

These types of messages are called traps under SNMPv1 and notifications under SNMPv2C. The Microsoft WinSNMP implementation always translates SNMPv1 traps to the SNMPv2C format, as defined by RFC 1908.

When you call the [**SnmpCreatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu) function to create a trap PDU, you can create only an SNMPv2C trap PDU. The only type of trap PDU you can update with a call to the [**SnmpSetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata) function is an SNMPv2C trap PDU.

For more information, see the following topics.



| Topic                                                                                    | Description |
|------------------------------------------------------------------------------------------|-------------|
| [Translating Traps from SNMPv1 to SNMPv2C](translating-traps-from-snmpv1-to-snmpv2c.md) |             |
| [Trap Formats](trap-formats.md)                                                         |             |



 

 

 




