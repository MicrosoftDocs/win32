---
Description: A transaction manager (TM) is an instance of a log. In KTM, the TM objects specify the log and some of the functionality of the TM. There are typically many TM objects on a particular node. Resource managers (RMs) must be associated with a specific TM.
ms.assetid: 8d43977a-84cf-4109-b7db-f9c94a226c5d
title: Transaction Managers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Transaction Managers

A transaction manager (TM) is an instance of a log. In KTM, the TM objects specify the log and some of the functionality of the TM. There are typically many TM objects on a particular node. Resource managers (RMs) must be associated with a specific TM. There are three types of TMs:

-   A volatile TM, which has no log.
-   A regular TM, which has a log and is used to coordinate the transactions of one or more RMs.
-   A superior transaction manager.

## Volatile Transaction Managers

A volatile TM is a TM for read-only or volatile RMs. It does not have a log and does not persist the state of transactions across system restarts.

## Transaction Managers

TMs have a log, one or more durable or volatile RMs, or both. The TM will persist the state of a transaction across system restarts until the transactions are completed. A presumed-abort model is used, so transactions which were active but not prepared when the TM object is shut down are rolled back. When you open a TM for the first time, you must recover the TM by calling the [**RecoverTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-recovertransactionmanager?branch=master) function.

## Superior Transaction Managers

A superior TM is a TM for other TMs. It coordinates transactions. It also issues **TRANSACTION\_NOTIFY\_PREPARE** notifications to the Kernel Transaction Manager (KTM). An example of a superior TM is the Microsoft Distributed Transaction Coordinator (DTC). This ability comes with an added recovery-time responsibility. During recovery, the RM must first call the [**OpenEnlistment**](/windows/win32/Ktmw32/nf-ktmw32-openenlistment?branch=master) function to re-open the enlistment. It must also deliver (or re-deliver) the transaction's outcome if the transaction was committed; it is free to deliver an outcome by calling either the [**CommitTransaction**](/windows/win32/Ktmw32/nf-ktmw32-committransaction?branch=master) function or the [**RollbackTransaction**](/windows/win32/Ktmw32/nf-ktmw32-rollbacktransaction?branch=master) function. This obligation does not end until it has received an associated **TRANSACTION\_NOTIFY\_COMMIT\_COMPLETE** or **TRANSACTION\_NOTIFY\_ROLLBACK\_COMPLETE** notification event.If a superior TM fails to perform these operations at recovery time, the KTM will clean up any transactions that have not received outcomes by the end of the recovery phase. However, this can result in inconsistent transaction outcomes.

## Transaction Manager Functions

The following functions are used with transaction managers.



| Function                                                                            | Description                                                                                    |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**CreateTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-createtransactionmanager?branch=master)                        | Creates a new transaction manager (TM) object and returns a handle with the specified access.  |
| [**GetCurrentClockTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-getcurrentclocktransactionmanager?branch=master) | Obtains a virtual clock value from a transaction manager.                                      |
| [**GetTransactionManagerId**](/windows/win32/Ktmw32/nf-ktmw32-gettransactionmanagerid?branch=master)                          | Obtains an identifier for the specified transaction manager.                                   |
| [**OpenTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-opentransactionmanager?branch=master)                            | Opens an existing transaction manager.                                                         |
| [**RecoverTransactionManager**](/windows/win32/Ktmw32/nf-ktmw32-recovertransactionmanager?branch=master)                      | Recovers a transaction manager's state from its log file.                                      |
| [**RollforwardTransactionManager**](/windows/win32/KtmW32/nf-ktmw32-rollforwardtransactionmanager?branch=master)              | Recovers a transaction manager's state from its log file to the specified virtual clock value. |



 

 

 



