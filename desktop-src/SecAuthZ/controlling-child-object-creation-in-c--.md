---
description: You can use the DACL of a container object to control who is allowed to create child objects within the container.
ms.assetid: 95f2f058-f847-4f58-b469-090bf599ae98
title: Controlling Child Object Creation in C++
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Child Object Creation in C++

You can use the DACL of a container object to control who is allowed to create child objects within the container. This can be important because the creator of an object is typically assigned as the object's owner, and an object's owner can control access to the object.

The various types of container objects have specific access rights that control the ability to create child objects. For example, a thread must have KEY\_CREATE\_SUB\_KEY access to a registry key to create a subkey under the key. The DACL of a registry key can contain ACEs that allow or deny this access right. Similarly, NTFS supports the FILE\_ADD\_FILE and FILE\_ADD\_SUBDIRECTORY access rights for controlling the ability to create files or directories in a directory.

The ADS\_RIGHT\_DS\_CREATE\_CHILD access right controls the creation of child objects in a directory service (DS) object. However, DS objects can contain different types of objects, so the system supports a finer granularity of control. You can use [object-specific ACEs](object-specific-aces.md) to allow or deny the right to create a specified type of child object. You can allow a user to create one type of child object while preventing the user from creating other types of child objects.

The following example uses the [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla) function to add an object-specific ACE to an ACL. The ACE grants permission to create a specified type of child object. The **grfAccessPermissions** member of the [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structure is set to ADS\_RIGHT\_DS\_CREATE\_CHILD to indicate that the ACE controls the child object creation. The **ObjectsPresent** member of the [**OBJECTS\_AND\_SID**](/windows/desktop/api/AccCtrl/ns-accctrl-objects_and_sid) structure is set to ACE\_OBJECT\_TYPE\_PRESENT to indicate that the **ObjectTypeGuid** member contains a valid GUID. The GUID identifies a type of child object whose creation is being controlled.

In the following example, pOldDACL must be a valid pointer to an existing [**ACL**](/windows/desktop/api/Winnt/ns-winnt-acl) structure. For information about how to create an **ACL** structure for an object, see [Creating a Security Descriptor for a New Object in C++](creating-a-security-descriptor-for-a-new-object-in-c--.md).


```C++
DWORD dwRes;
PACL pOldDACL = NULL;
PACL pNewDACL = NULL;
GUID guidChildObjectType = GUID_NULL;   // GUID of object to control creation of
PSID pTrusteeSID = NULL;           // trustee for new ACE
EXPLICIT_ACCESS ea;
OBJECTS_AND_SID ObjectsAndSID;

// pOldDACL must be a valid pointer to an existing ACL structure.

// guidChildObjectType must be the GUID of an object type 
// that is a possible child of the object associated with pOldDACL.
 
// Initialize an OBJECTS_AND_SID structure with object type GUIDs and 
// the SID of the trustee for the new ACE. 

ZeroMemory(&ObjectsAndSID, sizeof(OBJECTS_AND_SID));
ObjectsAndSID.ObjectsPresent = ACE_OBJECT_TYPE_PRESENT;
ObjectsAndSID.ObjectTypeGuid = guidChildObjectType;
ObjectsAndSID.InheritedObjectTypeGuid  = GUID_NULL;
ObjectsAndSID.pSid = (SID *)pTrusteeSID;

// Initialize an EXPLICIT_ACCESS structure for the new ACE. 

ZeroMemory(&ea, sizeof(EXPLICIT_ACCESS));
ea.grfAccessPermissions = ADS_RIGHT_DS_CREATE_CHILD;
ea.grfAccessMode = GRANT_ACCESS;
ea.grfInheritance= NO_INHERITANCE;
ea.Trustee.TrusteeForm = TRUSTEE_IS_OBJECTS_AND_SID;
ea.Trustee.ptstrName = (LPTSTR) &ObjectsAndSID;

// Create a new ACL that merges the new ACE
// into the existing DACL.

dwRes = SetEntriesInAcl(1, &ea, pOldDACL, &pNewDACL);
```



 

 



