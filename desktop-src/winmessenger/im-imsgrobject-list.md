---
title: IMsgrObject List property
description: Retrieves information about users from an MLIST.
ms.assetid: efa3e9bc-1d34-429d-bc95-44bed1e8b5e7
keywords:
- List property Windows Messenger
- List property Windows Messenger , IMsgrObject interface
- IMsgrObject interface Windows Messenger , List property
topic_type:
- apiref
api_name:
- IMsgrObject.List
- IMsgrObject.get_List
api_location:
- Msmsgs.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMsgrObject::List property

\[**List** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves information about users from an [**MLIST**](im-mlist.md).

> [!Note]  
> The **List** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.

 

This property is read-only.

## Syntax


```C++
HRESULT get_List(
  [in]          MLIST      mList,
  [out, retval] IMsgrUsers **ppUsers
);
```



## Property value

Address of a pointer to an [**IMsgrUsers**](im-imsgrusers.md) interface.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





