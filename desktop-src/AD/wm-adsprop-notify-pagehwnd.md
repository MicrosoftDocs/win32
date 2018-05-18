---
title: WM\_ADSPROP\_NOTIFY\_PAGEHWND message
description: An Active Directory directory service property sheet extension calls the ADsPropSetHwnd to inform the notification object of the property page window handle.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'eb8bf525-cd7f-44d0-a0f9-43178a29c443'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["WM_ADSPROP_NOTIFY_PAGEHWND message Active Directory"]
topic_type:
- apiref
api_name:
- WM_ADSPROP_NOTIFY_PAGEHWND
api_location:
- Adsprop.h
api_type:
- HeaderDef
---

# WM\_ADSPROP\_NOTIFY\_PAGEHWND message

An Active Directory directory service property sheet extension calls the [**ADsPropSetHwnd**](adspropsethwnd.md) to inform the notification object of the property page window handle. The **ADsPropSetHwnd** function sends the **WM\_ADSPROP\_NOTIFY\_PAGEHWND** message to the notification object, which informs the notification object of the property page window handle.


```C++
WM_ADSPROP_NOTIFY_PAGEHWND

    WPARAM hPage
    LPARAM ptzTitle
    
```



## Parameters

<dl> <dt>

*hNotifyObj* 
</dt> <dd>

The handle of the notification object. To obtain this handle, call [**ADsPropCreateNotifyObj**](adspropcreatenotifyobj.md).

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

An Active Directory property sheet extension normally calls the [**ADsPropSetHwnd**](adspropsethwnd.md) function while processing the [**WM\_INITDIALOG**](_win32_wm_initdialog_cpp) message.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Adsprop.h</dt> </dl> |



## See also

<dl> <dt>

[Messages in Active Directory Domain Services](messages-in-active-directory-domain-services.md)
</dt> <dt>

[**ADsPropSetHwnd**](adspropsethwnd.md)
</dt> <dt>

[**ADsPropCreateNotifyObj**](adspropcreatenotifyobj.md)
</dt> <dt>

[**WM\_INITDIALOG**](_win32_wm_initdialog_cpp)
</dt> </dl>

 

 





