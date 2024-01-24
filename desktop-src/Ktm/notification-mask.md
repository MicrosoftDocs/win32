---
description: Lists the different types of notifications that can be received by an enlistment.
ms.assetid: 65db8ba5-193c-439b-8e8c-6cb4a9bd4efd
title: NOTIFICATION_MASK (KtmTypes.h)
ms.topic: reference
ms.date: 05/31/2018
---

# NOTIFICATION\_MASK

Lists the different types of notifications that can be received by an enlistment.

<dl> <dt>

<span id="TRANSACTION_NOTIFY_MASK"></span><span id="transaction_notify_mask"></span>**TRANSACTION\_NOTIFY\_MASK**
</dt> <dd> <dl> <dt>

0x3FFFFFFF
</dt> <dt>



A mask that indicates all valid bits for a transaction notification.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_PREPREPARE"></span><span id="transaction_notify_preprepare"></span>**TRANSACTION\_NOTIFY\_PREPREPARE**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



This notification is called after a client calls [**CommitTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-committransaction) and either no resource manager (RM) supports single-phase commit or a superior transaction manager (TM) calls [**PrePrepareEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-preprepareenlistment). This notification is received by the RMs indicating that they should complete any work that could cause other RMs to need to enlist in a transaction, such as flushing its cache. After completing these operations the RM must call [**PrePrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-prepreparecomplete). To receive this notification the RM must also support **TRANSACTION\_NOTIFY\_PREPARE** and **TRANSACTION\_NOTIFY\_COMMIT**.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_PREPARE"></span><span id="transaction_notify_prepare"></span>**TRANSACTION\_NOTIFY\_PREPARE**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



This notification is called after the **TRANSACTION\_NOTIFY\_PREPREPARE** processing is complete. It signals the RM to complete all the work that is associated with this enlistment so that it can guarantee that a commit operation could succeed and an abort operation could also succeed. Typically, the bulk of the work for a transaction is done during the prepare phase. For durable RMs, they must log their state prior to calling the [**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete) function. This is the last chance for the RM to request that the transaction be rolled back.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_COMMIT"></span><span id="transaction_notify_commit"></span>**TRANSACTION\_NOTIFY\_COMMIT**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



This notification signals the RM to complete all the work that is associated with this enlistment. Typically, the RM releases any locks, releases any information necessary to roll back the transaction. The RM must respond by calling the [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete) function when it has finished these operations.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_ROLLBACK"></span><span id="transaction_notify_rollback"></span>**TRANSACTION\_NOTIFY\_ROLLBACK**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



This notification signals the RM to undo all the work it has done that is associated with the transaction.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_PREPREPARE_COMPLETE"></span><span id="transaction_notify_preprepare_complete"></span>**TRANSACTION\_NOTIFY\_PREPREPARE\_COMPLETE**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



This notification signals to the superior TM that a pre-prepare operation was completed successfully.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_PREPARE_COMPLETE"></span><span id="transaction_notify_prepare_complete"></span>**TRANSACTION\_NOTIFY\_PREPARE\_COMPLETE**
</dt> <dd> <dl> <dt>

0x00000020
</dt> <dt>



This notification signals to the superior TM that a prepare operation was completed successfully.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_COMMIT_COMPLETE"></span><span id="transaction_notify_commit_complete"></span>**TRANSACTION\_NOTIFY\_COMMIT\_COMPLETE**
</dt> <dd> <dl> <dt>

0x00000040
</dt> <dt>



This notification signals to the superior TM that a commit operation was completed successfully.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_ROLLBACK_COMPLETE"></span><span id="transaction_notify_rollback_complete"></span>**TRANSACTION\_NOTIFY\_ROLLBACK\_COMPLETE**
</dt> <dd> <dl> <dt>

0x00000080
</dt> <dt>



This notification signals to the superior TM that a rollback operation was completed successfully.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_RECOVER"></span><span id="transaction_notify_recover"></span>**TRANSACTION\_NOTIFY\_RECOVER**
</dt> <dd> <dl> <dt>

0x00000100
</dt> <dt>



This notification signals to RMs that they should recover their state because a transaction outcome must be redelivered. For example, when an RM is recovered, and when there are transactions left in-doubt. This notification is delivered once the in-doubt state is resolved.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_SINGLE_PHASE_COMMIT"></span><span id="transaction_notify_single_phase_commit"></span>**TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT**
</dt> <dd> <dl> <dt>

