---
title: DMsgrSessionManagerEvents OnLockStatusChanged event
description: Fires when the lock status changes.
ms.assetid: f2a5101c-d286-4bf9-aca7-2876d9be6277
keywords:
- OnLockStatusChanged event Windows Messenger
- OnLockStatusChanged event Windows Messenger , DMsgrSessionManagerEvents interface
- DMsgrSessionManagerEvents interface Windows Messenger , OnLockStatusChanged event
topic_type:
- apiref
api_name:
- DMsgrSessionManagerEvents.OnLockStatusChanged
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMsgrSessionManagerEvents::OnLockStatusChanged event

\[**OnLockStatusChanged** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when the lock status changes.

## Syntax


```C++
void OnLockStatusChanged(
  [in] LockStatus eStatus
);
```



## Parameters

<dl> <dt>

*eStatus* \[in\]
</dt> <dd>

Varible of type **LockStatus** that contains the value of the new lock status.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Sessions.h (include Mdispid.h)</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Sessions.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md)
</dt> <dt>

[**LockStatus**](im-lockstatus-enum.md)
</dt> </dl>

 

 





