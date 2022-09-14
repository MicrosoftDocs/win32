---
title: MCI_HMS_SECOND macro (Mciapi.h)
description: The MCI\_HMS\_SECOND macro retrieves the seconds component from a parameter containing packed hours/minutes/seconds (HMS) information.
ms.assetid: b6895bec-524f-4345-ae65-e75168855df2
keywords:
- MCI_HMS_SECOND macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_HMS_SECOND
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_HMS\_SECOND macro

The **MCI\_HMS\_SECOND** macro retrieves the seconds component from a parameter containing packed hours/minutes/seconds (HMS) information.

## Syntax


```C++
BYTE MCI_HMS_SECOND(
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

Returns the seconds component of the specified HMS information.

## Remarks

Time in HMS format is expressed as a **DWORD** value with the least significant byte containing hours, the next least significant byte containing minutes, and the next least significant byte containing seconds. The most significant byte is unused.

The **MCI\_HMS\_SECOND** macro is defined as follows:


```C++
#define MCI_HMS_SECOND(hms) ((BYTE)((hms) >> 16)) 
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

 

 





