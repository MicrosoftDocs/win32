---
title: MCI_TMSF_FRAME macro (Mciapi.h)
description: The MCI\_TMSF\_FRAME macro retrieves the frames component from a parameter containing packed tracks/minutes/seconds/frames (TMSF) information.
ms.assetid: 1ba78d4f-4537-4955-abcc-842976b6b5b9
keywords:
- MCI_TMSF_FRAME macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_TMSF_FRAME
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_TMSF\_FRAME macro

The **MCI\_TMSF\_FRAME** macro retrieves the frames component from a parameter containing packed tracks/minutes/seconds/frames (TMSF) information.

## Syntax


```C++
BYTE MCI_TMSF_FRAME(
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

Returns the frames component of the specified TMSF information.

## Remarks

Time in TMSF format is expressed as a **DWORD** value with the least significant byte containing tracks, the next least significant byte containing minutes, the next least significant byte containing seconds, and the most significant byte containing frames.

The **MCI\_TMSF\_FRAME** macro is defined as follows:


```C++
#define MCI_TMSF_FRAME(tmsf) ((BYTE)((tmsf) >> 24)) 
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

 

 





