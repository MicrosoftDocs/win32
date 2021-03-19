---
title: '_WAVEFORMATEX structure'
description: The \_WAVEFORMATEX structure defines the format of waveform-audio data.
ms.assetid: 2128f07a-4858-49b7-b031-16d4a84c9d32
keywords:
- _WAVEFORMATEX structure windows Media Device Manager
topic_type:
- apiref
api_name:
- _WAVEFORMATEX
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# \_WAVEFORMATEX structure

The **\_WAVEFORMATEX** structure defines the format of waveform-audio data.

## Syntax


```C++
typedef struct _tWAVEFORMATEX {
  WORD  wFormatTag;
  WORD  nChannels;
  DWORD nSamplesPerSec;
  DWORD nAvgBytesPerSec;
  WORD  nBlockAlign;
  WORD  wBitsPerSample;
  WORD  cbSize;
} _WAVEFORMATEX;
```



## Members

<dl> <dt>

**wFormatTag**
</dt> <dd>

Must be set to a format or formats supported by the device. Note that previous versions of the Windows Media Device Manager recommended using WMDM\_WAVE\_FORMAT\_ALL to indicate support for all formats. However, this is no longer recommended, as different media players will interpret this in different ways, and few devices can truly play any file format. It is now recommended that you use the WMDM\_ENUM\_PROP\_VALID\_VALUES\_ANY value of the [**WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM**](wmdm-enum-prop-valid-values-form.md) enumeration, or better yet specify a range of formats with the [**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md) structure.

</dd> <dt>

**nChannels**
</dt> <dd>

Number of channels in the waveform-audio data. Monaural data uses one channel, and stereo data uses two channels.

</dd> <dt>

**nSamplesPerSec**
</dt> <dd>

Sample rate, in samples per second (Hertz), at which each channel must be played or recorded. Common values for **nSamplesPerSec** are 8.0 kilohertz (kHz), 11.025 kHz, 22.05 kHz, and 44.1 kHz.

</dd> <dt>

**nAvgBytesPerSec**
</dt> <dd>

Required average data-transfer rate for the format tag, in bytes per second. Playback and recording software can estimate buffer sizes by using the **nAvgBytesPerSec** member.

</dd> <dt>

**nBlockAlign**
</dt> <dd>

Block alignment, in bytes. The block alignment is the minimum atomic unit of data for the **wFormatTag** format type. Playback and recording software must process a multiple of **nBlockAlign** bytes of data at a time. Data written and read from a device must always start at the beginning of a block. For example, it is not possible to correctly start playing PCM data in the middle of a sample (that is, on a boundary that is not block aligned).

</dd> <dt>

**wBitsPerSample**
</dt> <dd>

Bits per sample for the **wFormatTag** format type.

</dd> <dt>

**cbSize**
</dt> <dd>

This member is ignored.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMDSPDevice::GetFormatSupport**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspdevice-getformatsupport)
</dt> <dt>

[**IMDSPStorage::CreateStorage**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorage-createstorage)
</dt> <dt>

[**IMDSPStorage::GetAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorage-getattributes)
</dt> <dt>

[**IWMDMDevice::GetFormatSupport**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-getformatsupport)
</dt> <dt>

[**IWMDMOperation::GetObjectAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-getobjectattributes)
</dt> <dt>

[**IWMDMOperation::SetObjectAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-setobjectattributes)
</dt> <dt>

[**IWMDMStorage::GetAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-getattributes)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





