---
title: DMsgrObjectEvents OnListAddResult event
description: Indicates the result of an attempt to add to the Messenger User object's User List.
ms.assetid: d949fc45-7349-4d8f-8f31-f6194f402465
keywords:
- OnListAddResult event Windows Messenger
- OnListAddResult event Windows Messenger , DMsgrObjectEvents interface
- DMsgrObjectEvents interface Windows Messenger , OnListAddResult event
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnListAddResult
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DMsgrObjectEvents::OnListAddResult event

\[**OnListAddResult** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates the result of an attempt to add to the **Messenger User** object's User List.

> [!Note]  
> The **OnListAddResult** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnContactListAdd**](im-dmessengerevents-oncontactlistadd.md) instead.

 

## Syntax


```C++
void OnListAddResult(
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



 

 





