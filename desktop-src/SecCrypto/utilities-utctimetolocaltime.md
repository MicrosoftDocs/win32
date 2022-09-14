---
description: Converts Coordinated Universal Time (Greenwich Mean Time) to the computer's local time.
ms.assetid: 4085d7cb-d346-477d-a043-e96fb951c35a
title: Utilities.UTCTimeToLocalTime method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Utilities.UTCTimeToLocalTime
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Utilities.UTCTimeToLocalTime method

\[The **UTCTimeToLocalTime** method is available for use in the operating systems specified in the Requirements section.\]

The **UTCTimeToLocalTime** method converts Coordinated Universal Time (Greenwich Mean Time) to the computer's local time.

## Syntax


```VB
Utilities.UTCTimeToLocalTime( _
  ByVal UTCTime _
)
```



## Parameters

<dl> <dt>

*UTCTime* \[in\]
</dt> <dd>

The Coordinated Universal Time to be converted to the computer's local time.

</dd> </dl>

## Return value

The local time that corresponds to the specified Coordinated Universal Time.

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

 

 




