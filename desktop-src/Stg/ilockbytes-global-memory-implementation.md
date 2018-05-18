---
title: ILockBytes - Global Memory Implementation
description: The ILockBytes global memory implementation is implemented on a byte array object underlying a COM compound file storage object, and designed to read and write directly to global memory.
ms.assetid: '6ab019b0-34d7-4b6e-ba77-6b6881fabd29'
keywords: ["ILockBytes Strctd Stg , implementations, global memory", "ILockBytes Strctd Stg , implementations"]
---

# ILockBytes - Global Memory Implementation

The ILockBytes global memory implementation is implemented on a byte array object underlying a COM compound file storage object, and designed to read and write directly to global memory.

## When to Use

Methods of [**ILockBytes**](ilockbytes.md) are called from the compound file implementations of [**IStorage**](istorage.md) and [**IStream**](istream.md) on the compound file storage object created through a call to [**StgCreateDocfile**](stgcreatedocfile.md).

## Remarks

The following are the methods of the [**ILockBytes**](ilockbytes.md) Global Memory Implementation.

<dl> <dt>

<span id="ILockBytes__ReadAt"></span><span id="ilockbytes__readat"></span><span id="ILOCKBYTES__READAT"></span>**ILockBytes::ReadAt**
</dt> <dd>

Reads a block of bytes from a specified offset at the beginning of the byte array.

</dd> <dt>

<span id="ILockBytes__WriteAt"></span><span id="ilockbytes__writeat"></span><span id="ILOCKBYTES__WRITEAT"></span>**ILockBytes::WriteAt**
</dt> <dd>

Writes the block of bytes from a specified offset at the beginning of the byte array.

</dd> <dt>

<span id="ILockBytes__Flush"></span><span id="ilockbytes__flush"></span><span id="ILOCKBYTES__FLUSH"></span>**ILockBytes::Flush**
</dt> <dd>

Unlike file-based implementation, calling this method in global memory implementation has no effect.

</dd> <dt>

<span id="ILockBytes__SetSize"></span><span id="ilockbytes__setsize"></span><span id="ILOCKBYTES__SETSIZE"></span>**ILockBytes::SetSize**
</dt> <dd>

Sets the size of the byte array.

</dd> <dt>

<span id="ILockBytes__LockRegion"></span><span id="ilockbytes__lockregion"></span><span id="ILOCKBYTES__LOCKREGION"></span>**ILockBytes::LockRegion**
</dt> <dd>

This implementation does not support locking, so *dwLocksType* is set to zero. The caller must ensure accesses are valid and mutually exclusive.

</dd> <dt>

<span id="ILockBytes__UnlockRegion"></span><span id="ilockbytes__unlockregion"></span><span id="ILOCKBYTES__UNLOCKREGION"></span>**ILockBytes::UnlockRegion**
</dt> <dd>

This implementation does not support locking.

</dd> <dt>

<span id="ILockBytes__Stat"></span><span id="ilockbytes__stat"></span><span id="ILOCKBYTES__STAT"></span>**ILockBytes::Stat**
</dt> <dd>

The COM-provided [**IStorage::Stat**](istorage-stat.md) implementation calls the [**ILockBytes::Stat**](ilockbytes-stat.md) method to retrieve data about the byte array object. If there is no reasonable name for the byte array, the COM-provided **ILockBytes::Stat** method returns **NULL** in the **pwcsName** member of the [**STATSTG**](statstg.md) structure.

</dd> </dl>

## Related topics

<dl> <dt>

[**ILockBytes**](ilockbytes.md)
</dt> <dt>

[**IStorage**](istorage.md)
</dt> <dt>

[**IStream**](istream.md)
</dt> </dl>

 

 




