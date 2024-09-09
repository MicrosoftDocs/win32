---
description: Tables that list functionality and feature support comparisons for the four main Windows file systems, NTFS, exFAT, UDF, and FAT32.
ms.assetid: 28cf2805-f1ce-46b4-bf08-a329f67f4d99
title: File System Functionality Comparison
ms.topic: article
ms.date: 05/31/2018
---

# File System Functionality Comparison

The following tables list functionality and feature support comparisons for the four main Windows file systems, NTFS, exFAT, UDF, and FAT32:

-   [Functionality](#file-system-functionality-comparison)
-   [Limits](#limits)
-   [Journaling and Change Log](#journaling-and-change-log)
-   [Block Allocation Features](#block-allocation-features)
-   [Security](#security)
-   [Compression](#compression)
-   [Quotas](#quotas)
-   [Single-Instance Store](#single-instance-store)
-   [Related topics](#related-topics)

## Functionality



| Feature                             | NTFS                           | exFAT          | UDF                           | FAT32                      |
|-------------------------------------|--------------------------------|----------------|-------------------------------|----------------------------|
| Creation time stamps<br/>     | Yes<br/>                 | Yes<br/> | Yes<br/>                | Yes<br/>             |
| Last access time stamps<br/>  | No (see note below)<br/> | Yes<br/> | Yes<br/>                | Yes (date only)<br/> |
| Last change time stamps<br/>  | Yes<br/>                 | Yes<br/> | Yes<br/>                | Yes<br/>             |
| Last archive time stamps<br/> | No<br/>                  | No<br/>  | No<br/>                 | No<br/>              |
| Case-sensitive<br/>           | Yes (option)<br/>        | No<br/>  | Yes<br/>                | No<br/>              |
| Case-preserving<br/>          | Yes<br/>                 | Yes<br/> | Yes<br/>                | Yes<br/>             |
| Hard links<br/>               | Yes<br/>                 | No<br/>  | Yes<br/>                | No<br/>              |
| Soft links<br/>               | Yes<br/>                 | No<br/>  | No<br/>                 | No<br/>              |
| Sparse files<br/>             | Yes<br/>                 | No<br/>  | Yes<br/>                | No<br/>              |
| Named streams<br/>            | Yes<br/>                 | No<br/>  | Yes<br/>                | No<br/>              |
| Oplocks<br/>                  | Yes<br/>                 | Yes<br/> | Yes<br/>                | Yes<br/>             |
| Extended attributes<br/>      | Yes<br/>                 | No<br/>  | Yes (on-disk only)<br/> | No<br/>              |
| Alternate data streams<br/>   | Yes<br/>                 | No<br/>  | Yes<br/>                | No<br/>              |
| Mount points<br/>             | Yes<br/>                 | No<br/>  | No<br/>                 | No<br/>              |



 

**Windows Server 2003 and Windows XP:** The NTFS last access time stamp field is updated.

## Limits



| Feature                             | NTFS                                                                                      | exFAT                                                                                     | UDF                                                                                       | FAT32                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Maximum file name length<br/> | 255 Unicode characters<br/>                                                         | 255 Unicode characters<br/>                                                         | 127 Unicode or 254 ASCII characters<br/>                                            | 255 Unicode characters<br/>                                                         |
| Maximum path name length<br/> | 32,760 Unicode characters with each path component no more than 255 characters<br/> | 32,760 Unicode characters with each path component no more than 255 characters<br/> | 32,760 Unicode characters with each path component no more than 255 characters<br/> | 32,760 Unicode characters with each path component no more than 255 characters<br/> |
| Maximum file size<br/>        | 2^64–1 bytes<br/>                                                                   | 2^64–1 bytes<br/>                                                                   | 2^64–1 bytes<br/>                                                                   | 4 GiB<br/>                                                                          |
| Maximum volume size<br/>      | 16 TB (4 KB Cluster Size) or 256TB (64 KB Cluster Size)<br/>                        | 2^32–1 clusters (Maximum cluster size = 2^25–1)<br/>                               | 2^32 blocks<br/>                                                                    | 2^32 blocks<br/>                                                                    |



 

## Journaling and Change Log



| Feature                             | NTFS           | exFAT         | UDF           | FAT32         |
|-------------------------------------|----------------|---------------|---------------|---------------|
| Metadata-only journaling<br/> | Yes<br/> | No<br/> | No<br/> | No<br/> |
| File change log<br/>          | Yes<br/> | No<br/> | No<br/> | No<br/> |



 

## Block Allocation Features



| Feature                        | NTFS                                                                        | exFAT         | UDF            | FAT32         |
|--------------------------------|-----------------------------------------------------------------------------|---------------|----------------|---------------|
| Tail packing<br/>        | Yes (small files are made resident in the MFT stream descriptor)<br/> | No<br/> | No<br/>  | No<br/> |
| Extents<br/>             | Yes<br/>                                                              | No<br/> | Yes<br/> | No<br/> |
| Variable block size<br/> | No (set by the volume)<br/>                                           | No<br/> | No<br/>  | No<br/> |



 

## Security



| Feature                                  | NTFS                                                 | exFAT               | UDF                 | FAT32         |
|------------------------------------------|------------------------------------------------------|---------------------|---------------------|---------------|
| Track file owner<br/>              | Yes<br/>                                       | No<br/>       | No<br/>       | No<br/> |
| POSIX file permissions<br/>        | No (available in POSIX subsystem feature)<br/> | No<br/>       | Yes<br/>      | No<br/> |
| Access control lists<br/>          | Yes<br/>                                       | No<br/>       | No<br/>       | No<br/> |
| File system  level encryption<br/> | Yes<br/>                                       | No<br/>       | No<br/>       | No<br/> |
| Checksum/ECC<br/>                  | No<br/>                                        | Metadata<br/> | Metadata<br/> | No<br/> |



 

## Compression



| Feature                         | NTFS           | exFAT         | UDF           | FAT32         |
|---------------------------------|----------------|---------------|---------------|---------------|
| Built-in compression<br/> | Yes<br/> | No<br/> | No<br/> | No<br/> |



 

## Quotas



| Feature                               | NTFS                           | exFAT         | UDF           | FAT32         |
|---------------------------------------|--------------------------------|---------------|---------------|---------------|
| User-level disk space<br/>      | Yes<br/>                 | No<br/> | No<br/> | No<br/> |
| Directory-level disk space<br/> | No (see note below)<br/> | No<br/> | No<br/> | No<br/> |



 

**Note**  The directory-level disk space quotas feature on NTFS is available through the File Server Resource Manager.

## Single-Instance Store



| Feature               | NTFS                           | exFAT         | UDF           | FAT32         |
|-----------------------|--------------------------------|---------------|---------------|---------------|
| File level<br/> | No (see note below)<br/> | No<br/> | No<br/> | No<br/> |



 

**Note**  Single-instance store for NTFS is available as part of the Single Instance Storage feature in Windows Server.

## Related topics

<dl> <dt>

[About File Management](about-file-management.md)
</dt> <dt>

[Single-Instance Store and SIS Backup](/windows/desktop/Backup/single-instance-store-and-sis-backup)
</dt> </dl>

 

