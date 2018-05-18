---
title: LDAP\_SERVER\_SORT\_OID control code
description: Used with an extended LDAP search function to instruct the server to sort the search results before returning it to the client application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '03c51778-45ed-46de-94a2-425bf7030cf0'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["LDAP_SERVER_SORT_OID control code LDAP"]
topic_type:
- apiref
api_name:
- LDAP_SERVER_SORT_OID
api_location:
- Winldap.h
api_type:
- HeaderDef
---

# LDAP\_SERVER\_SORT\_OID control code

The LDAP\_SERVER\_SORT\_OID control is used with an extended LDAP search function to instruct the server to sort the search results before returning it to the client application. The control specifies the sort key and sort behavior to be used by the server.

To use this control, format the control contents using the [**ldap\_create\_sort\_control**](ldap-create-sort-control.md) function, or set the members of the [**LDAPControl**](ldapcontrol.md) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_SORT_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_SORT\_OID, which is defined as "1.2.840.113556.1.4.473".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence of parameters that enables the application to specify the sort keys and matching rules, if any. In the [**berval**](berval.md) structure, set **bv\_val** to a pointer to the sequence that contains the sort key data and set **bv\_len** to the length of the sequence. For more information, see Remarks.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether sorting the search results is critical to the application.

</dd> </dl>

## Remarks

The Sort control is used with the extended search functions, such as [**ldap\_search\_ext**](ldap-search-ext.md), to specify the key or keys used by the server to sort the search results before returning them to the client. The **ldctl\_value** field is set to the following BER-encoded sequence.


```C++
Sequence of Sequence {
  attributeType    OCTET STRING,
  orderingRule     MatchingRuleID (optional),
  reverseOrder     BOOLEAN
}
```



The [**ber\_printf**](ber-printf.md) function is used to create the sequence data. The sort key list sequence is in order of highest to lowest sort key precedence.

The following table lists the sequence fields.



| Sequence data                | Description                                                                                                                                                                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **attributeType**<br/> | This is an OCTET STRING that describes the DS attribute used as a sort key, such as "Name", "PrimaryPhone", "Address", and so on. If multiple **attributeType** sort keys are specified, the server returns an **unwillingToPerform** error.<br/> |
| **orderingRule**<br/>  | This specifies a matching rule that will cause the sort to be performed according to the specified rule.<br/>                                                                                                                                     |
| **reverseOrder**<br/>  | This **BOOLEAN** flag specifies that the search results are sorted in reverse order. The default value is **FALSE**.<br/>                                                                                                                         |



 

### 

The matching rules, listed in the following table, are supported. The search results will be sorted according to the specified locale.



