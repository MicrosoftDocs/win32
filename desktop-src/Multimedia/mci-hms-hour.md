---
title: MCI_HMS_HOUR macro (Mciapi.h)
description: The MCI\_HMS\_HOUR macro retrieves the hours component from a parameter containing packed hours/minutes/seconds (HMS) information.
ms.assetid: 55968b2b-2bfe-48ac-a50f-5c8741d11e33
keywords:
- MCI_HMS_HOUR macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_HMS_HOUR
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_HMS\_HOUR macro

The **MCI\_HMS\_HOUR** macro retrieves the hours component from a parameter containing packed hours/minutes/seconds (HMS) information.

## Syntax


```C++
BYTE MCI_HMS_HOUR(
   DWORD dwHMS
);
```



## Parameters

<dl> <dt>

*dwHMS* 
</dt> <dd>

Time in HMS format.

</dd> </dl>

## Return value

Returns the hours component of the specified HMS information.

## Remarks

Time in HMS format is expressed as a **DWORD** value with the least significant byte containing hours, the next least significant byte containing minutes, and the next least significant byte containing seconds. The most significant byte is unused.

The **MCI\_HMS\_HOUR** macro is defined as follows:


```C++
#define MCI_HMS_HOUR(hms) ((BYTE)(hms)) 
```



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mciapi.h</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Macros](mci-macros.md)
</dt> </dl>

 

 





