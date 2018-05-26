---
title: Access Control and Write Operations
description: Property modifications fail if the caller does not have sufficient rights.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: eb5b97fb-4654-444e-9f5a-9a4be27ef1a3
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Access Control and Writer Operations AD
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Access Control and Write Operations

Property modifications fail if the caller does not have sufficient rights. For write operations that batch modifications to multiple properties, the entire operation fails if the caller does not have the necessary rights to a single one of the modified properties. For example, you can make multiple [**IADs::Put**](https://msdn.microsoft.com/library/aa746352) calls to set multiple properties on an object. However, when you call [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354) to write the new data from the local cache to the directory, **SetInfo** will fail if the caller does not have write access to all the modified properties. Similarly, the [**IDirectoryObject::SetObjectAttributes**](https://msdn.microsoft.com/library/aa746360) method fails to set any properties if the caller does not have access to all the properties being set. So you should batch multiple modify operations only if you know that all modifications will succeed. To determine the attributes of a directory object that the caller has the ability to modify, read the object's **allowedAttributesEffective** attribute.

If the caller does not have sufficient rights to modify a property, the following return codes may be returned:

E\_ADS\_PROPERTY\_NOT\_SET E\_ADS\_PROPERTY\_NOT\_MODIFIED

 

 




