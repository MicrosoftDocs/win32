---
title: IMsTscAxEvents OnAuthenticationWarningDisplayed method
description: Called before an ActiveX control displays an authentication dialog box (for example, the certificate error dialog box).
ms.assetid: ce307e5f-5e26-4041-bbd5-6871c0678da4
ms.tgt_platform: multiple
keywords:
- OnAuthenticationWarningDisplayed method Remote Desktop Services
- OnAuthenticationWarningDisplayed method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnAuthenticationWarningDisplayed method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnAuthenticationWarningDisplayed
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnAuthenticationWarningDisplayed method

Called before an ActiveX control displays an authentication dialog box (for example, the certificate error dialog box).

## Syntax


```C++
void OnAuthenticationWarningDisplayed();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If needed, the [**UIParentWindowHandle**](imsrdpclientnonscriptable2-uiparentwindowhandle.md) property of the [**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md) interface can be used to ensure that the modal authentication dialog to be displayed will be parented by a specified window (this may be necessary to prevent users from using other dialog boxes while the authentication dialog box is displayed). By default, the parent is the ActiveX control window.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2008 with SP1<br/>                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**OnAuthenticationWarningDismissed**](imstscaxevents-onauthenticationwarningdismissed.md)
</dt> <dt>

[**UIParentWindowHandle**](imsrdpclientnonscriptable2-uiparentwindowhandle.md)
</dt> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





