---
title: IStream - Compound File Implementation
description: The IStream interface supports reading and writing data to stream objects. In a structured storage object, stream objects contain the data and storages provide the structure.
ms.assetid: '52474e37-0e14-4dcc-8e04-4442cfd26eb3'
keywords: ["IStream Strctd Stg , compound file implementation"]
---

# IStream - Compound File Implementation

The [**IStream**](istream.md) interface supports reading and writing data to stream objects. In a structured storage object, stream objects contain the data and storages provide the structure. Simple data can be written directly to a stream, but more frequently, streams are elements nested within a storage object. They are similar to standard files.

The specification of [**IStream**](istream.md) defines more functionality than the COM implementation supports. For example, the **IStream** interface defines streams up to 2⁶⁴ bytes in length requiring a 64-bit seek pointer. However, the COM implementation only supports streams up to 2³² bytes in length (4 GB) and read and write operations are always limited to 2³² bytes at a time. The COM implementation also does not support stream transactioning or region locking.

To create a simple stream based on global memory, get an [**IStream**](istream.md) pointer by calling the API function [**CreateStreamOnHGlobal**](createstreamonhglobal.md). To get an **IStream** pointer within a compound file object, call either [**StgCreateDocfile**](stgcreatedocfile.md) or [**StgOpenStorage**](stgopenstorage.md). These functions retrieve an [**IStorage**](istorage.md) pointer, with which you can then call [**CreateStream**](istorage-createstream.md) or [**OpenStream**](istorage-openstream.md) for an **IStream** pointer. In either case, the same **IStream** implementation code is used.

> [!Note]  
> The compound file implementation of structured storage does not succeed on a [**QueryInterface**](_com_iunknown_queryinterface) method for [**ISequentialStream**](isequentialstream.md), but it includes the [**Read**](isequentialstream-read.md) and [**Write**](isequentialstream-write.md) methods through the [**IStream**](istream.md) interface pointer.

 

## When to Use

Call the methods of [**IStream**](istream.md) to read and write data to a stream.

Because stream objects can be marshaled to other processes, applications can share the data in storage objects without having to use global memory. In the COM compound file implementation of stream objects, the custom marshaling facilities in COM create a remote version of the original object in the new process when the two processes have shared-memory access. Thus, the remote version does not need to communicate with the original process to carry out its functions.

The remote version of the stream object shares the same seek pointer as the original stream. If you do not want to share the seek pointer, use the [**IStream::Clone**](istream-clone.md) method to provide a copy of the stream object for the remote process.

