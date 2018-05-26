---
title: MCIWNDM\_OPEN message
description: The MCIWNDM\_OPEN message opens an MCI device and associates it with an MCIWnd window.
ms.assetid: ad1dfe0f-015b-45a9-ab88-cc0bdf0aa057
keywords:
- MCIWNDM_OPEN message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_OPEN
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCIWNDM\_OPEN message

The **MCIWNDM\_OPEN** message opens an MCI device and associates it with an MCIWnd window. For MCI devices that use data files, this macro can also open a specified data file, name a new file to be created, or display a dialog box to let the user select a file to open. You can send this message explicitly or by using the [**MCIWndOpen**](/windows/win32/Vfw/nf-vfw-mciwndopen?branch=master) macro.


```C++
MCIWNDM_OPEN 
wParam = (WPARAM) (UINT) wFlags; 
lParam = (LPARAM) (LPVOID) szFile; 
```



## Parameters

<dl> <dt>

<span id="wFlags"></span><span id="wflags"></span><span id="WFLAGS"></span>*wFlags*
</dt> <dd>

Flags associated with the device or file to open. The MCIWNDOPENF\_NEW flag specifies a new file is to be created with the name specified in **szFile**.

</dd> <dt>

<span id="szFile"></span><span id="szfile"></span><span id="SZFILE"></span>*szFile*
</dt> <dd>

Pointer to a null-terminated string identifying the filename or MCI device name to open. Specify  1 for this parameter to display the Open dialog box.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndOpen**](/windows/win32/Vfw/nf-vfw-mciwndopen?branch=master)
</dt> </dl>

 

 





