---
description: Poolable objects must meet certain requirements to enable a single object instance to be used by multiple clients.
ms.assetid: 2cd4211e-be12-4197-8b43-5cb9f2321016
title: Requirements for Poolable Objects
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Poolable Objects

Poolable objects must meet certain requirements to enable a single object instance to be used by multiple clients.

## Stateless

To maintain security, consistency, and isolation, poolable objects should hold no client-specific state from client to client. You can manage any per-client state by using [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol), performing context-specific initialization with [**IObjectControl::Activate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-activate) and cleaning up any client state with [**IObjectControl::Deactivate**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-deactivate). For more detail, see [Controlling Object Lifetime and State](controlling-object-lifetime-and-state.md).

## No Thread Affinity

Poolable objects cannot be bound to a particular thread; otherwise, performance could be potentially disastrous. For this reason, poolable objects cannot be marked to run in the apartment model; they must run in the multithreaded apartment or the neutral apartment. In addition, poolable objects should not use thread local storage nor should they aggregate the free-threaded marshaler. For more detail about threading in COM+, see [COM+ Threading Models](com--threading-models.md).

> [!Note]  
> The Microsoft Visual Basic 6.0 and earlier development environments can create only apartment model components. However, in Visual Basic .NET, components can be pooled.

 

## Aggregatable

Poolable objects must support aggregation—that is, they must support being created by invoking [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) with a non-NULL *pUnkOuter* argument. When COM+ activates a pooled object, it creates an aggregate to manage the lifetime of the pooled object and to call methods on [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol). For details on writing aggregatable objects, see [Aggregation](/windows/desktop/com/aggregation).

## Transactional Components

Poolable objects that participate in transactions must manually enlist managed resources. While it is pooled, if your object holds a managed resource such as a database connection, there will be no way for the resource manager to automatically enlist in a transaction when the object is activated in given context. Therefore, the object itself must handle the logic of detecting the transaction, turning off the resource manager's auto-enlistment and manually enlisting any resources that it holds. In addition, a transactional pooled object should reflect the current state of its resources in the parameter values of [**IObjectControl::CanBePooled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-canbepooled). For more detail, see [Pooling Transactional Objects](pooling-transactional-objects.md).

## Implement IObjectControl to Manage the Object Lifetime

Poolable objects should implement [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol), although it is not strictly necessary to do so. Transactional components that are pooled, however, must implement **IObjectControl**. These components should monitor the state of the resources they hold and indicate when they can't be reused; when [**IObjectControl::CanBePooled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-canbepooled) returns false, it will doom a transaction. For more detail, see [Controlling Object Lifetime and State](controlling-object-lifetime-and-state.md).

## Language Restrictions

Components developed using Microsoft Visual Basic 6.0 and earlier cannot be pooled because these components will be apartment-model threaded. However, in Visual Basic .NET, components can be pooled.

## Legacy Components

As long as they are non-transactional and conform to the appropriate preceding requirements, components can be pooled even if they were not specifically written with pooling capability in mind. It is not necessary to implement [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol); a component that does not do so simply won't participate in managing its lifetime. If [**IObjectControl::CanBePooled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontrol-canbepooled) is not implemented, the object will continue to be reused until the pool attains maximum size.

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

[Pooling Transactional Objects](pooling-transactional-objects.md)
</dt> </dl>

 

 
