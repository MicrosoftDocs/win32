---
description: Application recycling can significantly increase the overall stability of your COM+ applications by offering a quick fix for known problems and helping to protect against unexpected ones.
ms.assetid: bf98318b-4d87-44cc-85a1-68faf5547e06
title: COM+ Application Recycling Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Application Recycling Concepts

Application recycling can significantly increase the overall stability of your COM+ applications by offering a quick fix for known problems and helping to protect against unexpected ones. For example, application performance can degrade over time because of problems such as memory leaks, nonscalable resource usage, and process failure. COM+ provides application recycling as a solution to these problems. You can use application recycling to automatically shut down a process and restart it, thus reinitializing a failing process and reallocating memory it uses.

Application recycling works by creating a duplicate of the Dllhost process associated with an application. This duplicate Dllhost process services all future object requests, which leaves the old Dllhost to finish servicing the remaining object requests. The old Dllhost process is shut down when it detects the release of all external references to objects in the process or when the expiration time-out value is reached. Through this behavior, application recycling ensures that a client application does not experience a service interruption.

> [!Note]  
> You cannot recycle a COM+ application that has been configured to run as a Windows service. Also, library applications have the recycling and pooling properties of their host process.

 

You can configure application recycling administratively, by using the Component Services administrative tool, or programmatically, through the COM+ Administrative SDK. You can recycle processes based on several criteria, determined by the following properties of a [**COMAdminCatalogObject**](comadmincatalogobject.md) object in the [**Applications**](applications.md) collection:

-   **RecycleLifetimeLimit.** The maximum number of minutes a process can run before it's recycled. The valid range is 0 through 30,240 minutes (21 days). The default number of minutes is 0, which indicates that the process will not recycle from reaching a lifetime limit.
-   **RecycleMemoryLimit.** The maximum amount of process memory usage (in kilobytes) before recycling the process. If the process memory usage exceeds the specified number for longer than one minute, the process is recycled. The valid range is 0 through 1,048,576 KB. The default amount of memory usage is 0 KB, which indicates that the process will not recycle from reaching a memory limit.
-   **RecycleCallLimit.** The maximum number of calls that application objects can accept before recycling the process. The valid range is 0 through 1,048,576 calls. The default number of calls is 0, which indicates that the process will not recycle from reaching a call limit.
-   **RecycleActivationLimit.** The maximum number of application object activations to accept before recycling the process. The valid range is 0 through 1,048,576 activations. The default number of activations is 0, which indicates that the process will not recycle from reaching an activation limit.

Additionally, the RecycleExpirationTimeout property of the [**COMAdminCatalogObject**](comadmincatalogobject.md) object is used to force the shutdown of a recycled process. It indicates the number of minutes to wait for the release of all external references to objects in the recycled process before forcibly shutting down the process. The valid range is 1 through 1440 minutes (24 hours), and the default expiration time-out is 15 minutes. This value is used only when it is already determined that a process will be recycled based on the other criteria.

You can select more than one criterion for recycling an application. COM+ recycles the application after the first of the set of criteria is satisfied. You can set the expiration time-out value to determine how long an old Dllhost process can spend completing remaining service requests before being forcibly shut down.

The [**ApplicationInstances**](applicationinstances.md) collection provides the HasRecycled property, which provides a way to determine whether the application has ever been recycled.

## Related topics

<dl> <dt>

[COM+ Application Recycling Tasks](com--application-recycling-tasks.md)
</dt> <dt>

[**RecycleSurrogate**](/windows/desktop/api/ComSvcs/nf-comsvcs-recyclesurrogate)
</dt> </dl>

 

 



