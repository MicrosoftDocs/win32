---
title: OP_POLICY_ELEMENT
description: OP_POLICY_ELEMENT IDL Definition
ms.assetid: 69f6e0e7-3f47-4fee-8a4c-df94093dcffa
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_POLICY_ELEMENT structure

Defines a registry key and a value name, type, and value that should be configured under that key.

## Syntax

```C++
typedef struct _OP_POLICY_ELEMENT
{
    [string] wchar_t                *pKeyPath;
    [string] wchar_t                *pValueName;
    ULONG                           ulValueType;
    ULONG                           cbValueData;
    [size_is(cbValueData)]  PBYTE   pValueData;
} OP_POLICY_ELEMENT, *POP_POLICY_ELEMENT;
```

## Members

### pKeyPath

Contains the path of the registry key.

### pValueName

Contains the name of the registry value.

### ulValueType

Contains one of the values from [Registry Value Types](../sysinfo/registry-value-types.md).

### cbValueData

Contains the size of pValueData in bytes.

### ulValueType

Contains the value of the registry value.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)