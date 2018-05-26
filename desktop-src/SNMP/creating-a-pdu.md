---
title: Creating a PDU
description: To create and initialize a PDU a WinSNMP application calls the SnmpCreatePdu function.
ms.assetid: 7f02a2c6-19bc-456f-bf04-3297d19000f6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a PDU

To create and initialize a PDU a WinSNMP application calls the [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master) function. The application must call **SnmpCreatePdu** before it calls the [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master) function to request that the Microsoft WinSNMP implementation transmit a PDU. The application must also call [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master) before it calls the [**SnmpEncodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpencodemsg?branch=master) function to request encoding of an SNMP message.

The application must call the [**SnmpFreePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreepdu?branch=master) function to release the resources that the [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master) function allocates for new PDUs.

 

 




