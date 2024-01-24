---
title: OP_POLICY_PART
description: OP_POLICY_PART IDL Definition
ms.assetid: 3988b298-b21d-4476-bfa5-ac606bcbd6c8
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_POLICY_PART structure

Contains an array of OP_POLICY_ELEMENT_LIST structures.

## Syntax

```C++
typedef struct _OP_POLICY_PART
{
    ULONG                                       cElementLists;
    [size_is(cElementLists)]
                        POP_POLICY_ELEMENT_LIST pElementLists;
    OP_BLOB                                     Extension;
} OP_POLICY_PART, *POP_POLICY_PART;
```

## Members

### cElementLists

Contains the number of elements in pElementLists.

### pElementLists

Contains an array of OP_POLICY_ELEMENT_LIST structures.

### Extension

Reserved for future use and must contain all zeros.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**OP\_POLICY\_ELEMENT\_LIST**](odj-op_policy_element_list.md)
