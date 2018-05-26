---
title: DMsgrObjectEvents OnUserFriendlyNameChangeResult event
description: Indicates that a user in the User List has changed his or her friendly name.
ms.assetid: 1d49af38-8f35-4b2b-8345-dcd586dc2708
keywords:
- OnUserFriendlyNameChangeResult event Windows Messenger
- OnUserFriendlyNameChangeResult event Windows Messenger , DMsgrObjectEvents interface
- DMsgrObjectEvents interface Windows Messenger , OnUserFriendlyNameChangeResult event
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnUserFriendlyNameChangeResult
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMsgrObjectEvents::OnUserFriendlyNameChangeResult event

\[**OnUserFriendlyNameChangeResult** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a user in the User List has changed his or her friendly name.

> [!Note]  
> The **OnUserFriendlyNameChangeResult** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnContactFriendlyNameChange**](im-dmessengerevents-oncontactfriendlynamechange.md) instead.

 

## Syntax


```C++
void OnUserFriendlyNameChangeResult(
  [in] long      hr,
  [in] IMsgrUser *pUser,
  [in] BSTR      bstrPrevFriendlyName
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **long**.

</dd> <dt>

*pUser* \[in\]
</dt> <dd>

Pointer to an [**IMsgrUser**](im-imsgruser.md) interface.

</dd> <dt>

*bstrPrevFriendlyName* \[in\]
</dt> <dd>

**BSTR** that contains the user's previous friendly name.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                  |                                |
|----------------------------------|--------------------------------|
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



 

 





