---
title: ICM_GETQUALITY message (Vfw.h)
description: The ICM\_GETQUALITY message queries a video compression driver to return its current quality setting.
ms.assetid: 8da99a26-7b2a-4118-89e1-7485915cbdc9
keywords:
- ICM_GETQUALITY message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_GETQUALITY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_GETQUALITY message

The **ICM\_GETQUALITY** message queries a video compression driver to return its current quality setting.


```C++
ICM_GETQUALITY 
wParam = (DWORD) (LPVOID) &dwICValue; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="dwICValue"></span><span id="dwicvalue"></span><span id="DWICVALUE"></span>*dwICValue*
</dt> <dd>

Address to contain the current quality value. Quality values range from 0 to 10,000.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the driver supports this message or ICERR\_UNSUPPORTED otherwise.

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

 

 





