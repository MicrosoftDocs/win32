---
title: WM\_ADSPROP\_NOTIFY\_PAGEINIT message
description: An Active Directory property sheet extension calls the ADsPropGetInitInfo to obtain data about regarding the directory object that the property sheet extension applies to.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 473c5a75-d0d9-4d12-b855-63683e8cdf3f
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- WM_ADSPROP_NOTIFY_PAGEINIT message Active Directory
topic_type:
- apiref
api_name:
- WM_ADSPROP_NOTIFY_PAGEINIT
api_location:
- Adsprop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WM\_ADSPROP\_NOTIFY\_PAGEINIT message

An Active Directory property sheet extension calls the [**ADsPropGetInitInfo**](/windows/win32/Adsprop/nf-adsprop-adspropgetinitinfo?branch=master) to obtain data about regarding the directory object that the property sheet extension applies to. The **ADsPropGetInitInfo** function sends the **WM\_ADSPROP\_NOTIFY\_PAGEINIT** message to the notification object to achieve this result.


```C++
WM_ADSPROP_NOTIFY_PAGEINIT

    WPARAM wParam
    LPARAM pADsPropInitParams
    
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle of the notification object. This is the *hNotifyObject* parameter obtained by a call to [**ADsPropCreateNotifyObj**](/windows/win32/Adsprop/nf-adsprop-adspropcreatenotifyobj?branch=master).

</dd> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*pADsPropInitParams* 
</dt> <dd>

Pointer to an [**ADSPROPINITPARAMS**](/windows/win32/Adsprop/ns-adsprop-_adspropinitparams?branch=master) structure that receives the directory object information. This is the *pInitParams* parameter passed to [**ADsPropCreateNotifyObj**](/windows/win32/Adsprop/nf-adsprop-adspropcreatenotifyobj?branch=master).

</dd> </dl>

## Return value

This message has no return value.

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

[**ADsPropGetInitInfo**](/windows/win32/Adsprop/nf-adsprop-adspropgetinitinfo?branch=master)
</dt> <dt>

[**ADSPROPINITPARAMS**](/windows/win32/Adsprop/ns-adsprop-_adspropinitparams?branch=master)
</dt> </dl>

 

 





