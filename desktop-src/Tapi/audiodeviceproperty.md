---
description: The AudioDeviceProperty enum is used by the ITAudioDeviceControl::GetRange, ITAudioDeviceControl::Get, and ITAudioDeviceControl::Set methods to indicate the property being addressed.
ms.assetid: 0ed9b75e-3c79-4e41-9883-63b85ebfae06
title: AudioDeviceProperty enumeration (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AudioDeviceProperty enumeration

\[ This enumeration is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **AudioDeviceProperty** enum is used by the [**ITAudioDeviceControl::GetRange**](itaudiodevicecontrol-getrange.md), [**ITAudioDeviceControl::Get**](itaudiodevicecontrol-get.md), and [**ITAudioDeviceControl::Set**](itaudiodevicecontrol-set.md) methods to indicate the property being addressed.

## Syntax


```C++
} AudioDeviceProperty;
```



## Constants

<dl> <dt>

<span id="AudioDevice_DuplexMode"></span><span id="audiodevice_duplexmode"></span><span id="AUDIODEVICE_DUPLEXMODE"></span>**AudioDevice\_DuplexMode**
</dt> <dd>

Indicates that the duplex mode of the device is being set or retrieved.

</dd> <dt>

<span id="AudioDevice_AutomaticGainControl"></span><span id="audiodevice_automaticgaincontrol"></span><span id="AUDIODEVICE_AUTOMATICGAINCONTROL"></span>**AudioDevice\_AutomaticGainControl**
</dt> <dd>

Indicates that the automatic gain control of the device is being set or retrieved.

</dd> <dt>

<span id="AudioDevice_AcousticEchoCancellation"></span><span id="audiodevice_acousticechocancellation"></span><span id="AUDIODEVICE_ACOUSTICECHOCANCELLATION"></span>**AudioDevice\_AcousticEchoCancellation**
</dt> <dd>

Indicates that the acoustic echo cancellation properties of the device are being set or retrieved.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                       |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl> |



## See also

<dl> <dt>

[**ITAudioDeviceControl::GetRange**](itaudiodevicecontrol-getrange.md)
</dt> <dt>

[**ITAudioDeviceControl::Get**](itaudiodevicecontrol-get.md)
</dt> <dt>

[**ITAudioDeviceControl::Set**](itaudiodevicecontrol-set.md)
</dt> </dl>

 

 




