---
title: IMsgrUsers Item method
description: Retrieves a specific MessengerUser object by numeric index.
ms.assetid: 2ebad5d1-5cc4-449c-b0b8-66710f7ce8ea
keywords:
- Item method Windows Messenger
- Item method Windows Messenger , IMsgrUsers interface
- IMsgrUsers interface Windows Messenger , Item method
topic_type:
- apiref
api_name:
- IMsgrUsers.Item
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

# IMsgrUsers::Item method

\[**Item** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a specific **MessengerUser** object by numeric index.

> [!Note]  
> The **Item** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Item**](im-imessengercontacts-item.md) instead.

 

## Syntax


```C++
HRESULT Item(
  [in]          long               Index,
  [out, retval] IMessengerIMWindow **ppIMWindow
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **long**

**LONG** that specifies the index of the desired **MessengerUser**.

</dd> <dt>

*ppIMWindow* \[out, retval\]
</dt> <dd>

Type: **IMessengerIMWindow\*\***

Address of a pointer to the [**IMessengerIMWindow**](im-imessengerimwindow.md) interface on a **MessengerUser** object requested with *Index*.

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



 

 





