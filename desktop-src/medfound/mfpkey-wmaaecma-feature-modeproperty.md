---
description: Enables the application to override the default settings on various properties of the Voice Capture DSP.
ms.assetid: 1c11e817-36bd-4a5d-9c2b-6a91e86f623f
title: MFPKEY_WMAAECMA_FEATURE_MODE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATURE\_MODE Property

Enables the application to override the default settings on various properties of the Voice Capture DSP.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_FALSE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

If this property is VARIANT\_TRUE, the application can set the following properties on the DSP:

-   [MFPKEY\_WMAAECMA\_FEATR\_AES](mfpkey-wmaaecma-featr-aesproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_AGC](mfpkey-wmaaecma-featr-agcproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_CENTER\_CLIP](mfpkey-wmaaecma-featr-center-clipproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_ECHO\_LENGTH](mfpkey-wmaaecma-featr-echo-lengthproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_FRAME\_SIZE](mfpkey-wmaaecma-featr-frame-sizeproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_MICARR\_MODE](mfpkey-wmaaecma-featr-micarr-modeproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_MICARR\_PREPROC](mfpkey-wmaaecma-featr-micarr-preprocproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_NOISE\_FILL](mfpkey-wmaaecma-featr-noise-fillproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_NS](mfpkey-wmaaecma-featr-nsproperty.md)
-   [MFPKEY\_WMAAECMA\_FEATR\_VAD](mfpkey-wmaaecma-featr-vadproperty.md)

If this property is VARIANT\_FALSE, the DSP ignores these properties and uses its default settings. The default value of this property is VARIANT\_FALSE.

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

 

 
