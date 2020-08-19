---
title: Object Management
description: This section covers the correct use of Windows Filtering Platform (WFP) API object types.
ms.assetid: '2625ef9a-0e62-4e21-ba93-047965d0d782'
ms.topic: article
ms.date: 05/31/2018
---

# Object Management

This section covers the correct use of Windows Filtering Platform (WFP) API object types.

## Sessions

The WFP API is session-oriented, and most function calls are made within the context of a session. A new client session is created by calling [**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0). The session ends either when the client calls [**FwpmEngineClose0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineclose0) or the client process terminates. When a session is destroyed, either on purpose or by the RPC rundown, the Base Filtering Engine (BFE) first aborts any existing transaction.

When creating a new session, the caller can create a dynamic session by passing the [**FWPM\_SESSION\_FLAG\_DYNAMIC**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_session0) flag to [**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0). Any objects added during a dynamic session are automatically deleted when the session ends.

## Transactions

The WFP API is transactional, and most function calls are made within the context of a transaction. Callers can use [**FwpmTransactionBegin0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionbegin0), [**FwpmTransactionCommit0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactioncommit0), and [**FwpmTransactionAbort0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionabort0) to explicitly control transactions. However, if a function call is made outside of an explicit transaction, it will be executed within an implicit transaction. If a transaction is in progress, when a session terminates, it is automatically aborted. Implicit transactions are never forcibly aborted.

Transactions are either read-only or read/write and enforce rigorous Atomic Consistent Isolated Durable ([ACID](../cossdk/acid-properties.md)) semantics.

Each client session can have only one transaction in progress at a time. If the caller attempts to begin a second transaction before committing or aborting the first, BFE returns an error.

If an operation fails during the course of a transaction, it does not affect the overall state of the transaction. For example, suppose the client begins a transaction and successfully calls [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0) three times before a fourth call fails. The client now has the option of:

-   Aborting the transaction, in which case none of the filters will be added.
-   Committing the transaction, in which case the first three filters will be added.
-   Continuing with more operations including potentially retrying the failed [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0).

When beginning a transaction, BFE will wait until the session's [**txnWaitTimeoutInMSec**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_session0) expires to acquire the lock. If the lock is not acquired within this time, the lock acquisition (and the [**FwpmTransactionBegin0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionbegin0) call) will fail. This prevents clients from indefinitely failing to respond. If the client did not specify a lock timeout, it defaults to 15 seconds.

Each transaction also has a lock timeout. This is the maximum amount of time that it can own the lock. If the owner does not release the lock within this time, the transaction is forcibly aborted, causing the lock to be released. The lock timeout is not configurable. It is infinite for kernel-mode callers and one hour for user-mode callers. If a transaction is forcibly aborted, the next call made within that transaction will fail with **FWP\_E\_TXN\_ABORTED**.

## Object Lifetimes

Objects can have one of four possible lifetimes:

-   Dynamic — An object is dynamic only if it is added using a dynamic session handle. Dynamic objects live until they are deleted or the owning session terminates.
-   Static — Objects are static by default. Static objects live until they are deleted, BFE stops, or the system is shutdown.
-   Persistent — Persistent objects are created by passing the appropriate **FWPM\_\*\_FLAG\_PERSISTENT** flag to an **Fwpm\*Add0** function. Persistent objects live until they are deleted.
-   Built-in — Built-in objects are predefined by BFE and cannot be added or deleted. They live forever.

Filters in kernel-mode layers can be marked as boot-time filters by passing the appropriate flag to [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0). Boot-time filters are added to the system when the TCP/IP driver starts, and removed when BFE finishes initialization. Persistent objects are added when BFE starts.

In many cases, a policy provider may not want its persistent policy enforced if the provider has been disabled. When adding a provider, the caller can specify an optional Windows service name. When adding persistent objects, the caller can optionally specify the provider that "owns" that object. At service start, BFE only adds persistent objects to the system if they are not associated with a provider, or the associated provider has no Windows service name, or the associated Windows service is set to auto-start.

## Object Associations

Some objects have references to other objects. For example, a filter always references a layer and may reference a callout and a provider context. Objects cannot refer to objects that may have a shorter lifetime. Thus, a dynamic object cannot refer to a dynamic object from a different session. A static object cannot refer to a dynamic object. A persistent object cannot refer to a dynamic object, a static object, or a persistent object owned by a different provider.

An object cannot be deleted until all objects that reference it have first been deleted.

## LUIDs and GUIDs

All user mode WFP API objects (FWPM) are identified by a globally unique identifier (**GUID**) and reference other objects by their **GUID**s. The **GUID** need only be unique within the object type. For example, a filter and a provider context can have the same **GUID**, but two filters cannot. When adding a new object, callers can assign the object's **GUID** or leave it zero-initialized and let BFE assign the **GUID**.

All kernel mode WFP API objects (FWPS) are identified by a locally unique identifier (**LUID**) and reference other objects by their LUID. The switch from **GUID** to **LUID** enables WFP to conserve non-paged pool and optimize run-time processing. The width of the **LUID** depends on the object type and ranges from a **UINT16** to a **UINT64**. **LUID**s are always assigned by BFE.

 

 