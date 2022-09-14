---
description: You can configure a component to be pooled only when it is correctly written to support being pooled. For details of these requirements, see Requirements for Poolable Objects.
ms.assetid: ffd812cc-811e-4f2a-8736-d1cb22d5abb7
title: Configuring a Component to Be Pooled
ms.topic: article
ms.date: 05/31/2018
---

# Configuring a Component to Be Pooled

You can configure a component to be pooled only when it is correctly written to support being pooled. For details of these requirements, see [Requirements for Poolable Objects](requirements-for-poolable-objects.md).

> [!Note]  
> By default, a component is not configured to be pooled.

 

When you configure a component to be pooled, you can specify the following properties to determine how COM+ maintains the pool:

-   **Minimum pool size.** Represents the number of objects that are created when the application starts and the minimum number of objects that are maintained in the pool while the application is running. If the number of available objects in the pool drops below the specified minimum, new objects are created to meet any outstanding object requests and refill the pool. If the number of available objects in the pool is greater than the minimum number, those surplus objects are destroyed during a clean-up cycle.
-   **Maximum pool size.** Represents the maximum number of pooled objects that the pooling manager will create, both actively used by clients and inactive in the pool. When creating objects, the pooling manager checks to verify that the maximum pool size has not been reached and, if it hasn't, the pool manager creates a new instance of the object to dispense to the client. If the maximum pool size has been reached, client requests will be queued and will receive the first available object from the pool on a first-come first-served basis. Object creation requests will time-out after a specified period.
-   **Creation timeout (ms).** Specifies how long a client will wait, in milliseconds, for an object to be returned from the pool after a call to [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance). If the client call is unsuccessful, the error E\_TIMEOUT is returned.

**To set pooling-related properties**

1.  In the details pane of the Component Services administrative tool, right-click the component that you want to configure, and then click **Properties**.

2.  In the component properties dialog box, click the **Activation** tab.

3.  To enable object pooling for the component, select the **Enable object pooling** check box.

4.  In the **Minimum pool size** box, enter the minimum number of objects of this type in the pool. The pool will be maintained to have at least this many objects.

5.  In the u box, enter the maximum number of objects of this type in the pool. The number of objects, both activated and deactivated, will never exceed this value.

6.  In the **Creation timeout (ms)** box, enter the amount of time, in milliseconds, a client will wait for a pooled object if one is not immediately available.

## Related topics

<dl> <dt>

[Monitoring Object Statistics](monitoring-object-statistics.md)
</dt> </dl>

 

 
