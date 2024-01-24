---
title: ICM_SETSTATE message (Vfw.h)
description: The ICM\_SETSTATE message notifies a video compression driver to set the state of the compressor. You can send this message explicitly or by using the ICSetState macro.
ms.assetid: d1a91847-2893-4c8b-9ca1-02db71ec2c81
keywords:
- ICM_SETSTATE message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_SETSTATE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_SETSTATE message

The **ICM\_SETSTATE** message notifies a video compression driver to set the state of the compressor. You can send this message explicitly or by using the [**ICSetState**](/windows/desktop/api/Vfw/nf-vfw-icsetstate) macro.


```C++
ICM_SETSTATE 
wParam = (DWORD_PTR) (LPVOID) pv; 
lParam = (DWORD_PTR) cb; 
```



## Parameters

<dl> <dt>

<span id="pv"></span><span id="PV"></span>*pv*
</dt> <dd>

Pointer to a block of memory containing configuration data. You can specify **NULL** for this parameter to reset the compressor to its default state.

</dd> <dt>

<span id="cb"></span><span id="CB"></span>*cb*
</dt> <dd>

Size, in bytes, of the block of memory.

</dd> </dl>

## Return Value

Returns the number of bytes used by the compressor if successful or zero otherwise.

## Remarks

The information used by this message is private and specific to a given compressor. Client applications should use this message only to restore information previously obtained with the [**ICM\_GETSTATE**](icm-getstate.md) message and should use the [**ICM\_CONFIGURE**](icm-configure.md) message to adjust the configuration of a video compression driver.

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

 

 





