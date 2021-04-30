---
title: STGM Constants (ObjBase.h)
description: Flags that indicate conditions for creating and deleting the object and access modes for the object.
ms.assetid: 15a35da9-332a-46e1-9190-500c95e26f59
topic_type:
- apiref
api_name:
- STGM_READ
- STGM_WRITE
- STGM_READWRITE
- STGM_SHARE_DENY_NONE
- STGM_SHARE_DENY_READ
- STGM_SHARE_DENY_WRITE
- STGM_SHARE_EXCLUSIVE
- STGM_PRIORITY
- STGM_CREATE
- STGM_CONVERT
- STGM_FAILIFTHERE
- STGM_DIRECT
- STGM_TRANSACTED
- STGM_NOSCRATCH
- STGM_NOSNAPSHOT
- STGM_SIMPLE
- STGM_DIRECT_SWMR
- STGM_DELETEONRELEASE
api_location:
- ObjBase.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# STGM Constants

The STGM constants are flags that indicate conditions for creating and deleting the object and access modes for the object. The STGM constants are included in the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage), [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream), and [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interfaces and in the [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile), [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex), [**StgCreateDocfileOnILockBytes**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfileonilockbytes), [**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage), and [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) functions.

These elements are often combined using an **OR**operator. They are interpreted in groups as listed in the following table. It is not valid to use more than one element from a single group.

Use a flag from the creation group when creating an object, such as with [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) or [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream).

For more information about transactioning, see the Remarks section.



| Group                      | Flag                         | Value       |
|----------------------------|------------------------------|-------------|
| Access                     | **STGM\_READ**               | 0x00000000L |
|                            | **STGM\_WRITE**              | 0x00000001L |
|                            | **STGM\_READWRITE**          | 0x00000002L |
| Sharing                    | **STGM\_SHARE\_DENY\_NONE**  | 0x00000040L |
|                            | **STGM\_SHARE\_DENY\_READ**  | 0x00000030L |
|                            | **STGM\_SHARE\_DENY\_WRITE** | 0x00000020L |
|                            | **STGM\_SHARE\_EXCLUSIVE**   | 0x00000010L |
|                            | **STGM\_PRIORITY**           | 0x00040000L |
| Creation                   | **STGM\_CREATE**             | 0x00001000L |
|                            | **STGM\_CONVERT**            | 0x00020000L |
|                            | **STGM\_FAILIFTHERE**        | 0x00000000L |
| Transactioning             | **STGM\_DIRECT**             | 0x00000000L |
|                            | **STGM\_TRANSACTED**         | 0x00010000L |
| Transactioning Performance | **STGM\_NOSCRATCH**          | 0x00100000L |
|                            | **STGM\_NOSNAPSHOT**         | 0x00200000L |
| Direct SWMR and Simple     | **STGM\_SIMPLE**             | 0x08000000L |
|                            | **STGM\_DIRECT\_SWMR**       | 0x00400000L |
| Delete On Release          | **STGM\_DELETEONRELEASE**    | 0x04000000L |



 

<dl> <dt>

<span id="STGM_READ"></span><span id="stgm_read"></span>**STGM\_READ**
</dt> <dd> <dl> <dt>

0x00000000L
</dt> <dt>



Indicates that the object is read-only, meaning that modifications cannot be made. For example, if a stream object is opened with **STGM\_READ**, the [**ISequentialStream::Read**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-read) method may be called, but the [**ISequentialStream::Write**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-write) method may not. Similarly, if a storage object opened with **STGM\_READ**, the [**IStorage::OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream) and [**IStorage::OpenStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstorage) methods may be called, but the [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) and [**IStorage::CreateStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstorage) methods may not.


</dt> </dl> </dd> <dt>

<span id="STGM_WRITE"></span><span id="stgm_write"></span>**STGM\_WRITE**
</dt> <dd> <dl> <dt>

0x00000001L
</dt> <dt>



Enables you to save changes to the object, but does not permit access to its data. The provided implementations of the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) and [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interfaces do not support this write-only mode.


</dt> </dl> </dd> <dt>

<span id="STGM_READWRITE"></span><span id="stgm_readwrite"></span>**STGM\_READWRITE**
</dt> <dd> <dl> <dt>

0x00000002L
</dt> <dt>



Enables access and modification of object data. For example, if a stream object is created or opened in this mode, it is possible to call both [**IStream::Read**](/windows/desktop/api/Objidl/nn-objidl-istream) and **IStream::Write**. Be aware that this constant is not a simple binary **OR** operation of the **STGM\_WRITE** and **STGM\_READ** elements.


</dt> </dl> </dd> <dt>

<span id="STGM_SHARE_DENY_NONE"></span><span id="stgm_share_deny_none"></span>**STGM\_SHARE\_DENY\_NONE**
</dt> <dd> <dl> <dt>

0x00000040L
</dt> <dt>



Specifies that subsequent openings of the object are not denied read or write access. If no flag from the sharing group is specified, this flag is assumed.


</dt> </dl> </dd> <dt>

<span id="STGM_SHARE_DENY_READ"></span><span id="stgm_share_deny_read"></span>**STGM\_SHARE\_DENY\_READ**
</dt> <dd> <dl> <dt>

0x00000030L
</dt> <dt>



Prevents others from subsequently opening the object in **STGM\_READ** mode. It is typically used on a root storage object.


</dt> </dl> </dd> <dt>

<span id="STGM_SHARE_DENY_WRITE"></span><span id="stgm_share_deny_write"></span>**STGM\_SHARE\_DENY\_WRITE**
</dt> <dd> <dl> <dt>

0x00000020L
</dt> <dt>



Prevents others from subsequently opening the object for **STGM\_WRITE** or **STGM\_READWRITE** access. In transacted mode, sharing of **STGM\_SHARE\_DENY\_WRITE** or **STGM\_SHARE\_EXCLUSIVE** can significantly improve performance because they do not require snapshots. For more information about transactioning, see the Remarks section.


</dt> </dl> </dd> <dt>

<span id="STGM_SHARE_EXCLUSIVE"></span><span id="stgm_share_exclusive"></span>**STGM\_SHARE\_EXCLUSIVE**
</dt> <dd> <dl> <dt>

0x00000010L
</dt> <dt>



Prevents others from subsequently opening the object in any mode. Be aware that this value is not a simple bitwise **OR** operation of the **STGM\_SHARE\_DENY\_READ** and **STGM\_SHARE\_DENY\_WRITE** values. In transacted mode, sharing of **STGM\_SHARE\_DENY\_WRITE** or **STGM\_SHARE\_EXCLUSIVE** can significantly improve performance because they do not require snapshots. For more information about transactioning, see the Remarks section.


</dt> </dl> </dd> <dt>

<span id="STGM_PRIORITY"></span><span id="stgm_priority"></span>**STGM\_PRIORITY**
</dt> <dd> <dl> <dt>

0x00040000L
</dt> <dt>



Opens the storage object with exclusive access to the most recently committed version. Thus, other users cannot commit changes to the object while you have it open in priority mode. You gain performance benefits for copy operations, but you prevent others from committing changes. Limit the time that objects are open in priority mode. You must specify **STGM\_DIRECT** and **STGM\_READ** with priority mode, and you cannot specify **STGM\_DELETEONRELEASE**. **STGM\_DELETEONRELEASE** is only valid when creating a root object, such as with [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex). It is not valid when opening an existing root object, such as with [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex). It is also not valid when creating or opening a subelement, such as with [**IStorage::OpenStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstorage).


</dt> </dl> </dd> <dt>

<span id="STGM_CREATE"></span><span id="stgm_create"></span>**STGM\_CREATE**
</dt> <dd> <dl> <dt>

0x00001000L
</dt> <dt>



Indicates that an existing storage object or stream should be removed before the new object replaces it. A new object is created when this flag is specified only if the existing object has been successfully removed.

This flag is used when attempting to create:

-   A storage object on a disk, but a file of that name exists.
-   An object inside a storage object, but an object with the specified name exists.
-   A byte array object, but one with the specified name exists.

This flag cannot be used with open operations, such as [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) or [**IStorage::OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream).


</dt> </dl> </dd> <dt>

<span id="STGM_CONVERT"></span><span id="stgm_convert"></span>**STGM\_CONVERT**
</dt> <dd> <dl> <dt>

0x00020000L
</dt> <dt>



Creates the new object while preserving existing data in a stream named "Contents". In the case of a storage object or a byte array, the old data is formatted into a stream regardless of whether the existing file or byte array currently contains a layered storage object. This flag can only be used when creating a root storage object. It cannot be used within a storage object; for example, in [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream). It is also not valid to use this flag and the **STGM\_DELETEONRELEASE** flag simultaneously.


</dt> </dl> </dd> <dt>

<span id="STGM_FAILIFTHERE"></span><span id="stgm_failifthere"></span>**STGM\_FAILIFTHERE**
</dt> <dd> <dl> <dt>

0x00000000L
</dt> <dt>



Causes the create operation to fail if an existing object with the specified name exists. In this case, **STG\_E\_FILEALREADYEXISTS** is returned. This is the default creation mode; that is, if no other create flag is specified, **STGM\_FAILIFTHERE** is implied.


</dt> </dl> </dd> <dt>

<span id="STGM_DIRECT"></span><span id="stgm_direct"></span>**STGM\_DIRECT**
</dt> <dd> <dl> <dt>

0x00000000L
</dt> <dt>



Indicates that, in direct mode, each change to a storage or stream element is written as it occurs. This is the default if neither **STGM\_DIRECT** nor **STGM\_TRANSACTED** is specified.


</dt> </dl> </dd> <dt>

<span id="STGM_TRANSACTED"></span><span id="stgm_transacted"></span>**STGM\_TRANSACTED**
</dt> <dd> <dl> <dt>

0x00010000L
</dt> <dt>



Indicates that, in transacted mode, changes are buffered and written only if an explicit commit operation is called. To ignore the changes, call the [**Revert**](/windows/desktop/api/Objidl/nf-objidl-istream-revert) method in the [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream), [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage), or [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface. The COM compound file implementation of **IStorage** does not support transacted streams, which means that streams can be opened only in direct mode, and you cannot revert changes to them, however transacted storages are supported. The compound file, stand-alone, and NTFS file system implementations of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) similarly do not support transacted, simple property sets because these property sets are stored in streams. However, transactioning of nonsimple property sets, which can be created by specifying the **PROPSETFLAG\_NONSIMPLE** flag in the *grfFlags* parameter of [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create), are supported.


</dt> </dl> </dd> <dt>

<span id="STGM_NOSCRATCH"></span><span id="stgm_noscratch"></span>**STGM\_NOSCRATCH**
</dt> <dd> <dl> <dt>

0x00100000L
</dt> <dt>



Indicates that, in transacted mode, a temporary scratch file is usually used to save modifications until the **Commit** method is called. Specifying **STGM\_NOSCRATCH** permits the unused portion of the original file to be used as work space instead of creating a new file for that purpose. This does not affect the data in the original file, and in certain cases can result in improved performance. It is not valid to specify this flag without also specifying **STGM\_TRANSACTED**, and this flag may only be used in a root open. For more information about NoScratch mode, see the Remarks section.


</dt> </dl> </dd> <dt>

<span id="STGM_NOSNAPSHOT"></span><span id="stgm_nosnapshot"></span>**STGM\_NOSNAPSHOT**
</dt> <dd> <dl> <dt>

0x00200000L
</dt> <dt>



This flag is used when opening a storage object with **STGM\_TRANSACTED** and without **STGM\_SHARE\_EXCLUSIVE** or **STGM\_SHARE\_DENY\_WRITE**. In this case, specifying **STGM\_NOSNAPSHOT** prevents the system-provided implementation from creating a snapshot copy of the file. Instead, changes to the file are written to the end of the file. Unused space is not reclaimed unless consolidation is performed during the commit, and there is only one current writer on the file. When the file is opened in no snapshot mode, another open operation cannot be performed without specifying **STGM\_NOSNAPSHOT**. This flag may only be used in a root open operation. For more information about NoSnapshot mode, see the Remarks section.


</dt> </dl> </dd> <dt>

<span id="STGM_SIMPLE"></span><span id="stgm_simple"></span>**STGM\_SIMPLE**
</dt> <dd> <dl> <dt>

0x08000000L
</dt> <dt>



Provides a faster implementation of a compound file in a limited, but frequently used, case. For more information, see the Remarks section.


</dt> </dl> </dd> <dt>

<span id="STGM_DIRECT_SWMR"></span><span id="stgm_direct_swmr"></span>**STGM\_DIRECT\_SWMR**
</dt> <dd> <dl> <dt>

0x00400000L
</dt> <dt>



Supports direct mode for single-writer, multireader file operations. For more information, see the Remarks section.


</dt> </dl> </dd> <dt>

<span id="STGM_DELETEONRELEASE"></span><span id="stgm_deleteonrelease"></span>**STGM\_DELETEONRELEASE**
</dt> <dd> <dl> <dt>

0x04000000L
</dt> <dt>



Indicates that the underlying file is to be automatically destroyed when the root storage object is released. This feature is most useful for creating temporary files. This flag can only be used when creating a root object, such as with [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex). It is not valid when opening a root object, such as with [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex), or when creating or opening a subelement, such as with [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream). It is also not valid to use this flag and the STGM\_CONVERT flag simultaneously.


</dt> </dl> </dd> </dl>

## Remarks

You can combine these flags, but you can only choose one flag from each group of related flags. Typically one flag from each of the access and sharing groups must be specified for all functions and methods which use these constants. Flags from other groups are optional.

### Transacted Mode

When the **STGM\_DIRECT**flag is specified, only one of the following combination of flags may be specified from the access and sharing groups.

``` syntax
    STGM_READ      | STGM_SHARE_DENY_WRITE
```

``` syntax
    STGM_READWRITE | STGM_SHARE_EXCLUSIVE
```

``` syntax
    STGM_READ      | STGM_PRIORITY
```

Be aware that direct mode is implied by the absence of **STGM\_TRANSACTED**. That is, if neither **STGM\_DIRECT** nor **STGM\_TRANSACTED** is specified, **STGM\_DIRECT** is assumed.

When the **STGM\_TRANSACTED** flag is specified, objects are created or opened in transacted mode. In this mode, changes to an object do not persist until they are committed. For example, changes to a transacted storage object are not persisted until the [**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit) method is called. Changes to such a storage object will be lost if the storage object is released (final release) before the **Commit** method is called, or if the [**IStorage::Revert**](/windows/desktop/api/Objidl/nf-objidl-istorage-revert) method is called.

When an object is created or opened in transacted mode, the implementation must keep both the original data and updates to this data, so that updates can be reverted if necessary. This is typically performed by writing changes to a scratch area until they are committed, or by creating a copy, called a snapshot, of the most recently committed data.

When a root storage object is opened in transacted mode, the location and behavior of the scratch data and the snapshot copies can be controlled to optimize performance with the **STGM\_NOSCRATCH** and **STGM\_NOSNAPSHOT** flags. (A root storage object is obtained from, for example, the [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) function; a storage object obtained from the [**IStorage::OpenStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstorage) method is a substorage object.) Typically, the scratch data and snapshots are stored in temporary files, separate from the storage.

The effect of these flags depends on the number of readers and/or writers accessing the root storage.

In the "single-writer" case, a transacted mode storage object is opened for write access and there can be no other access to the file. That is, the file is opened with **STGM\_TRANSACTED**, access of **STGM\_WRITE** or **STGM\_READWRITE**, and sharing of **STGM\_SHARE\_EXCLUSIVE**. In this case, changes to the storage object are written to the scratch area. When those changes are committed, they are copied to the original storage. Therefore, if no changes are actually made to the storage object, there will be no unnecessary data transfer.

In the "multiple-writer" case, a transacted storage object is opened for write access, but is shared in such asway as to allow other writers. That is, the storage object is opened with **STGM\_TRANSACTED**, access of **STGM\_WRITE** or **STGM\_READWRITE**, and sharing of **STGM\_SHARE\_DENY\_READ**. If sharing of **STGM\_SHARE\_DENY\_NONE** is specified instead, then the case is "multiple-writer, multiple-reader". In these cases, a snapshot of the original data will be made during the open operation. Therefore, even if no changes are actually made to the storage and/or it is not actually opened by another writer simultaneously, data transfer is still necessary during the open. As a result the best open-time performance can be obtained by opening the storage object in **STGM\_SHARE\_DENY\_WRITE** or **STGM\_SHARE\_EXCLUSIVE** modes. For more information about how changes are committed when there are multiple writers, see [**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit).

In the "single-writer, multiple-reader" case, a transacted storage object is opened for write access, but is shared with readers. That is, the storage object is opened by the writer with **STGM\_TRANSACTED**, access of **STGM\_READWRITE** or **STGM\_WRITE**, and sharing of **STGM\_SHARE\_DENY\_WRITE**. The storage is opened by readers with **STGM\_TRANSACTED**, access of **STGM\_READ**, and sharing of **STGM\_SHARE\_DENY\_NONE**. In this case the writer uses the scratch area to store uncommitted changes. As in the cases above, the reader incurs an open-time performance penalty while a snapshot copy of the data is created.

Typically, the scratch area is a temporary file, separate from the original data. When changes are committed to the original file, the data must be transferred from the temporary file. To avoid this data transfer, the **STGM\_NOSCRATCH**flag may be specified. When this flag is specified, portions of the storage object file are used for the scratch area, rather than a separate temporary file. As a result, committing changes can be performed quickly, because little data transfer is required. The disadvantage is that the storage file can become larger than it would otherwise be, because it must be grown to be large enough for both the original data and the scratch area. To consolidate the data and remove this unnecessary area, reopen the root storage in transacted mode, but without setting the **STGM\_NOSCRATCH** flag. Then, call [**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit) with the **STGC\_CONSOLIDATE** flag set.

The snapshot area, like the scratch area, is also, typically, a temporary file, and this too can be affected with a STGM flag. By specifying the **STGM\_NOSNAPSHOT** flag, a separate temporary snapshot file is not created. Instead, the original data is never modified, even if there are one or more writers per object. When changes are committed, they are added to the file, but the original data remains intact. This mode increases efficiency because it reduces run time by eliminating the requirement of creating a snapshot during the open operation. However, using this mode may result in a very large storage file because data in the file can never be overwritten. This is no limit to the size of files opened in NoSnapshot mode.

### Direct Single-Writer, Multiple-Reader Mode

As described, it is possible to have a single writer and multiple readers of a storage object, if that object is opened in transacted mode. It is also possible to achieve the single-writer, multireader case in direct mode, by specifying the **STGM\_DIRECT\_SWMR** flag.

In **STGM\_DIRECT\_SWMR** mode, it is possible for one caller to open an object for read/write access, while other callers simultaneously have the file open for read-only access. It is not valid to use this flag in combination with the **STGM\_TRANSACTED** flag. In this mode, the writer opens the object with the following flags:

**STGM\_DIRECT\_SWMR** \| **STGM\_READWRITE** \| **STGM\_SHARE\_DENYWRITE**

and each of the readers opens the object with these flags:

**STGM\_DIRECT\_SWMR** \| **STGM\_READ** \| **STGM\_SHARE\_DENY\_NONE**

In this mode, to modify the storage object, the writer must get exclusive access to the object. This is possible when all the readers have closed it. The writer uses the [**IDirectWriterLock**](/windows/desktop/api/Objidl/nn-objidl-idirectwriterlock) interface to obtain this exclusive access.

### Simple Mode

Simple mode (**STGM\_SIMPLE**) is useful for applications that perform complete save operations. It is efficient, but has the following constraints:

-   No support exists for substorages.
-   The storage object, and stream objects obtained from it, cannot be marshaled.
-   Each stream has a minimum size. If fewer than the minimum bytes are written into a stream when the stream is released, the stream is extended to the minimum size. For example, the minimum size for a particular [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) implementation is 4 KB. A stream is created and 1 KB is written to it. At the final release of that **IStream**, the stream size will be automatically extended to 4 KB. Subsequently, opening the stream and calling the [**IStream::Stat**](/windows/desktop/api/Objidl/nf-objidl-istream-stat) method will show a size of 4 KB.
-   Not all methods of [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) or [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) will be supported by the implementation. For more information, see [IStorage - Compound File Implementation](istorage-compound-file-implementation.md), and [IStream - Compound File Implementation](istream-compound-file-implementation.md).

[Marshaling](/windows/desktop/Midl/marshaling-ole-data-types) is the process of packaging, unpackaging, and sending interface method parameters across thread or process boundaries within a Remote Procedure Call (RPC). For more information, see [Marshaling Details](../com/marshaling-details.md) and [Interface Marshaling](../com/interface-marshaling.md).

When a storage object is obtained by a Create operation in simple mode:

-   Stream elements can be created, but not opened.
-   When a stream element is created by calling [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream), it is not possible to create another stream until that stream object is released.
-   After all streams are written, call [**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit) to flush the changes.

When a storage object is obtained by an Open operation in simple mode:

-   It is possible to open only one stream element at a time.
-   It is not possible to change the size of a stream by calling the [**IStream::SetSize**](/windows/desktop/api/Objidl/nf-objidl-istream-setsize) method or by seeking or writing beyond the end of the stream. However, because all streams are of a minimum size, it is possible to use the stream up to that size, even if less data was originally written to it. To determine the size of a stream, use the [**IStream::Stat**](/windows/desktop/api/Objidl/nf-objidl-istream-stat) method.

Be aware that, if a storage element is modified by a storage object that is not in simple mode, it will not be possible, again, to open that storage element in simple mode.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ObjBase.h</dt> </dl> |



## See also

<dl> <dt>

[**ISequentialStream::Read**](/windows/desktop/api/Objidl/nf-objidl-isequentialstream-read)
</dt> <dt>

[**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage)
</dt> <dt>

[**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile)
</dt> <dt>

[**StgCreateDocfileOnILockBytes**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfileonilockbytes)
</dt> <dt>

[**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex)
</dt> <dt>

[**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage)
</dt> <dt>

[**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex)
</dt> <dt>

[**StgOpenStorageOnILockBytes**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageonilockbytes)
</dt> </dl>

 

