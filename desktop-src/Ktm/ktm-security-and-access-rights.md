---
description: The Windows security model enables callers of Kernel Transaction Manager (KTM) to control access to transaction, transaction manager, resource manager, and enlistment objects.
ms.assetid: c9d51d4d-9f07-44d6-a2e1-4a47367cc4ae
title: KTM Security and Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# KTM Security and Access Rights

The Windows security model enables callers of Kernel Transaction Manager (KTM) to control access to transaction, transaction manager, resource manager, and enlistment objects. For more information, see [Access-Control Model](/windows/desktop/SecAuthZ/access-control-model). For applications that are not concerned about security, transactions can be created with permissive access control lists (ACLs) that allow any resource manager to enlist on a transaction.

## Transactions

When a client uses the [**OpenTransaction**](/windows/desktop/api/Ktmw32/nf-ktmw32-opentransaction) function, the system checks the requested access rights against the security descriptor for the transaction object.

The valid access rights for transaction objects include the ability to query and set information, enlist, and various transaction operations, as well as [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights). [**Transaction Access Masks**](transaction-access-masks.md) list the specific access rights for a transaction.

Because transactions have a durable state, it is critical that RMs and TMs that interact with the KTM fulfill their obligations with regard to recovery. Failure to fulfill these obligations can result in resource leaks that are not cleaned up, even by a system reboot. Consider the effect of a persistent leak or malicious code that caused the KTM to consume kernel resources until it resulted in a system failure; after the resulting reboot, the KTM would read its log and re-create all the persistent objects, potentially causing the same system failure to recur. Quota-based throttling will prevent persistent resource starvation from a rogue or ill-behaving RM. Finally, administrative mechanisms must be created that allow for the detection and correction of such persistent leaks.

## Transaction Managers

When a client uses the [**OpenTransactionManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-opentransactionmanager) function, the system checks the requested access rights against the security descriptor for the resource manager object.

The valid access rights for transaction manager objects include the ability to query and set information, create RMs, and recover and rename operations, as well as [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights). [**Transaction Manager Access Masks**](transaction-manager-access-masks.md) lists the specific access rights for a transaction manager.

A resource manager can create its own transaction manager objects with restrictive ACLs to limit which resource managers can participate in transactions that use that transaction manager's log.

## Resource Managers

When a client uses the [**OpenResourceManager**](/windows/desktop/api/Ktmw32/nf-ktmw32-openresourcemanager) function, the system checks the requested access rights against the security descriptor for the resource manager object.

The valid access rights for resource manager objects include the ability to query and set information, recover, enlist, registration operations, and propagation and recover operations, as well as [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights). [**Resource Manager Access Masks**](resource-manager-access-masks.md) lists the specific access rights for a resource manager.

A resource manager can create its own resource manager objects with restrictive ACLs if it wishes to prevent malicious code from intercepting notifications or forcing particular transactional outcomes.

## Enlistments

When a client uses the [**OpenEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-openenlistment) function, the system checks the requested access rights against the security descriptor for the enlistment object.

The valid access rights for enlistment objects include the ability to query and set information, recover operations, as well as [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights). [**Enlistment Access Masks**](enlistment-access-masks.md) lists the specific access rights for an enlistment.

 

 
