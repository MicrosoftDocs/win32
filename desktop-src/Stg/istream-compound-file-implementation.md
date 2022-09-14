---
title: IStream - Compound File Implementation
description: The IStream interface supports reading and writing data to stream objects. In a structured storage object, stream objects contain the data and storages provide the structure.
ms.assetid: 52474e37-0e14-4dcc-8e04-4442cfd26eb3
keywords:
- IStream Strctd Stg , compound file implementation
ms.topic: article
ms.date: 05/31/2018
---

# IStream - Compound File Implementation

The [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interface supports reading and writing data to stream objects. In a structured storage object, stream objects contain the data and storages provide the structure. Simple data can be written directly to a stream, but more frequently, streams are elements nested within a storage object. They are similar to standard files.

The specification of [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) defines more functionality than the COM implementation supports. For example, the **IStream** interface defines streams up to 2⁶⁴ bytes in length requiring a 64-bit seek pointer. However, the COM implementation only supports streams up to 2³² bytes in length (4 GB) and read and write operations are always limited to 2³² bytes at a time. The COM implementation also does not support stream transactioning or region locking.

To create a simple stream based on global memory, get an [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) pointer by calling the API function [**CreateStreamOnHGlobal**](/windows/desktop/api/combaseapi/nf-combaseapi-createstreamonhglobal). To get an **IStream** pointer within a compound file object, call either [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) or [**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage). These functions retrieve an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) pointer, with which you can then call [**CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) or [**OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream) for an **IStream** pointer. In either case, the same **IStream** implementation code is used.

