---
Description: 'Note  This interface has been deprecated. Note  Microsoft does not provide an implementation of this interface.'
ms.assetid: 'fb2927cf-c979-411f-a896-d010b684acf2'
title: IAMAnalogVideoEncoder interface
---

# IAMAnalogVideoEncoder interface

> [!Note]  
> This interface has been deprecated.

 

> [!Note]  
> Microsoft does not provide an implementation of this interface. Third parties might implement it.

 

The **IAMAnalogVideoEncoder** interface might be implemented by a hardware video encoder in video capture operations when an application is streaming data to disk and sending it back out to videotape.

## Members

The **IAMAnalogVideoEncoder** interface inherits from the [**IUnknown**](com.iunknown) interface. **IAMAnalogVideoEncoder** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMAnalogVideoEncoder** interface has these methods.



| Method                                                                          | Description                                                                                                    |
|:--------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**get\_AvailableTVFormats**](iamanalogvideoencoder-get-availabletvformats.md) | Retrieves the analog video standards (NTSC/M, PAL/B, SECAM/K1, and so on) supported by the encoder.<br/> |
| [**get\_CCEnable**](iamanalogvideoencoder-get-ccenable.md)                     | Determines whether closed captioning is currently enabled.<br/>                                          |
| [**get\_CopyProtection**](iamanalogvideoencoder-get-copyprotection.md)         | Determines whether copy protection is currently enabled.<br/>                                            |
| [**get\_TVFormat**](iamanalogvideoencoder-get-tvformat.md)                     | Retrieves the analog video standard that the encoder is currently set to.<br/>                           |
| [**put\_CCEnable**](iamanalogvideoencoder-put-ccenable.md)                     | Enables or disables closed captioning.<br/>                                                              |
| [**put\_CopyProtection**](iamanalogvideoencoder-put-copyprotection.md)         | Sets the level of copy protection for the encoder.<br/>                                                  |
| [**put\_TVFormat**](iamanalogvideoencoder-put-tvformat.md)                     | Sets the encoder to a particular analog video standard.<br/>                                             |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




