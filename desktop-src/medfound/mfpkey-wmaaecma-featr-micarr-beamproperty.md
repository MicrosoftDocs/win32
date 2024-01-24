---
description: Specifies which beam the Voice Capture DSP uses for microphone array processing.
ms.assetid: 9ed761da-3f1b-47e8-b71f-becc56fe8801
title: MFPKEY_WMAAECMA_FEATR_MICARR_BEAM Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_MICARR\_BEAM Property

Specifies which beam the Voice Capture DSP uses for microphone array processing.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Set this property if the value of the [MFPKEY\_WMAAECMA\_FEATR\_MICARR\_MODE](mfpkey-wmaaecma-featr-micarr-modeproperty.md) property is MICARRAY\_EXTERN\_BEAM.

If the value of [**MFPKEY\_WMAAECMA\_FEATR\_MICARR\_MODE**](mfpkey-wmaaecma-featr-micarr-modeproperty.md) is MICARRAY\_SINGLE\_BEAM, you can read this property to query which beam was selected by the DSP.

This property can have the following values. Values are in degrees horizontal.



| Value | Description              |
|-------|--------------------------|
| 0     | -50 degrees.             |
| 1     | -40 degrees.             |
| 2     | -30 degrees.             |
| 3     | -20 degrees.             |
| 4     | -10 degrees.             |
| 5     | 0 degrees (center beam). |
| 6     | 10 degrees.              |
| 7     | 20 degrees.              |
| 8     | 30 degrees.              |
| 9     | 40 degrees.              |
| 10    | 50 degrees.              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Voice Capture DSP](voicecapturedmo.md)
</dt> </dl>

 

 
