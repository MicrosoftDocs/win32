---
Description: Kernel Transaction Manager (KTM) is a transaction management service. It makes transactions available as kernel objects and provides transaction management services to system components such as Transactional NTFS (TxF).
ms.assetid: 85a79698-a1ae-45a4-805e-25175034fa65
title: About KTM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About KTM

Kernel Transaction Manager (KTM) is a transaction management service. It makes transactions available as kernel objects and provides transaction management services to system components such as [Transactional NTFS](https://msdn.microsoft.com/library/windows/desktop/bb968806) (TxF).

The following topics describe the uses and features of KTM:

-   [What is a Transaction?](what-is-a-transaction.md)
-   [Working With Transactions](programming-model.md)
-   [Writing a Resource Manager](writing-a-resource-manager.md)
-   [Interoperability With Other Windows Features](interoperability-with-other-windows-features.md)
-   [KTM Security and Access Rights](ktm-security-and-access-rights.md)

KTM relies on the [Common Log File System](https://msdn.microsoft.com/library/windows/desktop/bb986747) for its operation. CLFS is a logging system that is capable of enabling transactions.

 

 



