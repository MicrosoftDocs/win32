---
title: Object Names and Identities
description: An object in Active Directory Domain Services has several identities, including the following.
ms.assetid: ad8bc74d-45a8-4df3-bfb8-35dd376b9c0b
ms.tgt_platform: multiple
keywords:
- object names and identities Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Object Names and Identities

An object in Active Directory Domain Services has several identities, including the following.

## Relative Distinguished Name

The relative distinguished name is the name defined by an object's naming attribute. The **rDnAttID** attribute of a **classSchema** object identifies the naming attribute for instances of the class. Most object classes use the **cn** (Common-Name) attribute as the naming attribute. An object's relative distinguished name must be unique in the container where the object resides. There can be many object instances with the same relative distinguished name, but no two can be in same container. For more information about the **rDnAttID** attribute and **classSchema** objects, see [Characteristics of Object Classes](characteristics-of-object-classes.md).

## Distinguished Name

The [*distinguished name*](/previous-versions/windows/desktop/legacy/ms681901(v=vs.85)) is the current name of the object and is contained in the **distinguishedName** attribute of the object. The distinguished name is a string that includes the location of the object and is formed by concatenating the relative distinguished name of the object and each of its ancestors all the way to root. For example, the distinguished name of the Users container in the Fabrikam.com domain would be "CN=Users,DC=Fabrikam,DC=com". Distinguished names are unique within a forest. An object's distinguished name changes when the object is moved or renamed.

## Object GUID

The object GUID is a globally unique identifier assigned by Active Directory Domain Services when the object instance is created. The object GUID is contained in the **objectGUID** attribute of the object. A GUID is a 128-bit number guaranteed to be unique in space and time. Object GUIDs never change, so if an object is renamed or moved anywhere in the enterprise forest, the object GUID remains the same. Applications that save references to objects in Active Directory Domain Services must use the object GUID to ensure that the object reference will survive a rename of the object. The distinguished name for an object might change, but the object GUID will not.

## Other Identities

Object instances can have many other attributes, and the attributes can be used for identification by applications. For example, security principal objects (instances of the **user**, **computer**, and **group** object classes) have **userPrincipalName**, **sAMAccountName**, and **objectSid** attributes. These attributes are very important "names" for Windows 2000, but these are not part of the object identity from the directory's perspective.

 

 