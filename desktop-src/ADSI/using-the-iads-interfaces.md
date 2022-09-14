---
title: Using the IADs Interfaces
description: ADSI, each element of a directory service is represented by an ADSI object, which is a Component Object Model (COM) object that supports the standard COM IUnknown interface as well as the IDispatch and IADs interfaces.
ms.assetid: bdbf2012-6863-4611-8173-6a3cd9c4960f
ms.tgt_platform: multiple
keywords:
- IADs ADSI ,using
- ADSI ADSI ,using,using the IADs interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Using the IADs Interfaces

ADSI, each element of a directory service is represented by an ADSI object, which is a Component Object Model (COM) object that supports the standard COM [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface as well as the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) and [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interfaces. **IADs** supplies the basic maintenance functions for ADSI objects.

Each ADSI object must support this interface, which serves to:

-   Provide object identification by name, class, or ADsPath.
-   Identify the object container that manages creating and deleting objects.
-   Obtain the object schema definition.
-   Load the object attributes to the property cache and commit changes to the persistent directory store.
-   Access and modify the object attribute values in the property cache.

The [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface is designed to ensure that ADSI objects provide network administrators and directory service providers with an efficient and consistent representation of various underlying directory services.

![adsi object supporting the iads interface](images/ds2iads.png)

The preceding figure shows a generic ADSI object that support the fundamental interfaces [**IADs**](/windows/desktop/api/Iads/nn-iads-iads), [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist), [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown), [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject), and [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch). An ADSI object such as this manages data from the data store of the underlying directory service through the interfaces it supports. This data is known as the properties of the object, and the routines that obtain and set these properties are known as property methods. Read-only properties have one property method that obtains the property value. Read/write properties have two methods; a method that sets the value and one that obtains the value. Properties are implemented on each ADSI object using a [property cache](the-adsi-attribute-cache.md). [**IADs::get\_ADsPath**](iads-property-methods.md) and **IADs::put\_ADsPath** are examples of property methods. Property methods are not apparent to Visual Basic and other Automation clients that enable direct references to the property. For example, Visual Basic refers to **IADs::ADsPath** directly using the **Object.ADsPath** syntax. For more information, see [Interface Property Methods](interface-property-methods.md).

In addition, an ADSI object interacts with other ADSI objects and directly to a namespace through methods. Methods execute immediately. Examples of methods include [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) and [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo).

Properties, property methods, and methods are all accessed through standard COM interfaces.

An ADSI object is uniquely identified by its ADsPath. For example, an ADsPath for the LDAP namespace is "LDAP://MyServer/DC=Fabrikam,DC=COM". For more information about ADsPaths, see [ADSI Binding](binding-to-an-adsi-object.md). For programmers familiar with COM monikers, this is conceptually similar to the COM moniker display name.

Any ADSI object that contains other ADSI objects, called an ADSI container object, also supports the [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) interface, which provides methods and properties that manage the creation, deletion, and enumeration of ADSI objects contained by the object. The following figure shows an ADSI container object.

![adsi container object](images/dsiadsc.png)

Most ADSI objects are contained by other objects. The only ADSI object with no parent container is the top-level ADSI **Namespaces** object ("ADS:").

The [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method on a container object persistently stores the cached properties of the ADSI container object to storage in addition to any objects created with the [**IADsContainer::Create**](/windows/desktop/api/Iads/nf-iads-iadscontainer-create) method. [**IADsContainer::Delete**](/windows/desktop/api/Iads/nf-iads-iadscontainer-delete) does not affect the property cache but deletes the underlying namespace directory element represented by this object.

 

 