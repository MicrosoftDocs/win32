---
description: The AudioSettingsProperty enum is used by the ITAudioSettings::GetRange, ITAudioSettings::Get, and ITAudioSettings::Set methods to indicate the audio setting property being addressed.
ms.assetid: b91c8213-f102-4ebb-ad8a-e43709b3daad
title: AudioSettingsProperty enumeration (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AudioSettingsProperty enumeration

\[ This enumeration is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **AudioSettingsProperty** enum is used by the [**ITAudioSettings::GetRange**](itaudiosettings-getrange.md), [**ITAudioSettings::Get**](itaudiosettings-get.md), and [**ITAudioSettings::Set**](itaudiosettings-set.md) methods to indicate the audio setting property being addressed.

## Syntax


```C++
} AudioSettingsProperty;
```



## Constants

<dl> <dt>

<span id="AudioSettings_SignalLevel"></span><span id="audiosettings_signallevel"></span><span id="AUDIOSETTINGS_SIGNALLEVEL"></span>**AudioSettings\_SignalLevel**
</dt> <dd>

Signal settings property.

</dd> <dt>

<span id="AudioSettings_SilenceThreshold"></span><span id="audiosettings_silencethreshold"></span><span id="AUDIOSETTINGS_SILENCETHRESHOLD"></span>**AudioSettings\_SilenceThreshold**
</dt> <dd>

Silence threshold property.

</dd> <dt>

<span id="AudioSettings_Volume"></span><span id="audiosettings_volume"></span><span id="AUDIOSETTINGS_VOLUME"></span>**AudioSettings\_Volume**
</dt> <dd>

Volume property.

</dd> <dt>

<span id="AudioSettings_Balance"></span><span id="audiosettings_balance"></span><span id="AUDIOSETTINGS_BALANCE"></span>**AudioSettings\_Balance**
</dt> <dd>

Balance property.

</dd> <dt>

<span id="AudioSettings_Loudness"></span><span id="audiosettings_loudness"></span><span id="AUDIOSETTINGS_LOUDNESS"></span>**AudioSettings\_Loudness**
</dt> <dd>

Loudness property.

</dd> <dt>

<span id="AudioSettings_Treble"></span><span id="audiosettings_treble"></span><span id="AUDIOSETTINGS_TREBLE"></span>**AudioSettings\_Treble**
</dt> <dd>

Treble property.

</dd> <dt>

<span id="AudioSettings_Bass"></span><span id="audiosettings_bass"></span><span id="AUDIOSETTINGS_BASS"></span>**AudioSettings\_Bass**
</dt> <dd>

Bass property.

</dd> <dt>

<span id="AudioSettings_Mono"></span><span id="audiosettings_mono"></span><span id="AUDIOSETTINGS_MONO"></span>**AudioSettings\_Mono**
</dt> <dd>

Monaural property.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                       |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl> |



## See also

<dl> <dt>

[**ITAudioSettings::GetRange**](itaudiosettings-getrange.md)
</dt> <dt>

[**ITAudioSettings::Get**](itaudiosettings-get.md)
</dt> <dt>

[**ITAudioSettings::Set**](itaudiosettings-set.md)
</dt> </dl>

 

 




