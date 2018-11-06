---
title: Setting the Entity and Context Translation Mode
description: The WinSNMP application can specify the interpretation and translation of entity and context parameters by setting the entity and context translation mode. The Microsoft WinSNMP implementation stores the mode in a database.
ms.assetid: 2550f235-1351-440a-8b4e-f0d30b058229
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Entity and Context Translation Mode

The WinSNMP application can specify the interpretation and translation of entity and context parameters by setting the entity and context translation mode. The Microsoft WinSNMP implementation stores the mode in a database.

The setting of the entity and context translation mode determines the manner in which the [**SnmpStrToEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtoentity) function and the [**SnmpStrToContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtocontext) function interpret input strings. The setting also determines the type of output string that the [**SnmpEntityToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpentitytostr) and the [**SnmpContextToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcontexttostr) functions return. For more information, see [Support for IPX Address Strings in WinSNMP](support-for-ipx-address-strings-in-winsnmp.md).

The implementation returns the current default entity and context translation mode in the *nTranslateMode* parameter of the [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup) function. To retrieve the current entity and context translation mode in effect for the implementation, an application can call the [**SnmpGetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgettranslatemode) function at any time.

The valid entity and context translation modes follow.

| Mode                      | Meaning                                                                                                                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SNMPAPI\_TRANSLATED       | The implementation uses its database to translate user-friendly names for SNMP entities and managed objects. The implementation translates them into their SNMPv1 or SNMPv2C components.                                                                                                  |
| SNMPAPI\_UNTRANSLATED\_V1 | The implementation interprets SNMP entity parameters as literal SNMP transport addresses, and context parameters as literal SNMP community strings. For SNMPv2 destination entities, the implementation creates outgoing SNMP messages that contain a value of zero in the version field. |
| SNMPAPI\_UNTRANSLATED\_V2 | The implementation interprets SNMP entity parameters as SNMP transport addresses, and context parameters as literal SNMP community strings. For SNMPv2 destination entities, the implementation creates outgoing SNMP messages that contain a value of 1 in the version field.            |



 

The implementation tries to associate resources in its database with the literal transport address of the management entity.

To change the entity and context translation mode setting a WinSNMP application must call the [**SnmpSetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettranslatemode) function. If the requested translation mode is invalid, the function fails, and [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror) returns the error code SNMPAPI\_MODE\_INVALID.

 

 




