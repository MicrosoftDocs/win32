---
description: This topic introduces the effect of Advanced Format storage devices on software, discusses what applications can do to help support this type of media, and discusses the infrastructure that Microsoft introduced with Windows 7 SP1 and Windows Server 2008 R2 SP1 to enable developers to support these types of devices.
ms.assetid: 1D2847A7-15E9-42E0-90EB-7F43E76D3E44
title: 512-byte Emulation (512e) Disk Compatibility Update
ms.topic: article
ms.date: 05/31/2018
---

# 512-byte Emulation (512e) Disk Compatibility Update

## Platform

 **Clients** - Windows Vista, Windows 7, Windows 7 SP1  
**Servers** - Windows Server 2008, Windows Server 2008 R2, Windows Server 2008 R2 SP1  

## Feature Impact

**Severity** - High  
**Frequency** - High  









## Description

Areal densities are increasing yearly, and with the recent advent of 3 TB disks, the error correction mechanisms used to deal with the decreasing Signal-to-Noise-Ratio (SNR) are becoming space inefficient – that is, an increased amount of overhead is required to ensure the media is usable. One of the storage industry solutions for improving this error correction mechanism is to introduce a different physical media format that includes a larger physical sector size. This new physical media format is called *Advanced Format*. Therefore, it is no longer safe to make any assumptions regarding the sector size of modern storage devices, and developers will need to study the assumptions underlying their code to determine if there is an impact.

This topic introduces the effect of Advanced Format storage devices on software, discusses what applications can do to help support this type of media, and discusses the infrastructure to enable developers to support these types of devices. While the material presented in this topic provides guidelines for improving compatibility with Advanced Format disks, the information applies generally to all systems with Advanced Format disks. The following versions of Windows provide support for querying the physical sector size:

-   Windows 7 with Microsoft KB 982018
-   Windows 7 SP1
-   Windows Server 2008 R2 with Microsoft KB 982018
-   Windows Server 2008 R2 SP1
-   Windows Vista with Microsoft KB 2553708
-   Windows Server 2008 with Microsoft KB 2553708