0x00000200
</dt> <dt>



This notification signals the RM to complete and commit the transaction without using a two-phase commit protocol. If the RM wants to use a two-phase operation, it must respond by calling the [**SinglePhaseReject**](/windows/desktop/api/Ktmw32/nf-ktmw32-singlephasereject) function.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_DELEGATE_COMMIT"></span><span id="transaction_notify_delegate_commit"></span>**TRANSACTION\_NOTIFY\_DELEGATE\_COMMIT**
</dt> <dd> <dl> <dt>

0x00000400
</dt> <dt>



KTM is signaling to the superior TM to perform a commit operation.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_RECOVER_QUERY"></span><span id="transaction_notify_recover_query"></span>**TRANSACTION\_NOTIFY\_RECOVER\_QUERY**
</dt> <dd> <dl> <dt>

0x00000800
</dt> <dt>



KTM is signaling to the superior TM to query the status of an in-doubt transaction.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_ENLIST_PREPREPARE"></span><span id="transaction_notify_enlist_preprepare"></span>**TRANSACTION\_NOTIFY\_ENLIST\_PREPREPARE**
</dt> <dd> <dl> <dt>

0x00001000
</dt> <dt>



This notification signals to the superior TM that pre-prepare notifications must be delivered on the specified enlistment.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_LAST_RECOVER"></span><span id="transaction_notify_last_recover"></span>**TRANSACTION\_NOTIFY\_LAST\_RECOVER**
</dt> <dd> <dl> <dt>

0x00002000
</dt> <dt>



This notification indicates that the recovery operation is complete for this RM.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_INDOUBT"></span><span id="transaction_notify_indoubt"></span>**TRANSACTION\_NOTIFY\_INDOUBT**
</dt> <dd> <dl> <dt>

0x00004000
</dt> <dt>



The specified transaction is in an in-doubt state. The RM receives this notification during recovery operations when a transaction has been prepared, but there is no superior transaction manager (TM) available. For example, when a transaction involves a remote TM and that node is unavailable, its node is unavailable, or the local [Distributed Transaction Coordinator](/previous-versions/windows/desktop/ms684146(v=vs.85)) service is unavailable, the transaction state is in-doubt.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_TM_ONLINE"></span><span id="transaction_notify_tm_online"></span>**TRANSACTION\_NOTIFY\_TM\_ONLINE**
</dt> <dd> <dl> <dt>

0x02000000
</dt> <dt>



The TM is online and accepting requests.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_REQUEST_OUTCOME"></span><span id="transaction_notify_request_outcome"></span>**TRANSACTION\_NOTIFY\_REQUEST\_OUTCOME**
</dt> <dd> <dl> <dt>

0x20000000
</dt> <dt>



Signals to RMs that there is outcome information available, and that a request for that information should be made.


</dt> </dl> </dd> <dt>

<span id="TRANSACTION_NOTIFY_COMMIT_FINALIZE"></span><span id="transaction_notify_commit_finalize"></span>**TRANSACTION\_NOTIFY\_COMMIT\_FINALIZE**
</dt> <dd> <dl> <dt>

0x40000000
</dt> <dt>



Reserved.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                            |
| Header<br/>                   | <dl> <dt>KtmTypes.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator](/previous-versions/windows/desktop/ms684146(v=vs.85))
</dt> <dt>

[Kernel Transaction Manager Constants](kernel-transaction-manager-constants.md)
</dt> <dt>

[**CreateEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-createenlistment)
</dt> <dt>

[**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete)
</dt> <dt>

[**GetNotificationResourceManager**](/windows/desktop/api/KtmW32/nf-ktmw32-getnotificationresourcemanager)
</dt> <dt>

[**GetNotificationResourceManagerAsync**](/windows/desktop/api/KtmW32/nf-ktmw32-getnotificationresourcemanagerasync)
</dt> <dt>

[**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete)
</dt> <dt>

[**SinglePhaseReject**](/windows/desktop/api/Ktmw32/nf-ktmw32-singlephasereject)
</dt> <dt>

[**TRANSACTION\_NOTIFICATION**](/windows/desktop/api/KtmTypes/ns-ktmtypes-transaction_notification)
</dt> </dl>

 

