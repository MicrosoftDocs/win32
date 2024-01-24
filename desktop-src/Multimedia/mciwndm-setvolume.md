---
title: MCIWNDM_SETVOLUME message (Vfw.h)
description: The MCIWNDM\_SETVOLUME message sets the volume level of an MCI device. You can send this message explicitly or by using the MCIWndSetVolume macro.
ms.assetid: 04151588-b761-447a-9a57-808c034c3059
keywords:
- MCIWNDM_SETVOLUME message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_SETVOLUME
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_SETVOLUME message

The **MCIWNDM\_SETVOLUME** message sets the volume level of an MCI device. You can send this message explicitly or by using the [**MCIWndSetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetvolume) macro.


```C++
MCIWNDM_SETVOLUME 
wParam = 0; 
lParam = (LPARAM) (UINT) iVol; 
```



## Parameters

<dl> <dt>

<span id="iVol"></span><span id="ivol"></span><span id="IVOL"></span>*iVol*
</dt> <dd>

New volume level. Specify 1000 for normal volume level. Specify a higher value for a louder volume or a lower value for a quieter volume.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSetVolume**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetvolume)
</dt> </dl>

 

 





