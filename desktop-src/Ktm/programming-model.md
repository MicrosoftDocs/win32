---
description: Application writers can make minor source code changes to add transacted file and registry operations using the Kernel Transaction Manager (KTM).
ms.assetid: 356c66dc-5ddd-472f-835c-2e2cb019bcfd
title: Working With Transactions
ms.topic: article
ms.date: 05/31/2018
---

# Working With Transactions

Application writers can make minor source code changes to add transacted file and registry operations using the Kernel Transaction Manager (KTM). Typically, this will involve creating a transaction and passing the handle to other functions provided by transactional resources such as [Transactional NTFS](/windows/desktop/FileIO/transactional-ntfs-portal) and the Transacted Registry.

KTM provides mechanisms for your application to participate in transactions as well as to write your own transactional resource manager. There are functions that allow you to create, manage, and work with four classes of kernel objects: transactions, transaction managers, resource managers, and enlistments. If you are simply using transactions, you only need to work with transaction objects and use these functions:

-   [**CreateTransaction**](/windows/desktop/api/KtmW32/nf-ktmw32-createtransaction)
-   [**CommitTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-committransaction)
-   [**RollbackTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbacktransaction)

Never assume a transaction is active. Transactions can be rolled back for many reasons and at any time.

Windows exposes a handle-based interface to system resources. To work with an operating system object, the application first requests a handle to the object, and then uses this handle in subsequent function calls to access or modify the object. A handle can usually be opened in different modes; the mode specified affects the semantics of subsequent function calls. For example, a file handle that is opened by a call to [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) with the *dwDesiredAccess* flag set to **GENERIC\_READ** cannot be used in calls that modify the file.

You can coordinate with [Distributed Transaction Coordinator](/previous-versions/windows/desktop/ms684146(v=vs.85)) user-mode resources such as SQL or MSMQ, and with kernel-mode resources that use the KTM. First, create a DTC transaction, or a [**System.Transactions**](/dotnet/api/system.transactions?view=dotnet-plat-ext-3.1) object, then call the [**IKernelTransaction**](/previous-versions/windows/desktop/aa344210(v=vs.85)) object, from which you can obtain the KTM handle. The **IKernelTransaction** object creates a KTM transaction that is subordinate to the DTC transaction. With this handle, you can create your transacted objects, but signal the outcome of the transaction using DTC or **System.Transactions**.

 

 
