---
description: Specifies whether the Voice Capture DSP stores time stamp statistics in the registry.
ms.assetid: c44462be-ccdf-4a49-bb77-6e816def4849
title: MFPKEY_WMAAECMA_RETRIEVE_TS_STATS Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_RETRIEVE\_TS\_STATS Property

Specifies whether the Voice Capture DSP stores time stamp statistics in the registry.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_FALSE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Acoustic echo cancellation (AEC) algorithms depend on accurate time stamps on the audio streams. In reality, time stamps are often imperfect, and different audio devices can exhibit different rates of variance and drift. When AEC is enabled, the DSP collects statistics about the time stamps and uses this information to compensate for inaccuracies.

If the value of this property is VARIANT\_TRUE, the DSP saves the statistics that it collects in the registry. The next time the DSP performs AEC using the same pair of audio devices, it reads the statistical information from the registry, which enables the DSP to perform more efficiently.

If you set the value of this property to VARIANT\_TRUE and you are using the DSP in filter mode, you should also set the [MFPKEY\_WMAAECMA\_DEVICEPAIR\_GUID](mfpkey-wmaaecma-devicepair-guidproperty.md) property. In source mode, this is not required.

The default value of this property is VARIANT\_FALSE. The DSP uses this property only when AEC processing is enabled.

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

 

 
