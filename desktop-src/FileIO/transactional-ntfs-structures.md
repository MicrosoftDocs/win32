---
Description: 'Transactional NTFS (TxF) structures.'
ms.assetid: '85b3cf8e-bff3-4693-b00e-64bf5d1f5065'
title: TxF Structures
---

# TxF Structures

Transactional NTFS (TxF) provides the following structures.

## In this section



| Structure                                                                                                    | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TXFS\_CREATE\_MINIVERSION\_INFO**](txfs-create-miniversion-info.md)<br/>                           | Contains the version information about the miniversion created by [**FSCTL\_TXFS\_CREATE\_MINIVERSION**](fsctl-txfs-create-miniversion.md).<br/>                                            |
| [**TXFS\_GET\_METADATA\_INFO\_OUT**](txfs-get-metadata-info-out.md)<br/>                              | Contains the version information about the miniversion that is created.<br/>                                                                                                                 |
| [**TXF\_ID**](txf-id.md)<br/>                                                                         | Represents a unique identifier within the context of the Resource Manager.<br/>                                                                                                              |
| [**TXFS\_GET\_TRANSACTED\_VERSION**](txfs-get-transacted-version.md)<br/>                             | Contains the information about the base and latest versions of the specified file.<br/>                                                                                                      |
| [**TXFS\_LIST\_TRANSACTION\_LOCKED\_FILES**](txfs-list-transaction-locked-files.md)<br/>              | Contains a list of files locked by a transacted writer.<br/>                                                                                                                                 |
| [**TXFS\_LIST\_TRANSACTION\_LOCKED\_FILES\_ENTRY**](txfs-list-transaction-locked-files-entry.md)<br/> | Contains information about a locked transaction.<br/>                                                                                                                                        |
| [**TXFS\_LIST\_TRANSACTIONS**](txfs-list-transactions.md)<br/>                                        | Contains a list of transactions.<br/>                                                                                                                                                        |
| [**TXFS\_LIST\_TRANSACTIONS\_ENTRY**](txfs-list-transactions-entry.md)<br/>                           | Contains information about a transaction.<br/>                                                                                                                                               |
| [**TXF\_LOG\_RECORD\_AFFECTED\_FILE**](txf-log-record-affected-file.md)<br/>                          | Contains information for a file that was affected by a transaction.<br/>                                                                                                                     |
| [**TXF\_LOG\_RECORD\_BASE**](txf-log-record-base.md)<br/>                                             | Contains the basic record information.<br/>                                                                                                                                                  |
| [**TXF\_LOG\_RECORD\_TRUNCATE**](txf-log-record-truncate.md)<br/>                                     | Contains the record for a truncate operation.<br/>                                                                                                                                           |
| [**TXF\_LOG\_RECORD\_WRITE**](txf-log-record-write.md)<br/>                                           | Contains the record for a write operation.<br/>                                                                                                                                              |
| [**TXFS\_MODIFY\_RM**](txfs-modify-rm.md)<br/>                                                        | Contains the information required when modifying log parameters and logging mode for a secondary resource manager.<br/>                                                                      |
| [**TXFS\_QUERY\_RM\_INFORMATION**](txfs-query-rm-information.md)<br/>                                 | Contains information about the resource manager (RM).<br/>                                                                                                                                   |
| [**TXFS\_READ\_BACKUP\_INFORMATION\_OUT**](txfs-read-backup-information-out.md)<br/>                  | Contains a Transactional NTFS (TxF) specific structure. This information should only be used when calling [**TXFS\_WRITE\_BACKUP\_INFORMATION**](txfs-write-backup-information.md).<br/>    |
| [**TXFS\_SAVEPOINT\_INFORMATION**](txfs-savepoint-information.md)<br/>                                | The [**FSCTL\_TXFS\_SAVEPOINT\_INFORMATION**](txfs-savepoint-information.md) structure specifies the action to perform, and on which transaction.<br/>                                      |
| [**TXFS\_TRANSACTION\_ACTIVE\_INFO**](txfs-transaction-active-info.md)<br/>                           | Contains the flag that indicates whether transactions were active or not when a snapshot was taken.<br/>                                                                                     |
| [**TXFS\_WRITE\_BACKUP\_INFORMATION**](txfs-write-backup-information.md)<br/>                         | Contains a Transactional NTFS (TxF) specific structure. This information should only be used when calling [**TXFS\_WRITE\_BACKUP\_INFORMATION**](txfs-read-backup-information-out.md).<br/> |



 

 

 




