---
title: IMsgrObject LocalFriendlyName property
description: Retrieves the friendly (display) name of the local client user.
ms.assetid: 56b524fe-4a0e-4121-b421-c1ee589dc19d
keywords:
- LocalFriendlyName property Windows Messenger
- LocalFriendlyName property Windows Messenger , IMsgrObject interface
- IMsgrObject interface Windows Messenger , LocalFriendlyName property
topic_type:
- apiref
api_name:
- IMsgrObject.LocalFriendlyName
- IMsgrObject.get_LocalFriendlyName
api_location:
- Msmsgs.exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMsgrObject::LocalFriendlyName property

\[**LocalFriendlyName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the friendly (display) name of the local client user.

> [!Note]  
> The **LocalFriendlyName** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MyFriendlyName**](im-imessenger-myfriendlyname.md) instead.

 

This property is read-only.

## Syntax


```C++
HRESULT get_LocalFriendlyName(
  [out, retval] BSTR *pbstrName
);
```



## Property value

Pointer to a **BSTR** that contains the current user's friendly name.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





