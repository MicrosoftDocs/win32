---
title: IMsTscAxEvents OnAutoReconnecting2 method
description: Called when a client is in the process of automatically reconnecting a session with a Remote Desktop Session Host (RD Session Host) server. | IMsTscAxEvents OnAutoReconnecting2 method
ms.assetid: 20F69798-5397-440C-9D0D-45AE417623A7
ms.tgt_platform: multiple
keywords:
- OnAutoReconnecting2 method Remote Desktop Services
- OnAutoReconnecting2 method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnAutoReconnecting2 method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnAutoReconnecting2
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnAutoReconnecting2 method

Called when a client is in the process of automatically reconnecting a session with a Remote Desktop Session Host (RD Session Host) server. This is an enhanced version of the [**OnAutoReconnecting**](-imstscaxevents--onautoreconnecting.md) method.

## Syntax


```C++
void OnAutoReconnecting2(
  [in] LONG         disconnectReason,
  [in] VARIANT_BOOL networkAvailable,
  [in] LONG         attemptCount,
  [in] LONG         maxAttemptCount
);
```



## Parameters

<dl> <dt>

*disconnectReason* \[in\]
</dt> <dd>

Code that describes the reason for the last session disconnection.

</dd> <dt>

*networkAvailable* \[in\]
</dt> <dd>

Specifies if the network is available.

</dd> <dt>

*attemptCount* \[in\]
</dt> <dd>

Number of attempts that have been made in the current automatic reconnection process. This count increases by one for each attempt made.

</dd> <dt>

*maxAttemptCount* \[in\]
</dt> <dd>

The maximum number of attempts that will be made in the current automatic reconnection process.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





