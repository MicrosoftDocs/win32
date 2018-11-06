---
title: IDirectWriterLock - Compound File Implementation
description: The compound file implementation of IDirectWriterLock provides a way to open a compound file in direct mode with a single writer and multiple readers.
ms.assetid: 4b247dae-d937-430a-bdb7-c47fa3c026b6
keywords:
- IDirectWriterLock Strctd Stg , compound file implementation
ms.topic: article
ms.date: 05/31/2018
---

# IDirectWriterLock - Compound File Implementation

The compound file implementation of [**IDirectWriterLock**](/windows/desktop/api/Objidl/nn-objidl-idirectwriterlock) provides a way to open a compound file in direct mode with a single writer and multiple readers.

Compound files can be opened in direct mode using the STGM\_DIRECT flag. The [**IDirectWriterLock**](/windows/desktop/api/Objidl/nn-objidl-idirectwriterlock) interface sets the STGM\_READWRITE\|STGM\_SHARE\_DENY\_WRITE flag as valid in direct mode without requiring the overhead of a snapshot copy.

When a compound file is opened in transacted mode using the STGM\_TRANSACTED flag, you can also have multiple readers and a single writer using the STGM\_READWRITE\|STGM\_SHARE\_DENY\_WRITE flag. However, in this case, a snapshot copy of the file is made for the readers. There is often overhead of a scratch copy.

## When to Use

Use the system-supplied implementation of [**IDirectWriterLock**](/windows/desktop/api/Objidl/nn-objidl-idirectwriterlock) when you open a storage in direct mode (STGM\_DIRECT) with the STGM\_READWRITE\|STGM\_SHARE\_DENY\_WRITE flags.

To obtain a pointer to [**IDirectWriterLock**](/windows/desktop/api/Objidl/nn-objidl-idirectwriterlock), call **QueryInterface** on [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) to get the root storage object for the compound file.

Call [**IDirectWriterLock::WaitForWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-waitforwriteaccess) to obtain exclusive write access to a compound file. Call [**IDirectWriterLock::ReleaseWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-releasewriteaccess) to release exclusive write access.

[**IDirectWriterLock::HaveWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-havewriteaccess) indicates whether the file is currently locked.

## Remarks

The compound file implementation of the single-writer, multiple-reader feature is based on range locking. The writer obtains exclusive access to the storage to write after all current readers have closed the storage. While the writer is active, subsequent readers cannot open the storage. The writer calls [**IDirectWriterLock::WaitForWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-waitforwriteaccess) to obtain exclusive write access. The writer must then call [**IDirectWriterLock::ReleaseWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-releasewriteaccess) to release the storage.

The call to [**IDirectWriterLock::WaitForWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-waitforwriteaccess) is required before writing in this single-reader, multiple-writer mode. Attempts to write to the file without calling **IDirectWriterLock::WaitForWriteAccess** first result in STG\_E\_ACCESSDENIED. This error is returned even if the writer opened the file initially, and no readers currently have the file open.

## Marshaling Considerations

Custom marshaling is typically used when a compound file is marshaled to another process on the same machine. When marshaling storages, access rights are not considered, and the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) pointer is passed to the new process with the same access modes and rights as the original marshaling process. For more information about access modes, see [**STGM Constants**](stgm-constants.md). During marshaling, no locks are taken or verified to ensure exclusive write access. In this case, there is no enforcement of the single-writer policy for compound files opened in the single-writer, multiple-reader mode. Instead, enforcement is handled internally by the compound file implementation.

Because the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) pointer is passed to another process during marshaling, it is possible for two processes to have simultaneous access to the same compound file. Even though a caller may have obtained exclusive write access to the storage by calling [**IDirectWriterLock::WaitForWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-waitforwriteaccess), the marshaled version can also have access simultaneously. The marshaled versions are not forced to close while the single writer accesses the file. In this case, the compound file implementation synchronizes the writes internally.

If a single writer obtains exclusive access by calling, [**IDirectWriterLock::WaitForWriteAccess**](/windows/desktop/api/Objidl/nf-objidl-idirectwriterlock-waitforwriteaccess), the marshaled storage also has write access and does not have to call **IDirectWriterLock::WaitForWriteAccess**. Both processes have write access and synchronization is controlled by the internal compound file implementation.

## Related topics

<dl> <dt>

[**IDirectWriterLock**](/windows/desktop/api/Objidl/nn-objidl-idirectwriterlock)
</dt> </dl>

 

 




