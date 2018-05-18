---
title: ILockBytes - File-Based Implementation
description: Implemented on a byte array object underlying a COM compound file storage object, and designed to read and write directly to a disk file.
ms.assetid: '700b6a3c-1046-4c21-8887-16f344c23510'
keywords: ["ILockBytes Strctd Stg , implementations,file-based"]
---

# ILockBytes - File-Based Implementation

Implemented on a byte array object underlying a COM compound file storage object, and designed to read and write directly to a disk file.

## When to Use

Methods of [**ILockBytes**](ilockbytes.md) are called from the compound file implementations of [**IStorage**](istorage.md) and [**IStream**](istream.md) on the compound file storage object created through a call to [**StgCreateDocfile**](stgcreatedocfile.md), so you do not need to call them directly.

## Remarks

The following are the methods of the [**ILockBytes**](ilockbytes.md) File-Based Implementation.

<dl> <dt>

<span id="ILockBytes__ReadAt"></span><span id="ilockbytes__readat"></span><span id="ILOCKBYTES__READAT"></span>**ILockBytes::ReadAt**
</dt> <dd>

Reads a block of bytes from a specified offset at the beginning of the byte-array.

</dd> <dt>

<span id="ILockBytes__WriteAt"></span><span id="ilockbytes__writeat"></span><span id="ILOCKBYTES__WRITEAT"></span>**ILockBytes::WriteAt**
</dt> <dd>

Writes a block of bytes from a specified offset at the beginning of the byte array.

</dd> <dt>

<span id="ILockBytes__Flush"></span><span id="ilockbytes__flush"></span><span id="ILOCKBYTES__FLUSH"></span>**ILockBytes::Flush**
</dt> <dd>

Ensures that any internal buffers maintained by the [**ILockBytes**](ilockbytes.md) implementation are written out to the underlying physical storage.

</dd> <dt>

<span id="ILockBytes__SetSize"></span><span id="ilockbytes__setsize"></span><span id="ILOCKBYTES__SETSIZE"></span>**ILockBytes::SetSize**
</dt> <dd>

Sets the size of the byte array.

</dd> <dt>

<span id="ILockBytes__LockRegion"></span><span id="ilockbytes__lockregion"></span><span id="ILOCKBYTES__LOCKREGION"></span>**ILockBytes::LockRegion**
</dt> <dd>

The *dwLockTypes* parameter is set to LOCK\_ONLYONCE or LOCK\_EXCLUSIVE, which will allow or restrict access to locked regions.

</dd> <dt>

<span id="ILockBytes__UnlockRegion"></span><span id="ilockbytes__unlockregion"></span><span id="ILOCKBYTES__UNLOCKREGION"></span>**ILockBytes::UnlockRegion**
</dt> <dd>

This method unlocks the region locked by [**ILockBytes::LockRegion**](ilockbytes-lockregion.md).

</dd> <dt>

<span id="ILockBytes__Stat"></span><span id="ilockbytes__stat"></span><span id="ILOCKBYTES__STAT"></span>**ILockBytes::Stat**
</dt> <dd>

The COM-provided [**IStorage::Stat**](istorage-stat.md) implementation calls the [**ILockBytes::Stat**](ilockbytes-stat.md) method to retrieve information about the byte array object. If there is no reasonable name for the byte array, the COM-provided **ILockBytes::Stat** method returns **NULL** in the **pwcsName** member of the [**STATSTG**](statstg.md) structure.

</dd> </dl>

## Related topics

<dl> <dt>

[**ILockBytes**](ilockbytes.md)
</dt> <dt>

[**IStorage**](istorage.md)
</dt> <dt>

[**IStream**](istream.md)
</dt> </dl>

 

 




