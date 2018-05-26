---
title: Support for IPX Address Strings in WinSNMP
description: WinSNMP 2.0 formalizes the use of IPX address strings.
ms.assetid: b90b8e95-dab0-483b-9336-07e20c122cba
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Support for IPX Address Strings in WinSNMP

WinSNMP 2.0 formalizes the use of IPX address strings. If you specify an IPX address string as an input parameter to the [**SnmpStrToEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtoentity?branch=master) function, you must format the string using the following standards:

-   A network number that consists of eight hexadecimal digits (zero-filled if necessary)
-   A separator (either ":", "." or " – ")
-   A node number that consists of 12 hexadecimal digits (zero-filled if necessary)

For example, 00000001:00081A0D01C2 or 00000001.00081a0d01c2. Hexadecimal digits can be uppercase or lowercase.

This is the format the [**SnmpEntityToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpentitytostr?branch=master) function uses to return an IPX address string. The string is returned when an application that is operating in one of the SNMPAPI\_UNTRANSLATED modes calls the **SnmpEntityToStr** function. The string can also be returned when the application is operating in SNMPAPI\_TRANSLATED mode and no user-friendly name is available for the entity.

 

 




