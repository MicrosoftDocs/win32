---
title: CommonDialog.ShowSelectDevice method
description: Displays a dialog box that enables the user to select a hardware device for image acquisition.
ms.assetid: 1dfb76ca-5147-4e01-a7f3-1d579025474a
keywords:
- ShowSelectDevice method WIA Automation
- ShowSelectDevice method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowSelectDevice method
topic_type:
- apiref
api_name:
- CommonDialog.ShowSelectDevice
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

# CommonDialog.ShowSelectDevice method

Displays a dialog box that enables the user to select a hardware device for image acquisition.

## Syntax


```VB
ppResult = .ShowSelectDevice( _
  [ ByVal DeviceType As WiaDeviceType ], _
  [ ByVal AlwaysSelectDevice As VARIANT_BOOL ], _
  [ ByVal CancelError As VARIANT_BOOL ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*DeviceType* \[in, optional\]
</dt> <dd>

Type: **[**WiaDeviceType**](-wiaaut-wiadevicetype.md)**

[**WiaDeviceType**](-wiaaut-wiadevicetype.md) value.



| Value                                                                                                                                                  | Meaning                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt></dt> <dt>UnspecifiedDeviceType</dt> </dl> | Default. The device type is unknown.<br/> |



 

</dd> <dt>

*AlwaysSelectDevice* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to always show the select device dialog box.



| Value                                                                                                                                  | Meaning                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Default. Do not show the select device dialog box.<br/> |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Show the select device dialog box.<br/>                 |



 

</dd> <dt>

*CancelError* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to generate an error if the user cancels the dialog box.



| Value                                                                                                                                  | Meaning                                       |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Default. Do not generate an error.<br/> |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Generate an error.<br/>                 |



 

</dd> </dl>

## Return value

Type: **[**Device**](-wiaaut-device.md)\*\***

Returns the selected [**Device**](-wiaaut-device.md) object on success, otherwise returns **Nothing**.

## Remarks

For example code, see [Take a Picture](-wiaaut-shared-samples.md#take-a-picture) in Shared Samples.

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

[**CommonDialog**](-wiaaut-commondialog.md)
</dt> <dt>

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)
</dt> <dt>

[**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**Type (Device)**](-wiaaut-idevice-type.md)
</dt> <dt>

[**Connect**](-wiaaut-ideviceinfo-connect.md)
</dt> <dt>

[**Type (DeviceInfo)**](-wiaaut-ideviceinfo-type.md)
</dt> <dt>

[**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)
</dt> </dl>

 

 





