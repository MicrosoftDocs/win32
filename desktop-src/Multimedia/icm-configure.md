---
title: ICM_CONFIGURE message (Vfw.h)
description: The ICM\_CONFIGURE message notifies a video compression driver to display its configuration dialog box or queries a video compression driver to determine if it has a configuration dialog box.
ms.assetid: 9760788e-fa66-44d7-bda6-aa9536143774
keywords:
- ICM_CONFIGURE message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_CONFIGURE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_CONFIGURE message

The **ICM\_CONFIGURE** message notifies a video compression driver to display its configuration dialog box or queries a video compression driver to determine if it has a configuration dialog box. You can send this message explicitly or by using the [**ICConfigure**](/windows/desktop/api/Vfw/nf-vfw-icconfigure) macro.


```C++
ICM_CONFIGURE 
wParam = (DWORD_PTR) (UINT_PTR) hwnd; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="hwnd"></span><span id="HWND"></span>*hwnd*
</dt> <dd>

Handle to the parent window of the displayed dialog box. You can determine if a driver has a configuration dialog box by specifying  1 in this parameter, as in the [**ICQueryConfigure**](/windows/desktop/api/Vfw/nf-vfw-icqueryconfigure) macro.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the driver supports this message or ICERR\_UNSUPPORTED otherwise.

## Remarks

This message is different from the [**DRV\_CONFIGURE**](drv-configure.md) message used for hardware configuration. The dialog box for this message should let the user set and edit the internal state referenced by the [**ICM\_GETSTATE**](icm-getstate.md) and [**ICM\_SETSTATE**](icm-setstate.md) messages. For example, this dialog box can let the user change parameters affecting the quality level and other similar compression options.

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

 

 





