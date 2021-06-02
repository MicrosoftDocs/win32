---
description: The synchronization attribute is a declarative property that specifies what type of synchronization you want your components to have when they are activated.
ms.assetid: 7f044ee5-b99e-4f0c-a680-b1e2672949fc
title: Synchronization Attribute Values
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Attribute Values

The synchronization attribute is a declarative property that specifies what type of synchronization you want your components to have when they are activated. When you include the synchronization attribute, COM+ handles the details of synchronization on your behalf; you do not have to make any other calls.

Depending on its requirements, an object can share its caller's synchronization, require a new synchronization, or operate without synchronization.

COM+ provides the following synchronization attribute values:

-   **Disabled.** When you disable the synchronization attribute, COM+ ignores the synchronization requirements of the component in determining context for the object. As a result, the object may or may not share its caller's context (and synchronization).

    In general, you should use this attribute value when you know the component never accesses a resource manager. When migrating COM components to COM+, you must disable the synchronization attribute to maintain the same behavior as the unconfigured COM component. An unconfigured component is a COM component that has not been installed in a COM+ application.

-   **Not Supported.** An object with this value never participates in synchronization, regardless of the status of its caller. This setting is available only for components that are non-transactional and do not use the [COM+ just-in-time (JIT) activation](com--just-in-time-activation.md) service.

-   **Supported.** An object with this value participates in synchronization if it exists. You declare this value when you want an object to share in its caller's synchronization but not require synchronization of its own.

    A good reason to set your synchronization attribute to Supported is that this setting can be less expensive in terms of system resources. However, it is more difficult to write your component because of the need to protect it from concurrent calls. The implication of setting the synchronization attribute to Supported is that, under certain circumstances, an instance of your object may be created in such a way that it's not synchronized. If the component's threading model is Free or Both, you will have to protect your instance data with some type of locking mechanism. If the Threading Model is Apartment (STA), you won't need to protect your instance data.

-   **Required.** When you set this attribute, COM+ ensures that all objects created from the component will be synchronized. In effect, whenever COM+ creates an instance of your component, it makes sure there's only one thread going through this instance at a time.

    As COM+ activates an object, it looks at the synchronization status of its caller. If the caller is synchronized, COM+ flows the caller's synchronization boundary to include the new object. Otherwise, COM+ begins the synchronization.

-   **Requires New.** An object with this value must participate in a new synchronization, where COM+ manages contexts and apartments on behalf of all components involved in the call. COM+ automatically initiates a new synchronization, which is distinct from the caller's synchronization.

    A good reason to set your synchronization attribute to Requires New is that this setting allows you to make outside calls to an instance of your component more efficiently. However, it also makes calls between your object and the object that created it more expensive in terms of system resources.

    For example, assume a case where your object and its creator object share the same synchronization boundary. If client A calls the creator object and client B calls your object, the second call will have to wait until the first call is completed. If you set Requires New, your object is created in a separate synchronization boundary. In this case, calls from other objects can be processed at the same time. However, calls from the creator object to your object require more system resources because they must cross synchronization boundaries.

## Related topics

<dl> <dt>

[Setting the Synchronization Attribute](setting-the-synchronization-attribute.md)
</dt> <dt>

[Synchronization Dependencies](synchronization-dependencies.md)
</dt> </dl>

 

 



