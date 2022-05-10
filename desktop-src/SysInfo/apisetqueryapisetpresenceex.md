---
description: This API is intended for internal use only. It should not be used in your code.
title: ApiSetQueryApiSetPresenceEx function
ms.topic: reference
ms.date: 12/03/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ApiSetQueryApiSetPresenceEx
api_type: 
- DllExport
api_location: 
- api-ms-win-core-apiquery-l1-1-0.dll
- ntdll.dll
---

# ApiSetQueryApiSetPresenceEx function

This API is intended for internal use only and should not be used in your code.

## Syntax

```C++
BOOL WINAPI ApiSetQueryApiSetPresenceEx(
  _In_ PCUNICODE_STRING Namespace,
  _Out_ PBOOLEAN IsInSchema,
  _Out_ PBOOLEAN Present
);
```

## Parameters

<dl> <dt>

*Namespace* \[in\]
</dt> <dd></dd> <dt>

*IsInSchema* \[out\]
</dt> <dd></dd> <dt>

*Present* \[out\]
</dt> <dd></dd> </dl>

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 10 \[desktop apps only\] |
| Minimum supported server | Windows Server 2016 \[desktop apps only\] |
| Header | N/A |
| Library | <dl> <dt>Api-ms-win-core-apiquery-l1.lib; </dt> <dt>Api-ms-win-core-apiquery-l1-1-0.lib</dt> </dl> |
| DLL | <dl> <dt>Api-ms-win-core-apiquery-l1-1-0.dll</dt> </dl> |
