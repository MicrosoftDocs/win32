---
title: ICM_GET message (Vfw.h)
description: The ICM\_GET message retrieves an application-defined DWORD value from a video compression driver.
ms.assetid: 288c0053-16a1-4547-b748-da218a0b588c
keywords:
- ICM_GET message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_GET
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_GET message

The **ICM\_GET** message retrieves an application-defined **DWORD** value from a video compression driver.


```C++
ICM_GET 
wParam = (DWORD) (LPVOID) pv; 
lParam = (DWORD) cb; 
```



## Parameters

<dl> <dt>

<span id="pv"></span><span id="PV"></span>*pv*
</dt> <dd>

Pointer to a block of memory to be filled with the current state. You can also specify **NULL** to determine the amount of memory required by the state information.

</dd> <dt>

<span id="cb"></span><span id="CB"></span>*cb*
</dt> <dd>

Size, in bytes, of the block of memory.

</dd> </dl>

## Return Value

Returns the amount of memory, in bytes, required to store the status information.

## Remarks

The structure used to represent state information is driver specific and is defined by the driver.

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

 

 





