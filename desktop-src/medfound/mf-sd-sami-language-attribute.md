---
description: Contains the Synchronized Accessible Media Interchange (SAMI) language name that is defined for the stream.
ms.assetid: 3151c369-9d2b-4f03-9a4a-9b9267314dc1
title: MF_SD_SAMI_LANGUAGE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SD\_SAMI\_LANGUAGE attribute

Contains the Synchronized Accessible Media Interchange (SAMI) language name that is defined for the stream.

This attribute is present in the stream descriptors returned from the SAMI media source.

## Data type

Wide-character string

## Remarks

The SAMI language name is specified in the SAMI file.

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

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> <dt>

[**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> <dt>

[**IMFSAMIStyle**](/windows/desktop/api/mfidl/nn-mfidl-imfsamistyle)
</dt> </dl>

 

 




