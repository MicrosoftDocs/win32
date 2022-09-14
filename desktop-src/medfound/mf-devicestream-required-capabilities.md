---
description: Specifies a list of unicode strings representing the device capabilities required by the sensor transform.
ms.assetid: 4A129FEB-E650-47C9-ABC0-9A512EE4121D
title: MF_DEVICESTREAM_REQUIRED_CAPABILITIES attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_DEVICESTREAM\_REQUIRED\_CAPABILITIES attribute

Specifies a list of unicode strings representing the device capabilities required by the sensor transform.

## Data type

**WCHAR\***

## Remarks

This attribute is optional and only required if the sensor transform accesses a protected resource. The value must be a semicolon delimited list of string tokens defined in [**DeviceCapability**](/uwp/schemas/appxpackage/appxmanifestschema/element-devicecapability).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 
