---
Description: Contains the registered output types for a Media Foundation transform (MFT).
ms.assetid: 925267a2-4421-4874-a8a2-437876c729f1
title: MFT\_OUTPUT\_TYPES\_Attributes attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFT\_OUTPUT\_TYPES\_Attributes attribute

Contains the registered output types for a Media Foundation transform (MFT).

## Data type

**MFT\_REGISTER\_TYPE\_INFO\[\]** stored as **BYTE\[\]**

## Remarks

This attribute is set on the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointers returned by the [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function.

This attribute contains an array of [**MFT\_REGISTER\_TYPE\_INFO**](/windows/desktop/api/mfobjects/ns-mfobjects-__midl___midl_itf_mfobjects_0000_0008_0003) structures that describe one or more output formats supported by the MFT. These values are taken from the registry and are intended as a hint to the application. The MFT might support additional formats. To set the actual output format, you must create the MFT and call [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




