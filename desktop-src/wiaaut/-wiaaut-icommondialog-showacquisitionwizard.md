---
title: CommonDialog.ShowAcquisitionWizard method
description: Starts the Scanner and Camera Wizard.
ms.assetid: 886be445-a969-49e2-8bc8-baeed71e3478
keywords:
- ShowAcquisitionWizard method WIA Automation
- ShowAcquisitionWizard method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowAcquisitionWizard method
topic_type:
- apiref
api_name:
- CommonDialog.ShowAcquisitionWizard
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

# CommonDialog.ShowAcquisitionWizard method

Starts the **Scanner and Camera Wizard**.

## Syntax


```VB
pvResult = .ShowAcquisitionWizard( _
  ByVal Device As Device _
) As HRESULT
```



## Parameters

<dl> <dt>

*Device* \[in\]
</dt> <dd>

Type: **[**Device**](-wiaaut-device.md)\***

Required. [**Device**](-wiaaut-device.md) object.

</dd> </dl>

## Return value

Type: **VARIANT\***

Returns **Nothing**.

## Examples

The following example shows how to launch the Windows **Scanner and Camera Wizard**.


```
Dim dev 'As Device
Set dev = CommonDialog1.ShowSelectDevice
CommonDialog1.ShowAcquisitionWizard dev
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

[**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)
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

 

 





