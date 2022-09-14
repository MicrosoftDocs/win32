---
title: IFillLockBytes - Implementation
description: The system provides an IFillLockBytes implementation as part of the Compound Files implementation.
ms.assetid: a8aed8c5-3c4c-4cce-b568-68031da0edf5
keywords:
- IFillLockBytes Strctd Stg , implementation
ms.topic: article
ms.date: 05/31/2018
---

# IFillLockBytes - Implementation

The system provides an [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) implementation as part of the Compound Files implementation.

Downloading code can create an instance of an asynchronous Compound File object by calling [**StgOpenAsyncDocFileOnIFillLockBytes**](/windows/desktop/api/Objbase/nf-objbase-stgopenasyncdocfileonifilllockbytes). Downloading code can also create an instance of an asynchronous byte array wrapper object on an existing file or byte array by calling either the [**StgGetIFillLockBytesOnFile**](/windows/desktop/api/Objbase/nf-objbase-stggetifilllockbytesonfile) function or the [**StgGetIFillLockBytesOnILockBytes**](/windows/desktop/api/Objbase/nf-objbase-stggetifilllockbytesonilockbytes) function.

## When to Use

Currently, URL monikers are the only users of the COM asynchronous storage implementation.

## Remarks

The following are the four methods of the [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) implementation.

<dl> <dt>

<span id="IFillLockBytes__FillAppend"></span><span id="ifilllockbytes__fillappend"></span><span id="IFILLLOCKBYTES__FILLAPPEND"></span>**IFillLockBytes::FillAppend**
</dt> <dd>

Writes a new block of bytes to the end of a byte array. The size of the block is specified as a parameter to [**FillAppend**](/windows/desktop/api/Objidl/nf-objidl-ifilllockbytes-fillappend).

</dd> <dt>

<span id="IFillLockBytes__FillAt"></span><span id="ifilllockbytes__fillat"></span><span id="IFILLLOCKBYTES__FILLAT"></span>**IFillLockBytes::FillAt**
</dt> <dd>

Writes a new block of data to a specified location in the byte array.

</dd> <dt>

<span id="IFillLockBytes__SetFillSize"></span><span id="ifilllockbytes__setfillsize"></span><span id="IFILLLOCKBYTES__SETFILLSIZE"></span>**IFillLockBytes::SetFillSize**
</dt> <dd>

Sets the size of the byte array. Returns E\_FAIL from calls to [**ILockBytes::ReadAt**](/windows/desktop/api/Objidl/nf-objidl-ilockbytes-readat) that attempt to access data beyond the upper limit specified by the method.

</dd> <dt>

<span id="IFillLockBytes__Terminate"></span><span id="ifilllockbytes__terminate"></span><span id="IFILLLOCKBYTES__TERMINATE"></span>**IFillLockBytes::Terminate**
</dt> <dd>

Informs the byte array that a download has been terminated, either successfully or unsuccessfully.

</dd> </dl>

 

 




