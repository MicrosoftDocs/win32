---
title: MCIWNDM_CHANGESTYLES message (Vfw.h)
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
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_CHANGESTYLES message

The **MCIWNDM\_CHANGESTYLES** message changes the styles used by the MCIWnd window. You can send this message explicitly or by using the [**MCIWndChangeStyles**](/windows/desktop/api/Vfw/nf-vfw-mciwndchangestyles) macro.


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

New style settings for the window. Specify zero for this parameter to turn off all styles identified in the mask. For a list of the available styles, see the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function.

</dd> </dl>

## Return Value

Returns zero.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea)
</dt> <dt>

[**MCIWndChangeStyles**](/windows/desktop/api/Vfw/nf-vfw-mciwndchangestyles)
</dt> </dl>

 

 





