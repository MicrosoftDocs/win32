---
title: Accessing Property Cache with IADsProperty Interfaces
description: The IADsProperty interfaces consist of IADsPropertyList, IADsPropertyEntry, and IADsPropertyValue.
ms.assetid: ff15eb50-01ab-4b45-bcfd-1df01172f274
ms.tgt_platform: multiple
keywords:
- Accessing the Property Cache Directly with the IADsProperty Interfaces ADSI
- property cache ADSI
- property cache ADSI , using IADsProperty interfaces to access the property cache
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Property Cache with IADsProperty Interfaces

The [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty) interfaces consist of [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist), [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry), and [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue). These interfaces provide methods to directly access and manipulate the properties of an object cache. A property is known as a property entry and corresponds to an attribute defined in the schema. A property entry can have one, or many, property values. A set of property entries are organized as a property list.

The [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist) interface manages the property list of an ADSI object. The [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry) interface performs this operation for a property entry. Similarly, the [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue) interface represents one, or more, property values. Together, they provide a mechanism for users to:

-   Work directly with the property cache.
-   Work with directories that do not contain schemas, such as an LDAP version 2 server.

The [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty)\* interfaces operate strictly on the property cache and do not make any attempt to cooperate with the server to retrieve or modify the data in the persistent store. As such, these interfaces are used only to examine and manipulate properties in the client cache. Before using these interfaces, you must call the [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) method or the [**IADs::GetInfoEx**](/windows/desktop/api/Iads/nf-iads-iads-getinfoex) method explicitly to load the object properties into the cache, if the cache has not been initialized. After calling the methods of these interfaces, you must call [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) to persist the changes to the underlying directory store.

For more information and a code example that can used to implement these interfaces, see [Example Code for Using IADsProperty Interfaces to Access the Property Cache](example-code-for-using-iadsproperty-interfaces-to-access-the-property-cache.md).

 

 




