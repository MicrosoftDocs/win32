---
title: IMsTscAxEvents OnConnecting method
description: Called when the client control begins connecting to a server in response to a call to IMsTscAx Connect.
ms.assetid: c5e367a8-126a-48bb-bc94-1063f77e8239
ms.tgt_platform: multiple
keywords:
- OnConnecting method Remote Desktop Services
- OnConnecting method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnConnecting method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnConnecting
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnConnecting method

Called when the client control begins connecting to a server in response to a call to [**IMsTscAx::Connect**](imstscax-connect.md).

## Syntax


```C++
void OnConnecting();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that the control has begun connecting.

## Examples

The following example shows how to handle this event with Visual Basic Scripting code. The assumption in this example is that your control object is named "MsRdpClient".

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).


```VB
Sub MsRdpClient.OnConnecting()
    Msgbox("Connecting")
End sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





