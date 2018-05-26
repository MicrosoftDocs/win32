---
title: IMsgrObject LocalState property
description: Sets or retrieves the connection state of the local client user in the primary service.
ms.assetid: 751bed67-5c6b-4053-9079-b1b257171ca8
keywords:
- LocalState property Windows Messenger
- LocalState property Windows Messenger , IMsgrObject interface
- IMsgrObject interface Windows Messenger , LocalState property
topic_type:
- apiref
api_name:
- IMsgrObject.LocalState
- IMsgrObject.get_LocalState
- IMsgrObject.put_LocalState
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

# IMsgrObject::LocalState property

\[**LocalState** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the connection state of the local client user in the primary service.

> [!Note]  
> The **LocalState** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MyStatus**](im-imessenger-mystatus.md) instead.

 

This property is read/write.

## Syntax


```C++
HRESULT put_LocalState(
  [in]          MSTATE mState
);

HRESULT get_LocalState(
  [out, retval] MSTATE *pmState
);
```



## Property value

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





