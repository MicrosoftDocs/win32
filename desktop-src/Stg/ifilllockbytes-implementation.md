---
title: IFillLockBytes - Implementation
description: The system provides an IFillLockBytes implementation as part of the Compound Files implementation.
ms.assetid: 'a8aed8c5-3c4c-4cce-b568-68031da0edf5'
keywords: ["IFillLockBytes Strctd Stg , implementation"]
---

# IFillLockBytes - Implementation

The system provides an [**IFillLockBytes**](ifilllockbytes.md) implementation as part of the Compound Files implementation.

Downloading code can create an instance of an asynchronous Compound File object by calling [**StgOpenAsyncDocFileOnIFillLockBytes**](stgopenasyncdocfileonifilllockbytes.md). Downloading code can also create an instance of an asynchronous byte array wrapper object on an existing file or byte array by calling either the [**StgGetIFillLockBytesOnFile**](stggetifilllockbytesonfile.md) function or the [**StgGetIFillLockBytesOnILockBytes**](stggetifilllockbytesonilockbytes.md) function.

## When to Use

Currently, URL monikers are the only users of the COM asynchronous storage implementation.

## Remarks

The following are the four methods of the [**IFillLockBytes**](ifilllockbytes.md) implementation.

<dl> <dt>

<span id="IFillLockBytes__FillAppend"></span><span id="ifilllockbytes__fillappend"></span><span id="IFILLLOCKBYTES__FILLAPPEND"></span>**IFillLockBytes::FillAppend**
</dt> <dd>

Writes a new block of bytes to the end of a byte array. The size of the block is specified as a parameter to [**FillAppend**](ifilllockbytes-fillappend.md).

</dd> <dt>

<span id="IFillLockBytes__FillAt"></span><span id="ifilllockbytes__fillat"></span><span id="IFILLLOCKBYTES__FILLAT"></span>**IFillLockBytes::FillAt**
</dt> <dd>

Writes a new block of data to a specified location in the byte array.

</dd> <dt>

<span id="IFillLockBytes__SetFillSize"></span><span id="ifilllockbytes__setfillsize"></span><span id="IFILLLOCKBYTES__SETFILLSIZE"></span>**IFillLockBytes::SetFillSize**
</dt> <dd>

Sets the size of the byte array. Returns E\_FAIL from calls to [**ILockBytes::ReadAt**](ilockbytes-readat.md) that attempt to access data beyond the upper limit specified by the method.

</dd> <dt>

<span id="IFillLockBytes__Terminate"></span><span id="ifilllockbytes__terminate"></span><span id="IFILLLOCKBYTES__TERMINATE"></span>**IFillLockBytes::Terminate**
</dt> <dd>

Informs the byte array that a download has been terminated, either successfully or unsuccessfully.

</dd> </dl>

 

 




