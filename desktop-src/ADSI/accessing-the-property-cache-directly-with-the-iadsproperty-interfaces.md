---
title: Accessing the Property Cache Directly with the IADsProperty Interfaces
description: The IADsProperty interfaces consist of IADsPropertyList, IADsPropertyEntry, and IADsPropertyValue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ff15eb50-01ab-4b45-bcfd-1df01172f274
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Accessing the Property Cache Directly with the IADsProperty Interfaces ADSI
- property cache ADSI
- property cache ADSI , using IADsProperty interfaces to access the property cache
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Accessing the Property Cache Directly with the IADsProperty Interfaces

The [**IADsProperty**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master) interfaces consist of [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master), [**IADsPropertyEntry**](/windows/win32/Iads/nn-iads-iadspropertyentry?branch=master), and [**IADsPropertyValue**](/windows/win32/Iads/nn-iads-iadspropertyvalue?branch=master). These interfaces provide methods to directly access and manipulate the properties of an object cache. A property is known as a property entry and corresponds to an attribute defined in the schema. A property entry can have one, or many, property values. A set of property entries are organized as a property list.

The [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master) interface manages the property list of an ADSI object. The [**IADsPropertyEntry**](/windows/win32/Iads/nn-iads-iadspropertyentry?branch=master) interface performs this operation for a property entry. Similarly, the [**IADsPropertyValue**](/windows/win32/Iads/nn-iads-iadspropertyvalue?branch=master) interface represents one, or more, property values. Together, they provide a mechanism for users to:

-   Work directly with the property cache.
-   Work with directories that do not contain schemas, such as an LDAP version 2 server.

The [**IADsProperty**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)\* interfaces operate strictly on the property cache and do not make any attempt to cooperate with the server to retrieve or modify the data in the persistent store. As such, these interfaces are used only to examine and manipulate properties in the client cache. Before using these interfaces, you must call the [**IADs::GetInfo**](/windows/win32/Iads/nf-iads-iads-getinfo?branch=master) method or the [**IADs::GetInfoEx**](/windows/win32/Iads/nf-iads-iads-getinfoex?branch=master) method explicitly to load the object properties into the cache, if the cache has not been initialized. After calling the methods of these interfaces, you must call [**IADs::SetInfo**](/windows/win32/Iads/nf-iads-iads-setinfo?branch=master) to persist the changes to the underlying directory store.

For more information and a code example that can used to implement these interfaces, see [Example Code for Using IADsProperty Interfaces to Access the Property Cache](example-code-for-using-iadsproperty-interfaces-to-access-the-property-cache.md).

 

 




