---
Description: Contains the registered output types for a Media Foundation transform (MFT).
ms.assetid: 925267a2-4421-4874-a8a2-437876c729f1
title: MFT\_OUTPUT\_TYPES\_Attributes attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_OUTPUT\_TYPES\_Attributes attribute

Contains the registered output types for a Media Foundation transform (MFT).

## Data type

**MFT\_REGISTER\_TYPE\_INFO\[\]** stored as **BYTE\[\]**

## Remarks

This attribute is set on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers returned by the [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master) function.

This attribute contains an array of [**MFT\_REGISTER\_TYPE\_INFO**](/windows/win32/mfobjects/ns-mfobjects-__midl___midl_itf_mfobjects_0000_0008_0003?branch=master) structures that describe one or more output formats supported by the MFT. These values are taken from the registry and are intended as a hint to the application. The MFT might support additional formats. To set the actual output format, you must create the MFT and call [**IMFTransform::SetOutputType**](/windows/win32/mftransform/nf-mftransform-imftransform-setoutputtype?branch=master).

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

 

 




