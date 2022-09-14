---
title: IMsTscAxEvents OnLoginComplete method
description: Called when the client control has successfully logged on to a Remote Desktop Session Host (RD Session Host) server, following the display of the Windows Logon dialog box.
ms.assetid: acb345a6-3153-4b8f-ac51-fe0c19fa750a
ms.tgt_platform: multiple
keywords:
- OnLoginComplete method Remote Desktop Services
- OnLoginComplete method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnLoginComplete method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnLoginComplete
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnLoginComplete method

Called when the client control has successfully logged on to a Remote Desktop Session Host (RD Session Host) server, following the display of the Windows Logon dialog box.

## Syntax


```C++
void OnLoginComplete();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that the control has completed logon.

## Examples

The following example shows how to handle this event by using Visual Basic Scripting code. The assumption in this example is that your control object is named "MsRdpClient".

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).


```VB
Sub MsRdpClient.OnLoginComplete()
    Msgbox("Login has completed")
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

 

 





