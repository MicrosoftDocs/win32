---
title: DS-Heuristics attribute
description: Contains global settings for the entire forest.
ms.assetid: d5fd990b-7bbf-4ede-a3af-7f3f7ac959b3
ms.tgt_platform: multiple
keywords:
- DS-Heuristics attribute AD Schema
- dSHeuristics attribute AD Schema
topic_type:
- apiref
api_name:
- DS-Heuristics
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# DS-Heuristics attribute

Contains global settings for the entire forest.

There is information about adminSDholder exclusion bits available on the Microsoft Help and Support website in an article number [817433, Delegated permissions are not available and inheritance is automatically disabled](https://support.microsoft.com/default.aspx?scid=kb;EN-US;817433).



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | DS-Heuristics                               |
| Ldap-Display-Name | dSHeuristics                                |
| Size              | \-                                          |
| Update Privilege  | \-                                          |
| Update Frequency  | \-                                          |
| Attribute-Id      | 1.2.840.113556.1.2.212                      |
| System-Id-Guid    | f0f8ff86-1191-11d0-a060-00aa006c33ed        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | True                                             |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Remarks

Each Active Directory forest contains a DS-Heuristics attribute that contains settings for the entire forest. The DS-Heuristics attribute is an attribute of the "CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,&lt;Domain&gt;" object.

DS-Heuristics is a Unicode string in which each character contains a value for a single domain-wide setting. The DS-Heuristics string takes the following format.

``` syntax
|<1>|<2>|<3>|<4>|<5>|<6>|<7>|<8>|<9>|<10>|<11>|<12>|<13>|<14>|<15>|<16>|<17>|<18>|<19>|<20>|<21>|<22>|<23>|<24>|<25>|
```

To provide data validation, each tenth character is set to the character number divided by ten. For example, the tenth character is '1'; the twentieth character is '2', and so on.

Any character that is not set is assumed to be a '0'. If the DS-Heuristics attribute is not set, all values are assumed to be '0'. There are currently 25 characters being used and it is not necessary to pad the string to fill all 25 characters. For example, if the highest character being used is 7, then the string "0000002" is acceptable.

For details about each character, see [dSHeuristics in \[MS-ADTS\] Active Directory Technical Specification](/openspecs/windows_protocols/ms-adts/e5899be4-862e-496f-9a38-33950617d2c5).

### ANR Search Filters

Characters 1, 2, and 4 are used to modify the behavior of ANR search filters. If character 1 is set to '1', then the expansion of the ANR filter to include **GivenName** - **Surname** (when space is found) is disabled. If character 2 is set to '1', the expansion of the ANR filter to include **Surname** - **GivenName** is disabled. If an embedded space is present in the search string, the search string will normally be divided into two strings, which are compared pair-wise against the **GivenName** and **Surname** attributes. Setting characters 1 and 2 to '1' will prevent those matches from being attempted. This matching might be disabled if the administrator is confident that searches for "Jeff Smith" would always be provided as "jeff smith" and not "smith, jeff". Normally only one or the other match would be suppressed, according to local convention.

If the character 4 is set to '1' then Active Directory will perform "pre-emptive nickname resolution". That is, if the search string exactly matches the nickname of exactly one object in the search scope, that one object is returned as the result of the search, and the rest of ANR is skipped. Note that while the rest of ANR searching is available through LDAP, pre-emptive nickname resolution (also known as "nickname snap") is available only through MAPI.

## See also

<dl> <dt>

[dSHeuristics in \[MS-ADTS\] Active Directory Technical Specification](/openspecs/windows_protocols/ms-adts/e5899be4-862e-496f-9a38-33950617d2c5)
</dt> </dl>

 