For additional details, see [Information about Microsoft support policy for large-sector drives in Windows](https://support.microsoft.com/kb/2510009).

For more information about Advanced Format disks, please contact your storage vendor.

## Logical vs. Physical Sector Size

One of the concerns in introducing this change in the media format is compatibility with the software and hardware currently available in the market today. As a temporary solution, the storage industry is initially introducing disks that emulate a regular 512-byte sector disk, but make available information about the true sector size through standard ATA and SCSI commands. As a result of this emulation, there are two sector sizes:

-   **Logical Sector**: The unit that is used for logical block addressing for the media. We can also think of it as the smallest unit of write that the storage can accept. This is the emulation.

-   **Physical Sector**: The unit for which read and write operations to the device are completed in a single operation. This is the unit of atomic write.

Most current Windows APIs, such as **IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY** will return the logical sector size, but the physical sector size can be retrieved through the [IOCTL\_STORAGE\_QUERY\_PROPERTY](/windows-hardware/drivers/ddi/content/ntddstor/ni-ntddstor-ioctl_storage_query_property) control code, with the relevant information contained in the **BytesPerPhysicalSector** field in the [STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR](/windows/desktop/api/winioctl/ns-winioctl-storage_access_alignment_descriptor) structure. This is discussed in more detail later in the article.

## Initial Types of Large Sector Media

The storage industry is quickly ramping up efforts to transition to this new Advanced Format type of storage for media with 4 KB physical sector sizes. Two types of media will be released to the market:

-   **4 KB Native**: This media has no emulation layer and directly exposes 4 KB as its logical and physical sector size. This media is currently not supported by Windows and most other operating systems. However, Microsoft is conducting an investigation into the feasibility of supporting this type of media in a future version of Windows and will issue a Knowledge Base article when appropriate.
-   **512-byte Emulation (512e)**: This media has an emulation layer as discussed in the previous section and exposes 512-bytes as its logical sector size (similar to a regular disk today), but makes its physical sector size information (4 KB) available. This is what several storage vendors are currently introducing to the market. This overall issue with this new type of media is that the majority of application and operating systems do not understand the existence of the physical sector size, which can result in a number of issues as will be discussed below.

## How Emulation Works: Read-Modify-Write (RMW)

A storage medium has a certain unit within which the physical medium can be modified. That is, the media can only be written, or rewritten, in units of the physical sector size. Thus, writes that are not performed at this unit level would require additional steps, which we will walk through in the following example.

In this scenario, an application needs to update the contents of a Datastor record located within a 512-byte logical sector. The following diagram illustrates the steps necessary for the storage device to complete the write:

![steps needed to upgrade datastor record within a 512-byte logical sector](images/512ermwsteps.png)

As illustrated above, this process involves some work by the storage device that can result in a performance loss. To avoid this additional work, applications must be updated to do the following:

-   Query for the physical sector size.
-   Ensure writes are aligned to that reported physical sector size.

## The Resiliency Impact of Read-Modify-Write

Resiliency speaks of the ability for an application to recover state between sessions. We have seen what is necessary for a 512e storage device to perform a 512-byte sector write – the Read-Modify-Write cycle. Let’s look at what would happen if the process of overwriting the previous physical sector on the media was interrupted. What would be the consequences?

-   Because most hard disk drives update in place, the physical sector – that is, the portion of the media where the physical sector was located – could have been corrupted with incomplete information due to a partial overwrite. Put another way, you can think of it as potentially having lost all 8 logical sectors (which the physical sector logically contains).

-   While most applications with a data store are designed with the capability to recover from media errors, the loss of eight sectors, or put another way, the loss of eight commit records, can potentially make it impossible for the data store to recover gracefully. An administrator may need to manually restore the database from a backup or may even need to perform a lengthy rebuild.

-   One more important impact is that the act of another application causing a Read-Modify-Write cycle can potentially cause your data to be lost – even if your application is not running! This is simply because your data and the other application’s data could be located within the same physical sector.

With this in mind, it is important that application software reevaluate any assumptions taken in the code, and be aware of the logical-physical sector size distinction, along with some interesting customer scenarios discussed later in this article.

This issue is more likely to occur if your application relies on a log structure data store.

## Avoiding Read-Modify-Write

While some storage vendors may be introducing some levels of mitigation within certain 512e storage devices to try and help ease the performance and resiliency issues of the Read-Modify-Write cycle, there is only so much any mitigation can handle in terms of workload. As such, applications should not rely on this mitigation as a long-term solution.

The solution to this is not in-drive mitigation, but to have applications do the right set of things to avoid the Read-Modify-Write cycle. This section discusses common scenarios where applications may have issues with large sector disks, and suggests an avenue of investigation to try and resolve each issue.

### Issue 1: The partition is not aligned to a physical sector boundary

When the administrator/user partitions the disk, the first partition may not have been created on an aligned boundary. This may cause all subsequent writes to become unaligned to physical sector boundaries. As of Windows Vista SP1, and Windows Server 2008, the first partition is placed at the first 1024 KB of the disk (for disks 4GB or larger, otherwise the alignment is 64 KB) that is aligned to a 4 KB physical sector boundary. However, given the default partitioning in Windows XP, a 3rd party partitioning utility or incorrect usage of Windows APIs, created partitions may not be aligned to a physical sector boundary. Developers will need to ensure that the correct APIs are used to help ensure alignment. The recommended APIs to help ensure partition alignment are outlined below.

The **IVdsPack::CreateVolume** and **IVdsPack2::CreateVolume2** APIs do not use the specified alignment parameter when a new volume is created, and instead use the alignment value default for the operating system (Pre-Windows Vista SP1 will use 63 bytes, and post Windows Vista SP1 will use the defaults stated above). Thus, it is recommended that applications that need to create partitions use the **IVdsCreatePartitionEx::CreatePartitionEx** or **IVdsAdvancedDisk::CreatePartition** APIs instead, which use the specified alignment parameter.

The best way to help ensure that alignment is correct is to do it right when initially creating the partition. Otherwise your application will need to take alignment into account when performing writes or at initialization – which can be a very complex matter. As of Windows Vista SP1, this is generally not an issue; however, older versions of Windows can create unaligned partitions that can potentially lead to performance issues with some Advanced Format disks.

### Issue 2: Unbuffered Writes not aligned to Physical Sector Size

The basic issue is that unbuffered writes are not aligned to the reported physical sector size of the storage media, which triggers a Read-Modify-Write in the drive that can result in performance issues. Buffered writes, on the other hand, are aligned to the page size – 4 KB – which coincidently is the physical sector size of the first generation of large sector media. However, most applications with a data store perform unbuffered writes, and thus will need to ensure these writes are performed in units of the physical sector size.

To help determine if your application issues unbuffered I/O, check to see that you include the **FILE\_FLAG\_NO\_BUFFERING** flag in the *dwFlagsAndAttributes* parameter when you are calling the **CreateFile** function.

Moreover, if you are currently aligning the writes to the sector size, this sector size is most likely just the *logical* sector size, as most existing APIs that query for the sector size of the media really just query the unit of addressing – that is, the logical sector size. The sector size of interest here is the physical sector size, which is the real unit of atomicity. Some examples of APIs that retrieve the logical sector size are:

-   **GetDiskFreeSpace**, **GetDiskFreeSpaceEx**
-   **FileFsVolumeInformation**
-   **IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY**, **IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX**
-   **IVdsDisk::GetProperties**, **IVdsDisk3::GetProperties2**

**How to Query for the Physical Sector Size**

Microsoft has provided a code sample on MSDN detailing how an application can query for the physical sector size of the volume. The code sample is located at <https://msdn.microsoft.com/library/ff800831.aspx>.

While the code sample above allows you to get the physical sector size of the volume, you should do some basic sanity checking on the reported physical sector size before using it, as it has been observed that some drivers may not return correctly formatted data:

-   Make sure that the reported physical sector size is >= the reported logical sector size. If it is not, your application should use a physical sector size equal to the reported logical sector size.
-   Make sure that the reported physical sector size is a power of two. If it is not, your application should use a physical sector size equal to the reported logical sector size.
-   If the physical sector size is a power-of-two value between 512-bytes and 4 KB, you should consider using a physical sector size rounded down to the reported logical sector size.
-   If the physical sector size is a power-of-two value greater than 4 KB, you should evaluate your application’s ability to handle this scenario before using that value. Otherwise, you should consider using a physical sector size rounded down to 4 KB.

Using this IOCTL to get the physical sector size does have several limitations:

-   Requires elevated privilege. If your application is not running with privilege, you may need to write a Windows Service Application as noted above.

-   Does not support SMB volumes. You may also need to write a Windows Service Application to support physical sector size querying on these volumes.

-   Cannot be issued to any file handle (the IOCTL must be issued to a Volume Handle).

-   Supported only in Windows versions listed near the beginning of this article.

**Commit records are padded to 512-byte sectors**

Applications with a data store typically have some form of commit record that either maintains information about metadata changes or maintains the structure of the data store. In order to ensure that the loss of a sector does not affect multiple records, this commit record is typically padded out to a sector size. With a disk with a larger physical sector size, the application will need to query for the physical sector size as shown in the prior section, and ensure each commit record is padded to that size. Not only does this avoid the Read-Modify-Write cycle, it helps ensure that in case a physical sector was lost, only one Commit Record would be lost.

**Log files are written to in unaligned chunks**

Unbuffered I/O is typically used when updating or appending to a log file. There are several ways to help ensure these updates are correctly aligned:

-   Internally buffer log updates to the reported physical sector size of the operating media, and issue log writes only when a physical sector unit is full
-   Use buffered I/O

### Issue 3: File Formats relying on 512-byte Sectors

Some applications with standard file formats (such as VHD 1.0) may have these files hard-coded to assume a 512-byte sector size. Thus, updates and writes to this file would result in a Read-Modify-Write cycle on the device– which will potentially result in performance and resiliency concerns for your customers. However, there are ways for an application to provide support for operating on this type of media, for example:

-   Use buffering to ensure that writes are performed in units of the physical sector size
-   Implement an internal Read-Modify-Write that can help ensure that updates are performed in units of the reported physical sector size
-   If possible, pad records out to a physical sector, in such a way that the padding would be interpreted as empty space
-   Consider redesigning a new version of the application data structure with support for larger sectors

### Issue 4: The reported Physical Sector size can change between sessions

There are many scenarios where the reported physical sector size of the underlying storage that hosts the Datastor may change. The most common of these is when you migrate the Datastor to another volume, or even across the network. A change in the reported physical sector size may be an unexpected event for many applications and can potentially result in some applications even failing to re-initialize.

This is not the easiest scenario to support, and is mentioned here as an advisory. You should consider the mobility requirements of your customers and adjust your support accordingly to help ensure customers are not negatively impacted by using 512e media.

## 4 KB Native Media

512-byte emulation media is meant as a transitional step between 512-byte native and 4 KB-native media, and we expect to see 4 KB-native media released soon after 512e is available. There are several important implications with this media which should be noted:

-   The logical and physical sector sizes are both 4 KB
-   Because there is no emulation layer, unaligned writes will be failed by the storage
-   No hidden resiliency hit – applications either work or they don’t work

Although Microsoft is currently investigating support for these types of media in a future version of Windows and will issue a KB article when appropriate, application developers should consider preemptively providing support for these types of media.

## Closing

In this article we have discussed the affects that large sector media introduces with many common deployment scenarios. We have seen the performance and resiliency impact of Read-Modify-Write, some of the interesting scenarios that this media can introduce, and the set of issues they can potentially cause with software, which ultimately affects the end-user. The storage industry is rapidly transitioning to media with larger sector sizes, and very soon customers will not be able to purchase disks with traditional 512-byte sector sizes.

This is a living document, and is meant as an aid for developers to help understand this transition. You should start a conversation with your respective organizations, with customers, IT Pros, and your hardware vendors to talk about the large sector transition and how it affects the scenarios that are important to you.

## Links to Other Resources

-   **Windows General Support Statement**: <https://support.microsoft.com/kb/2510009>
-   **Hotfix for Windows 7 and Windows Server 2008 R2**: <https://support.microsoft.com/kb/982018>
-   **HyperV Support Statement**: <https://support.microsoft.com/kb/2515143>
-   **General information about the IOCTL\_STORAGE\_QUERY\_PROPERTY control code**: [https://msdn.microsoft.com/library/ff560590.aspx](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property)
-   **IOCTL\_STORAGE\_QUERY\_PROPERTY Control Code**: [https://msdn.microsoft.com/library/ff800830.aspx](/windows/win32/api/winioctl/ni-winioctl-ioctl_storage_query_property)
-   **General information about the STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR structure**: [https://msdn.microsoft.com/library/ff566344.aspx](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_access_alignment_descriptor)
-   **Description of the standard terminology used to describe Microsoft software updates**: <https://support.microsoft.com/kb/824684/>
-   **WDK sample code** with details for how to extract the reported storage access alignment information from the **STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR** structure when making a call to the **IOCTL\_STORAGE\_QUERY\_PROPERTY** control code: [/windows/desktop/api/winioctl/ns-winioctl-storage_access_alignment_descriptor](/windows/desktop/api/winioctl/ns-winioctl-storage_access_alignment_descriptor)
-   **General information about ImageX Command-Line Options**: <https://technet.microsoft.com/library/dd799302(WS.10).aspx>
-   **Intel Chipset driver requirements to support 4 KB Sector Drives**: <https://www.intel.com/support/chipsets/imsm/sb/CS-031502.htm>
-   For more information on Advanced Format Disks, visit the following IDEMA websites:
    -   <http://idema.org/?page_id=2172>
    -   <http://idema.org/?download=7926>

 

 
