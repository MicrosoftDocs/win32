---
description: Specifies the duration of echo that the acoustic echo cancellation (AEC) algorithm can handle, in milliseconds.
ms.assetid: d451b90f-7ef7-4f66-be83-aca93e3ad894
title: MFPKEY_WMAAECMA_FEATR_ECHO_LENGTH Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_ECHO\_LENGTH Property

Specifies the duration of echo that the acoustic echo cancellation (AEC) algorithm can handle, in milliseconds.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4

## Default Value

256

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

The AEC algorithm uses an adaptive filter whose length is determined by the duration of the echo. It is recommended that applications use one of the following values:

-   128
-   256
-   512
-   1024

The default value is 256 milliseconds, which is sufficient for most office and home environments. Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

The DSP uses this property only when AEC processing is enabled.

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

 

 
