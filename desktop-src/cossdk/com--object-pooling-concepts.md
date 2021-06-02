---
description: Object pooling is an automatic service provided by COM+ that enables you to configure a component to have instances of itself kept active in a pool, ready to be used by any client that requests the component.
ms.assetid: 74a45220-449a-4d89-a979-a206e5e3d3ad
title: COM+ Object Pooling Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Object Pooling Concepts

Object pooling is an automatic service provided by COM+ that enables you to configure a component to have instances of itself kept active in a pool, ready to be used by any client that requests the component. You can administratively configure and monitor the pool maintained for a given component, specifying characteristics such as pool size and creation request time-out values. When the application is running, COM+ manages the pool for you, handling the details of object activation and reuse according to the criteria you have specified.

You can achieve very significant performance and scaling benefits by reusing objects in this manner, particularly when they are written to take full advantage of reuse. With object pooling, you gain the following benefits:

-   You can speed object use time for each client, factoring out time-consuming initialization and resource acquisition from the actual work that the object performs for clients.
-   You can share the cost of acquiring expensive resources across all clients.
-   You can pre-allocate objects when the application starts, before any client requests come in.
-   You can govern resource use with administrative pool management for example, by setting an appropriate maximum pool level, you can keep open only as many database connections as you have a license for.
-   You can administratively configure pooling to take best advantage of available hardware resources you can easily adjust the pool configuration as available hardware resources change.
-   You can speed reactivation time for objects that use [just-in-time (JIT) activation](com--just-in-time-activation.md), while deliberately controlling how resources are dedicated to clients.

## Writing Poolable Objects

Poolable objects must meet certain requirements to enable a single object instance to be used by multiple clients. For example, they can't hold client state or have any thread affinity. Transactional objects also have particular requirements, in that managed resources held by a pooled object must be manually enlisted in a transaction.

Pooled objects can implement [**IObjectControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontrol) to control how they are reused. This enables them to perform initialization when activated in a given context, to clean up any client state on deactivation, and to indicate when they are in a non-reusable state.

Often, it useful to write poolable objects in a somewhat generic fashion so that they can be administratively customized with a constructor string. For example, an object might be written to hold a generic ODBC connection, with a particular DSN administratively specified in a constructor string.

The topics in this section, described in the following table, provide information about how object pooling works in COM+, as well as information about how to write, configure, and implement poolable objects.



| Topic                                                                                                 | Description                                                                                              |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [How Object Pooling Works](how-object-pooling-works.md)<br/>                                   | Presents basic concepts.<br/>                                                                      |
| [Improving Performance with Object Pooling](improving-performance-with-object-pooling.md)<br/> | Provides specific details on how you can use object pooling most effectively.<br/>                 |
| [Requirements for Poolable Objects](requirements-for-poolable-objects.md)<br/>                 | Provides details on how to write an object that is to be pooled.<br/>                              |
| [Pooling Transactional Objects](pooling-transactional-objects.md)<br/>                         | Provides details about the special requirements that apply to poolable transactional objects.<br/> |
| [Controlling Object Lifetime and State](controlling-object-lifetime-and-state.md)<br/>         | Describes how pooled objects can be implemented to control how they are reused.<br/>               |



 

## Related topics

<dl> <dt>

[COM+ Object Pooling Tasks](com--object-pooling-tasks.md)
</dt> </dl>

 

 




