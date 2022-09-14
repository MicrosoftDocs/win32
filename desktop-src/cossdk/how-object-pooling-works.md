---
description: When you configure a component to be pooled, COM+ will maintain instances of it in a pool, ready to be activated for any client requesting the component. Any object creation requests will be handled through the pool manager.
ms.assetid: 34978b50-cd20-42fd-ad46-410190478ef8
title: How Object Pooling Works
ms.topic: article
ms.date: 05/31/2018
---

# How Object Pooling Works

When you configure a component to be pooled, COM+ will maintain instances of it in a pool, ready to be activated for any client requesting the component. Any object creation requests will be handled through the pool manager.

Pools are configured and maintained on a per-component basis. A pool consists of homogeneous objects that share the same CLSID. The only exception is for transactional objects, for which subpools are maintained containing objects that have transaction affinity while a transaction is pending.

When the application starts, the pool will be populated up to the minimum level that you have administratively specified, as long as object creation succeeds. As client requests for the component come in, they are satisfied on a first-come first-served basis from the pool. If no pooled objects are available and the pool is not yet at its specified maximum level, a new object is created and activated for the client.

When the pool reaches its maximum level, client requests are queued and will receive the first available object from the pool. The number of objects, including both activated and deactivated, will never exceed the maximum pool value. Object creation requests will time out after an administratively specified period so that you can control how long clients will wait for object creation. Upon a time-out failure, the client will get back the error E\_TIMEOUT from [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).

Whenever possible, COM+ will attempt to reuse an object after a client releases it, until the pool reaches its maximum level. The object is responsible for monitoring its state to determine whether it can be reused and should return an appropriate value for [**IObjectControl::CanBePooled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-canbepooled).

When a pooled object is created, it is aggregated into a larger object that will manage the object's lifetime. The outer object calls methods on [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol) at appropriate times in the object's life cycle, as follows:

-   The [**Activate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-activate) method is called whenever the object is returned to a client, activated in a specific context.
-   The [**Deactivate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-deactivate) method is called whenever an object is released by the client or, in the case of a JIT-activated object, when it is deactivated.
-   The [**CanBePooled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-canbepooled) method is called whenever an object is to be returned to the general pool. If the object detects that some reusable resource is in a bad state, it should return **FALSE** for this method and the pool manager will discard the object.

An object does not necessarily need to implement [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol). If it does not, instances will always be reused, until the pool maximum level is reached.

For details about how to configure components to be pooled, see [Configuring a Component to Be Pooled](configuring-a-component-to-be-pooled.md).

## Related topics

<dl> <dt>

[COM+ Object Constructor Strings](com--object-constructor-strings.md)
</dt> <dt>

[Controlling Object Lifetime and State](controlling-object-lifetime-and-state.md)
</dt> <dt>

[Improving Performance with Object Pooling](improving-performance-with-object-pooling.md)
</dt> <dt>

[Pooling Transactional Objects](pooling-transactional-objects.md)
</dt> <dt>

[Requirements for Poolable Objects](requirements-for-poolable-objects.md)
</dt> </dl>

 

 
