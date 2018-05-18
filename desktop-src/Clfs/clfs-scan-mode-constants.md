---
Description: 'Controls how records are scanned.'
ms.assetid: '64bb2113-aded-4a80-8f1a-1668ad05ae1e'
title: 'CLFS\_SCAN\_MODE Constants'
---

# CLFS\_SCAN\_MODE Constants

Controls how records are scanned. The constants are passed to [**CreateLogContainerScanContext**](createlogcontainerscancontext.md), and have the following possible values.



| Constant/value                                                                                                                                                                                                                                   | Description                                                                                                                                                                                            |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CLFS_SCAN_INIT"></span><span id="clfs_scan_init"></span><dl> <dt>**CLFS\_SCAN\_INIT**</dt> <dt>0x01</dt> </dl>                      | Initializes the scan context, but does not allocate associated storage. <br/> The initialization is destructive, because all data that is stored in the current scan context is lost.<br/> |
| <span id="CLFS_SCAN_FORWARD"></span><span id="clfs_scan_forward"></span><dl> <dt>**CLFS\_SCAN\_FORWARD**</dt> <dt>0x02</dt> </dl>             | Causes the next call to [**ScanLogContainers**](scanlogcontainers.md) to proceed in a forward direction. <br/> Cannot be used if **CLFS\_SCAN\_BACKWARD** is specified.<br/>              |
| <span id="CLFS_SCAN_BACKWARD"></span><span id="clfs_scan_backward"></span><dl> <dt>**CLFS\_SCAN\_BACKWARD**</dt> <dt>0x04</dt> </dl>          | Causes the next call to [**ScanLogContainers**](scanlogcontainers.md) to proceed in a backward direction. <br/> Cannot be used if **CLFS\_SCAN\_FORWARD** is specified.<br/>              |
| <span id="CLFS_SCAN_CLOSE"></span><span id="clfs_scan_close"></span><dl> <dt>**CLFS\_SCAN\_CLOSE**</dt> <dt>0x08</dt> </dl>                   | Uninitializes the scan context, and deallocates system storage that is associated with a scan context.<br/>                                                                                      |
| <span id="CLFS_SCAN_INITIALIZED"></span><span id="clfs_scan_initialized"></span><dl> <dt>**CLFS\_SCAN\_INITIALIZED**</dt> <dt>0x10</dt> </dl> | Indicates that the scan context is already initialized.<br/>                                                                                                                                     |
| <span id="CLFS_SCAN_BUFFERED"></span><span id="clfs_scan_buffered"></span><dl> <dt>**CLFS\_SCAN\_BUFFERED**</dt> <dt>0x20</dt> </dl>          | Indicates that the scanned container descriptors are pre-fetched and buffered.<br/>                                                                                                              |



## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>Clfs.h (include Clfsw32.h)</dt> </dl> |



## See also

<dl> <dt>

[**CreateLogContainerScanContext**](createlogcontainerscancontext.md)
</dt> </dl>

 

 