> [!Note]If creating a stream object that is larger than the heap in your computer's memory and you are using an **HGLOBAL** handle to a global memory object, the stream object calls the [**GlobalRealloc**](https://msdn.microsoft.com/library/windows/desktop/aa366590) method internally whe it requires more memory. Because **GlobalRealloc** always copies data from the source to the destination, increasing a stream object from 20 MB to 25 MB, for example, requires large amounts of time. This is due to the size of the increments copied and is worsened if there is less than 45 MB of memory on the computer because of disk swapping.
>
> The preferred solution is to implement an [**IStream**](istream.md) method that uses memory allocated by [**VirtualAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366887) instead of [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574). This can reserve a large chunk of virtual address space and then commit memory within that address space as required. No data copying occurs and memory is committed only as it is required.
>
> An alternative to [**GlobalRealloc**](https://msdn.microsoft.com/library/windows/desktop/aa366590) is to call the [**IStream::SetSize**](istream-setsize.md) method on the stream object to increase the memory allocation in advance. This is not, however, as efficient as using [**VirtualAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366887), as described above.

 

## Methods

<dl> <dt>

<span id="ISequentialStream__Read"></span><span id="isequentialstream__read"></span><span id="ISEQUENTIALSTREAM__READ"></span>[**ISequentialStream::Read**](isequentialstream-read.md)
</dt> <dd>

Reads a specified number of bytes from the stream object into memory starting at the current seek pointer. This implementation returns S\_OK if the end of the stream was reached during the read. (This is the same as the "end of file" behavior found in the MS-DOS FAT file system.)

</dd> <dt>

<span id="ISequentialStream__Write"></span><span id="isequentialstream__write"></span><span id="ISEQUENTIALSTREAM__WRITE"></span>[**ISequentialStream::Write**](isequentialstream-write.md)
</dt> <dd>

Writes a specified number from bytes into the stream object starting at the current seek pointer. In this implementation, stream objects are not sparse. Any fill bytes are eventually allocated on the disk and assigned to the stream.

</dd> <dt>

<span id="IStream__Seek"></span><span id="istream__seek"></span><span id="ISTREAM__SEEK"></span>[**IStream::Seek**](istream-seek.md)
</dt> <dd>

Changes the seek pointer to a new location relative to the beginning of the stream, to the end of the stream, or to the current seek pointer.

</dd> <dt>

<span id="IStream__SetSize"></span><span id="istream__setsize"></span><span id="ISTREAM__SETSIZE"></span>[**IStream::SetSize**](istream-setsize.md)
</dt> <dd>

Changes the size of the stream object. In this implementation, there is no guarantee that the space allocated will be contiguous.

</dd> <dt>

<span id="IStream__CopyTo"></span><span id="istream__copyto"></span><span id="ISTREAM__COPYTO"></span>[**IStream::CopyTo**](istream-copyto.md)
</dt> <dd>

Copies a specified number of bytes from the current seek pointer in the stream to the current seek pointer in another stream.

</dd> <dt>

<span id="IStream__Commit"></span><span id="istream__commit"></span><span id="ISTREAM__COMMIT"></span>[**IStream::Commit**](istream-commit.md)
</dt> <dd>

The compound file implementation of [**IStream**](istream.md) supports opening streams only in direct mode, not transacted mode. Therefore, the method has no effect when called other than to flush all memory buffers to the next storage level.

In this implementation, it does not matter if you commit changes to streams, you need only commit changes for storage objects.

</dd> <dt>

<span id="IStream__Revert"></span><span id="istream__revert"></span><span id="ISTREAM__REVERT"></span>[**IStream::Revert**](istream-revert.md)
</dt> <dd>

This implementation does not support transacted streams, so a call to this method has no effect.

</dd> <dt>

<span id="IStream__LockRegion"></span><span id="istream__lockregion"></span><span id="ISTREAM__LOCKREGION"></span>[**IStream::LockRegion**](istream-lockregion.md)
</dt> <dd>

Range-locking is not supported by this implementation, so a call to this method has no effect.

</dd> <dt>

<span id="IStream__UnlockRegion"></span><span id="istream__unlockregion"></span><span id="ISTREAM__UNLOCKREGION"></span>[**IStream::UnlockRegion**](istream-unlockregion.md)
</dt> <dd>

Removes the access restriction on a range of bytes previously restricted with [**IStream::LockRegion**](istream-lockregion.md).

</dd> <dt>

<span id="IStream__Stat"></span><span id="istream__stat"></span><span id="ISTREAM__STAT"></span>[**IStream::Stat**](istream-stat.md)
</dt> <dd>

Retrieves the [**STATSTG**](statstg.md) structure for this stream

</dd> <dt>

<span id="IStream__Clone"></span><span id="istream__clone"></span><span id="ISTREAM__CLONE"></span>[**IStream::Clone**](istream-clone.md)
</dt> <dd>

Creates a new stream object with its own seek pointer that references the same bytes as the original stream.

</dd> </dl>

A simple-mode [**IStream**](istream.md) is subject to the following constraints.

-   A stream is simple mode if it was created or opened from a simple-mode storage. A storage is simple mode if it is created or opened with the STGM\_SIMPLE flag set in the *grfMode* parameter.
-   The [**Clone**](istream-clone.md) and [**CopyTo**](istream-copyto.md) methods are not supported.
-   The [**Stat**](istream-stat.md) method is supported, but the STATFLAG\_NONAME value must be specified.

## Related topics

<dl> <dt>

[**IStream**](istream.md)
</dt> <dt>

[**IStorage**](istorage.md)
</dt> <dt>

[**CreateStreamOnHGlobal**](createstreamonhglobal.md)
</dt> <dt>

[**StgCreateDocfile**](stgcreatedocfile.md)
</dt> <dt>

[**StgOpenStorage**](stgopenstorage.md)
</dt> </dl>

 

 




