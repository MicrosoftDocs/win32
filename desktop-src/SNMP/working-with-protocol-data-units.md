---
title: Working with Protocol Data Units
description: The Simple Network Management Protocol (SNMP) sends operation requests and responses as SNMP messages.
ms.assetid: 0928981c-4d60-4583-9eef-8127e05b1ba8
keywords:
- Working with Protocol Data Units SNMP
- Protocol Data Units SNMP , working with
ms.topic: article
ms.date: 05/31/2018
---

# Working with Protocol Data Units

The Simple Network Management Protocol (SNMP) sends operation requests and responses as SNMP messages. An SNMP message is an SNMP protocol data unit (PDU) plus additional message header elements defined by the relevant RFC. A PDU includes a variable binding list.

The structure of a PDU is restricted to the Microsoft WinSNMP implementation. A WinSNMP application can access a PDU with a handle of the type **HSNMP\_PDU**. The WinSNMP application must create a PDU before it calls the [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) function or the [**SnmpEncodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpencodemsg) function.

The application can extract and update the data elements of a PDU, and release resources allocated for PDUs. To perform these operations, the application uses the WinSNMP [PDU functions](winsnmp-functions.md). The following table lists topics that discuss working with PDUs in the WinSNMP programming environment.



| Topic                                                                        | Description                                                        |
|------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Creating a PDU](creating-a-pdu.md)                                         | Describes how to create a PDU.                                     |
| [Updating a PDU](updating-a-pdu.md)                                         | Describes how to retrieve and update PDU fields.                   |
| [Duplicating a PDU](duplicating-a-pdu.md)                                   | Describes how to duplicate a PDU.                                  |
| [Validating a PDU](validating-a-pdu.md)                                     | Describes the validation of a PDU.                                 |
| [Matching Response and Request PDUs](matching-response-and-request-pdus.md) | Describes the process of matching a response PDU to a request PDU. |



 

For more information, see [Working with Variable Binding Lists](working-with-variable-binding-lists.md) and [Resource Handle Objects](resource-handle-objects.md).

 

 




