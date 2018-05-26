---
Description: The following functions are used with transactions.
ms.assetid: e9704ea8-e67d-4278-b77e-1d4787224d52
title: Kernel Transaction Manager Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Kernel Transaction Manager Functions

The following functions are used with transactions.



| Function                                                            | Description                                                                                     |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**CommitTransaction**](/windows/win32/Ktmw32/nf-ktmw32-committransaction?branch=master)                      | Requests that the specified transaction be committed.                                           |
| [**CommitTransactionAsync**](/windows/win32/Ktmw32/nf-ktmw32-committransactionasync?branch=master)            | Requests that the specified transaction be committed.                                           |
| [**CreateTransaction**](/windows/win32/KtmW32/nf-ktmw32-createtransaction?branch=master)                      | Creates a new transaction object.                                                               |
| [**GetTransactionId**](/windows/win32/Ktmw32/nf-ktmw32-gettransactionid?branch=master)                        | Obtains the ID for the specified transaction.                                                   |
| [**GetTransactionInformation**](/windows/win32/Ktmw32/nf-ktmw32-gettransactioninformation?branch=master) | Returns the requested information about the specified transaction.                              |
| [**OpenTransaction**](/windows/win32/Ktmw32/nf-ktmw32-opentransaction?branch=master)                          | Opens an existing transaction.                                                                  |
| [**RollbackComplete**](/windows/win32/Ktmw32/nf-ktmw32-rollbackcomplete?branch=master)                        | Indicates that the resource manager (RM) has successfully completed rolling back a transaction. |
| [**RollbackTransaction**](/windows/win32/Ktmw32/nf-ktmw32-rollbacktransaction?branch=master)                  | Requests that the specified transaction be rolled back.                                         |
| [**RollbackTransactionAsync**](/windows/win32/Ktmw32/nf-ktmw32-rollbacktransactionasync?branch=master)        | Requests that the specified transaction be rolled back. This function returns asynchronously.   |
| [**SetTransactionInformation**](/windows/win32/Ktmw32/nf-ktmw32-settransactioninformation?branch=master)      | Sets the transaction information for the specified transaction.                                 |



 

The following functions are used with enlistments.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitComplete**](/windows/win32/Ktmw32/nf-ktmw32-commitcomplete?branch=master)                                          | Indicates that a RM has finished committing a transaction that was requested by the transaction manager (TM).                                                                                                                                                                                                                                                                        |
| [**CommitEnlistment**](/windows/win32/KtmW32/nf-ktmw32-commitenlistment?branch=master)                                      | Commits the transaction for the specified enlistment.                                                                                                                                                                                                                                                                                                                                |
| [**GetEnlistmentId**](/windows/win32/Ktmw32/nf-ktmw32-getenlistmentid?branch=master)                                        | Obtains the ID for the specified enlistment.                                                                                                                                                                                                                                                                                                                                         |
| [**CreateEnlistment**](/windows/win32/KtmW32/nf-ktmw32-createenlistment?branch=master)                                      | Creates an enlistment, sets its initial state, and opens a handle to the enlistment with the specified access.                                                                                                                                                                                                                                                                       |
| [**GetEnlistmentRecoveryInformation**](/windows/win32/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation?branch=master) | Retrieves an opaque structure of recovery data from KTM. Recovery information is stored in a log on behalf of a RM by calling the [**SetEnlistmentRecoveryInformation**](/windows/win32/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation?branch=master) function. After a failure, the RM can use the [**GetEnlistmentRecoveryInformation**](/windows/win32/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation?branch=master) function to retrieve the information. |
| [**OpenEnlistment**](/windows/win32/Ktmw32/nf-ktmw32-openenlistment?branch=master)                                          | Opens an existing enlistment object, and returns a handle to the enlistment.                                                                                                                                                                                                                                                                                                         |
| [**PrepareEnlistment**](/windows/win32/KtmW32/nf-ktmw32-prepareenlistment?branch=master)                                    | Called by superior TM to indicate that their pre-prepares work has been completed.                                                                                                                                                                                                                                                                                                   |
| [**PrePrepareEnlistment**](/windows/win32/KtmW32/nf-ktmw32-preprepareenlistment?branch=master)                              | Called by superior TM to indicate that their pre-prepares work has been completed.                                                                                                                                                                                                                                                                                                   |
| [**RecoverEnlistment**](/windows/win32/Ktmw32/nf-ktmw32-recoverenlistment?branch=master)                                    | Recovers an enlistment's state.                                                                                                                                                                                                                                                                                                                                                      |
| [**ReadOnlyEnlistment**](/windows/win32/Ktmw32/nf-ktmw32-readonlyenlistment?branch=master)                                  | Requests that the specified enlistment be converted to a read-only enlistment. A read-only enlistment cannot participate in the outcome of the transaction and is not durably recorded for recovery.                                                                                                                                                                                 |
| [**RollbackEnlistment**](/windows/win32/Ktmw32/nf-ktmw32-rollbackenlistment?branch=master)                                  | Rolls back the specified transaction that is associated with an enlistment. This function cannot be called for read-only enlistments.                                                                                                                                                                                                                                                |
| [**SetEnlistmentRecoveryInformation**](/windows/win32/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation?branch=master)      | Sets an opaque, user-defined structure of recovery data from KTM. Recovery information is stored in a log on behalf of a RM by calling [**SetEnlistmentRecoveryInformation**](/windows/win32/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation?branch=master). After a failure, the RM can use [**GetEnlistmentRecoveryInformation**](/windows/win32/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation?branch=master) to retrieve the information.                  |
| [**SinglePhaseReject**](/windows/win32/Ktmw32/nf-ktmw32-singlephasereject?branch=master)                                    | Indicates that the RM is refusing a single-phase request. When a TM receives this call, it initiates a two-phase commit and sends a prepare request to all enlisted RMs.                                                                                                                                                                                                             |



 

