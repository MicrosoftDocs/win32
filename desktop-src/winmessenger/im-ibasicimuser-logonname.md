---
title: IBasicIMUser LogonName property
description: Retrieves the Logon Name of the user.
ms.assetid: 2777d0f4-ace9-494c-89be-84794dcb4733
keywords:
- LogonName property Windows Messenger
- LogonName property Windows Messenger , IBasicIMUser interface
- IBasicIMUser interface Windows Messenger , LogonName property
topic_type:
- apiref
api_name:
- IBasicIMUser.LogonName
- IBasicIMUser.get_LogonName
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IBasicIMUser::LogonName property

\[**LogonName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the Logon Name of the user.

> [!Note]  
> The **LogonName** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**SigninName**](im-imessengercontact-signinname.md) instead.

 

This property is read-only.

## Syntax


```C++
HRESULT get_LogonName(
  [out, retval] BSTR *pbstrLogonName
);
```



## Property value

Pointer to a **BSTR** that receives the Logon Name of the user.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





