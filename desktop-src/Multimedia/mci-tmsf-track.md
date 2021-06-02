---
title: MCI_TMSF_TRACK macro (Mciapi.h)
description: The MCI\_TMSF\_TRACK macro retrieves the tracks component from a parameter containing packed tracks/minutes/seconds/frames (TMSF) information.
ms.assetid: 3455442c-5c66-47c7-b06b-1a2de0e2dfed
keywords:
- MCI_TMSF_TRACK macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_TMSF_TRACK
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_TMSF\_TRACK macro

The **MCI\_TMSF\_TRACK** macro retrieves the tracks component from a parameter containing packed tracks/minutes/seconds/frames (TMSF) information.

## Syntax


```C++
BYTE MCI_TMSF_TRACK(
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

Returns the tracks component of the specified TMSF information.

## Remarks

Time in TMSF format is expressed as a **DWORD** value with the least significant byte containing tracks, the next least significant byte containing minutes, the next least significant byte containing seconds, and the most significant byte containing frames.

The **MCI\_TMSF\_TRACK** macro is defined as follows:


```C++
#define MCI_TMSF_TRACK(tmsf) ((BYTE)(tmsf)) 
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

 

 





