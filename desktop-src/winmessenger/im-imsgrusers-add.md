---
title: IMsgrUsers Add method
description: Adds a MessengerUser object to a collection.
ms.assetid: ab176aba-ee6f-4358-8a6a-085713e4cd3c
keywords:
- Add method Windows Messenger
- Add method Windows Messenger , IMsgrUsers interface
- IMsgrUsers interface Windows Messenger , Add method
topic_type:
- apiref
api_name:
- IMsgrUsers.Add
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

# IMsgrUsers::Add method

\[**Add** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Adds a **MessengerUser** object to a collection.

> [!Note]  
> The **Add** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.

 

## Syntax


```C++
HRESULT Add(
  [in] IMsgrUser *pUser
);
```



## Parameters

<dl> <dt>

*pUser* \[in\]
</dt> <dd>

Type: **IMsgrUser\***

Pointer to an [**IMsgrUser**](im-imsgruser.md) interface.

</dd> </dl>

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



 

 