The following functions are used with resource managers.



| Function                                                                           | Description                                                                                                                                                      |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateResourceManager**](/windows/win32/Ktmw32/nf-ktmw32-createresourcemanager?branch=master)                             | Creates a new RM object, and associates the RM with a transaction manager (TM).                                                                                  |
| [**GetNotificationResourceManager**](/windows/win32/KtmW32/nf-ktmw32-getnotificationresourcemanager?branch=master)           | Requests and receives a notification for RM. This function is used by the RM register to receive notifications when a transaction changes state.                 |
| [**GetNotificationResourceManagerAsync**](/windows/win32/KtmW32/nf-ktmw32-getnotificationresourcemanagerasync?branch=master) | Requests and receives asynchronous notification for a RM. This function is used by the RM to register to receive notifications when a transaction changes state. |
| [**OpenResourceManager**](/windows/win32/Ktmw32/nf-ktmw32-openresourcemanager?branch=master)                                 | Opens an existing RM.                                                                                                                                            |
| [**PrepareComplete**](/windows/win32/Ktmw32/nf-ktmw32-preparecomplete?branch=master)                                         | Indicates that the RM has completed all processing necessary to guarantee that a commit or abort operation will succeed for the specified transaction.           |
| [**PrePrepareComplete**](/windows/win32/Ktmw32/nf-ktmw32-prepreparecomplete?branch=master)                                   | Signals that this RM has completed its preprepare work, so that other RMs can now begin their prepare operations.                                                |
| [**RecoverResourceManager**](/windows/win32/Ktmw32/nf-ktmw32-recoverresourcemanager?branch=master)                           | Recovers a RM's state from its log file.                                                                                                                         |
| [**SetResourceManagerCompletionPort**](/windows/win32/Ktmw32/nf-ktmw32-setresourcemanagercompletionport?branch=master)       | Associates the specified I/O completion port with the specified RM. This port receives all notifications for the RM.                                             |



 

The following functions are used with transaction managers.



| Function                                                                            | Description                                                                 |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**CreateTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-createtransactionmanager?branch=master)                        | Creates a new TM object and returns a handle with the specified access.     |
| [**GetCurrentClockTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-getcurrentclocktransactionmanager?branch=master) | Obtains a virtual clock value from a TM.                                    |
| [**GetTransactionManagerId**](/windows/win32/Ktmw32/nf-ktmw32-gettransactionmanagerid?branch=master)                          | Obtains an identifier for the specified TM.                                 |
| [**OpenTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-opentransactionmanager?branch=master)                            | Opens an existing TM.                                                       |
| [**OpenTransactionManagerById**](/windows/win32/Ktmw32/nf-ktmw32-opentransactionmanagerbyid?branch=master)                    | Opens an existing TM.                                                       |
| [**RecoverTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-recovertransactionmanager?branch=master)                      | Recovers a TM's state from its log file.                                    |
| [**RenameTransactionManager**](/windows/win32/KtmW32/nf-ktmw32-renametransactionmanager?branch=master)                        | Renames a TM.                                                               |
| [**RollforwardTransactionManager**](/windows/win32/KtmW32/nf-ktmw32-rollforwardtransactionmanager?branch=master)              | Recovers TM's state from its log file to the specified virtual clock value. |



 

 

 



