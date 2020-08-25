---
title: Fast Binding Option for Batch Write/Modify Operations
description: When a directory service object is bound to, ADSI creates a COM object that represents the specified directory object.
ms.assetid: cf41b0c4-7459-49cf-945b-8462c7d19947
ms.tgt_platform: multiple
keywords:
- Fast Binding Option for Batch Write/Modify Operations ADSI
- ADSI ADSI , Using, Fast Binding Option for Batch Write/Modify Operations
ms.topic: article
ms.date: 05/31/2018
---

# Fast Binding Option for Batch Write/Modify Operations

When a directory service object is bound to, ADSI creates a COM object that represents the specified directory object. When binding, ADSI will typically retrieve the **objectClass** attribute so that ADSI can expose the COM interfaces that are appropriate for that class of object. For example, a user object would expose the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) interface in addition to the base ADSI interfaces supported for all objects. For a single operation, this should have no effect on performance. However, if batch operations are performed that require hundreds or thousands of bindings over a slow connection and those operations are writing data to the directory service, it may be desirable to exchange full object support for faster binding. This is known as a fast-bind and is accomplished by specifying the **ADS\_FAST\_BIND** flag when [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) is called.

Fast-binding has the following restrictions:

-   The bind operation must be performed with the [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) function or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) method. The bind operation goes to the directory server once instead of twice. ADSI does not retrieve the **objectClass** attribute and, therefore, exposes only the base ADSI interfaces for the object.
-   The following interfaces are supported for the COM object:

    -   [**IADs**](/windows/desktop/api/Iads/nn-iads-iads)
    -   [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer)
    -   [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject)
    -   [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch)
    -   [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist)
    -   [**IADsObjectOptions**](/windows/desktop/api/Iads/nn-iads-iadsobjectoptions)
    -   [**ISupportErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-isupporterrorinfo)
    -   [**IADsDeleteOps**](/windows/desktop/api/Iads/nn-iads-iadsdeleteops)

-   If the [**IADsContainer::GetObject**](/windows/desktop/api/Iads/nf-iads-iadscontainer-getobject) method is used to bind to child objects, the child object has the same fast-bind characteristics as the parent.
-   The existence of the object being bound to is not verified during the bind operation, so subsequent method calls will fail if the object does not exist. Because of this, fast-binding should only be used for objects that are known to exist, for example, directly after performing a query that returned the distinguished names of the objects being bound to.
-   ADSI extensions are exposed for objects of class **top**. Therefore, only the extensions for the base ADSI interfaces listed above are exposed.

 

 