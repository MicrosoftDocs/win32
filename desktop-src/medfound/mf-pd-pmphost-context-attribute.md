---
Description: Contains a pointer to the proxy object for the applications presentation descriptor.
ms.assetid: 0cd83204-0d32-417c-8911-1d3358eb0802
title: MF\_PD\_PMPHOST\_CONTEXT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_PMPHOST\_CONTEXT attribute

Contains a pointer to the proxy object for the application's presentation descriptor.

## Data type

**IUnknown\***

## Remarks

The Protected Media Path (PMP) host uses this attribute to store the application's presentation descriptor on the remote presentation descriptor. The attribute value is a pointer to the [**IMFRemoteProxy**](/windows/win32/mfidl/nn-mfidl-imfremoteproxy?branch=master) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




