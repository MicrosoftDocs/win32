---
Description: 'The KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST property is a filter property whose value is a list of audio effect types that are applied to a particular KS pin factory, for a particular audio signal processing path.'
ms.assetid: '53FDAFE2-8E5C-42C7-A8F3-13666BA90D98'
title: 'KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST'
---

# KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST

The **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST** property is a filter property whose value is a list of audio effect types that are applied to a particular KS pin factory, for a particular audio signal processing path.

### Usage Summary Table



| Get            | Set           | Target                                       | Property descriptor type | Property value type                 |
|----------------|---------------|----------------------------------------------|--------------------------|-------------------------------------|
| Yes<br/> | No<br/> | Pin factory (via Filter instance)<br/> | KSP\_PIN<br/>      | [**KSP\_PINMODE**](ksp-pinmode.md) |



 

The property value is an array of zero or more audio effect type GUIDs (for example, AUDIO\_EFFECT\_TYPE\_ACOUSTIC\_ECHO\_CANCELLATION) that are in the pin’s signal processing path identified by the **KSP\_PINMODE** structure.

> [!Note]  
> The KSPROPERTY\_TYPE\_TOPOLOGY flag bit must not be set for this property.

 

### Return Value

The **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST** property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, this property request returns an appropriate error status code.

## Remarks

If an audio driver uses Microsoft’s generic proxy APO to retrieve the audio effects that are included in the different signal processing paths for a KS pin, then it must support this property. The generic proxy APO is contained in the *msapofxproxy.dll* file. Audio drivers can use this generic proxy APO when all signal processing is done in the audio driver, or in the corresponding digital signal processor (DSP) hardware component, with no processing being done in an APO. In this case, the APO’s only function is to report the signal processing effects to the audio system.

The generic proxy APO receives **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST** from the audio driver and uses it to report the effects to the audio system. The generic proxy APO assumes that the list of effects does not change while the KS pin’s filter interface is enabled.

If the property descriptor specifies a KS pin that does not support **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST**, then the driver must return STATUS\_NOT\_SUPPORTED.

If the property descriptor specifies an *AudioProcessingMode* value that the driver does not support, then the driver must return STATUS\_INVALID\_PARAMETER. Note that an audio driver must support the [**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](audio.ksproperty_audiosignalprocessing_modes) property to be able to indicate its supported audio signal processing modes.

## Requirements



|                    |                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------|
| Version<br/> | Windows 8.1<br/>                                                                    |
| Header<br/>  | <dl> <dt>Msapofxproxy.h</dt> </dl> |



## See also

<dl> <dt>

[**KSP\_PINMODE**](ksp-pinmode.md)
</dt> <dt>

[**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](audio.ksproperty_audiosignalprocessing_modes)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20KSPROPERTY_AUDIOEFFECTSDISCOVERY_EFFECTSLIST%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





