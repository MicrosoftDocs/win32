---
title: DMsgrObjectEvents OnLocalFriendlyNameChangeResult event
description: Indicates that the settings of a user in the local client's User List have changed.
ms.assetid: '0d5e4c23-fcf1-4e23-948d-c0c3c4beefe7'
keywords: ["OnLocalFriendlyNameChangeResult event Windows Messenger", "OnLocalFriendlyNameChangeResult event Windows Messenger , DMsgrObjectEvents interface", "DMsgrObjectEvents interface Windows Messenger , OnLocalFriendlyNameChangeResult event"]
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnLocalFriendlyNameChangeResult
api_type:
- COM
---

# DMsgrObjectEvents::OnLocalFriendlyNameChangeResult event

\[**OnLocalFriendlyNameChangeResult** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the settings of a user in the local client's User List have changed.

> [!Note]  
> The **OnLocalFriendlyNameChangeResult** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnMyFriendlyNameChange**](im-dmessengerevents-onmyfriendlynamechange.md) instead.

 

## Syntax


```C++
void OnLocalFriendlyNameChangeResult(
  [in] long         hr,
  [in] IMsgrService *pService,
  [in] BSTR         bstrPrevFriendlyName
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **long**.

</dd> <dt>

*pService* \[in\]
</dt> <dd>

Pointer to an [**IMsgrService**](im-imsgrservice.md) interface.

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
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



 

 





