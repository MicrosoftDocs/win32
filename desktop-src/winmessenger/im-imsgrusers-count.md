---
title: IMsgrUsers Count property
description: Retrieves the number of MessengerUser objects in the collection.
ms.assetid: 194e5dec-79b6-4f84-a334-393302d479d0
keywords:
- Count property Windows Messenger
- Count property Windows Messenger , IMsgrUsers interface
- IMsgrUsers interface Windows Messenger , Count property
topic_type:
- apiref
api_name:
- IMsgrUsers.Count
- IMsgrUsers.get_Count
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

# IMsgrUsers::Count property

\[**Count** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the number of **MessengerUser** objects in the collection.

> [!Note]  
> The **Count** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Count**](im-imessengercontacts-count.md) instead.

 

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *pcUsers
);
```



## Property value

Pointer to a **LONG** that provides the number of **MessengerUser** objects in the collection.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





