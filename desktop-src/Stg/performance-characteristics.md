---
title: Performance Characteristics
description: A call to the COM compound file implementation of the IPropertySetStorage interface to create a property set causes either a stream or storage to be created through a call to IStorage CreateStream or IStorage CreateStorage.
ms.assetid: 7773e649-19a4-4df2-84ed-027d73283140
ms.topic: article
ms.date: 05/31/2018
---

# Performance Characteristics

A call to the COM compound file implementation of the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface to create a property set causes either a stream or storage to be created through a call to [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) or [**IStorage::CreateStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstorage). A default property set is created in memory, but not flushed to disk. When there is a call to [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple), it operates within the buffer.

When a property set is opened, [IStorage::OpenStream](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream) or [IStorage::OpenStorage](/windows/desktop/api/Objidl/nf-objidl-istorage-openstorage) is used. The entire property set stream is read into contiguous memory. [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) operations then operate by reading the memory buffer. Therefore, the first access is expensive in terms of time (because of disk reads) but subsequent accesses are very efficient. Writes may be slightly more expensive because SetSize operations on the underlying stream may be required to guarantee that disk space is available if data is added.

No guarantees are made as to whether [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple) will flush updates. In general, the client should assume that **IPropertyStorage::WriteMultiple** only updates the in memory buffer. To flush data, [**IPropertyStorage::Commit**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-commit) or [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) (last release) should be called.

This design means that [**WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple) may succeed but the data is not actually persistently written.

> [!Note]  
> This size of the property set stream cannot exceed 256K bytes.

 

 

 