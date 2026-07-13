---
description: The temporal layer ID of the data contained in an IMFSample.
title: MFSampleExtension_TemporalLayerId attribute (Mfapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFSampleExtension\_TemporalLayerId attribute

The spatial layer ID of the data contained in an [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample).

## Data type

**UINT32**

## Remarks

A decoder MFT that supports temporal scalability can set this attribute on the **IMFSample** that contains the decoded bitstream data. This allows an application to discard **IMFSample** objects containing unwanted temporal layers without having to use [MFT_DECODER_OPERATING_POINT](mft-decoder-operating-point.md) to reconfigure the MFT. This is particularly useful when the highest layer that the application wants changes dynamically. Applications can retrieve this value from an **IMFSample** by invoking the [IMFAttributes::GetUINT32](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getuint32) method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 24H2<br/>                          |
| Minimum supported server<br/> | None.                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |