---
description: Application components use the COM+ resource dispenser to access and manage shared, nondurable state information, such as connections between components and a given resource manager.
ms.assetid: 252c7180-61b1-485d-883d-36bf77357a29
title: COM+ Resource Dispenser Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Resource Dispenser Concepts

Application components use the COM+ resource dispenser to access and manage shared, nondurable state information, such as connections between components and a given resource manager. At runtime, dynamic pools of resources, such as database connections, network connections, connections to queues, threads, objects, and memory blocks, are made available to the resource dispenser. The application process achieves high performance by using a minimum number of frequently used resources. The resource dispenser can also automate transactions and reclamation. (See [Automatic Resource Reclamation](automatic-resource-reclamation.md) for more information about this feature.)

> [!Note]  
> A *resource* is anything a resource dispenser creates. For example, a connection to a resource manager is a common resource. Resources reside in the resource dispenser's memory and are never copied to the dispenser manager. A resource is known only by an opaque handle (**RESID**) and may or may not be capable of performing transactions. Although the resources managed might often be connections to a component managing a durable state, the connections themselves are not durable. A resource dispenser often uses a related resource manager to retain the durable state.

 

Architecturally, the COM+ resource dispenser system consists of resource dispensers and a dispenser manager. Resource dispensers are user-supplied components that provide applications with simple interfaces to shared resources. The dispenser manager is a component provided by COM+ that coordinates the activities of the various resource dispensers.

A resource dispenser is a dynamic-link library (DLL) component that provides at least two interfaces. The first, [**IDispenserDriver**](/windows/desktop/api/ComSvcs/nn-comsvcs-idispenserdriver), provides the dispenser manager with basic information on how to create, destroy, and enlist the resources it manages. The second is exposed to the applications and can be a COM interface or set of interfaces or can be an application programming interface (API) to which a component is linked via an import library. An application can call any resource dispenser, which in turn may offer any API to the application. If the resource dispenser is an Automation component, it can be accessed from Microsoft Visual Basic. A resource dispenser is instantiated when an application component refers to it.

The dispenser manager provided by COM+ tracks resource dispensers and coordinates among them. It implements two interfaces: [**IDispenserManager**](/windows/desktop/api/ComSvcs/nn-comsvcs-idispensermanager) and [**IHolder**](/windows/desktop/api/ComSvcs/nn-comsvcs-iholder). resource dispensers register themselves using the **IDispenserManager** interface. The dispenser manager then gives them a pointer to an **IHolder** that they use to notify the dispenser manager of their activities.

A transactional resource dispenser must enlist in a Distributed Transaction Coordinator (DTC) transaction. This implies use of either an internal or an external (to the resource dispenser) resource manager that is OLE transactions-compliant.

> [!Note]  
> The COM+ programming model includes *declarative transactions*, which help protect the work performed by an application object during its lifetime. When an application object uses a COM+ resource dispenser, the work it performs is automatically transactional; that is, the component doesn't have to explicitly declare transactions. These transactions are defined in the OLE Transactions specification, implemented by the DTC, and initiated on behalf of the application object by COM+. See the DTC Development Guide for more information.

 

Resources need not be transactional. A resource dispenser that pools non-transactional resources can still achieve high performance by allowing application objects to access a shared pool of these resources. This type of resource dispenser returns S\_FALSE from the [**IDispenserDriver::EnlistResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispenserdriver-enlistresource) method, which means that the resource dispenser did not enlist the resource because the resource is not transactional.

The resource dispenser can also function independently of COM+, providing only resource pooling capabilities. For example, if a resource dispenser exposes an API (such as ODBC), the resource dispenser might be a DLL that is accessed by the application through an import library (or using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions). A resource dispenser might also be a COM component that an application accesses by calling [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance). Without COM+, a resource dispenser's [**EnlistResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispenserdriver-enlistresource) method can never be called because the dispenser manager has no knowledge of the current component transaction.

On startup, a resource dispenser DLL must register itself with the dispenser manager. The dispenser manager is the controlling executive that manages the loading and unloading of resource dispensers, provides the COM+ context, and controls the inventory statistics manager. (For more information, see [COM+ Dispenser Manager](com--dispenser-manager.md).) The resource dispenser first calls the [**GetDispenserManager**](/windows/desktop/api/MtxDM/nf-mtxdm-getdispensermanager) function and then calls the [**IDispenserManager::RegisterDispenser**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispensermanager-registerdispenser) method, passing the [**IDispenserDriver**](/windows/desktop/api/ComSvcs/nn-comsvcs-idispenserdriver) pointer that the resource dispenser implements. This call returns a reference to [**IHolder**](/windows/desktop/api/ComSvcs/nn-comsvcs-iholder).

To shut down, a resource dispenser calls [**IHolder::Close**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-close). To ensure a clean package shutdown, a resource dispenser must be able to handle the situation when calls continue to arrive from business objects after COM+ has asked the dispenser to shut down.

The following topics in this section provide more detailed information about the COM+ resource dispenser service:

-   [COM+ Dispenser Manager](com--dispenser-manager.md)
-   [COM+ Resource Dispenser Thread Types](com--resource-dispenser-thread-types.md)
-   [Pooled Resource States Available to COM+ Resource Dispenser](pooled-resource-states-available-to-com--resource-dispenser.md)
-   [Enlisting a Resource in a Transaction](enlisting-a-resource-in-a-transaction.md)
-   [Resource Dispenser Resource Allocation Process](resource-dispenser-resource-allocation-process.md)
-   [Tracking Non-Allocated Resources](tracking-non-allocated-resources.md)
-   [Automatic Resource Reclamation](automatic-resource-reclamation.md)
-   [Types Used in COM+ Resource Dispenser Interfaces](types-used-in-com--resource-dispenser-interfaces.md)
-   [COM+ Resource Dispenser Interfaces](com--resource-dispenser-interfaces.md)

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Tasks](com--resource-dispenser-tasks.md)
</dt> </dl>

 

 
