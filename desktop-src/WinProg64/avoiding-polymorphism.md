---
title: Avoiding Polymorphism
description: The new data types include two polymorphic types, INT\_PTR and LONG\_PTR.
ms.assetid: 3d18016d-772c-45bc-8057-7281e71a8707
keywords:
- polymorphism 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Avoiding Polymorphism

The new data types include two polymorphic types, **INT\_PTR** and **LONG\_PTR**. On 32-bit Windows, the **INT\_PTR** maps to **int** and the **LONG\_PTR** maps to **long**. On 64-bit Windows, both types map to the **\_\_int64** intrinsic type. The MIDL compiler supports these types for remote procedure calls, but there is an inherent limitation that you must keep in mind when using them in a distributed environment. Be sure to comment your code accordingly.

Regardless of the platform size, the wire size of these polymorphic types is always 32 bits. When unmarshaling on 64-bit Windows, the run-time library sign extends signed values and assigns zero to the high-order bytes for an unsigned value. When putting a 64-bit value on the wire, the run time truncates the high-order bytes. Thus, only the low-order 32-bit values are usable.

Use the polymorphic types only when necessary for porting. For new interfaces, use the MIDL intrinsic integer types **\_\_int32** and **\_\_int64**, or use a pointer type or context handle, whichever is most appropriate for the kind of data being transferred.

The 64-bit compiler supports a new polymorphic intrinsic **\_\_int3264**. Again, this type was developed to support porting efforts, in this case to support the **UINT\_PTR** types transparently. (Another intrinsic, **\_\_long3264**, will support the **ULONG\_PTR** type.) Do not use **\_\_int3264** directly; use the **INT\_PTR** type when you need a polymorphic type for porting reasons.

 

 




