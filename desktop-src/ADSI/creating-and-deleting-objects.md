---
title: Creating and Deleting Objects
description: With ADSI, objects are created and deleted using either the IADsContainer or IDirectoryObject interface.
ms.assetid: 4d1f7ac5-48d3-4ea9-91e4-0cd4bb2ec9f8
ms.tgt_platform: multiple
keywords:
- Creating and Deleting Objects ADSI
- ADSI, Creating and Deleting Objects
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Deleting Objects

With ADSI, objects are created and deleted using either the [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) or [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface.

## Creating an Object with IADsContainer

**To create an object with the IADsContainer interface**

1.  Bind to the container that will contain the object to be created and obtain the [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) interface.
2.  Use the [**IADsContainer.Create**](/windows/desktop/api/Iads/nf-iads-iadscontainer-create) method to create a new object in the container.
3.  Set the values for all of the required attributes for the object using the [**IADs.Put**](/windows/desktop/api/Iads/nf-iads-iads-put) or [**IADs.PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) method. The attributes required to create an object will depend on the directory service and the type of object created. For more information about creating Active Directory objects, see [Creating and Deleting Active Directory Objects](/windows/desktop/AD/creating-and-deleting-objects-in-active-directory-domain-services).
4.  Set the values for all of the desired optional attributes for the object using the [**IADs.Put**](/windows/desktop/api/Iads/nf-iads-iads-put) or [**IADs.PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) method.
5.  Call the [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method to commit the object and its attributes. The new object is not actually created in the underlying directory service until the **IADs.SetInfo** method is called to commit the attributes.

## Creating an Object with IDirectoryObject

**To create an object with the IDirectoryObject interface**

1.  Bind to the container that will contain the object to be created and obtain the [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface.
2.  Allocate an array of [**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info) structures that contains one structure for each attribute to be set when the object is created.
3.  Fill in an [**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info) structure for each required attribute for the object. The attributes required to create an object will depend on the directory service and the type of object created. For more information about creating Active Directory objects, see [Creating and Deleting Active Directory Objects](/windows/desktop/AD/creating-and-deleting-objects-in-active-directory-domain-services).
4.  Fill in an [**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info) structure for each optional attribute for the object.
5.  Use the [**IDirectoryObject::CreateDSObject**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-createdsobject) method to create the object in the container. This method also commits the object to the underlying directory service. If the [**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info) array does not contain all of the required attributes for the object, **IDirectoryObject::CreateDSObject** will fail.

## Deleting an Object

To delete an object use the [**IADsContainer::Delete**](/windows/desktop/api/Iads/nf-iads-iadscontainer-delete) or the [**IDirectoryObject::DeleteDSObject**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-deletedsobject) method. These methods will fail if the deleted object contains any child objects. Use the [**IADsDeleteOps::DeleteObject**](/windows/desktop/api/Iads/nf-iads-iadsdeleteops-deleteobject) method to delete a container and all of the container's child objects.

What happens to a deleted object depends on the underlying directory service. For more information about deleting Active Directory objects, see [Creating and Deleting Active Directory Objects](/windows/desktop/AD/creating-and-deleting-objects-in-active-directory-domain-services).

 

 