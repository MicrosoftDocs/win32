---
description: Indicates whether a stream contains protected content.
ms.assetid: 1c1a201c-4b55-4b86-a08f-d06c1a7db29d
title: MF_SD_PROTECTED attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SD\_PROTECTED attribute

Indicates whether a stream contains protected content.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to stream descriptors. If the value of the attribute is **TRUE**, the stream contains protected content. If the value is **FALSE**, or the attribute is not set, the stream contains clear content.

Instead of checking each stream for this attribute, you can pass a presentation descriptor to the [**MFRequireProtectedEnvironment**](/windows/desktop/api/mfidl/nf-mfidl-mfrequireprotectedenvironment) function. This function tests whether the presentation descriptor contains any protected streams.

A media source should set this attribute on the stream descriptor if the content requires the protected media path (PMP).

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples


```
// This function returns TRUE if the stream contains protected 
// content. You can also call the MFRequireProtectedEnvironment 
// function to test whether a presentation contains any streams
// with protected content.

BOOL StreamHasProtectedContent(IMFStreamDescriptor *pSD)
{
    return MFGetAttributeUINT32(pSD, MF_SD_PROTECTED, FALSE);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> </dl>

 

 




