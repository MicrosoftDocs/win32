---
title: WM\_ADSPROP\_NOTIFY\_ERROR message
description: The WM\_ADSPROP\_NOTIFY\_ERROR message adds an error message to a list of error messages that are displayed by calling the ADsPropShowErrorDialog function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7abf1b3d-5abe-42cd-baeb-1bf863c7f04d
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- WM_ADSPROP_NOTIFY_ERROR message Active Directory
topic_type:
- apiref
api_name:
- WM_ADSPROP_NOTIFY_ERROR
api_location:
- Adsprop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WM\_ADSPROP\_NOTIFY\_ERROR message

The **WM\_ADSPROP\_NOTIFY\_ERROR** message adds an error message to a list of error messages that are displayed by calling the [**ADsPropShowErrorDialog**](/windows/win32/Adsprop/nf-adsprop-adspropshowerrordialog?branch=master) function.


```C++
WM_ADSPROP_NOTIFY_ERROR

    WPARAM wParam
    LPARAM lParam
    
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle of the notification object. This is the *hNotifyObject* parameter obtained by [**ADsPropCreateNotifyObj**](/windows/win32/Adsprop/nf-adsprop-adspropcreatenotifyobj?branch=master).

</dd> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**ADSPROPERROR**](/windows/win32/Adsprop/ns-adsprop-_adsproperror?branch=master) structure that contains error message data.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

The [**ADsPropSendErrorMessage**](/windows/win32/Adsprop/nf-adsprop-adspropsenderrormessage?branch=master) function is the preferred method of sending this message.

The error messages added by the **WM\_ADSPROP\_NOTIFY\_ERROR** message are accumulated until [**ADsPropShowErrorDialog**](/windows/win32/Adsprop/nf-adsprop-adspropshowerrordialog?branch=master) is called. **ADsPropShowErrorDialog** combines and displays the accumulated error messages. When the error dialog is dismissed, the accumulated error messages are deleted.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Adsprop.h</dt> </dl> |



## See also

<dl> <dt>

[Messages in Active Directory Domain Services](messages-in-active-directory-domain-services.md)
</dt> <dt>

[**ADSPROPERROR**](/windows/win32/Adsprop/ns-adsprop-_adsproperror?branch=master)
</dt> <dt>

[**ADsPropSendErrorMessage**](/windows/win32/Adsprop/nf-adsprop-adspropsenderrormessage?branch=master)
</dt> <dt>

[**ADsPropShowErrorDialog**](/windows/win32/Adsprop/nf-adsprop-adspropshowerrordialog?branch=master)
</dt> </dl>

 

 





