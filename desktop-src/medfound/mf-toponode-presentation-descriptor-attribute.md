---
description: Contains a pointer to the presentation descriptor for the media source.
ms.assetid: 4f2c1ad8-fda9-482f-b82a-9838d15d2785
title: MF_TOPONODE_PRESENTATION_DESCRIPTOR attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_PRESENTATION\_DESCRIPTOR attribute

Contains a pointer to the presentation descriptor for the media source.

## Data type

**IUnknown\***

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**).

The value of the attribute is a pointer to the presentation descriptor's [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) interface. This attribute is required.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




