---
title: DMsgrObjectEvents OnLocalStateChangeResult event
description: Indicates that the status of the local client has been changed or that a status change was attempted.
ms.assetid: 0182e081-a109-46be-806b-034343bd6191
keywords:
- OnLocalStateChangeResult event Windows Messenger
- OnLocalStateChangeResult event Windows Messenger , DMsgrObjectEvents interface
- DMsgrObjectEvents interface Windows Messenger , OnLocalStateChangeResult event
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnLocalStateChangeResult
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DMsgrObjectEvents::OnLocalStateChangeResult event

\[**OnLocalStateChangeResult** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the status of the local client has been changed or that a status change was attempted.

> [!Note]  
> The **OnLocalStateChangeResult** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnMyStatusChange**](im-dmessengerevents-onmystatuschange.md) instead.

 

## Syntax


```C++
void OnLocalStateChangeResult(
  [in] long         hr,
  [in] MSTATE       mLocalState,
  [in] IMsgrService *pService
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **long**.

</dd> <dt>

*mLocalState* \[in\]
</dt> <dd>

[**MSTATE**](im-mstate.md) enumerated type.

</dd> <dt>

*pService* \[in\]
</dt> <dd>

Pointer to an [**IMsgrService**](im-imsgrservice.md) interface.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                  |                                |
|----------------------------------|--------------------------------|
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



 

 





