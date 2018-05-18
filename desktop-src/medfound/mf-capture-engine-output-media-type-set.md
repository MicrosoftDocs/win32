---
Description: 'Indicates that the output type has been set on the capture engine in response to IMFCaptureSink2::SetOutputType.'
ms.assetid: 'A48CBC82-87C2-4AED-B7E0-B7C60FCCE4CC'
title: 'MF\_CAPTURE\_ENGINE\_OUTPUT\_MEDIA\_TYPE\_SET attribute'
---

# MF\_CAPTURE\_ENGINE\_OUTPUT\_MEDIA\_TYPE\_SET attribute

Indicates that the output type has been set on the capture engine in response to [**IMFCaptureSink2::SetOutputType**](imftransform-setoutputtype.md).

## Data type

**GUID**

## Remarks

You can call [**IMFMediaEvent::GetStatus**](imfasyncresult-getstatus.md) to find out if the operation was successful or not.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Mfcaptureengine.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mfcaptureengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFCaptureSink2::SetOutputType**](imftransform-setoutputtype.md)
</dt> </dl>

 

 




