---
title: IMsgrUsers Remove method
description: Removes a MsgrObject object from a collection.
ms.assetid: 48753746-895d-4e53-ab58-16cdfe8a6adb
keywords:
- Remove method Windows Messenger
- Remove method Windows Messenger , IMsgrUsers interface
- IMsgrUsers interface Windows Messenger , Remove method
topic_type:
- apiref
api_name:
- IMsgrUsers.Remove
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

# IMsgrUsers::Remove method

\[**Remove** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Removes a [**MsgrObject**](im-msgrobject.md) object from a collection.

> [!Note]  
> The **Remove** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Remove**](im-imessengercontacts-remove.md) instead.

 

## Syntax


```C++
HRESULT Remove(
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



 

 





