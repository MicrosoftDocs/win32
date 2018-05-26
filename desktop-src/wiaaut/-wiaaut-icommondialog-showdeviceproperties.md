---
title: CommonDialog.ShowDeviceProperties method
description: Displays the Properties dialog box for the specified Device.
ms.assetid: 0c9617a1-d373-4017-bd5d-33882d40be71
keywords:
- ShowDeviceProperties method WIA Automation
- ShowDeviceProperties method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowDeviceProperties method
topic_type:
- apiref
api_name:
- CommonDialog.ShowDeviceProperties
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

# CommonDialog.ShowDeviceProperties method

Displays the **Properties** dialog box for the specified [**Device**](-wiaaut-device.md).

## Syntax


```VB
CommonDialog.ShowDeviceProperties( _
  ByVal Device As Device, _
  [ ByVal CancelError As VARIANT_BOOL ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*Device* \[in\]
</dt> <dd>

Type: **[**Device**](-wiaaut-device.md)\***

Required. [**Device**](-wiaaut-device.md) value.

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

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Examples

The following example shows how to display the **Properties** dialog box for the selected device.


```
Dim dev 'As Device
Set dev = CommonDialog1.ShowSelectDevice
CommonDialog1.ShowDeviceProperties dev
```



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

[**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)
</dt> <dt>

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**Connect**](-wiaaut-ideviceinfo-connect.md)
</dt> <dt>

[**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)
</dt> </dl>

 

 





