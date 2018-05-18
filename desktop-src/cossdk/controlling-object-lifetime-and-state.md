---
Description: Controlling Object Lifetime and State
ms.assetid: '172e07a2-1711-4353-9099-ff9d31a564c6'
title: Controlling Object Lifetime and State
---

# Controlling Object Lifetime and State

A pooled object can participate in how COM+ manages its activity in the pool by implementing [**IObjectControl**](iobjectcontrol.md). When a pooled object is created, it is aggregated into a larger object that will manage the object by calling the following methods on **IObjectControl** at regular points in the object's lifecycle:

-   [**Activate**](iobjectcontrol-activate.md)—Called whenever the object is returned to a client, activated in a specific context.
-   [**Deactivate**](iobjectcontrol-deactivate.md)—Called whenever an object is released by the client or, in the case of a JIT-activated object, when it is deactivated.
-   [**CanBePooled**](iobjectcontrol-canbepooled.md)—Called whenever an object is to be returned to the general pool.

Implementing [**IObjectControl**](iobjectcontrol.md) is optional, except for transactional objects, which should always implement [**CanBePooled**](iobjectcontrol-canbepooled.md) to monitor the state of the resources they hold. However, it is advisable to implement **IObjectControl** in most cases because it provides an efficient way to manage the behavior of a pooled object, as described below.

## Performing Context-Specific Initialization

Using [**Activate**](iobjectcontrol-activate.md), you can initialize the object in the context in which it is activated for a given client. For example, to determine whether the object has transaction affinity (its resources may already be enlisted), you might get the transaction ID associated with the context.

Typically you would use [**Activate**](iobjectcontrol-activate.md)to perform initialization that is consistent across any methods exposed by the object, treating it as the context-specific portion of the object's constructor.

## Cleaning Up Any Client State

Using [**Deactivate**](iobjectcontrol-deactivate.md), you can get rid of any client-specific state that might exist so that your object returns to the pool in a completely generic state and can then be used by any client without compromising security or isolation.

## Controlling Reuse of the Object

Using [**CanBePooled**](iobjectcontrol-canbepooled.md), you can monitor the internal state of your object and report on whether it is fit for its reuse. If **CanBePooled** returns True and the pool maximum has not been reached, the object is placed back in the general pool. If **CanBePooled** returns False, the object is discarded. In the case of transactional components, returning False will doom the current transaction.

Typically, you would keep some global data member for the object, and if you detect a connection to be bad or a resource of some kind to be in a bad state, set this to reflect the current situation and return it through [**CanBePooled**](iobjectcontrol-canbepooled.md).

If an object does not implement [**CanBePooled**](iobjectcontrol-canbepooled.md), instances will continue to be reused until the pool maximum level is reached.

## Related topics

<dl> <dt>

[COM+ Object Constructor Strings](com--object-constructor-strings.md)
</dt> <dt>

[How Object Pooling Works](how-object-pooling-works.md)
</dt> <dt>

[Improving Performance with Object Pooling](improving-performance-with-object-pooling.md)
</dt> <dt>

[Pooling Transactional Objects](pooling-transactional-objects.md)
</dt> <dt>

[Requirements for Poolable Objects](requirements-for-poolable-objects.md)
</dt> </dl>

 

 



