---
description: Transactional components that are to be pooled have special requirements.
ms.assetid: 32e2f830-c30a-4dbc-8e69-dd2038851998
title: Pooling Transactional Objects
ms.topic: article
ms.date: 05/31/2018
---

# Pooling Transactional Objects

Transactional components that are to be pooled have special requirements.

## Manually Enlisting Resources

Poolable objects that participate in transactions must manually enlist managed resources. If an object holds managed resources between clients, there will be no way for the resource manager to automatically enlist in a transaction when the object is activated in a given context.

The object itself must handle the logic of detecting the transaction, turning off the resource manager's auto-enlistment, and manually enlisting any resources that it holds. The steps for doing this are specific to the resource manager that you are using. If you need to do manual enlistment, consult the documentation for your resource manager.

As described below, objects can be pooled with transaction affinity while a transaction is active and can be activated with transaction affinity if called by a client associated with that transaction. Before enlisting resources, you should first check for transaction affinity. If the object has been taken from the pool specific to that transaction, it has already done work in that transaction and enlisted its resources.

## Turning Off Automatic Enlistment

Automatic enlistment should be turned off after the resource is acquired, usually in the object's constructor. That is, you disable automatic enlistment and then connect.

Disabling auto-enlistment can sometimes be a subtle procedure, particularly in the case of layered data access providers. Auto-enlistment is sometimes coupled with connection pooling, as with ODBC, and sometimes not, as with OLE DB. You might need to ensure that auto-enlistment is off at several levels of providers.

## Implementing IObjectControl

Poolable objects that participate in transactions must monitor the current state of resources they are holding. If the object detects that it is in a non-reusable state—for example, if a connection is bad—it should return False for [**IObjectControl::CanBePooled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-canbepooled). This will have the effect of both discarding the object instance and dooming the current transaction.

## Transaction-Specific Pools

A pool of objects is generally homogenous, and any pooled object not currently in use is good to return to any client. The only exception to this rule is in the case of transactional objects, for which object pooling is optimized. When the client requesting an object has an associated transaction, COM+ will scan the pool for an available object that is already associated with that transaction. If an object with transaction affinity is found, it is returned to the client; otherwise, an object from the general pool is returned.

In this manner, special subpools are maintained containing objects with affinity for a particular transaction. When the transaction commits or aborts, these objects are returned to the general pool with no transaction affinity, ready to be used by any client.

For this reason, when your component manually enlists its managed resources in a transaction, it should first check to see whether they are already enlisted. If so, there is no need to enlist.

## Related topics

<dl> <dt>

[COM+ Object Constructor Strings](com--object-constructor-strings.md)
</dt> <dt>

[Controlling Object Lifetime and State](controlling-object-lifetime-and-state.md)
</dt> <dt>

[How Object Pooling Works](how-object-pooling-works.md)
</dt> <dt>

[Improving Performance with Object Pooling](improving-performance-with-object-pooling.md)
</dt> <dt>

[Requirements for Poolable Objects](requirements-for-poolable-objects.md)
</dt> </dl>

 

 



