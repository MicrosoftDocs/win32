---
title: WM_ADSPROP_NOTIFY_APPLY message (Adsprop.h)
description: An Active Directory directory service property sheet extension sends the WM\_ADSPROP\_NOTIFY\_APPLY message to the notification object if the property page PSN\_APPLY handler succeeds.
ms.assetid: 3536054b-83ee-4cfa-ab54-c0af3a46289e
ms.tgt_platform: multiple
keywords:
- WM_ADSPROP_NOTIFY_APPLY message Active Directory
topic_type:
- apiref
api_name:
- WM_ADSPROP_NOTIFY_APPLY
api_location:
- Adsprop.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ADSPROP\_NOTIFY\_APPLY message

An Active Directory directory service property sheet extension sends the **WM\_ADSPROP\_NOTIFY\_APPLY** message to the notification object if the property page PSN\_APPLY handler succeeds.


```C++
WM_ADSPROP_NOTIFY_APPLY

    WPARAM wParam
    LPARAM lParam
    
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

The handle of the notification object. To obtain this handle, call [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj).

</dd> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

When adding pages to the Active Directory Manager MMC snap-in, Active Directory MMC property sheets create the notification objects by a call to the [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj) function, and then passes the notification object handle to each property page.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Adsprop.h</dt> </dl> |



## See also

<dl> <dt>

[**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj)
</dt> <dt>

[Messages in Active Directory Domain Services](messages-in-active-directory-domain-services.md)
</dt> </dl>

 

 





