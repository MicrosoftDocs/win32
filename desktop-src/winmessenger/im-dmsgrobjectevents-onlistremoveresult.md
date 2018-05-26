---
title: DMsgrObjectEvents OnListRemovedResult event
description: Indicates the result of an attempt to remove a user from the Messenger User objects User List.
ms.assetid: 2bfd454a-3956-4f9f-96b3-8834324f5500
keywords:
- OnListRemovedResult event Windows Messenger
- OnListRemovedResult event Windows Messenger , DMsgrObjectEvents interface
- DMsgrObjectEvents interface Windows Messenger , OnListRemovedResult event
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnListRemovedResult
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMsgrObjectEvents::OnListRemovedResult event

\[**OnListRemovedResult** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates the result of an attempt to remove a user from the **Messenger User** object's User List.

> [!Note]  
> The **OnListRemovedResult** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnContactListRemove**](im-dmessengerevents-oncontactlistremove.md) instead.

 

## Syntax


```C++
void OnListRemovedResult(
  [in] long      hr,
  [in] MLIST     mList,
  [in] IMsgrUser *pUser
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **long**.

</dd> <dt>

*mList* \[in\]
</dt> <dd>

[**MLIST**](im-mlist.md) enumerated type.

</dd> <dt>

*pUser* \[in\]
</dt> <dd>

Pointer to an [**IMsgrUser**](im-imsgruser.md) interface.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                  |                                |
|----------------------------------|--------------------------------|
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



 

 





