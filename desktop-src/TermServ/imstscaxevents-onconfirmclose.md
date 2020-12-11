---
title: IMsTscAxEvents OnConfirmClose method
description: Called when the client calls the IMsRdpClient RequestClose method.
ms.assetid: fb149fbc-9415-4c4c-8d4b-e22214ac38cb
ms.tgt_platform: multiple
keywords:
- OnConfirmClose method Remote Desktop Services
- OnConfirmClose method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnConfirmClose method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnConfirmClose
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnConfirmClose method

Called when the client calls the [**IMsRdpClient::RequestClose**](imsrdpclient-requestclose.md) method. In response to this event, the user should be prompted to confirm closing the connection. For more information, see the following Remarks section.

## Syntax


```C++
void OnConfirmClose(
  [out] VARIANT_BOOL *pfAllowClose
);
```



## Parameters

<dl> <dt>

*pfAllowClose* \[out\]
</dt> <dd>

If **VARIANT\_TRUE**, the default, indicates that the user wants to close the connection. If **VARIANT\_FALSE**, indicates that the user does not want to close the connection. For more information, see the following Remarks section.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

When a container application calls the [**IMsRdpClient::RequestClose**](imsrdpclient-requestclose.md) method, that method returns a value indicating whether the container should wait for an **OnConfirmClose** event to occur before closing the control connection. If **RequestClose** returns **controlCloseWaitForEvents**, and the user is connected and logged on to their Remote Desktop Services session, the **OnConfirmClose** event fires. At that point the container application can prompt the user, asking whether the user wants to close the connection. If the user wants to close the connection, the application should set the *pfAllowClose* parameter to **VARIANT\_TRUE** and proceed with closing the connection. If the user does not want to close, the application should set *pfAllowClose* to **VARIANT\_FALSE** and leave the connection open.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

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

 

 





