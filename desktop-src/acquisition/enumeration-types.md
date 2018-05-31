---
Description: Enumeration Types
ms.assetid: 767d20df-aeb4-4f86-a705-bfbb7dc254ff
title: Enumeration Types
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumeration Types

The Picture Acquisition application programming interface (API) implements the following enumerated types.



| Enumerated type                                                         | Description                                                                                                                                                                            |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DEVICE\_SELECTION\_DEVICE\_TYPE**](/windows/desktop/api/PhotoAcquire/ne-photoacquire-tagdevice_selection_device_type) | Indicates the type of a selected device; used by [**IPhotoAcquireDeviceSelectionDialog::DoModal**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquiredeviceselectiondialog-domodal).                                    |
| [**ERROR\_ADVISE\_MESSAGE\_TYPE**](/windows/desktop/api/PhotoAcquire/ne-photoacquire-tagerror_advise_message_type)       | Indicates the type of error values that can be passed to the *nMessageType* parameter of [**IPhotoAcquireProgressCB::ErrorAdvise**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireprogresscb-erroradvise).          |
| [**ERROR\_ADVISE\_RESULT**](/windows/desktop/api/PhotoAcquire/ne-photoacquire-tagerror_advise_result)                    | Indicates the type of error values that can be assigned to the *pnErrorAdviseResult* parameter of [**IPhotoAcquireProgressCB::ErrorAdvise**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireprogresscb-erroradvise). |
| [**PROGRESS\_DIALOG\_CHECKBOX\_ID**](/windows/desktop/api/PhotoAcquire/ne-photoacquire-tagprogress_dialog_checkbox_id)   | Indicates the check box on the [**IPhotoProgressDialog**](/windows/desktop/api/photoacquire/nn-photoacquire-iphotoprogressdialog) object.                                                                                            |
| [**PROGRESS\_DIALOG\_IMAGE\_TYPE**](/windows/desktop/api/PhotoAcquire/ne-photoacquire-tagprogress_dialog_image_type)     | Indicates the image type set in [**IPhotoProgressDialog::SetImage**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoprogressdialog-setimage).                                                                               |
| [**USER\_INPUT\_STRING\_TYPE**](/windows/desktop/api/PhotoAcquire/ne-photoacquire-taguser_input_string_type)             | Indicates the type of string to obtain from the user in [**IPhotoAcquireProgressCB::GetUserInput**](/windows/desktop/api/PhotoAcquire/nf-photoacquire-iphotoacquireprogresscb-getuserinput).                                         |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



