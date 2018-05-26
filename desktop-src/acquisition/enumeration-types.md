---
Description: Enumeration Types
ms.assetid: 767d20df-aeb4-4f86-a705-bfbb7dc254ff
title: Enumeration Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumeration Types

The Picture Acquisition application programming interface (API) implements the following enumerated types.



| Enumerated type                                                         | Description                                                                                                                                                                            |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DEVICE\_SELECTION\_DEVICE\_TYPE**](/windows/win32/PhotoAcquire/ne-photoacquire-tagdevice_selection_device_type?branch=master) | Indicates the type of a selected device; used by [**IPhotoAcquireDeviceSelectionDialog::DoModal**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquiredeviceselectiondialog-domodal?branch=master).                                    |
| [**ERROR\_ADVISE\_MESSAGE\_TYPE**](/windows/win32/PhotoAcquire/ne-photoacquire-tagerror_advise_message_type?branch=master)       | Indicates the type of error values that can be passed to the *nMessageType* parameter of [**IPhotoAcquireProgressCB::ErrorAdvise**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireprogresscb-erroradvise?branch=master).          |
| [**ERROR\_ADVISE\_RESULT**](/windows/win32/PhotoAcquire/ne-photoacquire-tagerror_advise_result?branch=master)                    | Indicates the type of error values that can be assigned to the *pnErrorAdviseResult* parameter of [**IPhotoAcquireProgressCB::ErrorAdvise**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireprogresscb-erroradvise?branch=master). |
| [**PROGRESS\_DIALOG\_CHECKBOX\_ID**](/windows/win32/PhotoAcquire/ne-photoacquire-tagprogress_dialog_checkbox_id?branch=master)   | Indicates the check box on the [**IPhotoProgressDialog**](/windows/win32/photoacquire/nn-photoacquire-iphotoprogressdialog?branch=master) object.                                                                                            |
| [**PROGRESS\_DIALOG\_IMAGE\_TYPE**](/windows/win32/PhotoAcquire/ne-photoacquire-tagprogress_dialog_image_type?branch=master)     | Indicates the image type set in [**IPhotoProgressDialog::SetImage**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoprogressdialog-setimage?branch=master).                                                                               |
| [**USER\_INPUT\_STRING\_TYPE**](/windows/win32/PhotoAcquire/ne-photoacquire-taguser_input_string_type?branch=master)             | Indicates the type of string to obtain from the user in [**IPhotoAcquireProgressCB::GetUserInput**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireprogresscb-getuserinput?branch=master).                                         |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



