---
title: MCI_TMSF_MINUTE macro (Mciapi.h)
description: The MCI\_TMSF\_MINUTE macro retrieves the minutes component from a parameter containing packed tracks/minutes/seconds/frames (TMSF) information.
ms.assetid: 9a972579-240f-4641-b65e-9088f39cdf9e
keywords:
- MCI_TMSF_MINUTE macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_TMSF_MINUTE
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_TMSF\_MINUTE macro

The **MCI\_TMSF\_MINUTE** macro retrieves the minutes component from a parameter containing packed tracks/minutes/seconds/frames (TMSF) information.

## Syntax


```C++
BYTE MCI_TMSF_MINUTE(
   DWORD dwTMSF
);
```



## Parameters

<dl> <dt>

*dwTMSF* 
</dt> <dd>

Time in TMSF format.

</dd> </dl>

## Return value

Returns the minutes component of the specified TMSF information.

## Remarks

Time in TMSF format is expressed as a **DWORD** value with the least significant byte containing tracks, the next least significant byte containing minutes, the next least significant byte containing seconds, and the most significant byte containing frames.

The **MCI\_TMSF\_MINUTE** macro is defined as follows:


```C++
#define MCI_TMSF_MINUTE(tmsf) ((BYTE)(((WORD)(tmsf)) >> 8)) 
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

 

 





