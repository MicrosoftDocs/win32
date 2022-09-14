---
title: Assigning Request Identifiers
description: A WinSNMP application can call the SnmpCreatePdu function or the SnmpSetPduData function to assign an application-generated request identifier to a PDU. The application must pass the value in the request\_id parameter.
ms.assetid: 72559054-982f-4c2b-83d2-268f130f6ea2
ms.topic: article
ms.date: 05/31/2018
---

# Assigning Request Identifiers

A WinSNMP application can call the [**SnmpCreatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu) function or the [**SnmpSetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata) function to assign an application-generated request identifier to a PDU. The application must pass the value in the *request\_id* parameter.

An application can request that the Microsoft WinSNMP implementation generate and assign a request identifier to a PDU by passing zero in the *request\_id* parameter of the [**SnmpCreatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu) function. The application can retrieve the assigned request identifier with a call to the [**SnmpGetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetpdudata) function.

To assign a request identifier equal to a specific value, including zero, the application must pass that value in the *request\_id* parameter of the [**SnmpSetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata) function.

When the implementation executes the application's retransmission policy, it includes the **request\_id** field of the original PDU in each retransmitted SNMP message. For more information, see [About Retransmission](about-retransmission.md) and [Managing the Retransmission Policy](managing-the-retransmission-policy.md).

> [!Note]  
> When the implementation receives traps from an SNMPv1 entity, it assigns a non-zero value to the **request\_id** field of the PDU. This value may duplicate a request identifier used by the application in a request PDU. Applications must check for duplication.

 

 

 




