---
title: IMsgrObject LocalLogonName property
description: Retrieves the sign-in name of the local client user.
ms.assetid: 53882d13-fe5f-493a-a180-0f54f5714abf
keywords:
- LocalLogonName property Windows Messenger
- LocalLogonName property Windows Messenger , IMsgrObject interface
- IMsgrObject interface Windows Messenger , LocalLogonName property
topic_type:
- apiref
api_name:
- IMsgrObject.LocalLogonName
- IMsgrObject.get_LocalLogonName
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

# IMsgrObject::LocalLogonName property

\[**LocalLogonName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the sign-in name of the local client user.

> [!Note]  
> The **LocalLogonName** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MySigninName**](im-imessenger-mysigninname.md) instead.

 

This property is read-only.

## Syntax


```C++
HRESULT get_LocalLogonName(
  [out, retval] BSTR *pbstrName
);
```



## Property value

Pointer to a **BSTR** that contains the current user's sign-in name.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





