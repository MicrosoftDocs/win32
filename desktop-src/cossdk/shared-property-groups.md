---
Description: To prevent name collisions among properties created by different objects, the shared property manager (SPM) uses shared property groups.
ms.assetid: f73d631e-2552-4358-903a-739e2df3657d
title: Shared Property Groups
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shared Property Groups

To prevent name collisions among properties created by different objects, the shared property manager (SPM) uses shared property groups. A shared property group is simply a namespace for a set of shared properties. Each property within a shared property group consists of a name, a value, and a position within the shared property group. Either the name or the position can be used to retrieve the property value. You can access and create shared property groups through the shared property group manager.

The SPM object model is shown in the following illustration.

![](images/1df31cd9-2fc4-48d3-ae68-cae38afb75a6.png)

The following are interfaces of the shared property manager:

-   [**ISharedPropertyGroupManager**](/windows/win32/ComSvcs/nn-comsvcs-isharedpropertygroupmanager?branch=master) is used to create shared property groups and to obtain access to existing shared property groups. You can access the **ISharedPropertyGroupManager** interface by creating an instance of the [**SharedPropertyGroupManager**](/windows/win32/ComSvcs/?branch=master) object by using either [**IObjectContext::CreateInstance**](/windows/win32/ComSvcs/nf-comsvcs-iobjectcontext-createinstance?branch=master) or [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615).

-   [**ISharedPropertyGroup**](/windows/win32/ComSvcs/nn-comsvcs-isharedpropertygroup?branch=master) is used to create and access the shared properties in a shared property group. You can access the **ISharedPropertyGroup** interface by creating a [**SharedPropertyGroup**](/windows/win32/ComSvcs/?branch=master) object with the [**ISharedPropertyGroupManager::CreatePropertyGroup**](/windows/win32/ComSvcs/nf-comsvcs-isharedpropertygroupmanager-createpropertygroup?branch=master) method. As with any COM object, you must release a **SharedPropertyGroup** object when you have finished using it.

-   [**ISharedProperty**](/windows/win32/ComSvcs/nn-comsvcs-isharedproperty?branch=master) is used to set or retrieve the value of a shared property. A shared property can contain any data type that can be represented by a Variant. You can access the **ISharedProperty** interface by creating a [**SharedProperty**](/windows/win32/ComSvcs/?branch=master) object with the [**ISharedPropertyGroup::CreateProperty**](/windows/win32/ComSvcs/nf-comsvcs-isharedpropertygroup-createproperty?branch=master) method or the [**ISharedPropertyGroup::CreatePropertyByPosition**](/windows/win32/ComSvcs/nf-comsvcs-isharedpropertygroup-createpropertybyposition?branch=master) method. A **SharedProperty** object can be created or accessed only from within a [**SharedPropertyGroup**](/windows/win32/ComSvcs/?branch=master) object. Again, you must release a **SharedProperty** object when you have finished using it.

## Related topics

<dl> <dt>

[COM+ Shared Property Manager](com--shared-property-manager.md)
</dt> </dl>

 

 



