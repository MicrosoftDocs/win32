---
description: Transactional NTFS (TxF) integrates transactions into the NTFS file system, which makes it easier for application developers and administrators to gracefully handle errors and preserve data integrity.
ms.assetid: 52341315-0412-4a87-aca0-9adea7aae62f
title: About Transactional NTFS
ms.topic: article
ms.date: 05/31/2018
---

# About Transactional NTFS

\[Microsoft strongly recommends developers utilize alternative means to achieve your application s needs. Many scenarios that TxF was developed for can be achieved through simpler and more readily available techniques. Furthermore, TxF may not be available in future versions of Microsoft Windows. For more information, and alternatives to TxF, please see [Alternatives to using Transactional NTFS](deprecation-of-txf.md).\]

Transactional NTFS (TxF) integrates transactions into the NTFS file system, which makes it easier for application developers and administrators to gracefully handle errors and preserve data integrity.

TxF can participate in distributed transactions that the [Distributed Transaction Coordinator (DTC)](/previous-versions/windows/desktop/ms684146(v=vs.85)) coordinates, which allows you to use TxF for the following:

-   Transactions that span multiple data stores, for example, a single transaction for file and SQL operations
-   Transactions that span multiple computers, for example, a single transaction for file updates on multiple computers

## In this section



| Topic                                                                                                                 | Description                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [When to Use Transactional NTFS](when-to-use-transactional-ntfs.md)<br/>                                       | Use Transactional NTFS to maintain data integrity.<br/>                                                                        |
| [Deploying Transactional NTFS](deploying-transactional-ntfs.md)<br/>                                           | Caching control in Transactional NTFS.<br/>                                                                                    |
| [How to Use Transactional NTFS](how-to-use-transactional-ntfs.md)<br/>                                         | Managing transacted file handles in Transactional NTFS.<br/>                                                                   |
| [Basic TxF Concepts](txf-basic-concepts.md)<br/>                                                               | Describes read-committed consistency, read-committed isolation, and transactional locking concepts in Transactional NTFS.<br/> |
| [Programming Considerations for Transactional NTFS](programming-considerations-for-transacted-fileio-.md)<br/> | Describes various programming considerations for Transactional NTFS.<br/>                                                      |
| [Performance Considerations for Transactional NTFS](performance-considerations-for-transactional-ntfs.md)<br/> | Recommendations for optimal file system transactions.<br/>                                                                     |



 

 

