---
title: IBasicIMOld CreateUser method
description: Creates a Basic Instant Messaging Service (IM) user object.
ms.assetid: 8edaca60-a9e3-4c1c-80b1-7b6711e1076f
keywords:
- CreateUser method Windows Messenger
- CreateUser method Windows Messenger , IBasicIMOld interface
- IBasicIMOld interface Windows Messenger , CreateUser method
topic_type:
- apiref
api_name:
- IBasicIMOld.CreateUser
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

# IBasicIMOld::CreateUser method

\[**CreateUser** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Creates a Basic Instant Messaging Service (IM) user object.

> [!Note]  
> The **CreateUser** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**GetContact**](im-imessenger-getcontact.md) instead.

 

## Syntax


```C++
HRESULT CreateUser(
  [in]          BSTR         bstrLogonName,
  [out, retval] IBasicIMUser **ppBIMUser
);
```



## Parameters

<dl> <dt>

*bstrLogonName* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that contains the user's sign-in name.

</dd> <dt>

*ppBIMUser* \[out, retval\]
</dt> <dd>

Type: **IBasicIMUser\*\***

Address of a pointer to an [**IBasicIMUser**](im-ibasicimuser.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





