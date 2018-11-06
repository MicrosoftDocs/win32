---
title: About SNMP Messages
description: The Simple Network Management Protocol uses messages to communicate and exchange information between remote SNMP entities.
ms.assetid: 9ba4b854-fc02-40c1-a92f-7c102c900e95
ms.topic: article
ms.date: 05/31/2018
---

# About SNMP Messages

The Simple Network Management Protocol uses messages to communicate and exchange information between remote SNMP entities. SNMP messages contain protocol data units (PDUs) plus additional message header elements defined by the relevant RFC. A PDU is a data packet that contains SNMP data components (or fields).

The format of an SNMP message is the same for both SNMPv1 and SNMPv2C. However, SNMPv2C supports additional PDU types. For example, it supports the [SNMP\_PDU\_GETBULK](snmp-variable-types-and-request-pdu-types.md) request type, which enables an application to efficiently retrieve large blocks of data from target entities.

 

 




