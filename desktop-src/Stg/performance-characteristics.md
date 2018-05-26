---
title: Performance Characteristics
description: A call to the COM compound file implementation of the IPropertySetStorage interface to create a property set causes either a stream or storage to be created through a call to IStorage CreateStream or IStorage CreateStorage.
ms.assetid: 7773e649-19a4-4df2-84ed-027d73283140
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Performance Characteristics

A call to the COM compound file implementation of the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface to create a property set causes either a stream or storage to be created through a call to [**IStorage::CreateStream**](/windows/win32/Objidl/nf-objidl-istorage-createstream?branch=master) or [**IStorage::CreateStorage**](/windows/win32/Objidl/nf-objidl-istorage-createstorage?branch=master). A default property set is created in memory, but not flushed to disk. When there is a call to [**IPropertyStorage::WriteMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-writemultiple?branch=master), it operates within the buffer.

When a property set is opened, [IStorage::OpenStream](/windows/win32/Objidl/nf-objidl-istorage-openstream?branch=master) or [IStorage::OpenStorage](/windows/win32/Objidl/nf-objidl-istorage-openstorage?branch=master) is used. The entire property set stream is read into contiguous memory. [**IPropertyStorage::ReadMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-readmultiple?branch=master) operations then operate by reading the memory buffer. Therefore, the first access is expensive in terms of time (because of disk reads) but subsequent accesses are very efficient. Writes may be slightly more expensive because SetSize operations on the underlying stream may be required to guarantee that disk space is available if data is added.

No guarantees are made as to whether [**IPropertyStorage::WriteMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-writemultiple?branch=master) will flush updates. In general, the client should assume that **IPropertyStorage::WriteMultiple** only updates the in memory buffer. To flush data, [**IPropertyStorage::Commit**](/windows/win32/Propidl/nf-propidl-ipropertystorage-commit?branch=master) or [**IUnknown::Release**](_com_iunknown_release) (last release) should be called.

This design means that [**WriteMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-writemultiple?branch=master) may succeed but the data is not actually persistently written.

> [!Note]  
> This size of the property set stream cannot exceed 256K bytes.

 

 

 




