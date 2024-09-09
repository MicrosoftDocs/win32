---
description: Indicates the lengths of NALUs in the sample. This is a MF BLOB that is set on compressed H.264 or H.265 samples.
ms.assetid: 09F54504-A6CF-4385-BDD7-8D23B1D0125C
title: MF_NALU_LENGTH_INFORMATION attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_NALU\_LENGTH\_INFORMATION attribute

Indicates the lengths of NALUs in the sample. This is a MF **BLOB** that is set on compressed H.264 or H.265 samples.

## Data type

**BLOB**

## Remarks

In order for this attribute to be present on a compressed sample, [MF\_NALU\__LENGTH_\_SET](mf-nalu-length-set.md) must be set appropriately for the corresponding encoder or decoder MFT.

Set MF\_NALU\_LENGTH\_INFORMATION as a **BLOB** on the sample, with one DWORD for each NALU in the sample. For example, if there are AUD (9 bytes), SPS (25 bytes), PPS (10 bytes), IDR slice1 (50 k), IDR slice 2 (60 k), then there should be 5 DWORDs with values 9, 25, 10, 50 k, 60 k in the **BLOB**.

Here some code that sets the **BLOB**, where **rgdwNALULengthInfo** is an array of type DWORD and **uiNaluLengthIdx** is the valid NALU lengths set to the **BLOB**.


```C++
m_spSample->SetBlob( MF_NALU_LENGTH_INFORMATION, 
                    (UINT8*) m_wpParent->m_pdwNALULengthInfo, 
                    sizeof(DWORD)*uiNaluLengthIdx ), 
                    done );
```

When MF\_NALU\_LENGTH\_INFORMATION is provided as input to a decoder, the decoder will use the NALU lengths to improve performance and reduce decode latency.

When MF\_NALU\_LENGTH\_INFORMATION is emitted from an encoder, the NALU lengths can be used to improve the performance of a mux operation or subsequent decode.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




