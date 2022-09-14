---
title: Structured Storage Interfaces
description: Structured Storage services are organized into three categories of interfaces.
ms.assetid: a4281f07-eae4-4bcb-8d16-b6c0bd3c5b21
keywords:
- Structured Storage Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Structured Storage Interfaces

Structured Storage services are organized into three categories of [interfaces](interfaces.md). Each set represents a successive level of indirection or abstraction between a compound file, the objects it contains, and the physical media in which these individual components are stored.

The first category of interfaces consists of [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage), [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream), and [**IRootStorage**](/windows/desktop/api/Objidl/nn-objidl-irootstorage). The first two interfaces define how objects are stored within a compound file. These interfaces provide methods for opening storage elements, committing and reverting changes, copying and moving elements, and reading and writing streams. These interfaces do not recognize the native data formats of the individual objects and therefore have no methods for saving those objects to persistent storage. The **IRootStorage** interface has a single method for associating a compound document with an underlying file system name. Clients must implement these interfaces for their compound files.

The second category of interfaces consists of the [**IPersist**](/windows/win32/api/objidl/nn-objidl-ipersist) interfaces, which objects implement to manage their persistent data. These interfaces provide methods to read the data formats of individual objects and therefore know how to store them. Objects are responsible for implementing these interfaces because clients do not know the native data formats of their nested objects. These interfaces, however, have no knowledge of specific physical storage media.

A third category consists of a single interface, [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes), which provides methods for writing files to specific physical media, such as a hard disk or tape drive. However, most applications will not implement the **ILockBytes** interface because COM already provides implementations for the two most common situations, which are File-based implementation and Memory-based implementation. The compound file storage object calls the **ILockBytes** methods you do not call them directly in the implementation.

## Compound File Implementation Limits

The COM implementation of Structured Storage architecture is called *compound files*. Storage objects, as implemented in compound files, include an implementation of the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) and [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interfaces.

Pointers to the compound file implementation of these interfaces are acquired by calling the [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) function to create a new compound file object, or [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) to open a previously created compound file.

An alternative method for acquiring a pointer to the compound file implementation of these interfaces is by calling the older and more limited [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) or [**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage) function. All four functions are treated as compound file implementations.

The compound file implementation can be configured to use 512 or 4096 byte sectors, as defined in the [**STGOPTIONS**](/windows/win32/api/coml2api/ns-coml2api-stgoptions) structure.

The compound file implementation of compound files is subject to the following implementation constraints.



| Limit                                           | Compound file                                                                                                                                                                      |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File size limits:                               | 512: 2 gigabytes (GB) 4096: Up to file system limits<br/>                                                                                                                    |
| Maximum heap size required for open elements:   | 512: 4 megabytes (MB) 4096: Up to virtual memory limits<br/>                                                                                                                 |
| Concurrent root opens (opens of the same file): | If STGM\_READ and STGM\_SHARE\_DENY\_WRITE are specified, limits are dictated by the file-system limits. Otherwise, there is a limit of 20 concurrent root opens of the same file. |
| Number of elements in a file:                   | 512: Unlimited, but performance may degrade if elements number in the thousands 4096: Unlimited<br/>                                                                         |



 

Due to the 4-MB heap-size limit, the number of open elements in transacted mode is typically limited to several thousand elements.

 

