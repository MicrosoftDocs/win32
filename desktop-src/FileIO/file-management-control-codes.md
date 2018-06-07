---
Description: Control codes used in file management.
ms.assetid: e27ded4b-d104-4244-b38e-5fed10d32e1e
title: File Management Control Codes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File Management Control Codes

The following control codes are used in file management.

## In this section



| Control Code                                                                                    | Description                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_ALLOW\_EXTENDED\_DASD\_IO**](/windows/desktop/api/WinIoCtl/)<br/>             | Signals the file system driver not to perform any I/O boundary checks on partition read or write calls.<br/>                                                                                  |
| [**FSCTL\_CREATE\_OR\_GET\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)<br/>          | Retrieves the object identifier for the specified file or directory. If no object identifier exists, using **FSCTL\_CREATE\_OR\_GET\_OBJECT\_ID** creates one.<br/>                           |
| [**FSCTL\_CSV\_CONTROL**](/windows/desktop/api/WinIoCtl/)<br/>                                     | Retrieves the results of a CSV control operation.<br/>                                                                                                                                        |
| [**FSCTL\_DELETE\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)<br/>                          | Removes the object identifier from a specified file or directory.<br/>                                                                                                                        |
| [**FSCTL\_DUPLICATE\_EXTENTS\_TO\_FILE**](/windows/desktop/api/WinIoCtl/)<br/>       | Instructs the file system to copy a range of file bytes on behalf of an application.<br/>                                                                                                     |
| [**FSCTL\_FILE\_LEVEL\_TRIM**](/windows/desktop/api/WinIoCtl/)<br/>                            | Indicates to the storage system which ranges in the file are not needed to be stored.<br/>                                                                                                    |
| [**FSCTL\_FILESYSTEM\_GET\_STATISTICS**](/windows/desktop/api/WinIoCtl/)<br/>        | Retrieves the information from various file system performance counters.<br/>                                                                                                                 |
| [**FSCTL\_FILESYSTEM\_GET\_STATISTICS\_EX**](/windows/desktop/api/WinIoCtl/)<br/> | Retrieves the information from various file system performance counters.<br/> Support for this control code started with Windows 10.<br/>                                               |
| [**FSCTL\_FIND\_FILES\_BY\_SID**](/windows/desktop/api/WinIoCtl/)<br/>                       | Searches a directory for a file whose creator owner matches the specified SID.<br/>                                                                                                           |
| [**FSCTL\_GET\_COMPRESSION**](/windows/desktop/api/WinIoCtl/)<br/>                             | Retrieves the current compression state of a file or directory on a volume whose file system supports per-stream compression.<br/>                                                            |
| [**FSCTL\_GET\_NTFS\_FILE\_RECORD**](/windows/desktop/api/WinIoCtl/)<br/>                 | Retrieves the first file record that is in use and is of a lesser than or equal ordinal value to the requested file reference number.<br/>                                                    |
| [**FSCTL\_GET\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)<br/>                                | Retrieves the object identifier for the specified file or directory.<br/>                                                                                                                     |
| [**FSCTL\_GET\_REPAIR**](/windows/desktop/api/WinIoCtl/)<br/>                                       | Retrieves information about the NTFS file system's self-healing mechanism.<br/>                                                                                                               |
| [**FSCTL\_INITIATE\_REPAIR**](/windows/desktop/api/WinIoCtl/)<br/>                             | Triggers the NTFS file system to start a self-healing cycle on a single file.<br/>                                                                                                            |
| [**FSCTL\_MAKE\_MEDIA\_COMPATIBLE**](/windows/desktop/api/WinIoCtl/)<br/>                | Closes an open UDF session on write-once media to make the media ROM compatible.<br/>                                                                                                         |
| [**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](/windows/desktop/api/WinIoCtl/)<br/>       | Notifies a server that a client application is ready to close a file.<br/>                                                                                                                    |
| [**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](/windows/desktop/api/WinIoCtl/)<br/>              | Responds to notification that an opportunistic lock on a file is about to be broken. Use this operation to unlock all opportunistic locks on the file but keep the file open.<br/>            |
| [**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](/windows/desktop/api/WinIoCtl/)<br/>          | Responds to notification that an exclusive opportunistic lock on a file is about to be broken. Use this operation to indicate that the file should receive a level 2 opportunistic lock.<br/> |
| [**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](/windows/desktop/api/WinIoCtl/)<br/>                    | Enables the calling application to wait for completion of an opportunistic lock break.<br/>                                                                                                   |
| [**FSCTL\_QUERY\_ALLOCATED\_RANGES**](/windows/desktop/api/WinIoCtl/)<br/>              | Scans a file or alternate stream looking for ranges that may contain nonzero data.<br/>                                                                                                       |
| [**FSCTL\_QUERY\_ON\_DISK\_VOLUME\_INFO**](/windows/desktop/api/WinIoCtl/)<br/>      | Requests UDF-specific volume information.<br/>                                                                                                                                                |
| [**FSCTL\_QUERY\_SPARING\_INFO**](/windows/desktop/api/WinIoCtl/)<br/>                      | Retrieves the defect management properties of the volume. Used for UDF file systems.<br/>                                                                                                     |
| [**FSCTL\_RECALL\_FILE**](/windows/desktop/api/WinIoCtl/)<br/>                                     | Recalls a file from storage media that Remote Storage manages, which is the hierarchical storage management software.<br/>                                                                    |
| [**FSCTL\_REQUEST\_BATCH\_OPLOCK**](/windows/desktop/api/WinIoCtl/)<br/>                  | Requests a batch opportunistic lock on a file.<br/>                                                                                                                                           |
| [**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/desktop/api/WinIoCtl/)<br/>                | Requests a filter opportunistic lock on a file.<br/>                                                                                                                                          |
| [**FSCTL\_REQUEST\_OPLOCK**](/windows/desktop/api/WinIoCtl/)<br/>                               | Requests an opportunistic lock (oplock) on a file and acknowledges that an oplock break has occurred.<br/>                                                                                    |
| [**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](/windows/desktop/api/WinIoCtl/)<br/>             | Requests a level 1 opportunistic lock on a file.<br/>                                                                                                                                         |
| [**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](/windows/desktop/api/WinIoCtl/)<br/>             | Requests a level 2 opportunistic lock on a file.<br/>                                                                                                                                         |
| [**FSCTL\_SET\_COMPRESSION**](/windows/desktop/api/WinIoCtl/)<br/>                             | Sets the compression state of a file or directory on a volume whose file system supports per-file and per-directory compression.<br/>                                                         |
| [**FSCTL\_SET\_DEFECT\_MANAGEMENT**](/windows/desktop/api/WinIoCtl/)<br/>                | Sets the software defect management state for the specified file. Used for UDF file systems.<br/>                                                                                             |
| [**FSCTL\_SET\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)<br/>                                | Sets the object identifier for the specified file or directory.<br/>                                                                                                                          |
| [**FSCTL\_SET\_OBJECT\_ID\_EXTENDED**](/windows/desktop/api/WinIoCtl/)<br/>             | Modifies user data associated with the object identifier for the specified file or directory.<br/>                                                                                            |
| [**FSCTL\_SET\_REPAIR**](/windows/desktop/api/WinIoCtl/)<br/>                                       | Sets the mode of an NTFS file system's self-healing capability.<br/>                                                                                                                          |
| [**FSCTL\_SET\_SPARSE**](/windows/desktop/api/WinIoCtl/)<br/>                                       | Marks the indicated file as sparse or not sparse. In a sparse file, large ranges of zeros may not require disk allocation.<br/>                                                               |
| [**FSCTL\_SET\_ZERO\_DATA**](/windows/desktop/api/WinIoCtl/)<br/>                                | Fills a specified range of a file with zeros (0).<br/>                                                                                                                                        |
| [**FSCTL\_SET\_ZERO\_ON\_DEALLOCATION**](/windows/desktop/api/WinIoCtl/)<br/>         | Indicates an NTFS file system file handle should have its clusters filled with zeros when it is deallocated.<br/>                                                                             |
| [**FSCTL\_WAIT\_FOR\_REPAIR**](/windows/desktop/api/WinIoCtl/)<br/>                            | Returns when the specified repairs are completed.<br/>                                                                                                                                        |



 

