---
title: Performance Characteristics
description: A call to the COM compound file implementation of the IPropertySetStorage interface to create a property set causes either a stream or storage to be created through a call to IStorage CreateStream or IStorage CreateStorage.
ms.assetid: '7773e649-19a4-4df2-84ed-027d73283140'
---

# Performance Characteristics

A call to the COM compound file implementation of the [**IPropertySetStorage**](ipropertysetstorage.md) interface to create a property set causes either a stream or storage to be created through a call to [**IStorage::CreateStream**](istorage-createstream.md) or [**IStorage::CreateStorage**](istorage-createstorage.md). A default property set is created in memory, but not flushed to disk. When there is a call to [**IPropertyStorage::WriteMultiple**](ipropertystorage-writemultiple.md), it operates within the buffer.

When a property set is opened, [IStorage::OpenStream](istorage-openstream.md) or [IStorage::OpenStorage](istorage-openstorage.md) is used. The entire property set stream is read into contiguous memory. [**IPropertyStorage::ReadMultiple**](ipropertystorage-readmultiple.md) operations then operate by reading the memory buffer. Therefore, the first access is expensive in terms of time (because of disk reads) but subsequent accesses are very efficient. Writes may be slightly more expensive because SetSize operations on the underlying stream may be required to guarantee that disk space is available if data is added.

No guarantees are made as to whether [**IPropertyStorage::WriteMultiple**](ipropertystorage-writemultiple.md) will flush updates. In general, the client should assume that **IPropertyStorage::WriteMultiple** only updates the in memory buffer. To flush data, [**IPropertyStorage::Commit**](ipropertystorage-commit.md) or [**IUnknown::Release**](_com_iunknown_release) (last release) should be called.

This design means that [**WriteMultiple**](ipropertystorage-writemultiple.md) may succeed but the data is not actually persistently written.

> [!Note]  
> This size of the property set stream cannot exceed 256K bytes.

 

 

 




