---
description: In COM+, shared transient state for objects is managed by using the shared property manager (SPM). The SPM is a resource dispenser that you can use to share state among multiple objects within a server process.
ms.assetid: 31b50c2a-68b5-4816-9a56-8cd9475e7beb
title: COM+ Shared Property Manager Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Shared Property Manager Concepts

In COM+, shared transient state for objects is managed by using the shared property manager (SPM). The SPM is a resource dispenser that you can use to share state among multiple objects within a server process.

You cannot use global variables in a distributed environment because of concurrency and name collision issues. The shared property manager eliminates name collisions by providing shared property groups, which establish unique namespaces for the shared properties they contain. The SPM also implements locks and semaphores to help protect shared properties from simultaneous access, which could result in lost updates and leave properties in an unpredictable state.

> [!Note]  
> Shared transient state is state information kept in memory that does not survive system failures. The information is designed to be shared by multiple objects across transaction (but not across process) boundaries.

 

Shared properties stored in the SPM are available only to objects running in the same process. This means that the objects that will use the SPM for storing values and that will need to have access to these values must be installed as part of the same COM+ application. It is possible for system administrators to move COM+ classes from one package to another after your COM+ application has been deployed. If you rely on several objects sharing properties through the SPM, you should clearly document that they must be installed in the same COM+ application.

It's also important for components sharing properties to have the same activation attribute. If two components in the same package have different activation attributes, they generally won't be able to share properties. For example, if one component is configured to run in a client process and the other is configured to run in a server process, their objects will usually run in different processes even though they're in the same package.

You should always instantiate the [**SharedPropertyGroupManager**](sharedpropertygroupmanager.md), [**SharedPropertyGroup**](sharedpropertygroup.md), and [**SharedProperty**](sharedproperty.md) objects from COM+ components rather than from a base client. If a base client creates shared property groups and properties, the shared properties are inside the base-client process, not in a server process. This means the COM+ objects cannot share the properties unless the objects are also running in the client process (which is generally not a good idea).

## Related topics

<dl> <dt>

[COM+ Shared Property Manager](com--shared-property-manager.md)
</dt> <dt>

[Shared Property Groups](shared-property-groups.md)
</dt> </dl>

 

 



