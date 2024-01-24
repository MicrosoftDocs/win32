---
title: String(Generalized-Time) syntax
description: A time string format defined by ASN.1 standards. | String(Generalized-Time) syntax
ms.assetid: c69ab29b-5877-47d4-b58d-4f103758dfac
ms.tgt_platform: multiple
keywords:
- String(Generalized-Time) syntax AD Schema
topic_type:
- apiref
api_name:
- String(Generalized-Time)
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# String(Generalized-Time) syntax

A time string format defined by ASN.1 standards. Use this syntax for storing time values in Generalized-Time format.

The format for the Generalized-Time syntax is "YYYYMMDDHHMMSS.0Z". An example of an acceptable value is "20010928060000.0Z". The "Z" indicates no time differential. Active Directory stores date/time as Greenwich Mean Time (GMT). If no time differential is specified, GMT is the default.

If the time is specified in a time zone other than GMT, the differential between the time zone and GMT is appended to the string instead of "Z" in the form "YYYYMMDDHHMMSS.0\[+/-\]HHMM". An example of an acceptable value is "20010928060000.0+0200". The differential is based on the formula: GMT=Local+differential.

For more information, see ISO 8601 and X680.



| Entry | Value |
|--------------|----------------------------------------------------------------------------|
| Name         | String(Generalized-Time)                                                   |
| Syntax ID    | 2.5.5.11                                                                   |
| OM ID        | 24                                                                         |
| MAPI Type    | SYSTIME                                                                    |
| ADS Type     | ADSTYPE\_UTC\_TIME                                                         |
| Variant Type | VT\_DATE                                                                   |
| SDS Type     | [System.DateTime](/dotnet/api/system.datetime) |



## See also

<dl> <dt>

[System.DateTime](/dotnet/api/system.datetime)
</dt> </dl>

 

 
