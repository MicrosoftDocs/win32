---
title: IMsRdpClientNonScriptable6 SendLocation3D method
description: Sends a latitude, longitude and altitude value to the server so the client’s geographic location can be reflected in the remote session.
ms.tgt_platform: multiple
keywords:
- SendLocation3D method Remote Desktop Services
- SendLocation3D method Remote Desktop Services, IMsRdpClientNonScriptable6 interface
- IMsRdpClientNonScriptable6 interface Remote Desktop Services, SendLocation3D method
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable6.SendLocation3D
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable6::SendLocation3D method

Sends a latitude, longitude and altitude value to the server so the client’s geographic location can be reflected in the remote session.

## Syntax

```C++
HRESULT SendLocation3D(
  [in] DOUBLE latitude,
  [in] DOUBLE longitude,
  [in] INT32 altitude
);
```

## Parameters

*latitude* \[in\]

The latitude of a geographic location. The valid range of latitude values is from -90.0 to 90.0 degrees.

*longitude* \[in\]

The longitude of a geographic location. The valid range of latitude values is from -180.0 to 180.0 degrees.

*altitude* \[in\]

The altitude of a geographic location in meters.

## Return value

Return **S\_OK** if successful.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1709 (build 16299)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClientNonScriptable6 is defined as 05293249-B28B-4DB8-BE64-1B2F496B910E            |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable6**](imsrdpclientnonscriptable6.md)
</dt> </dl>