The following control codes are used with [file compression and decompression](file-compression-and-decompression.md).

<dl>

[**FSCTL\_GET\_COMPRESSION**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_COMPRESSION**](/windows/desktop/api/WinIoCtl/)  
</dl>

The following control codes are used with [object identifiers](distributed-link-tracking-and-object-identifiers.md).

<dl>

[**FSCTL\_CREATE\_OR\_GET\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_DELETE\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_GET\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_OBJECT\_ID**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_OBJECT\_ID\_EXTENDED**](/windows/desktop/api/WinIoCtl/)  
</dl>

The following control codes are used with [opportunistic locks](opportunistic-locks.md).

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_OPLOCK**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](/windows/desktop/api/WinIoCtl/)  
</dl>

The following control codes are used with [sparse files](sparse-files.md).

<dl>

[**FSCTL\_QUERY\_ALLOCATED\_RANGES**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_SPARSE**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_ZERO\_DATA**](/windows/desktop/api/WinIoCtl/)  
</dl>

The following control codes are used with the NTFS self-healing mechanism.

<dl>

[**FSCTL\_GET\_REPAIR**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_INITIATE\_REPAIR**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_REPAIR**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_WAIT\_FOR\_REPAIR**](/windows/desktop/api/WinIoCtl/)  
</dl>

The following control codes are used with UDF.

<dl>

[**FSCTL\_MAKE\_MEDIA\_COMPATIBLE**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_QUERY\_ON\_DISK\_VOLUME\_INFO**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_QUERY\_SPARING\_INFO**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_SET\_DEFECT\_MANAGEMENT**](/windows/desktop/api/WinIoCtl/)  
</dl>

## Related topics

<dl> <dt>

[Directory Management Control Codes](directory-management-control-codes.md)
</dt> <dt>

[Volume Management Control Codes](volume-management-control-codes.md)
</dt> </dl>

 

 




