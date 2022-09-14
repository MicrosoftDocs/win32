---
title: WM_ADSPROP_NOTIFY_PAGEINIT message (Adsprop.h)
description: An Active Directory property sheet extension calls the ADsPropGetInitInfo to obtain data about regarding the directory object that the property sheet extension applies to.
ms.assetid: 473c5a75-d0d9-4d12-b855-63683e8cdf3f
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
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ADSPROP\_NOTIFY\_PAGEINIT message

An Active Directory property sheet extension calls the [**ADsPropGetInitInfo**](/windows/desktop/api/Adsprop/nf-adsprop-adspropgetinitinfo) to obtain data about regarding the directory object that the property sheet extension applies to. The **ADsPropGetInitInfo** function sends the **WM\_ADSPROP\_NOTIFY\_PAGEINIT** message to the notification object to achieve this result.


```C++
WM_ADSPROP_NOTIFY_PAGEINIT

    WPARAM wParam
    LPARAM pADsPropInitParams
    
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle of the notification object. This is the *hNotifyObject* parameter obtained by a call to [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj).

</dd> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*pADsPropInitParams* 
</dt> <dd>

Pointer to an [**ADSPROPINITPARAMS**](/windows/desktop/api/Adsprop/ns-adsprop-adspropinitparams) structure that receives the directory object information. This is the *pInitParams* parameter passed to [**ADsPropCreateNotifyObj**](/windows/desktop/api/Adsprop/nf-adsprop-adspropcreatenotifyobj).

</dd> </dl>

## Return value

This message has no return value.

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

[**ADsPropGetInitInfo**](/windows/desktop/api/Adsprop/nf-adsprop-adspropgetinitinfo)
</dt> <dt>

[**ADSPROPINITPARAMS**](/windows/desktop/api/Adsprop/ns-adsprop-adspropinitparams)
</dt> </dl>

 

 





