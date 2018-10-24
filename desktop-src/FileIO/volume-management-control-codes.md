---
Description: Control codes used in volume management.
ms.assetid: 87f39e1c-3ebf-4c6f-a842-699ec3c45e76
title: Volume Management Control Codes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Volume Management Control Codes

Control codes used in volume management.

## In this section



| Topic                                                                                                                                      | Description                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_CREATE\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364558(v=VS.85).aspx)<br/>                                                                 | Creates an update sequence number (USN) change journal stream on a target volume, or modifies an existing change journal stream.<br/>                                                                                                                               |
| [**FSCTL\_CSV\_QUERY\_DOWN\_LEVEL\_FILE\_SYSTEM\_CHARACTERISTICS**](https://msdn.microsoft.com/en-us/library/Dn280517(v=VS.85).aspx)<br/> | Retrieves information about a file system for which CSVFS is a proxy.<br/>                                                                                                                                                                                          |
| [**FSCTL\_DELETE\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364561(v=VS.85).aspx)<br/>                                                                 | Deletes the update sequence number (USN) change journal on a volume, or waits for notification of change journal deletion.<br/>                                                                                                                                     |
| [**FSCTL\_DISMOUNT\_VOLUME**](https://msdn.microsoft.com/en-us/library/Aa364562(v=VS.85).aspx)<br/>                                                                        | Dismounts a volume regardless of whether or not the volume is currently in use. For more information, see the Remarks section.<br/>                                                                                                                                 |
| [**FSCTL\_ENUM\_USN\_DATA**](https://msdn.microsoft.com/en-us/library/Aa364563(v=VS.85).aspx)<br/>                                                                           | Enumerates the update sequence number (USN) data between two specified boundaries to obtain master file table (MFT) records.<br/>                                                                                                                                   |
| [**FSCTL\_EXTEND\_VOLUME**](https://msdn.microsoft.com/en-us/library/Aa364564(v=VS.85).aspx)<br/>                                                                            | Increases the size of a mounted volume.<br/>                                                                                                                                                                                                                        |
| [**FSCTL\_GET\_BOOT\_AREA\_INFO**](https://msdn.microsoft.com/en-us/library/Dd405525(v=VS.85).aspx)<br/>                                                                | Retrieves the locations of boot sectors for a volume. <br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                                      |
| [**FSCTL\_GET\_INTEGRITY\_INFORMATION**](https://msdn.microsoft.com/en-us/library/Hh965606(v=VS.85).aspx)<br/>                                                   | Retrieves the integrity status of a file or directory on a ReFS volume.<br/>                                                                                                                                                                                        |
| [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](https://msdn.microsoft.com/en-us/library/Aa364569(v=VS.85).aspx)<br/>                                                            | Retrieves information about the specified NTFS file system volume.<br/>                                                                                                                                                                                             |
| [**FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE**](https://msdn.microsoft.com/en-us/library/Dd405526(v=VS.85).aspx)<br/>                                                | Returns the sector offset to the first logical cluster number (LCN) of the file system relative to the start of the volume.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/> |
| [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](https://msdn.microsoft.com/en-us/library/Aa364572(v=VS.85).aspx)<br/>                                                         | Given a file handle, retrieves a data structure that describes the allocation and location on disk of a specific file, or, given a volume handle, the locations of bad clusters on a volume.<br/>                                                                   |
| [**FSCTL\_GET\_VOLUME\_BITMAP**](https://msdn.microsoft.com/en-us/library/Aa364573(v=VS.85).aspx)<br/>                                                                   | Retrieves a bitmap of occupied and available clusters on a volume.<br/>                                                                                                                                                                                             |
| [**FSCTL\_IS\_CSV\_FILE**](https://msdn.microsoft.com/en-us/library/Dn280518(v=VS.85).aspx)<br/>                                                                               | Determines whether a file is stored on a CSVFS volume, or retrieves namespace information.<br/>                                                                                                                                                                     |
| [**FSCTL\_IS\_FILE\_ON\_CSV\_VOLUME**](https://msdn.microsoft.com/en-us/library/Dn280519(v=VS.85).aspx)<br/>                                                         | Determines whether a file is stored on a CSVFS volume, or retrieves namespace information.<br/>                                                                                                                                                                     |
| [**FSCTL\_IS\_VOLUME\_MOUNTED**](https://msdn.microsoft.com/en-us/library/Aa364574(v=VS.85).aspx)<br/>                                                                   | Determines whether the specified volume is mounted, or if the specified file or directory is on a mounted volume.<br/>                                                                                                                                              |
| [**FSCTL\_IS\_VOLUME\_OWNED\_BYCSVFS**](https://msdn.microsoft.com/en-us/library/Dn280520(v=VS.85).aspx)<br/>                                                      | Determines whether a volume is locked by CSVFS.<br/>                                                                                                                                                                                                                |
| [**FSCTL\_LOCK\_VOLUME**](https://msdn.microsoft.com/en-us/library/Aa364575(v=VS.85).aspx)<br/>                                                                                | Locks a volume if it is not in use.<br/>                                                                                                                                                                                                                            |
| [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](https://msdn.microsoft.com/en-us/library/Ff951637(v=VS.85).aspx)<br/>                                                | Given a handle to a NTFS volume or a file on a NTFS volume, returns a chain of data structures that describes streams that occupy the specified clusters.<br/>                                                                                                      |
| [**FSCTL\_MARK\_HANDLE**](https://msdn.microsoft.com/en-us/library/Aa364576(v=VS.85).aspx)<br/>                                                                                | Marks a specified file or directory and its change journal record with information about changes to that file or directory.<br/>                                                                                                                                    |
| [**FSCTL\_MOVE\_FILE**](https://msdn.microsoft.com/en-us/library/Aa364577(v=VS.85).aspx)<br/>                                                                                    | Relocates one or more virtual clusters of a file from one logical cluster to another within the same volume. This operation is used during [defragmentation](defragmenting-files.md).<br/>                                                                         |
| [**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](https://msdn.microsoft.com/en-us/library/Dd442655(v=VS.85).aspx)<br/>                                          | Queries for file system recognition information on a volume.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                                |
| [**FSCTL\_QUERY\_REGION\_INFO**](https://msdn.microsoft.com/en-us/library/Dn393706(v=VS.85).aspx)<br/>                                                                   | Retrieves the storage tier regions defined for a volume that supports data tiering.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                         |
| [**FSCTL\_QUERY\_STORAGE\_CLASSES**](https://msdn.microsoft.com/en-us/library/Dn393709(v=VS.85).aspx)<br/>                                                           | Retrieves the storage tiers defined for a volume that supports data tiering.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                |
| [**FSCTL\_QUERY\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364583(v=VS.85).aspx)<br/>                                                                   | Queries for information on the current update sequence number (USN) change journal, its records, and its capacity.<br/>                                                                                                                                             |
| [**FSCTL\_READ\_FILE\_USN\_DATA**](https://msdn.microsoft.com/en-us/library/Aa364584(v=VS.85).aspx)<br/>                                                                | Retrieves the update sequence number (USN) change-journal information for the specified file or directory.<br/>                                                                                                                                                     |
| [**FSCTL\_READ\_FROM\_PLEX**](https://msdn.microsoft.com/en-us/library/Aa364585(v=VS.85).aspx)<br/>                                                                         | Reads from the specified plex.<br/>                                                                                                                                                                                                                                 |
| [**FSCTL\_READ\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364586(v=VS.85).aspx)<br/>                                                                     | Retrieves the set of update sequence number (USN) change journal records between two specified USN values.<br/>                                                                                                                                                     |
| [**FSCTL\_REPAIR\_COPIES**](https://msdn.microsoft.com/en-us/library/Hh965608(v=VS.85).aspx)<br/>                                                                            | Repair data corruption by selecting the proper copy to use.<br/>                                                                                                                                                                                                    |
| [**FSCTL\_SET\_INTEGRITY\_INFORMATION**](https://msdn.microsoft.com/en-us/library/Hh965609(v=VS.85).aspx)<br/>                                                   | Retrieves the integrity status of a file or directory on a ReFS volume.<br/>                                                                                                                                                                                        |
| [**FSCTL\_SHRINK\_VOLUME**](https://msdn.microsoft.com/en-us/library/Aa964912(v=VS.85).aspx)<br/>                                                                            | Signals that the volume is to be prepared to perform the shrink operation, the shrink operation is to be committed, or the shrink operation is to be terminated.<br/>                                                                                               |
| [**FSCTL\_UNLOCK\_VOLUME**](https://msdn.microsoft.com/en-us/library/Aa364814(v=VS.85).aspx)<br/>                                                                            | Unlocks a volume.<br/>                                                                                                                                                                                                                                              |
| [**FSCTL\_USN\_TRACK\_MODIFIED\_RANGES**](https://msdn.microsoft.com/en-us/library/Mt684959(v=VS.85).aspx)<br/>                                                  | Enables range tracking feature for update sequence number (USN) change journal stream on a target volume, or modifies already enabled range tracking parameters.<br/>                                                                                               |
| [**FSCTL\_WRITE\_USN\_CLOSE\_RECORD**](https://msdn.microsoft.com/en-us/library/Aa364816(v=VS.85).aspx)<br/>                                                        | Generates a record in the update sequence number (USN) change journal stream for the input file.<br/>                                                                                                                                                               |
| [**IOCTL\_VOLUME\_GET\_GPT\_ATTRIBUTES**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_volume_get_gpt_attributes)<br/>                                                  | Retrieves the attributes for a volume.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                                                      |
| [**IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_volume_get_volume_disk_extents)<br/>                                       | Retrieves the physical location of a specified volume on one or more disks.<br/>                                                                                                                                                                                    |
| [**IOCTL\_VOLUME\_IS\_CLUSTERED**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_volume_is_clustered)<br/>                                                               | Determines whether the specified volume is clustered.<br/>                                                                                                                                                                                                          |
| [**IOCTL\_VOLUME\_IS\_CSV**](ioctl-volume-is-csv.md)<br/>                                                                           | Determines whether a volume is a CSV volume.<br/>                                                                                                                                                                                                                   |
| [**IOCTL\_VOLUME\_OFFLINE**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_volume_offline)<br/>                                                                          | Takes a volume offline.<br/>                                                                                                                                                                                                                                        |
| [**IOCTL\_VOLUME\_ONLINE**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_volume_online)<br/>                                                                            | Brings a volume online.<br/>                                                                                                                                                                                                                                        |



 

The following control codes are used with [change journals](change-journals.md).

-   [**FSCTL\_CREATE\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364558(v=VS.85).aspx)
-   [**FSCTL\_DELETE\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364561(v=VS.85).aspx)
-   [**FSCTL\_ENUM\_USN\_DATA**](https://msdn.microsoft.com/en-us/library/Aa364563(v=VS.85).aspx)
-   [**FSCTL\_MARK\_HANDLE**](https://msdn.microsoft.com/en-us/library/Aa364576(v=VS.85).aspx)
-   [**FSCTL\_QUERY\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364583(v=VS.85).aspx)
-   [**FSCTL\_READ\_FILE\_USN\_DATA**](https://msdn.microsoft.com/en-us/library/Aa364584(v=VS.85).aspx)
-   [**FSCTL\_READ\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364586(v=VS.85).aspx)
-   [**FSCTL\_WRITE\_USN\_CLOSE\_RECORD**](https://msdn.microsoft.com/en-us/library/Aa364816(v=VS.85).aspx)

The following are [defragmentation](defragmenting-files.md) control codes.

-   [**FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE**](https://msdn.microsoft.com/en-us/library/Dd405526(v=VS.85).aspx)
-   [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](https://msdn.microsoft.com/en-us/library/Aa364572(v=VS.85).aspx)
-   [**FSCTL\_GET\_VOLUME\_BITMAP**](https://msdn.microsoft.com/en-us/library/Aa364573(v=VS.85).aspx)
-   [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](https://msdn.microsoft.com/en-us/library/Ff951637(v=VS.85).aspx)
-   [**FSCTL\_MOVE\_FILE**](https://msdn.microsoft.com/en-us/library/Aa364577(v=VS.85).aspx)
-   [**FSCTL\_QUERY\_REGION\_INFO**](https://msdn.microsoft.com/en-us/library/Dn393706(v=VS.85).aspx)
-   [**FSCTL\_QUERY\_USN\_JOURNAL**](https://msdn.microsoft.com/en-us/library/Aa364583(v=VS.85).aspx)

## Related topics

<dl> <dt>

[Directory Management Control Codes](directory-management-control-codes.md)
</dt> <dt>

[File Management Control Codes](file-management-control-codes.md)
</dt> </dl>

 

 




