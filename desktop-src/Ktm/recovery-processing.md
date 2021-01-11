---
description: After any type of failure that disrupts normal transaction processing, KTM and each resource manager must perform recovery operations. Recovery is the process by which transaction participants arrive at a consistent view of each transactions state.
ms.assetid: 5bc9a155-6ba4-41f8-8e12-e87f48d83940
title: Recovery Processing
ms.topic: article
ms.date: 05/31/2018
---

# Recovery Processing

After any type of failure that disrupts normal transaction processing, KTM and each resource manager must perform *recovery* operations. Recovery is the process by which transaction participants arrive at a consistent view of each transaction's state.

Resource managers may be *in-doubt* about a transaction's outcome, meaning that at the time of failure, they had received a TRANSACTION\_NOTIFY\_PREPARE notification, had prepared to durable storage, but had not received (or received but not logged) a final outcome for the transaction. Similarly, KTM can be in-doubt about a transaction if it had been prepared but had not received (or received but not logged) an outcome. At recovery time, all outcomes that have been sent but not acknowledged must be re-sent. For example, if a resource manager received a TRANSACTION\_NOTIFY\_COMMIT notification and called the [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete) function, the RM may still receive a duplicate TRANSACTION\_NOTIFY\_COMMIT notification at recovery time.

For a transaction to properly recover after a resource manager or system failure, each resource manager must do the following each time it is started:

1.  Call the [**OpenResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-openresourcemanager) function to re-open its resource manager handle using its unique, persistent name. This informs KTM that the resource manager is running again and is available to perform recovery. If no enlistments exist to be recovered, the call to **OpenResourceManager** can fail. Call [**CreateResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-createresourcemanager) to re-create the RM object.
2.  Call [**RecoverResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-recoverresourcemanager). The resource manager will receive a [**TRANSACTION\_NOTIFY\_RECOVER**](notification-mask.md) notification event for each enlistment for which it needs to perform recovery operations, followed by a TRANSACTION\_NOTIFY\_LAST\_RECOVER. The notification event includes a globally unique identifier for both the transaction and the enlistment.
3.  Call the [**OpenEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-openenlistment) function to re-open each enlistment handle for which the resource manager received a TRANSACTION\_NOTIFY\_RECOVER notification.
4.  For each enlistment opened by [**OpenEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-openenlistment), call [**RecoverEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-recoverenlistment). This causes the TRANSACTION\_NOTIFY\_COMMIT or TRANSACTION\_NOTIFY\_INDOUBT notification to be redelivered.
5.  If the RM received TRANSACTION\_NOTIFY\_COMMIT, the RM can complete the transaction by calling [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete).

    If the RM received TRANSACTION\_NOTIFY\_INDOUBT, the RM should wait for the outcome notification to arrive.

6.  For any transactions that the RM does not receive a TRANSACTION\_NOTIFY\_RECOVER notification, but previously received a TRANSACTION\_NOTIFY\_PREPARE notification for, the RM should process the transaction as if it were rolled back.

> [!Note]
>
> Resource managers are allowed to enlist in or create new transactions while in the process of performing recovery.

 

KTM uses a *presumed abort* transaction model. The following scenario illustrates this behavior. Assume that KTM and an resource manager exist on the same computer. Suppose KTM issues a prepare notification for a transaction, but the system crashes before KTM logs the prepare notification. Further suppose that the resource manager receives and logs the prepare notification just before the system crashes. After the system is restored, KTM has no knowledge of the transaction, because it never logged the prepare phase. The resource manager has knowledge of the transaction, because it received, processed, and logged the prepare notification. When KTM issues its recovery notifications, the resource manager does not include a recovery notification for the transaction in question. With the presumed abort model, the resource manager in this case will treat the prepared transaction as aborted when it does not receive notifications to perform recovery on that transaction.

 

 



