---
description: Indicates the lengths of NALUs in the sample. This is a MF BLOB that is set on compressed input samples to the H.264 decoder.
ms.assetid: 09F54504-A6CF-4385-BDD7-8D23B1D0125C
title: MF_NALU_LENGTH_INFORMATION attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_NALU\_LENGTH\_INFORMATION attribute

Indicates the lengths of NALUs in the sample. This is a MF **BLOB** that is set on compressed input samples to the H.264 decoder.

## Data type

**BLOB**

## Remarks

In order for this attribute to be set, the media must be of type MEDIASUBTYPE\_H264 and the [MF\_NALU\_LENGTH\_SET](mf-nalu-length-set.md) attribute must be set on the input media type of MEDIASUBTYPE\_H264.

Set MF\_NALU\_LENGTH\_INFORMATION as a **BLOB** on the input sample, with one DWORD for each NALU in the sample. For example, if there are AUD (9 bytes), SPS (25 bytes), PPS (10 bytes), IDR slice1 (50 k), IDR slice 2 (60 k), then there should be 5 DWORDs with values 9, 25, 10, 50 k, 60 k in the **BLOB**.

Here some code that sets the **BLOB**, where **rgdwNALULengthInfo** is an array of type DWORD and **uiNaluLengthIdx** is the valid NALU lengths set to the **BLOB**.


```C++
m_spSample->SetBlob( MF_NALU_LENGTH_INFORMATION, 
                    (UINT8*) m_wpParent->m_pdwNALULengthInfo, 
                    sizeof(DWORD)*uiNaluLengthIdx ), 
                    done );
```



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

 

 




