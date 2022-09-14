---
description: The following functions are used with transactions.
ms.assetid: e9704ea8-e67d-4278-b77e-1d4787224d52
title: Kernel Transaction Manager Functions
ms.topic: article
ms.date: 05/31/2018
---

# Kernel Transaction Manager Functions

The following functions are used with transactions.



| Function                                                            | Description                                                                                     |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**CommitTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-committransaction)                      | Requests that the specified transaction be committed.                                           |
| [**CommitTransactionAsync**](/windows/desktop/api/Ktmw32/nf-ktmw32-committransactionasync)            | Requests that the specified transaction be committed.                                           |
| [**CreateTransaction**](/windows/desktop/api/KtmW32/nf-ktmw32-createtransaction)                      | Creates a new transaction object.                                                               |
| [**GetTransactionId**](/windows/desktop/api/Ktmw32/nf-ktmw32-gettransactionid)                        | Obtains the ID for the specified transaction.                                                   |
| [**GetTransactionInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-gettransactioninformation) | Returns the requested information about the specified transaction.                              |
| [**OpenTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-opentransaction)                          | Opens an existing transaction.                                                                  |
| [**RollbackComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackcomplete)                        | Indicates that the resource manager (RM) has successfully completed rolling back a transaction. |
| [**RollbackTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbacktransaction)                  | Requests that the specified transaction be rolled back.                                         |
| [**RollbackTransactionAsync**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbacktransactionasync)        | Requests that the specified transaction be rolled back. This function returns asynchronously.   |
| [**SetTransactionInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-settransactioninformation)      | Sets the transaction information for the specified transaction.                                 |



 

The following functions are used with enlistments.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete)                                          | Indicates that a RM has finished committing a transaction that was requested by the transaction manager (TM).                                                                                                                                                                                                                                                                        |
| [**CommitEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-commitenlistment)                                      | Commits the transaction for the specified enlistment.                                                                                                                                                                                                                                                                                                                                |
| [**GetEnlistmentId**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentid)                                        | Obtains the ID for the specified enlistment.                                                                                                                                                                                                                                                                                                                                         |
| [**CreateEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-createenlistment)                                      | Creates an enlistment, sets its initial state, and opens a handle to the enlistment with the specified access.                                                                                                                                                                                                                                                                       |
| [**GetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation) | Retrieves an opaque structure of recovery data from KTM. Recovery information is stored in a log on behalf of a RM by calling the [**SetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation) function. After a failure, the RM can use the [**GetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation) function to retrieve the information. |
| [**OpenEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-openenlistment)                                          | Opens an existing enlistment object, and returns a handle to the enlistment.                                                                                                                                                                                                                                                                                                         |
| [**PrepareEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-prepareenlistment)                                    | Called by superior TM to indicate that their pre-prepares work has been completed.                                                                                                                                                                                                                                                                                                   |
| [**PrePrepareEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-preprepareenlistment)                              | Called by superior TM to indicate that their pre-prepares work has been completed.                                                                                                                                                                                                                                                                                                   |
| [**RecoverEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-recoverenlistment)                                    | Recovers an enlistment's state.                                                                                                                                                                                                                                                                                                                                                      |
| [**ReadOnlyEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-readonlyenlistment)                                  | Requests that the specified enlistment be converted to a read-only enlistment. A read-only enlistment cannot participate in the outcome of the transaction and is not durably recorded for recovery.                                                                                                                                                                                 |
| [**RollbackEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackenlistment)                                  | Rolls back the specified transaction that is associated with an enlistment. This function cannot be called for read-only enlistments.                                                                                                                                                                                                                                                |
| [**SetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation)      | Sets an opaque, user-defined structure of recovery data from KTM. Recovery information is stored in a log on behalf of a RM by calling [**SetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation). After a failure, the RM can use [**GetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation) to retrieve the information.                  |
| [**SinglePhaseReject**](/windows/desktop/api/Ktmw32/nf-ktmw32-singlephasereject)                                    | Indicates that the RM is refusing a single-phase request. When a TM receives this call, it initiates a two-phase commit and sends a prepare request to all enlisted RMs.                                                                                                                                                                                                             |



 

The following functions are used with resource managers.



| Function                                                                           | Description                                                                                                                                                      |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-createresourcemanager)                             | Creates a new RM object, and associates the RM with a transaction manager (TM).                                                                                  |
| [**GetNotificationResourceManager**](/windows/desktop/api/KtmW32/nf-ktmw32-getnotificationresourcemanager)           | Requests and receives a notification for RM. This function is used by the RM register to receive notifications when a transaction changes state.                 |
| [**GetNotificationResourceManagerAsync**](/windows/desktop/api/KtmW32/nf-ktmw32-getnotificationresourcemanagerasync) | Requests and receives asynchronous notification for a RM. This function is used by the RM to register to receive notifications when a transaction changes state. |
| [**OpenResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-openresourcemanager)                                 | Opens an existing RM.                                                                                                                                            |
| [**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete)                                         | Indicates that the RM has completed all processing necessary to guarantee that a commit or abort operation will succeed for the specified transaction.           |
| [**PrePrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-prepreparecomplete)                                   | Signals that this RM has completed its preprepare work, so that other RMs can now begin their prepare operations.                                                |
| [**RecoverResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-recoverresourcemanager)                           | Recovers a RM's state from its log file.                                                                                                                         |
| [**SetResourceManagerCompletionPort**](/windows/desktop/api/Ktmw32/nf-ktmw32-setresourcemanagercompletionport)       | Associates the specified I/O completion port with the specified RM. This port receives all notifications for the RM.                                             |



 

The following functions are used with transaction managers.



| Function                                                                            | Description                                                                 |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**CreateTransactionManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-createtransactionmanager)                        | Creates a new TM object and returns a handle with the specified access.     |
| [**GetCurrentClockTransactionManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-getcurrentclocktransactionmanager) | Obtains a virtual clock value from a TM.                                    |
| [**GetTransactionManagerId**](/windows/desktop/api/Ktmw32/nf-ktmw32-gettransactionmanagerid)                          | Obtains an identifier for the specified TM.                                 |
| [**OpenTransactionManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-opentransactionmanager)                            | Opens an existing TM.                                                       |
| [**OpenTransactionManagerById**](/windows/desktop/api/Ktmw32/nf-ktmw32-opentransactionmanagerbyid)                    | Opens an existing TM.                                                       |
| [**RecoverTransactionManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-recovertransactionmanager)                      | Recovers a TM's state from its log file.                                    |
| [**RenameTransactionManager**](/windows/desktop/api/KtmW32/nf-ktmw32-renametransactionmanager)                        | Renames a TM.                                                               |
| [**RollforwardTransactionManager**](/windows/desktop/api/KtmW32/nf-ktmw32-rollforwardtransactionmanager)              | Recovers TM's state from its log file to the specified virtual clock value. |



 

 

 



