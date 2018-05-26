---
title: CommonDialog object
description: Contains all the methods that display a UI. The CommonDialog control is an invisible-at-run-time control that you can create using \ 0034;WIA.CommonDialog \ 0034; as the ProgID in a call to CreateObject or by dropping a CommonDialog object on a form.
ms.assetid: f7e46ee7-9d49-482c-a998-92555e979636
keywords:
- CommonDialog object WIA Automation
- CommonDialog object WIA Automation , described
topic_type:
- apiref
api_name:
- CommonDialog
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CommonDialog object

Contains all the methods that display a UI. The **CommonDialog** control is an invisible-at-run-time control that you can create using "WIA.CommonDialog" as the ProgID in a call to [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx) or by dropping a **CommonDialog** object on a form.

## Members

The **CommonDialog** object has these types of members:

-   [Methods](#methods)

### Methods

The **CommonDialog** object has these methods.



| Method                                                                           | Description                                                                                                                                                 |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)               | Displays one or more dialog boxes that enable the user to acquire an image from a hardware device. <br/>                                              |
| [**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)     | Starts the **Scanner and Camera Wizard**. <br/>                                                                                                       |
| [**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)       | Displays the **Properties** dialog box for the specified [**Device**](-wiaaut-device.md).<br/>                                                       |
| [**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)           | Displays the **Properties** dialog box for the specified [**Item**](-wiaaut-item.md).<br/>                                                           |
| [**ShowPhotoPrintingWizard**](-wiaaut-icommondialog-showphotoprintingwizard.md) | Starts the **Photo Printing Wizard** with the absolute path of a specific file or [**Vector**](-wiaaut-vector.md) of absolute paths to files.<br/>   |
| [**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)               | Displays a dialog box that enables the user to select a hardware device for image acquisition. <br/>                                                  |
| [**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)                 | Displays a dialog box that enables the user to select an [**Item**](-wiaaut-item.md) for transfer from a hardware device for image acquisition.<br/> |
| [**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)                       | Displays a **Progress** dialog box while transferring the specified [**Item**](-wiaaut-item.md) to the local computer.<br/>                          |



 

## Remarks

For example code, see [Display all the Properties for the Selected Device](-wiaaut-shared-samples.md#display-all-the-properties-for-the-selected-device---2) in Shared Samples.

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

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)
</dt> <dt>

[**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)
</dt> <dt>

[**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)
</dt> <dt>

[**ShowPhotoPrintingWizard**](-wiaaut-icommondialog-showphotoprintingwizard.md)
</dt> <dt>

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> </dl>

 

 





