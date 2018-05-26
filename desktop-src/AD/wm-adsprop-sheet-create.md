---
title: WM\_ADSPROP\_SHEET\_CREATE message
description: Sent to the notification object to create a secondary property sheet in an Active Directory MMC snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3efa25f2-cd39-44f8-952e-203f1519ce2c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- WM_ADSPROP_SHEET_CREATE message Active Directory
topic_type:
- apiref
api_name:
- WM_ADSPROP_SHEET_CREATE
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
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

The handle of the notification object. To obtain this handle, call [**ADsPropCreateNotifyObj**](/windows/win32/Adsprop/nf-adsprop-adspropcreatenotifyobj?branch=master).

</dd> <dt>

*wParam* 
</dt> <dd>

Contains a pointer to a [**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md) structure that defines the secondary page to create. Only one secondary property sheet can be created with the **WM\_ADSPROP\_SHEET\_CREATE** message, so the [**DSOBJECTNAMES**](/windows/win32/Dsclient/ns-dsclient-dsobjectnames?branch=master) structure can only contain one [**DSOBJECT**](/windows/win32/Dsclient/ns-dsclient-dsobject?branch=master) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used. Must be **NULL**.

</dd> </dl>

## Return value

The return value for this message is always zero.

## Remarks

The caller must allocate the [**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md) structure, the title string and all [**DSOBJECT**](/windows/win32/Dsclient/ns-dsclient-dsobject?branch=master) strings using a single call to the [**LocalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366723) function. The **WM\_ADSPROP\_SHEET\_CREATE** message is an asynchronous message, so it will return before the secondary sheet is created. Because of this, the memory must remain intact after the message returns. The receiver will free this memory with a single call to the [**LocalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366730) function after the secondary sheet is created.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**CFSTR\_DS\_PARENTHWND**](cfstr-ds-parenthwnd.md)
</dt> <dt>

[**DSA\_SEC\_PAGE\_INFO**](dsa-sec-page-info.md)
</dt> <dt>

[**DSOBJECTNAMES**](/windows/win32/Dsclient/ns-dsclient-dsobjectnames?branch=master)
</dt> <dt>

[**DSOBJECT**](/windows/win32/Dsclient/ns-dsclient-dsobject?branch=master)
</dt> <dt>

[**LocalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366723)
</dt> <dt>

[**LocalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366730)
</dt> </dl>

 

 





