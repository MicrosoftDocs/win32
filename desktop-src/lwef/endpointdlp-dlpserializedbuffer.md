---
description: Specifies a dynamically allocated string from an EndpointDlp API.
title: DlpSerializedBuffer structure (endpointdlp.h)
ms.topic: reference
ms.date: 09/05/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpSerializedBuffer
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DlpSerializedBuffer structure

Structure used to pass out a dynamically allocated string from an EndpointDlp API.

## Syntax

```cpp
    struct DlpSerializedBuffer
    {
        uint32_t bufferSize;
        _Field_z_ const WCHAR* buffer;
    };
```

## Members

*bufferSize* `[out]`

The size of the string in buffer (excluding the null terminator).

*buffer* `[out]`

A `NULL` terminated string.

## Remarks

Must be released using [DlpReleaseBuffer](endpointdlp-dlpreleasebuffer.md).

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows 11, version 24H2 (Build 26100) |
| DLL                      | EndpointDlp.dll |
