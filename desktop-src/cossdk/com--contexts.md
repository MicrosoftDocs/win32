---
description: For configured components running within COM+ applications, contexts are the foundation on which COM+ services are provided.
ms.assetid: 62a0bef2-c3c2-4a60-a5d1-6c038958e13e
title: COM+ Contexts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Contexts

For configured components running within COM+ applications, *contexts* are the foundation on which COM+ services are provided. In COM+, a context is defined as set of run-time properties associated with one or more COM objects that are used to provide services for those objects.

In COM+, every COM object is associated with precisely one context as it runs (that is, between its activation and deactivation), and every context resides within precisely one COM apartment. Multiple objects can run within the same context, and multiple contexts can reside within the same apartment. Initialized when an object is activated, context properties, such as security context properties, represent the run-time needs of an object.

> [!Note]  
> For unconfigured components that do not use COM+ services, the context is, for the most part, ignored.

 

COM+ uses context properties as the basis for providing run-time services. These properties hold state that determines how the execution environment performs services for objects within the context. In some cases, you can interact directly with an object's context properties to indicate some state relevant to a service being provided for the object. For example, you would do this when an object that is participating in an automatic transaction votes on the outcome of the transaction.

For a detailed discussion of the COM foundation of these concepts, see [Processes, Threads, and Apartments](/windows/desktop/com/processes--threads--and-apartments).

## Programmatic Interaction with Context Properties

Each context has an associated [**ObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-objectcontext) object that keeps track of its properties. You can access **ObjectContext** by calling the [**GetObjectContext**](/windows/desktop/api/ComSvcs/nf-comsvcs-getobjectcontext) function. After you have accessed **ObjectContext**, you can call methods on the [**IObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontext) interface it exposes to manipulate context properties.

For example, calling [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) has the effect of setting the transaction consistency bit to "consistent" and the [JIT-activation](com--just-in-time-activation.md) done bit to "done" on the context associated with the object. "Consistent" signals to COM+ that you vote to commit the transaction, and "done" indicates that your object is ready to be deactivated when the method returns.

In addition to [**IObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontext), other specialized interfaces providing access to context properties are [**IObjectContextInfo**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontextinfo), [**IContextState**](/windows/desktop/api/ComSvcs/nn-comsvcs-icontextstate), and [**IObjectContextActivity**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontextactivity). To a certain extent, [**ISecurityCallContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallcontext) also accesses context properties. You can use [**IGetSecurityCallContext::GetSecurityCallContext**](/windows/desktop/api/ComSvcs/nf-comsvcs-igetsecuritycallcontext-getsecuritycallcontext) to obtain **ISecurityCallContext**.

## Understanding Activation and Interception

Generally, you need to think about context only to the extent that it represents a number of properties, some of which you can set or get, that are used to provide COM+ services for your components. In some circumstances, however, you might need to consider the following two interrelated facets of contexts in greater detail:

-   [Context activation](context-activation.md), or the initialization of an object in an appropriate context.
-   [Interception](interception-of-cross-context-calls.md), or what COM+ does on calls across a context boundary.

## Relation to MTS Context Wrappers

Contexts effectively replace the MTS context wrappers. The purpose they served—providing automatic services by trapping creation requests—is now an integrated feature of COM+. As a result, you no longer need to use the [**SafeRef**](/windows/desktop/api/ComSvcs/nf-comsvcs-saferef) function. In MTS, **SafeRef** was used to obtain a reference to your object which could be passed outside of its context wrapper. In COM+, this is unnecessary; normal object references (**this** pointers) work.

 

 
