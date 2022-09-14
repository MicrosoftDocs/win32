---
description: Describes considerations for application control of file buffering, also known as unbuffered file input/output (I/O).
ms.assetid: ae1e5d0f-9b55-4aae-8402-b9c8e33d9363
title: File Buffering
ms.topic: article
ms.date: 05/31/2018
---

# File Buffering

This topic covers the various considerations for application control of file buffering, also known as unbuffered file input/output (I/O). File buffering is usually handled by the system behind the scenes and is considered part of [file caching](file-caching.md) within the Windows operating system unless otherwise specified. Although the terms *caching* and *buffering* are sometimes used interchangeably, this topic uses the term *buffering* specifically in the context of explaining how to interact with data that is not being cached (buffered) by the system, where it is otherwise largely out of the direct control of user-mode applications.

When opening or creating a file with the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function, the **FILE\_FLAG\_NO\_BUFFERING** flag can be specified to disable system caching of data being read from or written to the file. Although this gives complete and direct control over data I/O buffering, in the case of files and similar devices there are data alignment requirements that must be considered.

> [!Note]  
> This alignment information applies to I/O on devices such as files that support seeking and the concept of file position pointers (or *offsets*). For devices that do not seek, such as named pipes or communications devices, turning off buffering may not require any particular alignment. Any limitations or efficiencies that may be gained by alignment in that case are dependent on the underlying technology.

 

In a simple example, the application would open a file for write access with the **FILE\_FLAG\_NO\_BUFFERING** flag and then perform a call to the [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile) function using a data buffer defined within the application. This local buffer is, in these circumstances, effectively the only file buffer that exists for this operation. Because of physical disk layout, file system storage layout, and system-level file pointer position tracking, this write operation will fail unless the locally-defined data buffers meet certain alignment criteria, discussed in the following section.

> [!Note]  
> Discussion of caching does not consider any hardware caching on the physical disk itself, which is not guaranteed to be within the direct control of the system in any case. This has no effect on the requirements specified in this topic.

 

For more information on how **FILE\_FLAG\_NO\_BUFFERING** interacts with other cache-related flags, see [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea).

## Alignment and File Access Requirements

As previously discussed, an application must meet certain requirements when working with files opened with **FILE\_FLAG\_NO\_BUFFERING**. The following specifics apply:

-   File access sizes, including the optional file offset in the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure, if specified, must be for a number of bytes that is an integer multiple of the volume sector size. For example, if the sector size is 512 bytes, an application can request reads and writes of 512, 1,024, 1,536, or 2,048 bytes, but not of 335, 981, or 7,171 bytes.
-   File access buffer addresses for read and write operations should be physical sector-aligned, which means aligned on addresses in memory that are integer multiples of the volume's physical sector size. Depending on the disk, this requirement may not be enforced.

Application developers should take note of new types of storage devices being introduced into the market with a physical media sector size of 4,096 bytes. The industry name for these devices is "Advanced Format". As there may be compatibility issues with directly introducing 4,096 bytes as the unit of addressing for the media, a temporary compatibility solution is to introduce devices that emulate a regular 512-byte sector storage device but make available information about the true sector size through standard ATA and SCSI commands.

As a result of this emulation, there are in essence two sector sizes that developers will need to understand:

-   Logical Sector: The unit that is used for logical block addressing for the media. We can also think of it as the smallest unit of write that the storage can accept. This is the "emulation".
-   Physical Sector: The unit for which read and write operations to the device are completed in a single operation. This is the unit of atomic write, and what unbuffered I/O will need to be aligned to in order to have optimal performance and reliability characteristics.

Most current Windows APIs, such as [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_disk_get_drive_geometry) and [**GetDiskFreeSpace**](/windows/desktop/api/FileAPI/nf-fileapi-getdiskfreespacea), will return the logical sector size, but the physical sector size can be retrieved through the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_query_property) control code, with the relevant information contained in the **BytesPerPhysicalSector** member in the [**STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR**](/windows/desktop/api/WinIoCtl/ns-winioctl-storage_access_alignment_descriptor) structure. For an example, see the sample code at [**STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR**](/windows/desktop/api/WinIoCtl/ns-winioctl-storage_access_alignment_descriptor). Microsoft strongly recommends that developers align unbuffered I/O to the physical sector size as reported by the **IOCTL\_STORAGE\_QUERY\_PROPERTY** control code to help ensure their applications are prepared for this sector size transition.

**Windows Server 2003 and Windows XP:** The [**STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR**](/windows/desktop/api/WinIoCtl/ns-winioctl-storage_access_alignment_descriptor) structure is not available. It was introduced with Windows Vista and Windows Server 2008.

Because buffer addresses for read and write operations must be sector-aligned, the application must have direct control of how these buffers are allocated. One way to sector-align buffers is to use the [**VirtualAlloc**](/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc) function to allocate the buffers. Consider the following:

-   [**VirtualAlloc**](/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc) allocates memory that is aligned on addresses that are integer multiples of the system's page size. Page size is 4,096 bytes on x64 and x86 or 8,192 bytes for Itanium-based systems. For additional information, see the [**GetSystemInfo**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) function.
-   Sector size is typically 512 to 4,096 bytes for direct-access storage devices (hard drives) and 2,048 bytes for CD-ROMs.
-   Both page and sector sizes are powers of 2.

Therefore, in most situations, page-aligned memory will also be sector-aligned, because the case where the sector size is larger than the page size is rare.

Another way to obtain manually-aligned memory buffers is to use the [\_aligned\_malloc](/cpp/c-runtime-library/reference/aligned-malloc) function from the C Run-Time library. For an example of how to manually control buffer alignment, see the C++ language code example in the Example Code section of [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile).

 

 
