---
description: A resource manager enlists in a transaction when it begins participation in that particular transaction.
ms.assetid: 9c201699-c00b-4efe-9f30-8d4e182de785
title: Enlistments
ms.topic: article
ms.date: 05/31/2018
---

# Enlistments

A resource manager enlists in a transaction when it begins participation in that particular transaction. The enlistment defines which notifications the resource manager accepts. A resource manager creates an enlistment object when it enlists in a transaction. This object signals to KTM that the resource manager (RM) is requesting notifications about the specified transaction.

The RM provides a [**NOTIFICATION\_MASK**](notification-mask.md) structure that details which notifications it is requesting.

## Enlistment Functions

The following functions are used with enlistments.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete)                                          | Indicates that a resource manager (RM) has finished committing a transaction that was requested by the transaction manager (TM).                                                                                                                                                                                                                                                                        |
| [**CreateEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-createenlistment)                                      | Creates an enlistment, sets its initial state, and opens a handle to the enlistment with the specified access.                                                                                                                                                                                                                                                                                          |
| [**GetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation) | Retrieves an opaque structure of recovery data from KTM. Recovery information is stored in a log on behalf of a resource manager (RM) by calling the [**SetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation) function. After a failure, the RM can use the [**GetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation) function to retrieve the information. |
| [**OpenEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-openenlistment)                                          | Opens an existing enlistment object, and returns a handle to the enlistment.                                                                                                                                                                                                                                                                                                                            |
| [**ReadOnlyEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-readonlyenlistment)                                  | Requests that the specified enlistment be converted to a read-only enlistment. A read-only enlistment cannot participate in the outcome of the transaction and is not durably recorded for recovery.                                                                                                                                                                                                    |
| [**RollbackEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackenlistment)                                  | Rolls back the specified transaction that is associated with an enlistment. This function cannot be called for read-only enlistments.                                                                                                                                                                                                                                                                   |
| [**SetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation)      | Sets an opaque, user-defined structure of recovery data from KTM. Recovery information is stored in a log on behalf of a resource manager (RM) by calling [**SetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-setenlistmentrecoveryinformation). After a failure, the RM can use [**GetEnlistmentRecoveryInformation**](/windows/desktop/api/Ktmw32/nf-ktmw32-getenlistmentrecoveryinformation) to retrieve the information.                  |
| [**SinglePhaseReject**](/windows/desktop/api/Ktmw32/nf-ktmw32-singlephasereject)                                    | Indicates that the resource manager (RM) is refusing a single-phase request. When a transaction manager (TM) receives this call, it initiates a two-phase commit and sends a prepare request to all enlisted RMs.                                                                                                                                                                                       |



 

 

 



