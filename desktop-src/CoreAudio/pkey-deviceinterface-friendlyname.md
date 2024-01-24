---
description: The PKEY\_DeviceInterface\_FriendlyName property.
ms.assetid: beef2153-489f-4ff5-a161-b4e2cd4ac1fa
title: PKEY_DeviceInterface_FriendlyName (Functiondiscoverykeys\_devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_DeviceInterface\_FriendlyName

The **PKEY\_DeviceInterface\_FriendlyName** property contains the friendly name of the audio adapter to which the endpoint device is attached (for example, "XYZ Audio Adapter").

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains the friendly name.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                        |
| Header<br/>                   | <dl> <dt>Functiondiscoverykeys\_devpkey.h</dt> </dl> |



## See also

<dl> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> <dt>

[Device Properties](device-properties.md)
</dt> </dl>

 

 




