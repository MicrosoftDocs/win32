---
Description: 'If you are writing a service or component and need to use transactional services or if you need to monitor the state of a kernel transaction, you need to create a resource manager (RM).'
ms.assetid: '9b62ef58-9897-4573-bda4-8c3ec952b6d2'
title: Writing a Resource Manager
---

# Writing a Resource Manager

If you are writing a service or component and need to use transactional services or if you need to monitor the state of a kernel transaction, you need to create a resource manager (RM).

To write a resource manager, you must create multiple kernel objects. The objects that an RM uses are:

-   Transaction Manager (TM) objects
-   Resource Manager objects
-   Enlistment objects

First, create a TM object. There are two types of TMs:

-   Volatile – these TMs do not have a log and cannot recover their state
-   Durable – these TMs have a log

To create a durable TM, you must either create a CLFS log and call [**CreateTransactionManager**](createtransactionmanager.md) or have KTM create it for you. After a durable TM is created, you must first recover the TM by calling [**RecoverTransactionManager**](recovertransactionmanager.md). After the TM is recovered, it is available for use.

If you recovered an existing TM, all RMs associated with this TM will start receiving recovery messages. For more information, see [Recovery Processing](recovery-processing.md).

Next, you create a resource manager by calling [**CreateResourceManager**](createresourcemanager.md) with the TM handle. The RM can be volatile or durable. Only durable TMs can be used with durable RMs.

When working transactionally, you enlist in the transaction by calling [**CreateEnlistment**](createenlistment.md)and specifying which notifications to receive.

**Note**  You can start receiving notifications before the call to [**CreateEnlistment**](createenlistment.md) is completed.

When you receive a notification, call the appropriate "Complete\*" function when any work associated with processing the notification is completed. The complete functions are:

-   [**CommitComplete**](commitcomplete.md)
-   [**PrepareComplete**](preparecomplete.md)
-   [**PreprepareComplete**](prepreparecomplete.md)

If at any time a resource manager is unable to complete the work of the transaction, or if continuing would render your application unable to undo the work done within the transaction, you must roll back the transaction by calling [**RollbackEnlistment**](rollbackenlistment.md).

 

 



