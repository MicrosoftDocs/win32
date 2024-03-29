---
description: Contains one MACROBLOCK_DATA structure for each macroblock in the input frame.
title: MFSampleExtension_FeatureMap attribute (Mfapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFSampleExtension\_FeatureMap attribute

Contains one MACROBLOCK_DATA structure for each macroblock in the input frame.

## Data type

**BLOB**

## Remarks

Applications can retrieve this value from an **IMFSample** by invoking the [IMFAttributes::GetBlob](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getblob) method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 24H2<br/>                          |
| Minimum supported server<br/> | None.                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |