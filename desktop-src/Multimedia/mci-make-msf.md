---
title: MCI_MAKE_MSF macro (Mciapi.h)
description: The MCI\_MAKE\_MSF macro creates a time value in packed minutes/seconds/frames (MSF) format from the given minutes, seconds, and frame values.
ms.assetid: 8c981d84-b049-4448-a820-bff30896065e
keywords:
- MCI_MAKE_MSF macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_MAKE_MSF
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_MAKE\_MSF macro

The **MCI\_MAKE\_MSF** macro creates a time value in packed minutes/seconds/frames (MSF) format from the given minutes, seconds, and frame values.

## Syntax


```C++
DWORD MCI_MAKE_MSF(
   BYTE minutes,
   BYTE seconds,
   BYTE frames
);
```



## Parameters

<dl> <dt>

*minutes* 
</dt> <dd>

Number of minutes.

</dd> <dt>

*seconds* 
</dt> <dd>

Number of seconds.

</dd> <dt>

*frames* 
</dt> <dd>

Number of frames.

</dd> </dl>

## Return value

Returns the time in packed MSF format.

## Remarks

Time in MSF format is expressed as a **DWORD** value with the least significant byte containing minutes, the next least significant byte containing seconds, and the next least significant byte containing frames. The most significant byte is unused.

The **MCI\_MAKE\_MSF** macro is defined as follows:


```C++
#define MCI_MAKE_MSF(m, s, f) ((DWORD)(((BYTE)(m) | \ 
                              ((WORD)(s) << 8)) | \ 
                              (((DWORD)(BYTE)(f)) << 16))) 
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

 

 





