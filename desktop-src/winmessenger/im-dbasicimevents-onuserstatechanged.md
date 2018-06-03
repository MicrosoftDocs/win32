---
title: DBasicIMEvents OnUserStateChanged event
description: Indicates that the user's state has changed.
ms.assetid: 3ebc53aa-38f0-4214-b417-e994f13509d3
keywords:
- OnUserStateChanged event Windows Messenger
- OnUserStateChanged event Windows Messenger , DBasicIMEvents interface
- DBasicIMEvents interface Windows Messenger , OnUserStateChanged event
topic_type:
- apiref
api_name:
- DBasicIMEvents.OnUserStateChanged
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBasicIMEvents::OnUserStateChanged event

\[**OnUserStateChanged** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the user's state has changed.

> [!Note]  
> The **OnUserStateChanged** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnContactStatusChange**](im-dmessengerevents-oncontactstatuschange.md) instead.

 

## Syntax


```C++
void OnUserStateChanged(
  [in] IBasicIMUser *pBIMUser,
  [in] BIMSTATE     mPrevStateOE
);
```



## Parameters

<dl> <dt>

*pBIMUser* \[in\]
</dt> <dd>

Pointer to an [**IBasicIMUser**](im-ibasicimuser.md) interface.

</dd> <dt>

*mPrevStateOE* \[in\]
</dt> <dd>

[**BIMSTATE**](im-bimstate.md) enumerated type that receives the previous state of the user.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                  |                                |
|----------------------------------|--------------------------------|
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



 

 





