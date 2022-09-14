---
title: UUID
description: Provides a unique designation of an object such as an interface, a manager entry-point vector, or a client object.
ms.topic: reference
ms.date: 09/09/2019
---

# UUID structure

The **UUID** structure defines a Universally Unique Identifier (UUID). A **UUID** provides a unique designation of an object such as an interface, a manager entry-point vector, or a client object.

The **UUID** structure is a `typedef`'d synonym for the [GUID](/windows/win32/api/guiddef/ns-guiddef-guid) structure.

## Syntax

```cpp
typedef GUID UUID;
```

## Remarks

The RPC run-time libraries use **UUID**s to check for compatibility between clients and servers, and to select among multiple implementations of an interface.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | Defined in rpcdce.h; include rpc.h |

## See also

[GUID](/windows/win32/api/guiddef/ns-guiddef-guid)
[UUID\_VECTOR](/windows/win32/api/rpcdce/ns-rpcdce-uuid_vector)
