---
title: MCIWNDM\_CHANGESTYLES message
description: The MCIWNDM\_CHANGESTYLES message changes the styles used by the MCIWnd window. You can send this message explicitly or by using the MCIWndChangeStyles macro.
ms.assetid: 9074c21a-e49f-4089-a6d2-af8d513cb632
keywords:
- MCIWNDM_CHANGESTYLES message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_CHANGESTYLES
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

# MCIWNDM\_CHANGESTYLES message

The **MCIWNDM\_CHANGESTYLES** message changes the styles used by the MCIWnd window. You can send this message explicitly or by using the [**MCIWndChangeStyles**](/windows/win32/Vfw/nf-vfw-mciwndchangestyles?branch=master) macro.


```C++
MCIWNDM_CHANGESTYLES 
wParam = (WPARAM) (UINT) mask; 
lParam = (LPARAM) (LONG) value; 
```



## Parameters

<dl> <dt>

<span id="mask"></span><span id="MASK"></span>*mask*
</dt> <dd>

Mask that identifies the styles that can change. This mask is the bitwise OR operator of all styles that will be permitted to change.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

New style settings for the window. Specify zero for this parameter to turn off all styles identified in the mask. For a list of the available styles, see the [**MCIWndCreate**](/windows/win32/Vfw/nf-vfw-mciwndcreatea?branch=master) function.

</dd> </dl>

## Return Value

Returns zero.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCreate**](/windows/win32/Vfw/nf-vfw-mciwndcreatea?branch=master)
</dt> <dt>

[**MCIWndChangeStyles**](/windows/win32/Vfw/nf-vfw-mciwndchangestyles?branch=master)
</dt> </dl>

 

 





