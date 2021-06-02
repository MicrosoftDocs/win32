---
description: Converts the computer's local time to Coordinated Universal Time (Greenwich Mean Time).
ms.assetid: ff5d40ba-7d94-4f11-9c18-e41752d1d7b9
title: Utilities.LocalTimeToUTCTime method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Utilities.LocalTimeToUTCTime
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Utilities.LocalTimeToUTCTime method

\[The **LocalTimeToUTCTime** method is available for use in the operating systems specified in the Requirements section.\]

The **LocalTimeToUTCTime** method converts the computer's local time to Coordinated Universal Time (Greenwich Mean Time).

## Syntax


```VB
Utilities.LocalTimeToUTCTime( _
  ByVal LocalTime _
)
```



## Parameters

<dl> <dt>

*LocalTime* \[in\]
</dt> <dd>

The local time to be converted to Coordinated Universal Time.

</dd> </dl>

## Return value

The Coordinated Universal Time that corresponds to the specified local time.

## Remarks

While the system uses Coordinated Universal Time internally, applications generally display the local time, which is the date and time of day for the computer's local time zone.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Utilities**](utilities.md)
</dt> </dl>

 

 




