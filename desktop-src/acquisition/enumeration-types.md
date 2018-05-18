---
Description: Enumeration Types
ms.assetid: '767d20df-aeb4-4f86-a705-bfbb7dc254ff'
title: Enumeration Types
---

# Enumeration Types

The Picture Acquisition application programming interface (API) implements the following enumerated types.



| Enumerated type                                                         | Description                                                                                                                                                                            |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DEVICE\_SELECTION\_DEVICE\_TYPE**](device-selection-device-type.md) | Indicates the type of a selected device; used by [**IPhotoAcquireDeviceSelectionDialog::DoModal**](iphotoacquiredeviceselectiondialog-domodal.md).                                    |
| [**ERROR\_ADVISE\_MESSAGE\_TYPE**](error-advise-message-type.md)       | Indicates the type of error values that can be passed to the *nMessageType* parameter of [**IPhotoAcquireProgressCB::ErrorAdvise**](iphotoacquireprogresscb-erroradvise.md).          |
| [**ERROR\_ADVISE\_RESULT**](error-advise-result.md)                    | Indicates the type of error values that can be assigned to the *pnErrorAdviseResult* parameter of [**IPhotoAcquireProgressCB::ErrorAdvise**](iphotoacquireprogresscb-erroradvise.md). |
| [**PROGRESS\_DIALOG\_CHECKBOX\_ID**](progress-dialog-checkbox-id.md)   | Indicates the check box on the [**IPhotoProgressDialog**](iphotoprogressdialog.md) object.                                                                                            |
| [**PROGRESS\_DIALOG\_IMAGE\_TYPE**](progress-dialog-image-type.md)     | Indicates the image type set in [**IPhotoProgressDialog::SetImage**](iphotoprogressdialog-setimage.md).                                                                               |
| [**USER\_INPUT\_STRING\_TYPE**](user-input-string-type.md)             | Indicates the type of string to obtain from the user in [**IPhotoAcquireProgressCB::GetUserInput**](iphotoacquireprogresscb-getuserinput.md).                                         |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



