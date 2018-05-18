---
title: Creating and Deleting Objects
description: With ADSI, objects are created and deleted using either the IADsContainer or IDirectoryObject interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '4d1f7ac5-48d3-4ea9-91e4-0cd4bb2ec9f8'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Creating and Deleting Objects ADSI", "ADSI, Creating and Deleting Objects"]
---

# Creating and Deleting Objects

With ADSI, objects are created and deleted using either the [**IADsContainer**](iadscontainer.md) or [**IDirectoryObject**](idirectoryobject.md) interface.

## Creating an Object with IADsContainer

**To create an object with the IADsContainer interface**

1.  Bind to the container that will contain the object to be created and obtain the [**IADsContainer**](iadscontainer.md) interface.
2.  Use the [**IADsContainer.Create**](iadscontainer-create.md) method to create a new object in the container.
3.  Set the values for all of the required attributes for the object using the [**IADs.Put**](iads-put.md) or [**IADs.PutEx**](iads-putex.md) method. The attributes required to create an object will depend on the directory service and the type of object created. For more information about creating Active Directory objects, see [Creating and Deleting Active Directory Objects](https://msdn.microsoft.com/library/aa772216).
4.  Set the values for all of the desired optional attributes for the object using the [**IADs.Put**](iads-put.md) or [**IADs.PutEx**](iads-putex.md) method.
5.  Call the [**IADs.SetInfo**](iads-setinfo.md) method to commit the object and its attributes. The new object is not actually created in the underlying directory service until the **IADs.SetInfo** method is called to commit the attributes.

## Creating an Object with IDirectoryObject

**To create an object with the IDirectoryObject interface**

1.  Bind to the container that will contain the object to be created and obtain the [**IDirectoryObject**](idirectoryobject.md) interface.
2.  Allocate an array of [**ADS\_ATTR\_INFO**](ads-attr-info.md) structures that contains one structure for each attribute to be set when the object is created.
3.  Fill in an [**ADS\_ATTR\_INFO**](ads-attr-info.md) structure for each required attribute for the object. The attributes required to create an object will depend on the directory service and the type of object created. For more information about creating Active Directory objects, see [Creating and Deleting Active Directory Objects](https://msdn.microsoft.com/library/aa772216).
4.  Fill in an [**ADS\_ATTR\_INFO**](ads-attr-info.md) structure for each optional attribute for the object.
5.  Use the [**IDirectoryObject::CreateDSObject**](idirectoryobject-createdsobject.md) method to create the object in the container. This method also commits the object to the underlying directory service. If the [**ADS\_ATTR\_INFO**](ads-attr-info.md) array does not contain all of the required attributes for the object, **IDirectoryObject::CreateDSObject** will fail.

## Deleting an Object

To delete an object use the [**IADsContainer::Delete**](iadscontainer-delete.md) or the [**IDirectoryObject::DeleteDSObject**](idirectoryobject-deletedsobject.md) method. These methods will fail if the deleted object contains any child objects. Use the [**IADsDeleteOps::DeleteObject**](iadsdeleteops-deleteobject.md) method to delete a container and all of the container's child objects.

What happens to a deleted object depends on the underlying directory service. For more information about deleting Active Directory objects, see [Creating and Deleting Active Directory Objects](https://msdn.microsoft.com/library/aa772216).

 

 




