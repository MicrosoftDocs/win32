---
title: IMsRdpClientNonScriptable6 SendLocation2D method
description: Sends a latitude and longitude value to the server so the client's geographic location can be reflected in the remote session.
ms.tgt_platform: multiple
keywords:
- SendLocation2D method Remote Desktop Services
- SendLocation2D method Remote Desktop Services, IMsRdpClientNonScriptable6 interface
- IMsRdpClientNonScriptable6 interface Remote Desktop Services, SendLocation2D method
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable6.SendLocation2D
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable6::SendLocation2D method

Sends a latitude and longitude value to the server so the client's geographic location can be reflected in the remote session.

## Syntax

```C++
HRESULT SendLocation2D(
  [in] DOUBLE latitude,
  [in] DOUBLE longitude
);
```

## Parameters

*latitude* \[in\]

The latitude of a geographic location. The valid range of latitude values is from -90.0 to 90.0 degrees.

*longitude* \[in\]

The longitude of a geographic location. The valid range of latitude values is from -180.0 to 180.0 degrees.

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
