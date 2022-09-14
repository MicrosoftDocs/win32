---
title: MCI_MSF_SECOND macro (Mciapi.h)
description: The MCI\_MSF\_SECOND macro retrieves the seconds component from a parameter containing packed minutes/seconds/frames (MSF) information.
ms.assetid: 2d455ce3-1823-46fa-a59e-b9c5c2fe5eb9
keywords:
- MCI_MSF_SECOND macro Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_MSF_SECOND
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_MSF\_SECOND macro

The **MCI\_MSF\_SECOND** macro retrieves the seconds component from a parameter containing packed minutes/seconds/frames (MSF) information.

## Syntax


```C++
BYTE MCI_MSF_SECOND(
   DWORD dwMSF
);
```



## Parameters

<dl> <dt>

*dwMSF* 
</dt> <dd>

Time in MSF format.

</dd> </dl>

## Return value

Returns the seconds component of the specified MSF information.

## Remarks

Time in MSF format is expressed as a **DWORD** value with the least significant byte containing minutes, the next least significant byte containing seconds, and the next least significant byte containing frames. The most significant byte is unused.

The **MCI\_MSF\_SECOND** macro is defined as follows:


```C++
#define MCI_MSF_SECOND(msf) ((BYTE)(((WORD)(msf)) >> 8)) 
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

 

 





