---
Description: 'A resource manager enlists in a transaction when it begins participation in that particular transaction.'
ms.assetid: '9c201699-c00b-4efe-9f30-8d4e182de785'
title: Enlistments
---

# Enlistments

A resource manager enlists in a transaction when it begins participation in that particular transaction. The enlistment defines which notifications the resource manager accepts. A resource manager creates an enlistment object when it enlists in a transaction. This object signals to KTM that the resource manager (RM) is requesting notifications about the specified transaction.

The RM provides a [**NOTIFICATION\_MASK**](notification-mask.md) structure that details which notifications it is requesting.

## Enlistment Functions

The following functions are used with enlistments.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitComplete**](commitcomplete.md)                                          | Indicates that a resource manager (RM) has finished committing a transaction that was requested by the transaction manager (TM).                                                                                                                                                                                                                                                                        |
| [**CreateEnlistment**](createenlistment.md)                                      | Creates an enlistment, sets its initial state, and opens a handle to the enlistment with the specified access.                                                                                                                                                                                                                                                                                          |
| [**GetEnlistmentRecoveryInformation**](getenlistmentrecoveryinformation-func.md) | Retrieves an opaque structure of recovery data from KTM. Recovery information is stored in a log on behalf of a resource manager (RM) by calling the [**SetEnlistmentRecoveryInformation**](setenlistmentrecoveryinformation.md) function. After a failure, the RM can use the [**GetEnlistmentRecoveryInformation**](getenlistmentrecoveryinformation-func.md) function to retrieve the information. |
| [**OpenEnlistment**](openenlistment.md)                                          | Opens an existing enlistment object, and returns a handle to the enlistment.                                                                                                                                                                                                                                                                                                                            |
| [**ReadOnlyEnlistment**](readonlyenlistment.md)                                  | Requests that the specified enlistment be converted to a read-only enlistment. A read-only enlistment cannot participate in the outcome of the transaction and is not durably recorded for recovery.                                                                                                                                                                                                    |
| [**RollbackEnlistment**](rollbackenlistment.md)                                  | Rolls back the specified transaction that is associated with an enlistment. This function cannot be called for read-only enlistments.                                                                                                                                                                                                                                                                   |
| [**SetEnlistmentRecoveryInformation**](setenlistmentrecoveryinformation.md)      | Sets an opaque, user-defined structure of recovery data from KTM. Recovery information is stored in a log on behalf of a resource manager (RM) by calling [**SetEnlistmentRecoveryInformation**](setenlistmentrecoveryinformation.md). After a failure, the RM can use [**GetEnlistmentRecoveryInformation**](getenlistmentrecoveryinformation-func.md) to retrieve the information.                  |
| [**SinglePhaseReject**](singlephasereject.md)                                    | Indicates that the resource manager (RM) is refusing a single-phase request. When a transaction manager (TM) receives this call, it initiates a two-phase commit and sends a prepare request to all enlisted RMs.                                                                                                                                                                                       |



 

 

 



