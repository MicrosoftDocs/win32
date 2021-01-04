---
title: IMsTscAxEvents OnAuthenticationWarningDismissed method
description: Called after an ActiveX control displays an authentication dialog box (for example, the certificate error dialog box).
ms.assetid: bf5dbe4a-9129-47b3-9808-ed09d9010099
ms.tgt_platform: multiple
keywords:
- OnAuthenticationWarningDismissed method Remote Desktop Services
- OnAuthenticationWarningDismissed method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnAuthenticationWarningDismissed method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnAuthenticationWarningDismissed
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnAuthenticationWarningDismissed method

Called after an ActiveX control displays an authentication dialog box (for example, the certificate error dialog box).

## Syntax


```C++
void OnAuthenticationWarningDismissed();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If needed, the [**UIParentWindowHandle**](imsrdpclientnonscriptable2-uiparentwindowhandle.md) property of the [**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md) interface can be used to revert any parenting that may have been done in the [**OnAuthenticationWarningDisplayed**](imstscaxevents-onauthenticationwarningdisplayed.md) method.

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

[**OnAuthenticationWarningDisplayed**](imstscaxevents-onauthenticationwarningdisplayed.md)
</dt> <dt>

[**UIParentWindowHandle**](imsrdpclientnonscriptable2-uiparentwindowhandle.md)
</dt> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





