---
description: The PKEY\_Device\_DeviceDesc property contains the device description of the endpoint device (for example, &\#0034;Speakers&\#0034;).
ms.assetid: 23715497-a74d-4dab-aade-c7779fe80aa6
title: PKEY_Device_DeviceDesc (Functiondiscoverykeys\_devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_Device\_DeviceDesc

The **PKEY\_Device\_DeviceDesc** property contains the device description of the endpoint device (for example, "Speakers").

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains the device description.

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

 

 




