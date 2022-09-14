---
description: Specifies a list of bit rates and corresponding buffer windows for a variable bit rate (VBR) Advanced Systems Format (ASF) file.
ms.assetid: e45d055f-d404-47e9-b3c8-ac743b290138
title: MF_PD_ASF_METADATA_LEAKY_BUCKET_PAIRS attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_METADATA\_LEAKY\_BUCKET\_PAIRS attribute

Specifies a list of bit rates and corresponding buffer windows for a variable bit rate (VBR) Advanced Systems Format (ASF) file.

## Data type

Byte array

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method generates this attribute that applies to the presentation descriptor for ASF content.

The value of the attribute has the following format:

``` syntax
struct {
    WORD wReserved;
    WM_LEAKY_BUCKET_PAIR bucket[2];
};
```

The **WM\_LEAKY\_BUCKET\_PAIR** structure is defined as follows:

``` syntax
typedef struct _WMLeakyBucketPair {
  DWORD  dwBitrate;
  DWORD  msBufferWindow;
} WM_LEAKY_BUCKET_PAIR;
```

For each bit rate, the **msBufferWindow** member indicates how much content is buffered before playback begins, in milliseconds. The size of the buffer in bytes equals **msBufferWinow** x **dwBitrate** / 8000.

> [!Note]  
> This attribute corresponds to the **ASFLeakyBucketPairs** attribute in the Windows Media Format SDK.

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




