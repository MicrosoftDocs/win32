---
description: The GetRange method retrieves the range of valid values for a given audio settings property.
ms.assetid: 09ee0c59-6ae6-47eb-a8cf-6b24e759d7fb
title: ITAudioSettings::GetRange method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITAudioSettings::GetRange method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetRange** method retrieves the range of valid values for a given [**audio settings property**](audiosettingsproperty.md).

## Syntax


```C++
HRESULT get_Terminal(
  [out] ITTerminal **ppTerminal
);
```



## Parameters

<dl> <dt>

*Property* \[in\]
</dt> <dd>

Member of the [**AudioSettingsProperty**](audiosettingsproperty.md) enum.

</dd> <dt>

*plMin* \[out\]
</dt> <dd>

Minimum valid value for the input property.

</dd> <dt>

*plMax* \[out\]
</dt> <dd>

Maximum valid value for the input property.

</dd> <dt>

*plSteppingDelta* \[out\]
</dt> <dd>

Increment by which the property value can be increased or decreased.

</dd> <dt>

*plDefault* \[out\]
</dt> <dd>

Default value for the *Property* parameter.

</dd> <dt>

*plFlags* \[out\]
</dt> <dd>

Value of the [**TAPIControlFlags**](tapicontrolflags.md) enum indicating how the *Property* value is controlled.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITAudioSettings**](itaudiosettings.md)
</dt> <dt>

[**TAPIControlFlags**](tapicontrolflags.md)
</dt> <dt>

[**AudioSettingsProperty**](audiosettingsproperty.md)
</dt> </dl>

 

 




