---
title: About Retransmission
description: A WinSNMP application can make SNMP operation requests in various ways.
ms.assetid: 71150a66-74a3-4957-bc70-3dd25c3b9c71
ms.topic: article
ms.date: 05/31/2018
---

# About Retransmission

A WinSNMP application can make SNMP operation requests in various ways. The application can issue several requests to an SNMP agent, without waiting for a response, or it can issue a single request and wait for the response. Since SNMP can be implemented on multiple transport protocols, delivery mechanisms and reliability characteristics can vary.

When you code the WinSNMP application you must determine the level of reliability you need for communications operations, based on the way the application issues operation requests. Then you must select a retransmission strategy and implement a retransmission policy.

A retransmission policy includes a time-out period and a retry count. A time-out period is the elapsed time, in hundredths of a second, between an application's issuance of an [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) request and its receipt of the corresponding message. The application receives the message as a result of a call to the [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function. The time-out value is the period of time the Microsoft WinSNMP implementation waits for an entity to respond to a communication request. If there is no response within the time-out period, the implementation either retransmits the request if the retry count value specifies retransmission attempts, or it fails the call to [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg). A retry count is the maximum number of retransmission attempts the implementation makes if an SNMP transmission request fails.

The implementation stores time-out values and retry counts in its database for the application. The implementation stores individual values for each destination entity.

Applications must establish their own polling frequencies and they must manage timer variables. For more information, see [Managing the Retransmission Policy](managing-the-retransmission-policy.md).

 

 




