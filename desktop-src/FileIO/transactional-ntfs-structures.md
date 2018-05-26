---
Description: Transactional NTFS (TxF) structures.
ms.assetid: 85b3cf8e-bff3-4693-b00e-64bf5d1f5065
title: TxF Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TxF Structures

Transactional NTFS (TxF) provides the following structures.

## In this section



| Structure                                                                                                    | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TXFS\_CREATE\_MINIVERSION\_INFO**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_create_miniversion_info?branch=master)<br/>                           | Contains the version information about the miniversion created by [**FSCTL\_TXFS\_CREATE\_MINIVERSION**](/windows/win32/WinIoCtl/?branch=master).<br/>                                            |
| [**TXFS\_GET\_METADATA\_INFO\_OUT**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_get_metadata_info_out?branch=master)<br/>                              | Contains the version information about the miniversion that is created.<br/>                                                                                                                 |
| [**TXF\_ID**](/windows/win32/TxfW32/ns-txfw32-_txf_id?branch=master)<br/>                                                                         | Represents a unique identifier within the context of the Resource Manager.<br/>                                                                                                              |
| [**TXFS\_GET\_TRANSACTED\_VERSION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_get_transacted_version?branch=master)<br/>                             | Contains the information about the base and latest versions of the specified file.<br/>                                                                                                      |
| [**TXFS\_LIST\_TRANSACTION\_LOCKED\_FILES**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_list_transaction_locked_files?branch=master)<br/>              | Contains a list of files locked by a transacted writer.<br/>                                                                                                                                 |
| [**TXFS\_LIST\_TRANSACTION\_LOCKED\_FILES\_ENTRY**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_list_transaction_locked_files_entry?branch=master)<br/> | Contains information about a locked transaction.<br/>                                                                                                                                        |
| [**TXFS\_LIST\_TRANSACTIONS**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_list_transactions?branch=master)<br/>                                        | Contains a list of transactions.<br/>                                                                                                                                                        |
| [**TXFS\_LIST\_TRANSACTIONS\_ENTRY**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_list_transactions_entry?branch=master)<br/>                           | Contains information about a transaction.<br/>                                                                                                                                               |
| [**TXF\_LOG\_RECORD\_AFFECTED\_FILE**](/windows/win32/TxfW32/ns-txfw32-_txf_log_record_affected_file?branch=master)<br/>                          | Contains information for a file that was affected by a transaction.<br/>                                                                                                                     |
| [**TXF\_LOG\_RECORD\_BASE**](/windows/win32/TxfW32/ns-txfw32-_txf_log_record_base?branch=master)<br/>                                             | Contains the basic record information.<br/>                                                                                                                                                  |
| [**TXF\_LOG\_RECORD\_TRUNCATE**](/windows/win32/TxfW32/ns-txfw32-_txf_log_record_truncate?branch=master)<br/>                                     | Contains the record for a truncate operation.<br/>                                                                                                                                           |
| [**TXF\_LOG\_RECORD\_WRITE**](/windows/win32/TxfW32/ns-txfw32-_txf_log_record_write?branch=master)<br/>                                           | Contains the record for a write operation.<br/>                                                                                                                                              |
| [**TXFS\_MODIFY\_RM**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_modify_rm?branch=master)<br/>                                                        | Contains the information required when modifying log parameters and logging mode for a secondary resource manager.<br/>                                                                      |
| [**TXFS\_QUERY\_RM\_INFORMATION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_query_rm_information?branch=master)<br/>                                 | Contains information about the resource manager (RM).<br/>                                                                                                                                   |
| [**TXFS\_READ\_BACKUP\_INFORMATION\_OUT**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_read_backup_information_out?branch=master)<br/>                  | Contains a Transactional NTFS (TxF) specific structure. This information should only be used when calling [**TXFS\_WRITE\_BACKUP\_INFORMATION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_write_backup_information?branch=master).<br/>    |
| [**TXFS\_SAVEPOINT\_INFORMATION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_savepoint_information?branch=master)<br/>                                | The [**FSCTL\_TXFS\_SAVEPOINT\_INFORMATION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_savepoint_information?branch=master) structure specifies the action to perform, and on which transaction.<br/>                                      |
| [**TXFS\_TRANSACTION\_ACTIVE\_INFO**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_transaction_active_info?branch=master)<br/>                           | Contains the flag that indicates whether transactions were active or not when a snapshot was taken.<br/>                                                                                     |
| [**TXFS\_WRITE\_BACKUP\_INFORMATION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_write_backup_information?branch=master)<br/>                         | Contains a Transactional NTFS (TxF) specific structure. This information should only be used when calling [**TXFS\_WRITE\_BACKUP\_INFORMATION**](/windows/win32/WinIoCtl/ns-winioctl-_txfs_read_backup_information_out?branch=master).<br/> |



 

 

 




