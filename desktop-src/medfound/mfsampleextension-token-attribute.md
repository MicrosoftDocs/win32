---
Description: Contains a pointer to the token that was provided to the IMFMediaStreamRequestSample method.
ms.assetid: 9403bb15-e912-4aa3-9af1-fef4a4f9b242
title: MFSampleExtension\_Token attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_Token attribute

Contains a pointer to the token that was provided to the [**IMFMediaStream::RequestSample**](/windows/win32/mfidl/nf-mfidl-imfmediastream-requestsample?branch=master) method.

## Data type

**IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Applies to

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)

## Remarks

This attribute applies to media samples. The value of the attribute is the **IUnknown** pointer that is passed to the *pToken* parameter of the [**RequestSample**](/windows/win32/mfidl/nf-mfidl-imfmediastream-requestsample?branch=master) method. The caller uses this attribute to track the status of the request.

If you are writing a custom media source, set this attribute on the sample when the media stream delivers a sample in response to the [**RequestSample**](/windows/win32/mfidl/nf-mfidl-imfmediastream-requestsample?branch=master) method, unless the value of *pToken* is **NULL**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 




