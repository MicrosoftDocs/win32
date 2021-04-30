---
title: WM_ADSPROP_NOTIFY_PAGEHWND message (Adsprop.h)
description: An Active Directory directory service property sheet extension calls the ADsPropSetHwnd to inform the notification object of the property page window handle.
ms.assetid: eb8bf525-cd7f-44d0-a0f9-43178a29c443
ms.tgt_platform: multiple
keywords:
- WM_ADSPROP_NOTIFY_PAGEHWND message Active Directory
topic_type:
- apiref
api_name:
- WM_ADSPROP_NOTIFY_PAGEHWND
api_location:
- Adsprop.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ADSPROP\_NOTIFY\_PAGEHWND message

An Active Directory directory service property sheet extension calls the [**ADsPropSetHwnd**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsethwnd) to inform the notification object of the property page window handle. The **ADsPropSetHwnd** function sends the **WM\_ADSPROP\_NOTIFY\_PAGEHWND** message to the notification object, which informs the notification object of the property page window handle.


```C++
WM_ADSPROP_NOTIFY_PAGEHWND

    WPARAM hPage
    LPARAM ptzTitle
    
```



## Parameters

<dl> <dt>

*hNotifyObj* 
</dt> <dd>

The handle of the notification object. To obtain this handle, call [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj).

</dd> <dt>

*hPage* 
</dt> <dd>

A window handle of the property page.

</dd> <dt>

*ptzTitle* 
</dt> <dd>

Pointer to a NULL-terminated **WCHAR** buffer that contains the title of the property page.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

An Active Directory property sheet extension normally calls the [**ADsPropSetHwnd**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsethwnd) function while processing the [**WM\_INITDIALOG**](../dlgbox/wm-initdialog.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Adsprop.h</dt> </dl> |



## See also

<dl> <dt>

[Messages in Active Directory Domain Services](messages-in-active-directory-domain-services.md)
</dt> <dt>

[**ADsPropSetHwnd**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsethwnd)
</dt> <dt>

[**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj)
</dt> <dt>

[**WM\_INITDIALOG**](../dlgbox/wm-initdialog.md)
</dt> </dl>

 

