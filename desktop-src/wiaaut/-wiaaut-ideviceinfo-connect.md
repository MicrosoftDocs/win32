---
title: DeviceInfo.Connect method
description: Establishes a connection with a device.
ms.assetid: fe77af57-d2bf-49d7-ba85-72e8251c6d50
keywords:
- Connect method WIA Automation
- Connect method WIA Automation , DeviceInfo object
- DeviceInfo object WIA Automation , Connect method
topic_type:
- apiref
api_name:
- DeviceInfo.Connect
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DeviceInfo.Connect method

Establishes a connection with a device.

## Syntax


```VB
ppResult = .Connect( _
) As HRESULT
```



## Parameters

This method has no parameters.

## Return value

Type: **[**Device**](-wiaaut-device.md)\*\***

Returns a [**Device**](-wiaaut-device.md) object.

## Remarks

For example code, see [Implement a Web Camera ASP Page](-wiaaut-shared-samples.md#implement-a-web-camera-asp-page) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)
</dt> <dt>

[**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)
</dt> <dt>

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**DeviceInfo**](-wiaaut-deviceinfo.md)
</dt> <dt>

[**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)
</dt> </dl>

 

 





