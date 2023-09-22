---
title: IMsRdpClientNonScriptable8 CorrelationId property
description: Gets a GUID uniquely identifying the client's remote session.
ms.tgt_platform: multiple
keywords:
- CorrelationId property Remote Desktop Services
- CorrelationId property Remote Desktop Services , IMsRdpClientNonScriptable8 interface
- IMsRdpClientNonScriptable8 interface Remote Desktop Services , CorrelationId property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable8.CorrelationId
- IMsRdpClientNonScriptable8.get_CorrelationId
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/12/2023
---

# IMsRdpClientNonScriptable8::CorrelationId property

Gets a GUID uniquely identifying the client's remote session.

This property is read-only.

## Syntax

```C++
HRESULT get_CorrelationId( 
    [out, retval] GUID *correlationId
);
```

## Property value

A GUID uniquely identifying the client's remote session.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 11 Version 23H2      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClientNonScriptable8 is defined as B2B3FA47-3F11-4148-AD24-DFF8684A16D0           |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable8**](IMsRdpClientNonScriptable8.md)
</dt> </dl>