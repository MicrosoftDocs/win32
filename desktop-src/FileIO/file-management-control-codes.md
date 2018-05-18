---
Description: 'Control codes used in file management.'
ms.assetid: 'e27ded4b-d104-4244-b38e-5fed10d32e1e'
title: File Management Control Codes
---

# File Management Control Codes

The following control codes are used in file management.

## In this section



| Control Code                                                                                    | Description                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_ALLOW\_EXTENDED\_DASD\_IO**](fsctl-allow-extended-dasd-io.md)<br/>             | Signals the file system driver not to perform any I/O boundary checks on partition read or write calls.<br/>                                                                                  |
| [**FSCTL\_CREATE\_OR\_GET\_OBJECT\_ID**](fsctl-create-or-get-object-id.md)<br/>          | Retrieves the object identifier for the specified file or directory. If no object identifier exists, using **FSCTL\_CREATE\_OR\_GET\_OBJECT\_ID** creates one.<br/>                           |
| [**FSCTL\_CSV\_CONTROL**](fsctl-csv-control.md)<br/>                                     | Retrieves the results of a CSV control operation.<br/>                                                                                                                                        |
| [**FSCTL\_DELETE\_OBJECT\_ID**](fsctl-delete-object-id.md)<br/>                          | Removes the object identifier from a specified file or directory.<br/>                                                                                                                        |
| [**FSCTL\_DUPLICATE\_EXTENTS\_TO\_FILE**](fsctl-duplicate-extents-to-file.md)<br/>       | Instructs the file system to copy a range of file bytes on behalf of an application.<br/>                                                                                                     |
| [**FSCTL\_FILE\_LEVEL\_TRIM**](fsctl-file-level-trim.md)<br/>                            | Indicates to the storage system which ranges in the file are not needed to be stored.<br/>                                                                                                    |
| [**FSCTL\_FILESYSTEM\_GET\_STATISTICS**](fsctl-filesystem-get-statistics.md)<br/>        | Retrieves the information from various file system performance counters.<br/>                                                                                                                 |
| [**FSCTL\_FILESYSTEM\_GET\_STATISTICS\_EX**](fsctl-filesystem-get-statistics-ex.md)<br/> | Retrieves the information from various file system performance counters.<br/> Support for this control code started with Windows 10.<br/>                                               |
| [**FSCTL\_FIND\_FILES\_BY\_SID**](fsctl-find-files-by-sid.md)<br/>                       | Searches a directory for a file whose creator owner matches the specified SID.<br/>                                                                                                           |
| [**FSCTL\_GET\_COMPRESSION**](fsctl-get-compression.md)<br/>                             | Retrieves the current compression state of a file or directory on a volume whose file system supports per-stream compression.<br/>                                                            |
| [**FSCTL\_GET\_NTFS\_FILE\_RECORD**](fsctl-get-ntfs-file-record.md)<br/>                 | Retrieves the first file record that is in use and is of a lesser than or equal ordinal value to the requested file reference number.<br/>                                                    |
| [**FSCTL\_GET\_OBJECT\_ID**](fsctl-get-object-id.md)<br/>                                | Retrieves the object identifier for the specified file or directory.<br/>                                                                                                                     |
| [**FSCTL\_GET\_REPAIR**](fsctl-get-repair.md)<br/>                                       | Retrieves information about the NTFS file system's self-healing mechanism.<br/>                                                                                                               |
| [**FSCTL\_INITIATE\_REPAIR**](fsctl-initiate-repair.md)<br/>                             | Triggers the NTFS file system to start a self-healing cycle on a single file.<br/>                                                                                                            |
| [**FSCTL\_MAKE\_MEDIA\_COMPATIBLE**](fsctl-make-media-compatible.md)<br/>                | Closes an open UDF session on write-once media to make the media ROM compatible.<br/>                                                                                                         |
| [**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](fsctl-opbatch-ack-close-pending.md)<br/>       | Notifies a server that a client application is ready to close a file.<br/>                                                                                                                    |
| [**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](fsctl-oplock-break-ack-no-2.md)<br/>              | Responds to notification that an opportunistic lock on a file is about to be broken. Use this operation to unlock all opportunistic locks on the file but keep the file open.<br/>            |
| [**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)<br/>          | Responds to notification that an exclusive opportunistic lock on a file is about to be broken. Use this operation to indicate that the file should receive a level 2 opportunistic lock.<br/> |
| [**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](fsctl-oplock-break-notify.md)<br/>                    | Enables the calling application to wait for completion of an opportunistic lock break.<br/>                                                                                                   |
| [**FSCTL\_QUERY\_ALLOCATED\_RANGES**](fsctl-query-allocated-ranges.md)<br/>              | Scans a file or alternate stream looking for ranges that may contain nonzero data.<br/>                                                                                                       |
| [**FSCTL\_QUERY\_ON\_DISK\_VOLUME\_INFO**](fsctl-query-on-disk-volume-info.md)<br/>      | Requests UDF-specific volume information.<br/>                                                                                                                                                |
| [**FSCTL\_QUERY\_SPARING\_INFO**](fsctl-query-sparing-info.md)<br/>                      | Retrieves the defect management properties of the volume. Used for UDF file systems.<br/>                                                                                                     |
| [**FSCTL\_RECALL\_FILE**](fsctl-recall-file.md)<br/>                                     | Recalls a file from storage media that Remote Storage manages, which is the hierarchical storage management software.<br/>                                                                    |
| [**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)<br/>                  | Requests a batch opportunistic lock on a file.<br/>                                                                                                                                           |
| [**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)<br/>                | Requests a filter opportunistic lock on a file.<br/>                                                                                                                                          |
| [**FSCTL\_REQUEST\_OPLOCK**](fsctl-request-oplock.md)<br/>                               | Requests an opportunistic lock (oplock) on a file and acknowledges that an oplock break has occurred.<br/>                                                                                    |
| [**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](fsctl-request-oplock-level-1.md)<br/>             | Requests a level 1 opportunistic lock on a file.<br/>                                                                                                                                         |
| [**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)<br/>             | Requests a level 2 opportunistic lock on a file.<br/>                                                                                                                                         |
| [**FSCTL\_SET\_COMPRESSION**](fsctl-set-compression.md)<br/>                             | Sets the compression state of a file or directory on a volume whose file system supports per-file and per-directory compression.<br/>                                                         |
| [**FSCTL\_SET\_DEFECT\_MANAGEMENT**](fsctl-set-defect-management.md)<br/>                | Sets the software defect management state for the specified file. Used for UDF file systems.<br/>                                                                                             |
| [**FSCTL\_SET\_OBJECT\_ID**](fsctl-set-object-id.md)<br/>                                | Sets the object identifier for the specified file or directory.<br/>                                                                                                                          |
| [**FSCTL\_SET\_OBJECT\_ID\_EXTENDED**](fsctl-set-object-id-extended.md)<br/>             | Modifies user data associated with the object identifier for the specified file or directory.<br/>                                                                                            |
| [**FSCTL\_SET\_REPAIR**](fsctl-set-repair.md)<br/>                                       | Sets the mode of an NTFS file system's self-healing capability.<br/>                                                                                                                          |
| [**FSCTL\_SET\_SPARSE**](fsctl-set-sparse.md)<br/>                                       | Marks the indicated file as sparse or not sparse. In a sparse file, large ranges of zeros may not require disk allocation.<br/>                                                               |
| [**FSCTL\_SET\_ZERO\_DATA**](fsctl-set-zero-data.md)<br/>                                | Fills a specified range of a file with zeros (0).<br/>                                                                                                                                        |
| [**FSCTL\_SET\_ZERO\_ON\_DEALLOCATION**](fsctl-set-zero-on-deallocation.md)<br/>         | Indicates an NTFS file system file handle should have its clusters filled with zeros when it is deallocated.<br/>                                                                             |
| [**FSCTL\_WAIT\_FOR\_REPAIR**](fsctl-wait-for-repair.md)<br/>                            | Returns when the specified repairs are completed.<br/>                                                                                                                                        |



 

