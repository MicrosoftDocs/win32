---
title: WM_ADSPROP_SHEET_CREATE message
description: Sent to the notification object to create a secondary property sheet in an Active Directory MMC snap-in.
ms.assetid: 3efa25f2-cd39-44f8-952e-203f1519ce2c
ms.tgt_platform: multiple
keywords:
- WM_ADSPROP_SHEET_CREATE message Active Directory
topic_type:
- apiref
api_name:
- WM_ADSPROP_SHEET_CREATE
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ADSPROP\_SHEET\_CREATE message

The **WM\_ADSPROP\_SHEET\_CREATE** message is sent to the notification object to create a secondary property sheet in an Active Directory MMC snap-in.

> [!Note]  
> This message value is not defined in a published header file. To use this message value, you must define it yourself in the exact format shown.

 


```C++
#define WM_ADSPROP_SHEET_CREATE (WM_USER + 1108)
LRESULT SendMessage( (HWND)   hwnd, 
                     (UINT)   WM_ADSPROP_SHEET_CREATE,
                     (WPARAM) wParam, 
                     (LPARAM) lParam);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

The handle of the notification object. To obtain this handle, call [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj).

</dd> <dt>

*wParam* 
</dt> <dd>

Contains a pointer to a [**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md) structure that defines the secondary page to create. Only one secondary property sheet can be created with the **WM\_ADSPROP\_SHEET\_CREATE** message, so the [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) structure can only contain one [**DSOBJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used. Must be **NULL**.

</dd> </dl>

## Return value

The return value for this message is always zero.

## Remarks

The caller must allocate the [**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md) structure, the title string and all [**DSOBJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject) strings using a single call to the [**LocalAlloc**](/windows/desktop/api/winbase/nf-winbase-localalloc) function. The **WM\_ADSPROP\_SHEET\_CREATE** message is an asynchronous message, so it will return before the secondary sheet is created. Because of this, the memory must remain intact after the message returns. The receiver will free this memory with a single call to the [**LocalFree**](/windows/desktop/api/winbase/nf-winbase-localfree) function after the secondary sheet is created.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**CFSTR\_DS\_PARENTHWND**](cfstr-ds-parenthwnd.md)
</dt> <dt>

[**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md)
</dt> <dt>

[**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames)
</dt> <dt>

[**DSOBJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject)
</dt> <dt>

[**LocalAlloc**](/windows/desktop/api/winbase/nf-winbase-localalloc)
</dt> <dt>

[**LocalFree**](/windows/desktop/api/winbase/nf-winbase-localfree)
</dt> </dl>

 

