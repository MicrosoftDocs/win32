---
description: Releases a previously allocated DlpSerializedBuffer.
title: DlpReleaseBuffer function (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpReleaseBuffer
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpReleaseBuffer function

Releases a previously allocated [DlpSerializedBuffer](endpointdlp-dlpserializedbuffer.md).

## Syntax

```cpp
HRESULT WINAPI DlpReleaseBuffer(_In_ const DlpSerializedBuffer* buffer);
```

## Parameters

`buffer` [in]: A pointer to the [DlpSerializedBuffer](endpointdlp-dlpserializedbuffer.md) to be released. This parameter must not be `NULL`.

## Return value

Returns an `HRESULT` including, but not limited to, the following values:

| `HRESULT` | Description |
|---------|-------------|
| `S_OK` | The function completed successfully. |
| `FAILED` | An unexpected error prevented the function from completing. |

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |

## Related content

- [DlpSerializedBuffer](endpointdlp-dlpserializedbuffer.md)
