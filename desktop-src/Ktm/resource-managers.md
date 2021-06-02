---
description: Resource Managers
ms.assetid: c717b731-cf0b-45cb-bbff-695410fcf6ce
title: Resource Managers
ms.topic: article
ms.date: 05/31/2018
---

# Resource Managers

A resource manager uses the transaction manager log to track the transaction state. The resource manager's action when processing a transaction is as follows:

-   The client passes a transaction to the RM explicitly.
-   The RM enlists in the transaction using [**CreateEnlistment**](/windows/desktop/api/KtmW32/nf-ktmw32-createenlistment).
-   The user can then proceed to perform any operation.
-   When the user calls CommitTransaction, KTM sends a PREPARE\_TRANSACTION notification to the RM. At this point, the RM flushes to disk any changes that would be necessary to commit the transaction, but could fail. If these operations succeed, the RM signals that it is finished with the prepare operation by calling [**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete). If these operations fail, the RM responds by calling [**RollBackEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackenlistment).
-   The resource manager receives a prepare notification.
-   The resource manager flushes any data associated with the transaction to its Common Log Services log file.
-   The resource manager calls the [**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete) function and awaits to receive the transaction's outcome from the KTM.
-   Depending on the outcome of the transaction, the resource manager receives a commit or rollback notification event. If the resource manager receives a commit notification, it makes the changes permanent and informs the KTM by calling the [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete) function. If the resource manager receives a rollback notification, it discards all changes and reverts to the state that existed before any of the transacted changes and informs the KTM by calling [**RollbackComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackcomplete).

## Resource Manager Functions

The following functions are used with resource managers.



| Function                                                                           | Description                                                                                                                                                                      |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-createresourcemanager)                             | Creates a new resource manager (RM) object, and associates the RM with a transaction manager (TM).                                                                               |
| [**GetNotificationResourceManager**](/windows/desktop/api/KtmW32/nf-ktmw32-getnotificationresourcemanager)           | Requests and receives a notification for a resource manager (RM). This function is used by the RM register to receive notifications when a transaction changes state.            |
| [**GetNotificationResourceManagerAsync**](/windows/desktop/api/KtmW32/nf-ktmw32-getnotificationresourcemanagerasync) | Requests and receives asynchronous notification for a resource manager (RM). This function is used by the RM register to receive notifications when a transaction changes state. |
| [**OpenResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-openresourcemanager)                                 | Opens an existing resource manager (RM).                                                                                                                                         |
| [**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete)                                         | Indicates that the resource manager (RM) has completed all processing necessary to guarantee that a commit or abort operation will succeed for the specified transaction.        |
| [**PrePrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-prepreparecomplete)                                   | Signals that this resource manager has completed its preprepare work, so that other resource managers can now begin their prepare operations.                                    |
| [**SetResourceManagerCompletionPort**](/windows/desktop/api/Ktmw32/nf-ktmw32-setresourcemanagercompletionport)       | Associates the specified I/O completion port with the specified resource manager (RM). This port receives all notifications for the RM.                                          |



 

 

 



