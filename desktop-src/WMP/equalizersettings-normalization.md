---
title: EQUALIZERSETTINGS.normalization
description: The normalization attribute specifies or retrieves a value indicating whether normalization is enabled.
ms.assetid: d0819624-7bc5-447a-b890-c8af94faa7b0
keywords:
- EQUALIZERSETTINGS.normalization Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.normalization
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.normalization

The **normalization** attribute specifies or retrieves a value indicating whether normalization is enabled.

``` syntax
        elementID.normalization
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                         |
|-------|-------------------------------------|
| true  | Normalization is enabled.           |
| false | Default. Normalization is disabled. |



 

## Remarks

When normalization is enabled, the audio signal for an entire digital media file is scaled up to the maximum value. This allows multiple files to be played at approximately the same volume without requiring volume adjustments.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.normalizationAverage**](equalizersettings-normalizationaverage.md)
</dt> <dt>

[**EQUALIZERSETTINGS.normalizationPeak**](equalizersettings-normalizationpeak.md)
</dt> </dl>

 

 





