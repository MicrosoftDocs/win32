---
Description: Contains the class identifier (CLSID) of a Media Foundation transform (MFT).
ms.assetid: 99ee6f50-1de7-41ea-be5b-135730138d5d
title: MFT\_TRANSFORM\_CLSID\_Attribute attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_TRANSFORM\_CLSID\_Attribute attribute

Contains the class identifier (CLSID) of a Media Foundation transform (MFT).

## Data type

**GUID**

## Get/set

To get this attribute, call [**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master).

To set this attribute, call [**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master).

## Remarks

This attribute is set on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers returned by the [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master) function.

This attribute is used internally by the activation object when it creates the MFT. Applications should not use this CLSID directly to create the MFT, because the activation object might need to initialize the MFT. Therefore, to create an instance of the MFT, call [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master) on the activation object.

Note that the [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master) function behaves differently than the [**MFTEnum**](/windows/win32/mfapi/nf-mfapi-mftenum?branch=master) function in this respect. The **MFTEnum** function returns CLSIDs, which the application passes to the **CoCreateInstance** function. The **MFTEnumEx** function returns activation objects rather than CLSIDs.

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

 

 




