---
title: Mixed Mode Serialization of Context Handles
description: In Microsoft Windows XP, a single interface can accommodate both serialized and nonserialized context handles, which is called mixed-mode serialization.
ms.assetid: b52c1d6f-cdc5-4597-a36e-bb957e4aab01
keywords:
- MIDL language reference MIDL , mixed mode serialization of context handles
- context handles MIDL
- mixed mode serialization MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Mixed Mode Serialization of Context Handles

Starting with Windows XP, a single interface can accommodate both serialized and nonserialized context handles, enabling one method on an interface to access a context handle exclusively (serialized), while other methods access that context handle in shared mode (nonserialized). For more information about context handles, see the following attributes:

-   [**context\_handle**](context-handle.md)
-   [**context\_handle\_serialize**](context-handle-serialize.md)
-   [**context\_handle\_noserialize**](context-handle-noserialize.md)

Serialized and shared mode access capabilities are comparable to read/write locking mechanisms; methods using a serialized context handle are exclusive users (writers), whereas methods using a nonserialized context handle are shared users (readers). Methods that destroy or modify the state of a context handle must be serialized. Methods that do not modify the state of a context handle, such as those methods that simply read from a context handle, can be nonserialized. Using a context handle in mixed mode can substantially improve the scalability of a server, especially when multiple threads make simultaneous calls to the same context handle.

RPC does not enforce "write lock" on methods using a context handle in shared mode, which means applications must ensure that shared mode context handles are not modified. Modification of a context handle used in shared mode can result in subtle corruptions of context handle contents, which are impossible to debug.

Changing the serialization logic of a context handle affects only the server. Also, changing the serialization logic of a context handle does not affect the wire format, and therefore, changes to serialization logic on a server do not affect existing clients' capability to interact with the server.

Using only nonserialized context handles is not recommended. Servers that use nonserialized handles are should switch to serialized access for the method that closes the context handle.

Context handles that are \[out\]-only are typically used by creation methods, and do not require any serialization. Therefore, any serialization attribute applied to \[out\]-only context handles, such as [**context\_handle\_serialize**](context-handle-serialize.md) or [**context\_handle\_noserialize**](context-handle-noserialize.md), is ignored by RPC.

> [!Note]  
> Creation methods are implicitly serialized.

 

## Examples

The following two examples show how to enable mixed mode serialization of context handles.

The first example shows how to do so in the IDL file:

``` syntax
typedef [context_handle] void *TestContextHandleExclusive;
typedef [context_handle] TestContextHandleExclusive TestContextHandleShared;

void
UseShared(...
          [in] TestContextHandleShared *Ctx,
          ...);

void
UseExclusive(...
             [in, out] TestContextHandleExclusive *Ctx,
             ...);
```

The second example shows how to enable mixed mode serialization of context handles in the ACF file:

``` syntax
typedef [context_handle_serialize] TestContextHandleExclusive;

typedef [context_handle_noserialize] TestContextHandleShared;
```

## Related topics

<dl> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**context\_handle\_serialize**](context-handle-serialize.md)
</dt> <dt>

[**context\_handle\_noserialize**](context-handle-noserialize.md)
</dt> </dl>

 

 




