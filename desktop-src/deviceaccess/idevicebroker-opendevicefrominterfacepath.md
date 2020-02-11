---
title: IDeviceBroker OpenDeviceFromInterfacePath method
description: Attempts to open a device interface instance on behalf of a client. IID 8604b268-34A6-4b1A-A59F-CDBD8379FD98.
ms.assetid: 5ADDB994-3AAB-49B2-8B83-F71883AFD854
keywords:
- OpenDeviceFromInterfacePath method Device Access Broker API
- OpenDeviceFromInterfacePath method Device Access Broker API , IDeviceBroker interface
- IDeviceBroker interface Device Access Broker API , OpenDeviceFromInterfacePath method
topic_type:
- apiref
api_name:
- IDeviceBroker.OpenDeviceFromInterfacePath
api_type:
- COM
ms.topic: article
ms.date: 02/11/2020
api_location: 
ROBOTS: INDEX,FOLLOW
---

# IDeviceBroker::OpenDeviceFromInterfacePath method

> [!Important]  
> These interfaces are not supported and should not be used. Use the APIs in the [Device Access API C++ Programming Reference](device-access-api-c---programming-reference.md) instead.

Attempts to open a device interface instance on behalf of a client. IID = 8604b268-34A6-4b1A-A59F-CDBD8379FD98.

## Syntax

```C++
HRESULT OpenDeviceFromInterfacePath(
  [in]  PCWSTR pszDeviceInterfacePath,
  [in]  DWORD  desiredAccess,
  [in]  DWORD  shareMode,
  [in]  DWORD  flagsAndAttributes,
  [out] Handle *phDevice
);
```

## Parameters

<dl> <dt>

*pszDeviceInterfacePath* \[in\]
</dt> <dd>

Device interface instance to open.

</dd> <dt>

*desiredAccess* \[in\]
</dt> <dd>

Desired access to be passed to open.

</dd> <dt>

*shareMode* \[in\]
</dt> <dd>

Share mode to be passed to open.

</dd> <dt>

*flagsAndAttributes* \[in\]
</dt> <dd>

Flags and attributes to be passed to open.

</dd> <dt>

*\*phDevice* \[out\]
</dt> <dd>

Resulting handle if open was successful.

</dd> </dl>

## Return value

If this function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.
