---
title: WM_DSA_SHEET_CLOSE_NOTIFY message
description: Posted to the Active Directory MMC snap-in when a secondary property sheet is destroyed.
ms.assetid: 74271550-e1f7-4576-a04f-52d5b7c619cb
ms.tgt_platform: multiple
keywords:
- WM_DSA_SHEET_CLOSE_NOTIFY message Active Directory
topic_type:
- apiref
api_name:
- WM_DSA_SHEET_CLOSE_NOTIFY
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DSA\_SHEET\_CLOSE\_NOTIFY message

The **WM\_DSA\_SHEET\_CLOSE\_NOTIFY** message is posted to the Active Directory MMC snap-in when a secondary property sheet is destroyed.

> [!Note]  
> This message value is not defined in a published header file. To use this message value, you must define it yourself in the exact format shown.

 


```C++
#define WM_DSA_SHEET_CLOSE_NOTIFY (WM_USER + 5)
```




```C++
LRESULT SendMessage( (HWND)   hwnd, 
                     (UINT)   WM_DSA_SHEET_CLOSE_NOTIFY,
                     (WPARAM) wParam, 
                     (LPARAM) lParam);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

The window handle of the snap-in window that will process this message. This handle is obtained from the **hwndHidden** member of the [**PROPSHEETCFG**](propsheetcfg.md) structure.

</dd> <dt>

*wParam* 
</dt> <dd>

Contains an application-defined 32-bit value. This is obtained from the **wParamSheetClose** member of the [**PROPSHEETCFG**](propsheetcfg.md) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**PROPSHEETCFG**](propsheetcfg.md)
</dt> </dl>

 

 





