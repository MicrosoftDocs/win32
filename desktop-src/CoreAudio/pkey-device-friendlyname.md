---
description: The PKEY\_Device\_FriendlyName property contains the friendly name of the endpoint device (for example, &\#0034;Speakers (XYZ Audio Adapter)&\#0034;).
ms.assetid: 3ccd6a78-8bc3-4a46-8f11-7c2ae8a23c63
title: PKEY_Device_FriendlyName (Functiondiscoverykeys\_devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_Device\_FriendlyName

The **PKEY\_Device\_FriendlyName** property contains the friendly name of the endpoint device (for example, "Speakers (XYZ Audio Adapter)").

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains the friendly name of the endpoint device.

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

 

 