| Locale | Matching rule ID          | Language                        |
|--------|---------------------------|---------------------------------|
| 0x0436 | (1.2.840.113556.1.4.1461) | Afrikaans                       |
| 0x041C | (1.2.840.113556.1.4.1462) | Albanian                        |
| 0x0401 | (1.2.840.113556.1.4.1463) | Arabic:Saudi Arabia             |
| 0x0801 | (1.2.840.113556.1.4.1464) | Arabic:Iraq                     |
| 0x0C01 | (1.2.840.113556.1.4.1465) | Arabic:Egypt                    |
| 0x1001 | (1.2.840.113556.1.4.1466) | Arabic:Libya                    |
| 0x1401 | (1.2.840.113556.1.4.1467) | Arabic:Algeria                  |
| 0x1801 | (1.2.840.113556.1.4.1468) | Arabic:Morocco                  |
| 0x1C01 | (1.2.840.113556.1.4.1469) | Arabic:Tunisia                  |
| 0x2001 | (1.2.840.113556.1.4.1470) | Arabic:Oman                     |
| 0x2401 | (1.2.840.113556.1.4.1471) | Arabic:Yemen                    |
| 0x2801 | (1.2.840.113556.1.4.1472) | Arabic:Syria                    |
| 0x2C01 | (1.2.840.113556.1.4.1473) | Arabic:Jordan                   |
| 0x3001 | (1.2.840.113556.1.4.1474) | Arabic:Lebanon                  |
| 0x3401 | (1.2.840.113556.1.4.1475) | Arabic:Kuwait                   |
| 0x3801 | (1.2.840.113556.1.4.1476) | Arabic:UAE                      |
| 0x3C01 | (1.2.840.113556.1.4.1477) | Arabic:Bahrain                  |
| 0x4001 | (1.2.840.113556.1.4.1478) | Arabic:Qatar                    |
| 0x042B | (1.2.840.113556.1.4.1479) | Armenian                        |
| 0x044D | (1.2.840.113556.1.4.1480) | Assamese                        |
| 0x042C | (1.2.840.113556.1.4.1481) | Azeri:Latin                     |
| 0x082C | (1.2.840.113556.1.4.1482) | Azeri:Cyrillic                  |
| 0x042D | (1.2.840.113556.1.4.1483) | Basque (Basque)                 |
| 0x0423 | (1.2.840.113556.1.4.1484) | Belarussian                     |
| 0x0445 | (1.2.840.113556.1.4.1485) | Bengali                         |
| 0x0402 | (1.2.840.113556.1.4.1486) | Bulgarian                       |
| 0x0455 | (1.2.840.113556.1.4.1487) | Burmese                         |
| 0x0403 | (1.2.840.113556.1.4.1488) | Catalan                         |
| 0x0404 | (1.2.840.113556.1.4.1489) | Chinese:Taiwan                  |
| 0x0804 | (1.2.840.113556.1.4.1490) | Chinese:PRC                     |
| 0x0C04 | (1.2.840.113556.1.4.1491) | Chinese:Hong Kong SAR           |
| 0x1004 | (1.2.840.113556.1.4.1492) | Chinese:Singapore               |
| 0x1404 | (1.2.840.113556.1.4.1493) | Chinese:Macau SAR               |
| 0x041A | (1.2.840.113556.1.4.1494) | Croatian                        |
| 0x0405 | (1.2.840.113556.1.4.1495) | Czech                           |
| 0x0406 | (1.2.840.113556.1.4.1496) | Danish                          |
| 0x0413 | (1.2.840.113556.1.4.1497) | Dutch                           |
| 0x0813 | (1.2.840.113556.1.4.1498) | Dutch:Belgium                   |
| 0x0409 | (1.2.840.113556.1.4.1499) | English:United States           |
| 0x0809 | (1.2.840.113556.1.4.1500) | English:United Kingdom          |
| 0x0C09 | (1.2.840.113556.1.4.1665) | English:Australia               |
| 0x1009 | (1.2.840.113556.1.4.1666) | English:Canada                  |
| 0x1409 | (1.2.840.113556.1.4.1667) | English:New Zealand             |
| 0x1809 | (1.2.840.113556.1.4.1668) | English:Ireland                 |
| 0x1C09 | (1.2.840.113556.1.4.1505) | English:South Africa            |
| 0x2009 | (1.2.840.113556.1.4.1506) | English:Jamaica                 |
| 0x2409 | (1.2.840.113556.1.4.1507) | English:Caribbean               |
| 0x2809 | (1.2.840.113556.1.4.1508) | English:Belize                  |
| 0x2C09 | (1.2.840.113556.1.4.1509) | English:Trinidad                |
| 0x3009 | (1.2.840.113556.1.4.1510) | English:Zimbabwe                |
| 0x3409 | (1.2.840.113556.1.4.1511) | English:Philippines             |
| 0x0425 | (1.2.840.113556.1.4.1512) | Estonian                        |
| 0x0438 | (1.2.840.113556.1.4.1513) | Faeroese                        |
| 0x0429 | (1.2.840.113556.1.4.1514) | Persian                         |
| 0x040B | (1.2.840.113556.1.4.1515) | Finnish                         |
| 0x040C | (1.2.840.113556.1.4.1516) | French:France                   |
| 0x080C | (1.2.840.113556.1.4.1517) | French:Belgium                  |
| 0x0C0C | (1.2.840.113556.1.4.1518) | French:Canada                   |
| 0x100C | (1.2.840.113556.1.4.1519) | French:Switzerland              |
| 0x140C | (1.2.840.113556.1.4.1520) | French:Luxembourg               |
| 0x180C | (1.2.840.113556.1.4.1521) | French:Monaco                   |
| 0x0437 | (1.2.840.113556.1.4.1522) | Georgian                        |
| 0x0407 | (1.2.840.113556.1.4.1523) | German:Germany                  |
| 0x0807 | (1.2.840.113556.1.4.1524) | German:Switzerland              |
| 0x0C07 | (1.2.840.113556.1.4.1525) | German:Austria                  |
| 0x1007 | (1.2.840.113556.1.4.1526) | German:Luxembourg               |
| 0x1407 | (1.2.840.113556.1.4.1527) | German:Liechtenstein            |
| 0x0408 | (1.2.840.113556.1.4.1528) | Greek                           |
| 0x0447 | (1.2.840.113556.1.4.1529) | Gujarati                        |
| 0x040D | (1.2.840.113556.1.4.1530) | Hebrew                          |
| 0x0439 | (1.2.840.113556.1.4.1531) | Hindi                           |
| 0x040E | (1.2.840.113556.1.4.1532) | Hungarian                       |
| 0x040F | (1.2.840.113556.1.4.1533) | Icelandic                       |
| 0x0421 | (1.2.840.113556.1.4.1534) | Indonesian                      |
| 0x045E | (1.2.840.113556.1.4.1535) | Inukitut                        |
| 0x0410 | (1.2.840.113556.1.4.1536) | Italian:Italy                   |
| 0x0810 | (1.2.840.113556.1.4.1537) | Italian:Switzerland             |
| 0x0411 | (1.2.840.113556.1.4.1538) | Japanese                        |
| 0x044B | (1.2.840.113556.1.4.1539) | Kannada                         |
| 0x0460 | (1.2.840.113556.1.4.1540) | Kashmiri (Arabic)               |
| 0x0860 | (1.2.840.113556.1.4.1541) | Kashmiri                        |
| 0x043F | (1.2.840.113556.1.4.1542) | Kazakh                          |
| 0x0453 | (1.2.840.113556.1.4.1543) | Khmer                           |
| 0x0440 | (1.2.840.113556.1.4.1544) | Kirghiz                         |
| 0x0457 | (1.2.840.113556.1.4.1545) | Konkani                         |
| 0x0412 | (1.2.840.113556.1.4.1546) | Korean                          |
| 0x0812 | (1.2.840.113556.1.4.1547) | Korean:Johab                    |
| 0x0426 | (1.2.840.113556.1.4.1548) | Latvian                         |
| 0x0427 | (1.2.840.113556.1.4.1549) | Lithuanian                      |
| 0x042F | (1.2.840.113556.1.4.1550) | F.Y.R.O. Macedonia              |
| 0x043E | (1.2.840.113556.1.4.1551) | Malaysian                       |
| 0x083E | (1.2.840.113556.1.4.1552) | Malay Brunei Darussalam         |
| 0x044C | (1.2.840.113556.1.4.1553) | Malayalam                       |
| 0x043A | (1.2.840.113556.1.4.1554) | Maltese                         |
| 0x0458 | (1.2.840.113556.1.4.1555) | Manipuri                        |
| 0x044E | (1.2.840.113556.1.4.1556) | Marathi                         |
| 0x0461 | (1.2.840.113556.1.4.1557) | Nepali:Nepal                    |
| 0x0414 | (1.2.840.113556.1.4.1558) | Norwegian:Bokmal                |
| 0x0814 | (1.2.840.113556.1.4.1559) | Norwegian:Nynorsk               |
| 0x0448 | (1.2.840.113556.1.4.1560) | Oriya                           |
| 0x0415 | (1.2.840.113556.1.4.1561) | Polish                          |
| 0x0416 | (1.2.840.113556.1.4.1562) | Portuguese:Brazil               |
| 0x0816 | (1.2.840.113556.1.4.1563) | Portuguese:Portugal             |
| 0x0446 | (1.2.840.113556.1.4.1564) | Punjabi                         |
| 0x0418 | (1.2.840.113556.1.4.1565) | Romanian                        |
| 0x0419 | (1.2.840.113556.1.4.1566) | Russian                         |
| 0x044F | (1.2.840.113556.1.4.1567) | Sanskrit                        |
| 0x0C1A | (1.2.840.113556.1.4.1568) | Serbian:Cyrillic                |
| 0x081A | (1.2.840.113556.1.4.1569) | Serbian:Latin                   |
| 0x0459 | (1.2.840.113556.1.4.1570) | Sindhi:India                    |
| 0x041B | (1.2.840.113556.1.4.1571) | Slovak                          |
| 0x0424 | (1.2.840.113556.1.4.1572) | Slovenian                       |
| 0x040A | (1.2.840.113556.1.4.1573) | Spanish:Spain(Traditional Sort) |
| 0x080A | (1.2.840.113556.1.4.1574) | Spanish:Mexico                  |
| 0x0C0A | (1.2.840.113556.1.4.1575) | Spanish:Spain(Modern Sort)      |
| 0x100A | (1.2.840.113556.1.4.1576) | Spanish:Guatemala               |
| 0x140A | (1.2.840.113556.1.4.1577) | Spanish:Costa Rica              |
| 0x180A | (1.2.840.113556.1.4.1578) | Spanish:Panama                  |
| 0x1C0A | (1.2.840.113556.1.4.1579) | Spanish:Dominican Republic      |
| 0x200A | (1.2.840.113556.1.4.1580) | Spanish:Venezuela               |
| 0x240A | (1.2.840.113556.1.4.1581) | Spanish:Colombia                |
| 0x280A | (1.2.840.113556.1.4.1582) | Spanish:Peru                    |
| 0x2C0A | (1.2.840.113556.1.4.1583) | Spanish:Argentina               |
| 0x300A | (1.2.840.113556.1.4.1584) | Spanish:Ecuador                 |
| 0x340A | (1.2.840.113556.1.4.1585) | Spanish:Chile                   |
| 0x380A | (1.2.840.113556.1.4.1586) | Spanish:Uruguay                 |
| 0x3C0A | (1.2.840.113556.1.4.1587) | Spanish:Paraguay                |
| 0x400A | (1.2.840.113556.1.4.1588) | Spanish:Bolivia                 |
| 0x440A | (1.2.840.113556.1.4.1589) | Spanish:El Salvador             |
| 0x480A | (1.2.840.113556.1.4.1590) | Spanish:Honduras                |
| 0x4C0A | (1.2.840.113556.1.4.1591) | Spanish:Nicaragua               |
| 0x500A | (1.2.840.113556.1.4.1592) | Spanish:Puerto Rico             |
| 0x0441 | (1.2.840.113556.1.4.1593) | Swahili:Kenya                   |
| 0x041D | (1.2.840.113556.1.4.1594) | Swedish                         |
| 0x081D | (1.2.840.113556.1.4.1595) | Swedish:Finland                 |
| 0x0449 | (1.2.840.113556.1.4.1596) | Tamil                           |
| 0x0444 | (1.2.840.113556.1.4.1597) | Tatar:Tatarstan                 |
| 0x044A | (1.2.840.113556.1.4.1598) | Telugu                          |
| 0x041E | (1.2.840.113556.1.4.1599) | Thai                            |
| 0x041F | (1.2.840.113556.1.4.1600) | Turkish                         |
| 0x0422 | (1.2.840.113556.1.4.1601) | Ukrainian                       |
| 0x0420 | (1.2.840.113556.1.4.1602) | Urdu:Pakistan                   |
| 0x0820 | (1.2.840.113556.1.4.1603) | Urdu:India                      |
| 0x0443 | (1.2.840.113556.1.4.1604) | Uzbek:Latin                     |
| 0x0843 | (1.2.840.113556.1.4.1605) | Uzbek:Cyrillic                  |
| 0x042A | (1.2.840.113556.1.4.1606) | Vietnamese                      |
| 0x0    | (1.2.840.113556.1.4.1607) | Japanese:XJIS                   |
| 0x1    | (1.2.840.113556.1.4.1608) | Japanese:Unicode                |
| 0x0    | (1.2.840.113556.1.4.1609) | Chinese:Big5                    |
| 0x0    | (1.2.840.113556.1.4.1610) | Chinese:PRCP                    |
| 0x1    | (1.2.840.113556.1.4.1611) | Chinese:Unicode                 |
| 0x2    | (1.2.840.113556.1.4.1612) | Chinese:PRC                     |
| 0x3    | (1.2.840.113556.1.4.1613) | Chinese:BOPOMOFO                |
| 0x0    | (1.2.840.113556.1.4.1614) | Korean:KSC                      |
| 0x1    | (1.2.840.113556.1.4.1615) | Korean:Unicode                  |
| 0x1    | (1.2.840.113556.1.4.1616) | GERMAN\_PHONE\_BOOK             |
| 0x0    | (1.2.840.113556.1.4.1617) | HUNGARIAN\_DEFAULT              |
| 0x1    | (1.2.840.113556.1.4.1618) | HUNGARIAN\_TECHNICAL            |
| 0x0    | (1.2.840.113556.1.4.1619) | GEORGIAN\_TRADITIONAL           |
| 0x1    | (1.2.840.113556.1.4.1620) | GEORGIAN\_MODERN                |



 

Client applications should use the various API calls such as [**ldap\_create\_sort\_control**](ldap-create-sort-control.md), [**ldap\_search\_init\_page**](ldap-search-init-page.md), [**ldap\_parse\_result**](ldap-parse-result.md), [**ldap\_parse\_sort\_control**](ldap-parse-sort-control.md), and so on, instead of manually creating and specifying the sort controls.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winldap.h</dt> </dl> |



## See also

<dl> <dt>

[Data Structures](data-structures.md)
</dt> <dt>

[**LDAPMessage**](ldapmessage.md)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





