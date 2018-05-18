---
Description: 'The following functions are used with transactions.'
ms.assetid: 'e9704ea8-e67d-4278-b77e-1d4787224d52'
title: Kernel Transaction Manager Functions
---

# Kernel Transaction Manager Functions

The following functions are used with transactions.



| Function                                                            | Description                                                                                     |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**CommitTransaction**](committransaction.md)                      | Requests that the specified transaction be committed.                                           |
| [**CommitTransactionAsync**](committransactionasync.md)            | Requests that the specified transaction be committed.                                           |
| [**CreateTransaction**](createtransaction.md)                      | Creates a new transaction object.                                                               |
| [**GetTransactionId**](gettransactionid.md)                        | Obtains the ID for the specified transaction.                                                   |
| [**GetTransactionInformation**](gettransactioninformation-func.md) | Returns the requested information about the specified transaction.                              |
| [**OpenTransaction**](opentransaction.md)                          | Opens an existing transaction.                                                                  |
| [**RollbackComplete**](rollbackcomplete.md)                        | Indicates that the resource manager (RM) has successfully completed rolling back a transaction. |
| [**RollbackTransaction**](rollbacktransaction.md)                  | Requests that the specified transaction be rolled back.                                         |
| [**RollbackTransactionAsync**](rollbacktransactionasync.md)        | Requests that the specified transaction be rolled back. This function returns asynchronously.   |
| [**SetTransactionInformation**](settransactioninformation.md)      | Sets the transaction information for the specified transaction.                                 |



 

The following functions are used with enlistments.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitComplete**](commitcomplete.md)                                          | Indicates that a RM has finished committing a transaction that was requested by the transaction manager (TM).                                                                                                                                                                                                                                                                        |
| [**CommitEnlistment**](commitenlistment.md)                                      | Commits the transaction for the specified enlistment.                                                                                                                                                                                                                                                                                                                                |
| [**GetEnlistmentId**](getenlistmentid.md)                                        | Obtains the ID for the specified enlistment.                                                                                                                                                                                                                                                                                                                                         |
| [**CreateEnlistment**](createenlistment.md)                                      | Creates an enlistment, sets its initial state, and opens a handle to the enlistment with the specified access.                                                                                                                                                                                                                                                                       |
| [**GetEnlistmentRecoveryInformation**](getenlistmentrecoveryinformation-func.md) | Retrieves an opaque structure of recovery data from KTM. Recovery information is stored in a log on behalf of a RM by calling the [**SetEnlistmentRecoveryInformation**](setenlistmentrecoveryinformation.md) function. After a failure, the RM can use the [**GetEnlistmentRecoveryInformation**](getenlistmentrecoveryinformation-func.md) function to retrieve the information. |
| [**OpenEnlistment**](openenlistment.md)                                          | Opens an existing enlistment object, and returns a handle to the enlistment.                                                                                                                                                                                                                                                                                                         |
| [**PrepareEnlistment**](prepareenlistment.md)                                    | Called by superior TM to indicate that their pre-prepares work has been completed.                                                                                                                                                                                                                                                                                                   |
| [**PrePrepareEnlistment**](preprepareenlistment.md)                              | Called by superior TM to indicate that their pre-prepares work has been completed.                                                                                                                                                                                                                                                                                                   |
| [**RecoverEnlistment**](recoverenlistment.md)                                    | Recovers an enlistment's state.                                                                                                                                                                                                                                                                                                                                                      |
| [**ReadOnlyEnlistment**](readonlyenlistment.md)                                  | Requests that the specified enlistment be converted to a read-only enlistment. A read-only enlistment cannot participate in the outcome of the transaction and is not durably recorded for recovery.                                                                                                                                                                                 |
| [**RollbackEnlistment**](rollbackenlistment.md)                                  | Rolls back the specified transaction that is associated with an enlistment. This function cannot be called for read-only enlistments.                                                                                                                                                                                                                                                |
| [**SetEnlistmentRecoveryInformation**](setenlistmentrecoveryinformation.md)      | Sets an opaque, user-defined structure of recovery data from KTM. Recovery information is stored in a log on behalf of a RM by calling [**SetEnlistmentRecoveryInformation**](setenlistmentrecoveryinformation.md). After a failure, the RM can use [**GetEnlistmentRecoveryInformation**](getenlistmentrecoveryinformation-func.md) to retrieve the information.                  |
| [**SinglePhaseReject**](singlephasereject.md)                                    | Indicates that the RM is refusing a single-phase request. When a TM receives this call, it initiates a two-phase commit and sends a prepare request to all enlisted RMs.                                                                                                                                                                                                             |



 

The following functions are used with resource managers.



| Function                                                                           | Description                                                                                                                                                      |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateResourceManager**](createresourcemanager.md)                             | Creates a new RM object, and associates the RM with a transaction manager (TM).                                                                                  |
| [**GetNotificationResourceManager**](getnotificationresourcemanager.md)           | Requests and receives a notification for RM. This function is used by the RM register to receive notifications when a transaction changes state.                 |
| [**GetNotificationResourceManagerAsync**](getnotificationresourcemanagerasync.md) | Requests and receives asynchronous notification for a RM. This function is used by the RM to register to receive notifications when a transaction changes state. |
| [**OpenResourceManager**](openresourcemanager.md)                                 | Opens an existing RM.                                                                                                                                            |
| [**PrepareComplete**](preparecomplete.md)                                         | Indicates that the RM has completed all processing necessary to guarantee that a commit or abort operation will succeed for the specified transaction.           |
| [**PrePrepareComplete**](prepreparecomplete.md)                                   | Signals that this RM has completed its preprepare work, so that other RMs can now begin their prepare operations.                                                |
| [**RecoverResourceManager**](recoverresourcemanager.md)                           | Recovers a RM's state from its log file.                                                                                                                         |
| [**SetResourceManagerCompletionPort**](setresourcemanagercompletionport.md)       | Associates the specified I/O completion port with the specified RM. This port receives all notifications for the RM.                                             |



 

The following functions are used with transaction managers.



| Function                                                                            | Description                                                                 |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**CreateTransactionManager**](createtransactionmanager.md)                        | Creates a new TM object and returns a handle with the specified access.     |
| [**GetCurrentClockTransactionManager**](getcurrentclocktransactionmanager-func.md) | Obtains a virtual clock value from a TM.                                    |
| [**GetTransactionManagerId**](gettransactionmanagerid.md)                          | Obtains an identifier for the specified TM.                                 |
| [**OpenTransactionManager**](opentransactionmanager.md)                            | Opens an existing TM.                                                       |
| [**OpenTransactionManagerById**](opentransactionmanagerbyid.md)                    | Opens an existing TM.                                                       |
| [**RecoverTransactionManager**](recovertransactionmanager.md)                      | Recovers a TM's state from its log file.                                    |
| [**RenameTransactionManager**](renametransactionmanager.md)                        | Renames a TM.                                                               |
| [**RollforwardTransactionManager**](rollforwardtransactionmanager.md)              | Recovers TM's state from its log file to the specified virtual clock value. |



 

 

 



