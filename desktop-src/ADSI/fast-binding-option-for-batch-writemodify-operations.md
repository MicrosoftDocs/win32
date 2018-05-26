---
title: Fast Binding Option for Batch Write/Modify Operations
description: When a directory service object is bound to, ADSI creates a COM object that represents the specified directory object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cf41b0c4-7459-49cf-945b-8462c7d19947
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Fast Binding Option for Batch Write/Modify Operations ADSI
- ADSI ADSI , Using, Fast Binding Option for Batch Write/Modify Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Fast Binding Option for Batch Write/Modify Operations

When a directory service object is bound to, ADSI creates a COM object that represents the specified directory object. When binding, ADSI will typically retrieve the **objectClass** attribute so that ADSI can expose the COM interfaces that are appropriate for that class of object. For example, a user object would expose the [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master) interface in addition to the base ADSI interfaces supported for all objects. For a single operation, this should have no effect on performance. However, if batch operations are performed that require hundreds or thousands of bindings over a slow connection and those operations are writing data to the directory service, it may be desirable to exchange full object support for faster binding. This is known as a fast-bind and is accomplished by specifying the **ADS\_FAST\_BIND** flag when [**ADsOpenObject**](/windows/win32/Adshlp/nf-adshlp-adsopenobject?branch=master) or [**IADsOpenDSObject::OpenDSObject**](/windows/win32/Iads/nf-iads-iadsopendsobject-opendsobject?branch=master) is called.

Fast-binding has the following restrictions:

-   The bind operation must be performed with the [**ADsOpenObject**](/windows/win32/Adshlp/nf-adshlp-adsopenobject?branch=master) function or [**IADsOpenDSObject::OpenDSObject**](/windows/win32/Iads/nf-iads-iadsopendsobject-opendsobject?branch=master) method. The bind operation goes to the directory server once instead of twice. ADSI does not retrieve the **objectClass** attribute and, therefore, exposes only the base ADSI interfaces for the object.
-   The following interfaces are supported for the COM object:

    -   [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master)
    -   [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)
    -   [**IDirectoryObject**](/windows/win32/Iads/nn-iads-idirectoryobject?branch=master)
    -   [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master)
    -   [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master)
    -   [**IADsObjectOptions**](/windows/win32/Iads/nn-iads-iadsobjectoptions?branch=master)
    -   [**ISupportErrorInfo**](42d33066-36b4-4a5b-aa5d-46682e560f32)
    -   [**IADsDeleteOps**](/windows/win32/Iads/nn-iads-iadsdeleteops?branch=master)

-   If the [**IADsContainer::GetObject**](/windows/win32/Iads/nf-iads-iadscontainer-getobject?branch=master) method is used to bind to child objects, the child object has the same fast-bind characteristics as the parent.
-   The existence of the object being bound to is not verified during the bind operation, so subsequent method calls will fail if the object does not exist. Because of this, fast-binding should only be used for objects that are known to exist, for example, directly after performing a query that returned the distinguished names of the objects being bound to.
-   ADSI extensions are exposed for objects of class **top**. Therefore, only the extensions for the base ADSI interfaces listed above are exposed.

 

 