> [!Note]  
> The compound file implementation of structured storage does not succeed on a [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method for [**ISequentialStream**](/windows/desktop/api/Objidl/nn-objidl-isequentialstream), but it includes the [**Read**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-read) and [**Write**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-write) methods through the [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interface pointer.

 

## When to Use

Call the methods of [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) to read and write data to a stream.

Because stream objects can be marshaled to other processes, applications can share the data in storage objects without having to use global memory. In the COM compound file implementation of stream objects, the custom marshaling facilities in COM create a remote version of the original object in the new process when the two processes have shared-memory access. Thus, the remote version does not need to communicate with the original process to carry out its functions.

The remote version of the stream object shares the same seek pointer as the original stream. If you do not want to share the seek pointer, use the [**IStream::Clone**](/windows/desktop/api/Objidl/nf-objidl-istream-clone) method to provide a copy of the stream object for the remote process.

> [!Note]
> If creating a stream object that is larger than the heap in your computer's memory and you are using an **HGLOBAL** handle to a global memory object, the stream object calls the [**GlobalRealloc**](/windows/desktop/api/winbase/nf-winbase-globalrealloc) method internally whe it requires more memory. Because **GlobalRealloc** always copies data from the source to the destination, increasing a stream object from 20 MB to 25 MB, for example, requires large amounts of time. This is due to the size of the increments copied and is worsened if there is less than 45 MB of memory on the computer because of disk swapping.
>
> The preferred solution is to implement an [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) method that uses memory allocated by [**VirtualAlloc**](/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc) instead of [**GlobalAlloc**](/windows/desktop/api/winbase/nf-winbase-globalalloc). This can reserve a large chunk of virtual address space and then commit memory within that address space as required. No data copying occurs and memory is committed only as it is required.
>
> An alternative to [**GlobalRealloc**](/windows/desktop/api/winbase/nf-winbase-globalrealloc) is to call the [**IStream::SetSize**](/windows/desktop/api/Objidl/nf-objidl-istream-setsize) method on the stream object to increase the memory allocation in advance. This is not, however, as efficient as using [**VirtualAlloc**](/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc), as described above.

 

## Methods

<dl> <dt>

<span id="ISequentialStream__Read"></span><span id="isequentialstream__read"></span><span id="ISEQUENTIALSTREAM__READ"></span>[**ISequentialStream::Read**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-read)
</dt> <dd>

Reads a specified number of bytes from the stream object into memory starting at the current seek pointer. This implementation returns S\_OK if the end of the stream was reached during the read. (This is the same as the "end of file" behavior found in the MS-DOS FAT file system.)

</dd> <dt>

<span id="ISequentialStream__Write"></span><span id="isequentialstream__write"></span><span id="ISEQUENTIALSTREAM__WRITE"></span>[**ISequentialStream::Write**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-write)
</dt> <dd>

Writes a specified number from bytes into the stream object starting at the current seek pointer. In this implementation, stream objects are not sparse. Any fill bytes are eventually allocated on the disk and assigned to the stream.

</dd> <dt>

<span id="IStream__Seek"></span><span id="istream__seek"></span><span id="ISTREAM__SEEK"></span>[**IStream::Seek**](/windows/desktop/api/Objidl/nf-objidl-istream-seek)
</dt> <dd>

Changes the seek pointer to a new location relative to the beginning of the stream, to the end of the stream, or to the current seek pointer.

</dd> <dt>

<span id="IStream__SetSize"></span><span id="istream__setsize"></span><span id="ISTREAM__SETSIZE"></span>[**IStream::SetSize**](/windows/desktop/api/Objidl/nf-objidl-istream-setsize)
</dt> <dd>

Changes the size of the stream object. In this implementation, there is no guarantee that the space allocated will be contiguous.

</dd> <dt>

<span id="IStream__CopyTo"></span><span id="istream__copyto"></span><span id="ISTREAM__COPYTO"></span>[**IStream::CopyTo**](/windows/desktop/api/Objidl/nf-objidl-istream-copyto)
</dt> <dd>

Copies a specified number of bytes from the current seek pointer in the stream to the current seek pointer in another stream.

</dd> <dt>

<span id="IStream__Commit"></span><span id="istream__commit"></span><span id="ISTREAM__COMMIT"></span>[**IStream::Commit**](/windows/desktop/api/Objidl/nf-objidl-istream-commit)
</dt> <dd>

The compound file implementation of [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) supports opening streams only in direct mode, not transacted mode. Therefore, the method has no effect when called other than to flush all memory buffers to the next storage level.

In this implementation, it does not matter if you commit changes to streams, you need only commit changes for storage objects.

</dd> <dt>

<span id="IStream__Revert"></span><span id="istream__revert"></span><span id="ISTREAM__REVERT"></span>[**IStream::Revert**](/windows/desktop/api/Objidl/nf-objidl-istream-revert)
</dt> <dd>

This implementation does not support transacted streams, so a call to this method has no effect.

</dd> <dt>

<span id="IStream__LockRegion"></span><span id="istream__lockregion"></span><span id="ISTREAM__LOCKREGION"></span>[**IStream::LockRegion**](/windows/desktop/api/Objidl/nf-objidl-istream-lockregion)
</dt> <dd>

Range-locking is not supported by this implementation, so a call to this method has no effect.

</dd> <dt>

<span id="IStream__UnlockRegion"></span><span id="istream__unlockregion"></span><span id="ISTREAM__UNLOCKREGION"></span>[**IStream::UnlockRegion**](/windows/desktop/api/Objidl/nf-objidl-istream-unlockregion)
</dt> <dd>

Removes the access restriction on a range of bytes previously restricted with [**IStream::LockRegion**](/windows/desktop/api/Objidl/nf-objidl-istream-lockregion).

</dd> <dt>

<span id="IStream__Stat"></span><span id="istream__stat"></span><span id="ISTREAM__STAT"></span>[**IStream::Stat**](/windows/desktop/api/Objidl/nf-objidl-istream-stat)
</dt> <dd>

Retrieves the [**STATSTG**](/windows/win32/api/objidl/ns-objidl-statstg) structure for this stream

</dd> <dt>

<span id="IStream__Clone"></span><span id="istream__clone"></span><span id="ISTREAM__CLONE"></span>[**IStream::Clone**](/windows/desktop/api/Objidl/nf-objidl-istream-clone)
</dt> <dd>

Creates a new stream object with its own seek pointer that references the same bytes as the original stream.

</dd> </dl>

A simple-mode [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) is subject to the following constraints.

-   A stream is simple mode if it was created or opened from a simple-mode storage. A storage is simple mode if it is created or opened with the STGM\_SIMPLE flag set in the *grfMode* parameter.
-   The [**Clone**](/windows/desktop/api/Objidl/nf-objidl-istream-clone) and [**CopyTo**](/windows/desktop/api/Objidl/nf-objidl-istream-copyto) methods are not supported.
-   The [**Stat**](/windows/desktop/api/Objidl/nf-objidl-istream-stat) method is supported, but the STATFLAG\_NONAME value must be specified.

## Related topics

<dl> <dt>

[**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream)
</dt> <dt>

[**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage)
</dt> <dt>

[**CreateStreamOnHGlobal**](/windows/desktop/api/combaseapi/nf-combaseapi-createstreamonhglobal)
</dt> <dt>

[**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile)
</dt> <dt>

[**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage)
</dt> </dl>

 

 