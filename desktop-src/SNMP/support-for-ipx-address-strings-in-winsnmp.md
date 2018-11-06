---
title: Support for IPX Address Strings in WinSNMP
description: WinSNMP 2.0 formalizes the use of IPX address strings.
ms.assetid: b90b8e95-dab0-483b-9336-07e20c122cba
ms.topic: article
ms.date: 05/31/2018
---

# Support for IPX Address Strings in WinSNMP

WinSNMP 2.0 formalizes the use of IPX address strings. If you specify an IPX address string as an input parameter to the [**SnmpStrToEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtoentity) function, you must format the string using the following standards:

-   A network number that consists of eight hexadecimal digits (zero-filled if necessary)
-   A separator (either ":", "." or " – ")
-   A node number that consists of 12 hexadecimal digits (zero-filled if necessary)

For example, 00000001:00081A0D01C2 or 00000001.00081a0d01c2. Hexadecimal digits can be uppercase or lowercase.

This is the format the [**SnmpEntityToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpentitytostr) function uses to return an IPX address string. The string is returned when an application that is operating in one of the SNMPAPI\_UNTRANSLATED modes calls the **SnmpEntityToStr** function. The string can also be returned when the application is operating in SNMPAPI\_TRANSLATED mode and no user-friendly name is available for the entity.

 

 




