---
title: Creating a PDU
description: To create and initialize a PDU a WinSNMP application calls the SnmpCreatePdu function.
ms.assetid: '7f02a2c6-19bc-456f-bf04-3297d19000f6'
---

# Creating a PDU

To create and initialize a PDU a WinSNMP application calls the [**SnmpCreatePdu**](snmpcreatepdu.md) function. The application must call **SnmpCreatePdu** before it calls the [**SnmpSendMsg**](snmpsendmsg.md) function to request that the Microsoft WinSNMP implementation transmit a PDU. The application must also call [**SnmpCreatePdu**](snmpcreatepdu.md) before it calls the [**SnmpEncodeMsg**](snmpencodemsg.md) function to request encoding of an SNMP message.

The application must call the [**SnmpFreePdu**](snmpfreepdu.md) function to release the resources that the [**SnmpCreatePdu**](snmpcreatepdu.md) function allocates for new PDUs.

 

 




