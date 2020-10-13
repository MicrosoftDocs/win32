---
title: OP_POLICY_ELEMENT_LIST
description: OP_POLICY_ELEMENT_LIST IDL Definition
ms.assetid: 1eebbdd2-655b-4bd3-938c-6bc687ffe7bb
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_POLICY_ELEMENT_LIST structure

Defines  a root registry key and an array of registry key elements to be configured under that key.

## Syntax

```C++
typedef struct _OP_POLICY_ELEMENT_LIST
{
    [string] wchar_t                            *pSource;
    ULONG                                       ulRootKeyId;
    ULONG                                       cElements;
    [size_is(cElements)]    POP_POLICY_ELEMENT  pElements;
} OP_POLICY_ELEMENT_LIST, *POP_POLICY_ELEMENT_LIST;
```

## Members

### pSource

Contains the path of the Group Policy file that the contained elements were sourced from.

### ulRootKeyId

Contains the identifier of the root registry key; currently must be set to HKEY_LOCAL_MACHINE.

### cElements

Contains the number of elements in pElements.

### pElements

Contains an array of OP_POLICY_ELEMENT elements.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**OP\_POLICY\_ELEMENT**](odj-op_policy_element.md)
