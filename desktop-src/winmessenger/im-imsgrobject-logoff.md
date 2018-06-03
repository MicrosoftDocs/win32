---
title: IMsgrObject Logoff method
description: Signs the current client user out of all Messenger services.
ms.assetid: 16b7c2fb-1337-4a2b-8a5d-fed813d03f79
keywords:
- Logoff method Windows Messenger
- Logoff method Windows Messenger , IMsgrObject interface
- IMsgrObject interface Windows Messenger , Logoff method
topic_type:
- apiref
api_name:
- IMsgrObject.Logoff
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

# IMsgrObject::Logoff method

\[**Logoff** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Signs the current client user out of all Messenger services.

> [!Note]  
> The **Logoff** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Signout**](im-imessenger-signout.md) instead.

 

## Syntax


```C++
HRESULT Logoff();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





