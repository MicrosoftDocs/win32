---
title: Access Control and Write Operations
description: Property modifications fail if the caller does not have sufficient rights.
ms.assetid: eb5b97fb-4654-444e-9f5a-9a4be27ef1a3
ms.tgt_platform: multiple
keywords:
- Access Control and Writer Operations AD
ms.topic: article
ms.date: 05/31/2018
---

# Access Control and Write Operations

Property modifications fail if the caller does not have sufficient rights. For write operations that batch modifications to multiple properties, the entire operation fails if the caller does not have the necessary rights to a single one of the modified properties. For example, you can make multiple [**IADs::Put**](/windows/desktop/api/iads/nf-iads-iads-put) calls to set multiple properties on an object. However, when you call [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) to write the new data from the local cache to the directory, **SetInfo** will fail if the caller does not have write access to all the modified properties. Similarly, the [**IDirectoryObject::SetObjectAttributes**](/windows/desktop/api/iads/nf-iads-idirectoryobject-setobjectattributes) method fails to set any properties if the caller does not have access to all the properties being set. So you should batch multiple modify operations only if you know that all modifications will succeed. To determine the attributes of a directory object that the caller has the ability to modify, read the object's **allowedAttributesEffective** attribute.

If the caller does not have sufficient rights to modify a property, the following return codes may be returned:

E\_ADS\_PROPERTY\_NOT\_SET E\_ADS\_PROPERTY\_NOT\_MODIFIED

 

 