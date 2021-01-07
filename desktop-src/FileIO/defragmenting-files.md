---
description: Defragmentation is the process of moving portions of files around on a disk to defragment files, that is, the process of moving file clusters on a disk to make them contiguous.
ms.assetid: 27ccaab7-ec89-489b-80dc-df9beb7969bc
title: Defragmenting Files
ms.topic: article
ms.date: 05/31/2018
---

# Defragmenting Files

When a file is written to a disk, sometimes the file cannot be written in contiguous clusters. Noncontiguous clusters slow down the process of reading and writing a file. The further apart on a disk the noncontiguous clusters are, the worse the issue, because of the time it takes to move the read/write head of a hard disk drive. A file with noncontiguous clusters is *fragmented*. To optimize files for fast access, a volume can be defragmented.

*Defragmentation* is the process of moving portions of files around on a disk to defragment files, that is, the process of moving file clusters on a disk to make them contiguous. For more information, see the following sections:

-   [Defragmenting a file](#defragmenting-a-file)
-   [Minimizing interactions between defragmentation and shadow copies](#minimizing-interactions-between-defragmentation-and-shadow-copies)
-   [Files, streams, and stream types supported for defragmentation](#files-streams-and-stream-types-supported-for-defragmentation)

## Defragmenting a file

In a simple single-tasking operating system, the defragmentation software is the only task, and there are no other processes to read from or write to the disk. However, in a multitasking operating system, some processes can be reading from and writing to a hard disk drive while another process is defragmenting that hard disk drive. The trick is to avoid writes to a file that is being defragmented without stopping the writing process for very long. Solving this problem is not trivial, but it is possible.

To allow defragmentation without requiring detailed knowledge of a file system disk structure, a set of three control codes is provided. The control codes provide the following functionality:

-   Enable applications to locate empty clusters
-   Determine the disk location of file clusters
-   Move clusters on a disk

The control codes also transparently handle the problem of inhibiting and allowing other processes to read from and write to files during moves.

These operations can be performed without inhibiting other processes from running. However, the other processes have slower response times while a disk drive is being defragmented.

**To defragment a file**

1.  Use the [**FSCTL\_GET\_VOLUME\_BITMAP**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_volume_bitmap) control code to find a place on the volume that is large enough to accept an entire file.
    > [!Note]  
    > If necessary, move other files to make a place that is large enough. Ideally, there is enough unallocated clusters after the first extent of the file that you can move subsequent extents into the space after the first extent.

     

2.  Use the [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers) control code to get a map of the current layout of the file on the disk.
3.  Walk the [**RETRIEVAL\_POINTERS\_BUFFER**](/windows/desktop/api/WinIoCtl/ns-winioctl-retrieval_pointers_buffer) structure returned by [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers).
4.  Use the [**FSCTL\_MOVE\_FILE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_move_file) control code to move each cluster as you walk the structure.
    > [!Note]  
    > You may need to renew either the bitmap or the retrieval structure, or both at various times as other processes write to the disk.

     

Two of the operations that are used in the defragmentation process require a handle to a volume. Only administrators can obtain a handle to a volume, so only administrators can defragment a volume. An application should check the rights of a user who attempts to run defragmentation software, and it should not allow a user to defragment a volume if the user does not have the appropriate rights.

When using [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) to open a directory during defragmentation of a FAT or FAT32 file system volume, specify the **GENERIC\_READ** access mask value. Do not specify the **MAXIMUM\_ALLOWED** access mask value. Access to the directory is denied if that is done.

Do not attempt to move allocated clusters in an NTFS file system that extend beyond the cluster rounded file size, because the result is an error.

Re-parse points, bitmaps, and attribute lists in NTFS file system volumes can be defragmented, opened for reading and synchronization, and named using the *file*:*name*:*type* syntax; for example, *dirname*:$i30:$INDEX\_ALLOCATION, *mrp*::$DATA, *mrp*::$REPARSE\_POINT, and *mrp*::$ATTRIBUTE\_LIST.

When defragmenting NTFS file system volumes, defragmenting a virtual cluster beyond the allocation size of a file is allowed.

## Minimizing interactions between defragmentation and shadow copies

When possible, move data in blocks aligned relative to each other in 16-kilobyte (KB) increments. This reduces copy-on-write overhead when shadow copies are enabled, because shadow copy space is increased and performance is reduced when the following conditions occur:

-   The move request block size is less than or equal to 16 KB.
-   The move delta is not in increments of 16 KB.

The move delta is the number of bytes between the start of the source block and the start of the target block. In other words, a block starting at offset X (on-disk) can be moved to a starting offset Y if the absolute value of X minus Y is an even multiple of 16 KB. So, assuming 4-KB clusters, a move from cluster 3 to cluster 27 will be optimized, but a move from cluster 18 to cluster 24 will not. Note that mod(3,4) = 3 = mod(27,4). Mod 4 is chosen because four clusters at 4 KB each is equivalent to 16 KB. Therefore, a volume formatted to a 16-KB cluster size will result in all move files being optimized.

For more information about shadow copies, see [Volume Shadow Copy Service](/windows/desktop/VSS/about-the-volume-shadow-copy-service).

## Files, streams, and stream types supported for defragmentation

While most files can be moved using the [**FSCTL\_MOVE\_FILE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_move_file) control code, not all can be moved. Below is the list of files, streams, and stream types (also called attribute type codes) supported by **FSCTL\_MOVE\_FILE**. Other files, streams, and stream types are not supported by **FSCTL\_MOVE\_FILE**.

Stream types supported for any file or directory.

-   ::$DATA
-   ::$ATTRIBUTE\_LIST
-   ::$REPARSE\_POINT
-   ::$EA
-   ::$LOGGED\_UTILITY\_STREAM

**Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:  **::$EA and ::$LOGGED\_UTILITY\_STREAM are not supported before Windows 8 and Windows Server 2012

Stream types supported for any directory.

-   ::$BITMAP
-   ::$INDEX\_ALLOCATION

Following are the system file, stream, and stream types supported by [**FSCTL\_MOVE\_FILE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_move_file) in "*filename*:*streamname*:$*typename*" format.

-   $MFT::$DATA
-   $MFT::$ATTRIBUTE\_LIST
-   $MFT::$BITMAP
-   $AttrDef::$DATA
-   $AttrDef::$ATTRIBUTE\_LIST
-   $Secure:$SDS:$DATA
-   $Secure::$ATTRIBUTE\_LIST
-   $Secure:$SDH:$INDEX\_ALLOCATION
-   $Secure:$SDH:$BITMAP
-   $Secure:$SII:$INDEX\_ALLOCATION
-   $Secure:$SII:$BITMAP
-   $UpCase::$DATA
-   $UpCase::$ATTRIBUTE\_LIST
-   $Extend:$I30:$INDEX\_ALLOCATION
-   $Extend::$ATTRIBUTE\_LIST
-   $Extend:$I30:$BITMAP
-   $Extend\\$UsnJrnl:$J:$DATA
-   $Extend\\$UsnJrnl::$ATTRIBUTE\_LIST
-   $Extend\\$UsnJrnl:$Max:$DATA
-   $Extend\\$Quota:$Q:$INDEX\_ALLOCATION
-   $Extend\\$Quota::$ATTRIBUTE\_LIST
-   $Extend\\$Quota:$Q:$BITMAP
-   $Extend\\$Quota:$O:$INDEX\_ALLOCATION
-   $Extend\\$Quota:$O:$BITMAP
-   $Extend\\$ObjId:$O:$INDEX\_ALLOCATION
-   $Extend\\$ObjId::$ATTRIBUTE\_LIST
-   $Extend\\$ObjId:$O:$BITMAP
-   $Extend\\$Reparse:$R:$INDEX\_ALLOCATION
-   $Extend\\$Reparse::$ATTRIBUTE\_LIST
-   $Extend\\$Reparse:$R:$BITMAP
-   $Extend\\$RmMetadata:$I30:$INDEX\_ALLOCATION
-   $Extend\\$RmMetadata:$I30:$BITMAP
-   $Extend\\$RmMetadata::$ATTRIBUTE\_LIST
-   $Extend\\$RmMetadata\\$Repair::$DATA
-   $Extend\\$RmMetadata\\$Repair::$ATTRIBUTE\_LIST
-   $Extend\\$RmMetadata\\$Repair:$Config:$DATA
-   $Extend\\$RmMetadata\\$Txf:$I30:$INDEX\_ALLOCATION
-   $Extend\\$RmMetadata\\$Txf::$ATTRIBUTE\_LIST
-   $Extend\\$RmMetadata\\$Txf:$I30:$BITMAP
-   $Extend\\$RmMetadata\\$Txf:$TXF\_DATA:$LOGGED\_UTILITY\_STREAM
-   $Extend\\$RmMetadata\\$TxfLog:$I30:$INDEX\_ALLOCATION
-   $Extend\\$RmMetadata\\$TxfLog::$ATTRIBUTE\_LIST
-   $Extend\\$RmMetadata\\$TxfLog:$I30:$BITMAP
-   $Extend\\$RmMetadata\\$TxfLog\\$Tops::$DATA
-   $Extend\\$RmMetadata\\$TxfLog\\$Tops::$ATTRIBUTE\_LIST
-   $Extend\\$RmMetadata\\$TxfLog\\$Tops:$T:$DATA
-   $Extend\\$RmMetadata\\$TxfLog\\$TxfLog.blf::$DATA
-   $Extend\\$RmMetadata\\$TxfLog\\$TxfLog.blf::$ATTRIBUTE\_LIST

 

 
