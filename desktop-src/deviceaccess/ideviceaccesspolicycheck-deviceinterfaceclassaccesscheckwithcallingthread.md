---
title: IDeviceAccessPolicyCheck DeviceInterfaceClassAccessCheckWithCallingThread method
description: This API will determine if the token for the current context has access to the device interface class specified. IID 7D276FF2-CE90-4275-A2A8-9A48B10D3E0B.
ms.assetid: D7BFE1F3-4876-4BAB-A32D-46DB533140BB
keywords:
- DeviceInterfaceClassAccessCheckWithCallingThread method Device Access Broker API
- DeviceInterfaceClassAccessCheckWithCallingThread method Device Access Broker API , IDeviceAccessPolicyCheck interface
- IDeviceAccessPolicyCheck interface Device Access Broker API , DeviceInterfaceClassAccessCheckWithCallingThread method
topic_type:
- apiref
api_name:
- IDeviceAccessPolicyCheck.DeviceInterfaceClassAccessCheckWithCallingThread
api_type:
- COM
ms.topic: article
ms.date: 02/11/2020
api_location: 
ROBOTS: INDEX,FOLLOW
---

# IDeviceAccessPolicyCheck::DeviceInterfaceClassAccessCheckWithCallingThread method

> [!Important]  
> These interfaces are not supported and should not be used. Use the APIs in the [Device Access API C++ Programming Reference](device-access-api-c---programming-reference.md) instead.

This API will determine if the token for the current context has access to the device interface class specified. IID = 7D276FF2-CE90-4275-A2A8-9A48B10D3E0B.

## Syntax

```C++
HRESULT DeviceInterfaceClassAccessCheckWithCallingThread(
  [in] PCWSTR pszDeviceInterfaceClassGuid,
  [in] DWORD  dwClientThreadId
);
```

## Parameters

<dl> <dt>

*pszDeviceInterfaceClassGuid* \[in\]
</dt> <dd>

Device interface class GUID for which access should be checked.

</dd> <dt>

*dwClientThreadId* \[in\]
</dt> <dd>

Client thread ID where any associated UI should be shown if necessary.

</dd> </dl>

## Return value

If this function succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.
