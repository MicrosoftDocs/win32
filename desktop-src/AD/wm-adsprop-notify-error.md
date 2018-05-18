---
title: WM\_ADSPROP\_NOTIFY\_ERROR message
description: The WM\_ADSPROP\_NOTIFY\_ERROR message adds an error message to a list of error messages that are displayed by calling the ADsPropShowErrorDialog function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '7abf1b3d-5abe-42cd-baeb-1bf863c7f04d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["WM_ADSPROP_NOTIFY_ERROR message Active Directory"]
topic_type:
- apiref
api_name:
- WM_ADSPROP_NOTIFY_ERROR
api_location:
- Adsprop.h
api_type:
- HeaderDef
---

# WM\_ADSPROP\_NOTIFY\_ERROR message

The **WM\_ADSPROP\_NOTIFY\_ERROR** message adds an error message to a list of error messages that are displayed by calling the [**ADsPropShowErrorDialog**](adspropshowerrordialog.md) function.


```C++
WM_ADSPROP_NOTIFY_ERROR

    WPARAM wParam
    LPARAM lParam
    
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle of the notification object. This is the *hNotifyObject* parameter obtained by [**ADsPropCreateNotifyObj**](adspropcreatenotifyobj.md).

</dd> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**ADSPROPERROR**](adsproperror.md) structure that contains error message data.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

The [**ADsPropSendErrorMessage**](adspropsenderrormessage.md) function is the preferred method of sending this message.

The error messages added by the **WM\_ADSPROP\_NOTIFY\_ERROR** message are accumulated until [**ADsPropShowErrorDialog**](adspropshowerrordialog.md) is called. **ADsPropShowErrorDialog** combines and displays the accumulated error messages. When the error dialog is dismissed, the accumulated error messages are deleted.

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

[**ADSPROPERROR**](adsproperror.md)
</dt> <dt>

[**ADsPropSendErrorMessage**](adspropsenderrormessage.md)
</dt> <dt>

[**ADsPropShowErrorDialog**](adspropshowerrordialog.md)
</dt> </dl>

 

 





