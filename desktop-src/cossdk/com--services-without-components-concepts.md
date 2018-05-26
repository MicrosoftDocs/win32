---
Description: COM+ 1.5 introduces the ability to use COM+ services without components.
ms.assetid: da93d164-234a-4d1e-b82c-f3f904bb8cb6
title: COM+ Services Without Components Concepts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COM+ Services Without Components Concepts

COM+ 1.5 introduces the ability to use COM+ services without components. This significantly reduces the performance costs when using COM+ services from an environment that doesn't use components, and it also eliminates the complexity of using these services. Beginning with IIS 6.0, IIS and ASP take advantage of using COM+ services without components.

COM+ services were originally designed to be used with COM+ components. However, some programming environments are not component-based and therefore required substantial overhead to use COM+ services. For example, before the release of COM+ 1.5, IIS had to create shim objects solely to be able to use COM+ transaction services in ASP pages. The performance costs that come from creating those objects include storing the configuration data in both the IIS metabase and the COM+ registration database (RegDB) as well as the extra communication between the IIS metabase and the COM+ RegDB that is needed to effectively manage the configuration data.

If IIS needed to use a second COM+ service, such as synchronization, it had to create a completely different shim object to do so. To use both COM+ transactions and synchronization, a third type of shim object would be needed. The complexity of this approach scales as O(n2), making the implementation of new services extremely difficult.

With the introduction of COM+ services without components, the services that are needed are configured through an object instantiated from the class. The [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) class implements the interfaces needed to configure the different services while providing the flexibility to support multiple services at the same time and the ability to support new services in the future.

The configured services can then be used through two different mechanisms: They can be used through the [**CoCreateActivity**](/windows/win32/ComSvcs/nf-comsvcs-cocreateactivity?branch=master) function, which applies the services to all of the work submitted via the activity that is created by the function, and they can also be used by embedding the work that uses the services between calls to the [**CoEnterServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coenterservicedomain?branch=master) and [**CoLeaveServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coleaveservicedomain?branch=master) functions. None of these functions requires the creation of any new components to be able to use the COM+ services; only the [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) object is needed.

## Related topics

<dl> <dt>

[COM+ Services Without Components Tasks](com--services-without-components-tasks.md)
</dt> </dl>

 

 