The following control codes are used with [file compression and decompression](file-compression-and-decompression.md).

<dl>

[**FSCTL\_GET\_COMPRESSION**](fsctl-get-compression.md)  
[**FSCTL\_SET\_COMPRESSION**](fsctl-set-compression.md)  
</dl>

The following control codes are used with [object identifiers](distributed-link-tracking-and-object-identifiers.md).

<dl>

[**FSCTL\_CREATE\_OR\_GET\_OBJECT\_ID**](fsctl-create-or-get-object-id.md)  
[**FSCTL\_DELETE\_OBJECT\_ID**](fsctl-delete-object-id.md)  
[**FSCTL\_GET\_OBJECT\_ID**](fsctl-get-object-id.md)  
[**FSCTL\_SET\_OBJECT\_ID**](fsctl-set-object-id.md)  
[**FSCTL\_SET\_OBJECT\_ID\_EXTENDED**](fsctl-set-object-id-extended.md)  
</dl>

The following control codes are used with [opportunistic locks](opportunistic-locks.md).

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](fsctl-opbatch-ack-close-pending.md)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](fsctl-oplock-break-ack-no-2.md)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](fsctl-oplock-break-notify.md)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)  
[**FSCTL\_REQUEST\_OPLOCK**](fsctl-request-oplock.md)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](fsctl-request-oplock-level-1.md)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)  
</dl>

The following control codes are used with [sparse files](sparse-files.md).

<dl>

[**FSCTL\_QUERY\_ALLOCATED\_RANGES**](fsctl-query-allocated-ranges.md)  
[**FSCTL\_SET\_SPARSE**](fsctl-set-sparse.md)  
[**FSCTL\_SET\_ZERO\_DATA**](fsctl-set-zero-data.md)  
</dl>

The following control codes are used with the NTFS self-healing mechanism.

<dl>

[**FSCTL\_GET\_REPAIR**](fsctl-get-repair.md)  
[**FSCTL\_INITIATE\_REPAIR**](fsctl-initiate-repair.md)  
[**FSCTL\_SET\_REPAIR**](fsctl-set-repair.md)  
[**FSCTL\_WAIT\_FOR\_REPAIR**](fsctl-wait-for-repair.md)  
</dl>

The following control codes are used with UDF.

<dl>

[**FSCTL\_MAKE\_MEDIA\_COMPATIBLE**](fsctl-make-media-compatible.md)  
[**FSCTL\_QUERY\_ON\_DISK\_VOLUME\_INFO**](fsctl-query-on-disk-volume-info.md)  
[**FSCTL\_QUERY\_SPARING\_INFO**](fsctl-query-sparing-info.md)  
[**FSCTL\_SET\_DEFECT\_MANAGEMENT**](fsctl-set-defect-management.md)  
</dl>

## Related topics

<dl> <dt>

[Directory Management Control Codes](directory-management-control-codes.md)
</dt> <dt>

[Volume Management Control Codes](volume-management-control-codes.md)
</dt> </dl>

 

 




