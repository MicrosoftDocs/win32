---
title: MCI_HMS_MINUTE macro (Mciapi.h)
description: The MCI\_HMS\_MINUTE macro retrieves the minutes component from a parameter containing packed hours/minutes/seconds (HMS) information.
ms.assetid: d083f769-9825-48cc-80f9-34ce3ef66ad6
keywords:
- MCI_HMS_MINUTE macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_HMS_MINUTE
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_HMS\_MINUTE macro

The **MCI\_HMS\_MINUTE** macro retrieves the minutes component from a parameter containing packed hours/minutes/seconds (HMS) information.

## Syntax


```C++
BYTE MCI_HMS_MINUTE(
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

Returns the minutes component of the specified HMS information.

## Remarks

Time in HMS format is expressed as a **DWORD** value with the least significant byte containing hours, the next least significant byte containing minutes, and the next least significant byte containing seconds. The most significant byte is unused.

The **MCI\_HMS\_MINUTE** macro is defined as follows:


```C++
#define MCI_HMS_MINUTE(hms) ((BYTE)(((WORD)(hms)) >> 8)) 
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

 

 





