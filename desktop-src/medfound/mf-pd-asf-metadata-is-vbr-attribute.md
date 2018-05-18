---
Description: 'Specifies whether an Advanced Systems Format (ASF) file uses variable bit rate (VBR) encoding.'
ms.assetid: '69888d66-8e96-4a20-b8c5-a01267ff3c05'
title: 'MF\_PD\_ASF\_METADATA\_IS\_VBR attribute'
---

# MF\_PD\_ASF\_METADATA\_IS\_VBR attribute

Specifies whether an Advanced Systems Format (ASF) file uses variable bit rate (VBR) encoding.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to presentation descriptors for ASF content. If the value is **TRUE**, the file was encoded using VBR. If the value is **FALSE** or the attribute is not present, the file does not use VBR encoding.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](imfasfcontentinfo-generatepresentationdescriptor.md) method generates this attribute and sets it on the presentation descriptor.

> [!Note]  
> This attribute corresponds to the **IsVBR** attribute in the Windows Media Format SDK.

 

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




