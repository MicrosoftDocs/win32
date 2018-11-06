---
title: Differences between Stand-alone and Compound File Implementations
description: The stand-alone implementation of the property set interfaces and the compound file implementation differ in some ways.
ms.assetid: 650d4759-a58a-47a4-922d-5757e356cf56
keywords:
- IPropertyStorage Strctd Stg , implementations
- IPropertyStorage Strctd Stg , implementations, differences
ms.topic: article
ms.date: 05/31/2018
---

# Differences between Stand-alone and Compound File Implementations

The stand-alone implementation of the property set interfaces and the compound file implementation differ in some ways. In the compound-file implementation of stream, storage, property set storage, and property storage objects, the various interfaces coordinate with each another because they share a common implementation. In the stand-alone implementation, the interface implementations are distinct.

As a result, the compound-file implementation handles concurrency issues and synchronizes the property set object with the storage or stream object. With the stand-alone implementation, the client is responsible for handling concurrency and synchronization issues between the storage or stream object and the property set. A client can meet these requirements by following two simple rules. First, never manipulate a property set using its stream or storage interfaces while a property storage object is open on it. Second, always call **Commit** on a property storage object before calling **CopyTo**, **MoveElementTo**, or **Commit** on an ancestor storage object. Specifically, the following items require client attention:

-   In the compound-file implementation, a single mechanism provides concurrency protection for the storage object and its associated property set objects. However, in the stand-alone implementation, the storage object implementation is separate from the property set implementation and each provides its own concurrency mechanisms. Thus, in the stand-alone implementation, the client is responsible for maintaining concurrency protection between the two implementations through a mechanism of mutual exclusion.
-   In the compound file implementation, changes to property sets are buffered in a property-set cache. Then, when the [**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit) method is called on the storage object, the compound files implementation automatically flushes the property-set changes from the property-set buffer before the storage object is committed. Thus, the property-set changes are made visible as part of the transaction being committed.

    In the stand-alone implementation, the client must explicitly flush the property-set buffer by calling [**IPropertyStorage::Commit**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-commit) before calling the [**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit) method on the storage. Alternatively, the client can use the new PROPSETFLAG\_UNBUFFERED value in the stand-alone implementation to write directly to the property set instead of caching changes to the property set's internal buffer. If PROPSETFLAG\_UNBUFFERED is used, the client's responsibilities are automatically met. The compound file implementation does not support the PROPSETFLAG\_UNBUFFERED value. For more information, see [**PROPSETFLAG Constants**](propsetflag-constants.md).

-   As with transacted storages, the compound file implementation updates the property set by flushing its internal buffer before executing a call to [**IStorage::CopyTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-copyto) or [**IStorage::MoveElementTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-moveelementto). Thus, changes to the property set are reflected in the copied or moved storage element.

    In the stand-alone implementation, the client must explicitly flush the property set buffer by calling [**IPropertyStorage::Commit**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-commit) before calling [**IStorage::CopyTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-copyto) or [**IStorage::MoveElementTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-moveelementto). Alternatively, the client can use the new PROPSETFLAG\_UNBUFFERED value to write directly to the property set instead of caching changes to the property set buffer. For more information, see [**PROPSETFLAG Constants**](propsetflag-constants.md).

 

 




