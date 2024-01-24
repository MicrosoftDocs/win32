---
title: IMsTscAxEvents OnServiceMessageReceived method
description: Called when the client receives a system message.
ms.assetid: 9D230AA3-30F8-4BDF-89D6-D33AF42D0E85
ms.tgt_platform: multiple
keywords:
- OnServiceMessageReceived method Remote Desktop Services
- OnServiceMessageReceived method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnServiceMessageReceived method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnServiceMessageReceived
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnServiceMessageReceived method

Called when the client receives a system message.

## Syntax


```C++
void OnServiceMessageReceived(
  [in] BSTR serviceMessage
);
```



## Parameters

<dl> <dt>

*serviceMessage* \[in\]
</dt> <dd>

Specifies the system message.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

For more information about system messages, see [Configure Messaging for a Remote Desktop Gateway Server](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd834700(v=ws.11)).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

