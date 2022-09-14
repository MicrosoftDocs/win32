---
title: New API allows apps to send "TRIM and Unmap" hints to storage media
description: New API allows apps to send \ 0034;TRIM and Unmap \ 0034; hints to storage media
ms.assetid: DDBC3592-BD4D-4826-83FE-387564DA07E8
ms.topic: article
ms.date: 05/31/2018
---

# New API allows apps to send "TRIM and Unmap" hints to storage media

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

TRIM hints notify the drive that certain sectors that previously were allocated are no longer needed by the app and can be purged. This is typically used when an app makes large space allocations via a file and then self-manages the allocations to the file (for example, Virtual Hard Disk files).

**What is TRIM?**

Solid state drives (SSDs) are typically flash memory based block-erased devices; this means that when data is written to the SSD, it cannot be over-written in place and must be written elsewhere until the block can be garbage collected. Since the SSD has no internal mechanism for determining that certain blocks are removed and others are needed. The only time the SSD can mark a sector ‘dirty’ is when it is over-written. In other cases, such as when a file is deleted, the SSD retains these sectors because the deletion is performed as a master file table (MFT) change only, and not as an operation to all the sectors of the file. In Windows 7, we introduced a standard way of communicating with SSDs about sectors that are not needed any more. This command is defined in the T13 specification as the TRIM command; NTFS sends the TRIM command for some normal inline operations such as “deletefile.”

**Other uses of TRIM in the storage world**

Like SSDs, storage area networks (SANs) and the new Windows 8 feature Software Spaces implementations consume TRIM command hints to manage their spaces in thinly provisioned environments. SANs and Software Spaces allocate regions of storage in sizes that are greater than sectors or clusters (anywhere from 1MB to 1GB). When they receive TRIM hints for its allocation size (or greater than the allocation size), the SAN/SSD can de-allocate a region to free up the space for other files. They typically pass through all TRIM hints to the underlying media (SSD or HDD) so that they can consume the freed up space as appropriate. They do not typically move data around to de-allocate regions, nor do they keep track of TRIM areas to de-allocated regions (when the region is empty).

Thinly provisioned SANs use the TRIM hints that are passed to them to help reduce the overall physical storage footprint, hence reducing cost. The [T10 SCSI specification](https://www.t10.org) defines the ‘Unmap’ command (similar to the TRIM command); here the command is applicable to all kinds of storage including HDDs, SSDs, and others. The UnMap command helps to remove physical blocks from the SAN’s allocation.

## How to use the new API


```
#define FSCTL_FILE_LEVEL_TRIM CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 130, METHOD_BUFFERED, FILE_WRITE_DATA)

Where 
typedef struct _EXTENT_PAIR {
    ULONGLONG Offset;
    ULONGLONG Length;
} EXTENT_PAIR, *PEXTENT_PAIR;

typedef struct _FILE_LEVEL_TRIM {
    //
    // A count of how many Offset:Length pairs are given
    //
    DWORD PairCount;
    //
    // All the pairs.
    //
    EXTENT_PAIR Pairs[1];
} FILE_LEVEL_TRIM, *PFILE_LEVEL_TRIM;
```



File TRIM is passed via the buffer if possible or asynchronously (non-buffered) to the Device IOCTL DSM command TRIM. This is mapped to the TRIM command for ATA devices and UnMap command for SCSI devices. The file TRIM code sends the regions one-by-one as specified by the extents above.

File TRIM does not wait for returns from the device, because the TRIM and Unmap commands are defined as hints to the underlying storage media and return codes are not expected.

**End-to-end workflow:**

1.  Call File Trim
    1.  File TRIM examines inputs for errors
    2.  File TRIM breaks up the extents into LCN regions
    3.  File TRIM rounds up and down for mis-aligned regions that are passed into TRIM
    4.  File TRIM purges entries in the cache that relate to the TRIM areas
    5.  File TRIM passes IOCTL\_DSM (Trim) per region
2.  File TRIM returns or errors
    1.  Error checking is done on input validity
    2.  If only some of the extents are valid, one error is returned for the complete API call

**Use cases**

**Consumer virtual hard disk (VHD) mounted on an SSD:**

The VHD is initially mounted on ‘clean’ unused media. As the VHD is used, the VHD consumes parts of the storage media for files, etc. When it deletes files in the storage media, these files are not removed from the SSD since the complete VHD is stored as one file on the SSD. The Hyper-V environment calls File TRIM for all regions that are deleted when delete-file occurs in the VHD environment. The File\_TRIMs are translated to the SSD so that the SSD performance can be optimized.

**Consumer VHD mounted on a thinly provisioned SAN:**

The VHD is initially mounted on one minimum slab of a thinly provisioned environment. As files are stored in the VHD, the storage footprint of the VHD grows in multiples of slabs. When files are removed in the VHD, the Hyper-V calls File\_TRIM to the underlying thinly provisioned SAN. If the TRIMs are bigger than the SLAB granularity, the SAN can now remove a SLAB and hence reduce the footprint of the VHD on that SAN.

If the VHD is resident on a Windows 8 based server, the Storage Optimizer will also send TRIMs to reduce the slab footprint of the VHD from within the mounted VHD.

## Tests

There are no comparable APIs in earlier operating system releases. There should be no performance impact from the actual API itself, though the storage media (if implemented correctly) can show better write performance. The API should be used very carefully; only extents that are no longer needed should be passed down as those extents will be permanently removed from the storage media.

## Resources

-   [T13 specification](https://www.t13.org/standards-published)
-   [T10 SCSI specification](https://www.t10.org/)

 

 




