---
title: Authentication (AD DS)
description: Every object in Active Directory Domain Services has a unique security descriptor that defines the access permissions that are required to read or update the object or its individual properties.
ms.assetid: a4a663d3-b0f3-4993-a74e-9e4f896e8c95
ms.tgt_platform: multiple
keywords:
- Active Directory,using,binding,authentication
- binding authentication AD
ms.topic: article
ms.date: 05/31/2018
---

# Authentication (AD DS)

Every object in Active Directory Domain Services has a unique security descriptor that defines the access permissions that are required to read or update the object or its individual properties. Access privileges are determined by the rights granted to a user's account or group memberships.

When an application binds to an object in the directory, the access privileges that the application has to that object are based on the user context specified during the bind operation. For the binding functions and methods [**ADsGetObject**](/windows/desktop/api/adshlp/nf-adshlp-adsgetobject), [**ADsOpenObject**](/windows/desktop/api/adshlp/nf-adshlp-adsopenobject), **GetObject**, [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/iads/nf-iads-iadsopendsobject-opendsobject), an application can implicitly use the credentials of the caller, explicitly specify the credentials of a user account, or use an unauthenticated user context (Guest).

 

 