---
description: Transactional NTFS (TxF) structures.
ms.assetid: 85b3cf8e-bff3-4693-b00e-64bf5d1f5065
title: TxF Structures
ms.topic: article
ms.date: 05/31/2018
---

# TxF Structures

Transactional NTFS (TxF) provides the following structures.

## In this section



| Structure                                                                                                    | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TXFS\_CREATE\_MINIVERSION\_INFO**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_create_miniversion_info)<br/>                           | Contains the version information about the miniversion created by [**FSCTL\_TXFS\_CREATE\_MINIVERSION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_txfs_create_miniversion).<br/>                                            |
| [**TXFS\_GET\_METADATA\_INFO\_OUT**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_get_metadata_info_out)<br/>                              | Contains the version information about the miniversion that is created.<br/>                                                                                                                 |
| [**TXF\_ID**](/windows/desktop/api/TxfW32/ns-txfw32-txf_id)<br/>                                                                         | Represents a unique identifier within the context of the Resource Manager.<br/>                                                                                                              |
| [**TXFS\_GET\_TRANSACTED\_VERSION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_get_transacted_version)<br/>                             | Contains the information about the base and latest versions of the specified file.<br/>                                                                                                      |
| [**TXFS\_LIST\_TRANSACTION\_LOCKED\_FILES**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_list_transaction_locked_files)<br/>              | Contains a list of files locked by a transacted writer.<br/>                                                                                                                                 |
| [**TXFS\_LIST\_TRANSACTION\_LOCKED\_FILES\_ENTRY**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_list_transaction_locked_files_entry)<br/> | Contains information about a locked transaction.<br/>                                                                                                                                        |
| [**TXFS\_LIST\_TRANSACTIONS**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_list_transactions)<br/>                                        | Contains a list of transactions.<br/>                                                                                                                                                        |
| [**TXFS\_LIST\_TRANSACTIONS\_ENTRY**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_list_transactions_entry)<br/>                           | Contains information about a transaction.<br/>                                                                                                                                               |
| [**TXF\_LOG\_RECORD\_AFFECTED\_FILE**](/windows/desktop/api/TxfW32/ns-txfw32-txf_log_record_affected_file)<br/>                          | Contains information for a file that was affected by a transaction.<br/>                                                                                                                     |
| [**TXF\_LOG\_RECORD\_BASE**](/windows/desktop/api/TxfW32/ns-txfw32-txf_log_record_base)<br/>                                             | Contains the basic record information.<br/>                                                                                                                                                  |
| [**TXF\_LOG\_RECORD\_TRUNCATE**](/windows/desktop/api/TxfW32/ns-txfw32-txf_log_record_truncate)<br/>                                     | Contains the record for a truncate operation.<br/>                                                                                                                                           |
| [**TXF\_LOG\_RECORD\_WRITE**](/windows/desktop/api/TxfW32/ns-txfw32-txf_log_record_write)<br/>                                           | Contains the record for a write operation.<br/>                                                                                                                                              |
| [**TXFS\_MODIFY\_RM**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_modify_rm)<br/>                                                        | Contains the information required when modifying log parameters and logging mode for a secondary resource manager.<br/>                                                                      |
| [**TXFS\_QUERY\_RM\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_query_rm_information)<br/>                                 | Contains information about the resource manager (RM).<br/>                                                                                                                                   |
| [**TXFS\_READ\_BACKUP\_INFORMATION\_OUT**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_read_backup_information_out)<br/>                  | Contains a Transactional NTFS (TxF) specific structure. This information should only be used when calling [**TXFS\_WRITE\_BACKUP\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_write_backup_information).<br/>    |
| [**TXFS\_SAVEPOINT\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_savepoint_information)<br/>                                | The [**FSCTL\_TXFS\_SAVEPOINT\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_savepoint_information) structure specifies the action to perform, and on which transaction.<br/>                                      |
| [**TXFS\_TRANSACTION\_ACTIVE\_INFO**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_transaction_active_info)<br/>                           | Contains the flag that indicates whether transactions were active or not when a snapshot was taken.<br/>                                                                                     |
| [**TXFS\_WRITE\_BACKUP\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_write_backup_information)<br/>                         | Contains a Transactional NTFS (TxF) specific structure. This information should only be used when calling [**TXFS\_WRITE\_BACKUP\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-txfs_read_backup_information_out).<br/> |



 

 

