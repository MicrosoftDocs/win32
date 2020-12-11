---
title: ICM_GETSTATE message (Vfw.h)
description: The ICM\_GETSTATE message queries a video compression driver to return its current configuration in a block of memory or to determine the amount of memory required to retrieve the configuration information.
ms.assetid: 4b77e294-f3aa-45f9-a4f4-f103b83eae8d
keywords:
- ICM_GETSTATE message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_GETSTATE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_GETSTATE message

The **ICM\_GETSTATE** message queries a video compression driver to return its current configuration in a block of memory or to determine the amount of memory required to retrieve the configuration information. You can send this message explicitly or by using the [**ICGetState**](/windows/desktop/api/Vfw/nf-vfw-icgetstate) macro.


```C++
ICM_GETSTATE 
wParam = (DWORD_PTR) (LPVOID) pv; 
lParam = (DWORD_PTR) cb; 
```



## Parameters

<dl> <dt>

<span id="pv"></span><span id="PV"></span>*pv*
</dt> <dd>

Pointer to a block of memory to contain the current configuration information. You can specify **NULL** for this parameter to determine the amount of memory required for the configuration information, as in [**ICGetStateSize**](/windows/desktop/api/Vfw/nf-vfw-icgetstatesize).

</dd> <dt>

<span id="cb"></span><span id="CB"></span>*cb*
</dt> <dd>

Size, in bytes, of the block of memory.

</dd> </dl>

## Return Value

If *pv* is **NULL**, returns the amount of memory, in bytes, required for configuration information.

If *pv* is not **NULL**, returns ICERR\_OK if successful or an error otherwise.

## Remarks

The structure used to represent configuration information is driver specific and is defined by the driver.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

 





