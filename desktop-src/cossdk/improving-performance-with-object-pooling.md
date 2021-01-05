---
description: Improving Performance with Object Pooling
ms.assetid: 7a8a38d8-6549-4686-a298-f3b427b380e3
title: Improving Performance with Object Pooling
ms.topic: article
ms.date: 05/31/2018
---

# Improving Performance with Object Pooling

Object pooling can be extremely effective in certain circumstances, yielding substantial increases in performance. The general idea for reusing objects to best advantage is to pool as many resources as possible, factoring out initialization from actual work performed, and then to administratively tailor the pool characteristics to actual hardware at deployment time. That is, you should proceed according to the following steps:

1.  Write the object so as to factor out expensive initialization and resource acquisition that is performed for any client as a prerequisite to doing actual work on the client's behalf. Write heavy object constructors to pool as many resources as possible so that these are held by the object and immediately available when clients get an object from the pool.
2.  Administratively configure the pool to achieve the best balance in available hardware resources, usually trading the memory dedicated to maintaining a pool of a certain size in exchange for faster client access and use of objects. At a certain point, pooling will achieve diminishing returns and you can get good enough performance while limiting possible resource usage by a particular component.

## Doing Actual Work or Acquiring Resources

If you have a component that clients will use briefly and in rapid succession, where a significant portion of object use time is spent in acquiring resources or initializing prior to doing specific work for the client, chances are that writing your component to use object pooling will be a big win for you.

You can write the component so that in the object's constructor you perform as much of the time-consuming work that is uniform for all clients as possible—acquiring one or several connections, running scripts, fetching initialization data from files or across a network, and so forth. This has the effect of pooling every such resource. You are pooling the combination of resources and generic state necessary to perform some work.

In this circumstance, when clients get an object from the pool, they have those resources immediately available. Typically, they will use the object to do some small unit of work, pushing or pulling data, and then the object will call [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) or [**IObjectContext::SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort) and return. With rapid-fire use patterns such as this, pooling yields excellent performance benefits. You can fully leverage the simplicity of the stateless automatic transaction programming model yet achieve performance on par with traditional stateful components.

However, if clients use an object for a long time each time they call it, pooling will make less sense. The speed advantage that you gain is marginal as use time increases relative to initialization time. You get diminishing returns that may not justify the cost of the memory necessary to hold a pool of active objects.

## Sharing Cost Across Multiple Clients

A variation on factoring out initialization is that you can use pooling to statistically amortize the cost of acquiring expensive resources. If you take the hit of acquisition or initialization once and then reuse the object, you share that cost across all clients that use the object during its lifetime. Heavy construction time is incurred only once per object.

## Preallocating Objects

If you specify a nonzero minimum pool size, that minimum number of objects will be created and pooled when the application starts, ready for any clients that call in to the application.

## Governing Resource Use with Pool Management

You can use the maximum pool size to govern very precisely how you use resources. For example, if you have licensed a certain number of database connections, you can control how many connections you have open at any time.

When you take into consideration client use patterns, object use characteristics, and physical resources such as memory and connections, you are likely to find some optimal balance point when you do performance tuning. Pooling objects will yield diminishing returns after a certain point. You can determine what level of performance you require and balance that against what resources are necessary to achieve it.

To facilitate performance tuning when you configure object pooling, you can monitor object statistics for the components in an application. For details, see [Monitoring Object Statistics](monitoring-object-statistics.md).

## Improve Performance of JIT-Activated Components

Object pooling works very well with the [COM+ just-in-time activation](com--just-in-time-activation.md) service. By pooling objects that are being JIT-activated, you can speed object reactivation. You get the benefits of holding the channel open by JIT activation while mitigating the cost of reactivation. You can use pooling in this case to govern how much memory you wish to allocate to objects that have references active.

You are most likely to be pooling JIT-activated components when they are transactional. Object pooling is optimized to handle transactional components. For more information, see [Pooling Transactional Objects](pooling-transactional-objects.md).

## Related topics

<dl> <dt>

[COM+ Object Constructor Strings](com--object-constructor-strings.md)
</dt> <dt>

[Controlling Object Lifetime and State](controlling-object-lifetime-and-state.md)
</dt> <dt>

[How Object Pooling Works](how-object-pooling-works.md)
</dt> <dt>

[Pooling Transactional Objects](pooling-transactional-objects.md)
</dt> <dt>

[Requirements for Poolable Objects](requirements-for-poolable-objects.md)
</dt> </dl>

 

 



