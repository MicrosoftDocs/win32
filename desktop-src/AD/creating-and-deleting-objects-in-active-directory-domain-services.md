---
title: Creating and Deleting Objects in Active Directory Domain Services
description: The procedure used to programmatically create and delete objects in Active Directory Domain Services is dependent upon the programming technology used.
ms.assetid: 13f83aea-ad39-4737-af3c-24316a31046d
ms.tgt_platform: multiple
keywords:
- Creating and Deleting Active Directory Objects Active Directory
- Active Directory Domain Services Active Directory , using creating and deleting objects
- objects Active Directory , creating and deleting Active Directory Domain Services objects
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Deleting Objects in Active Directory Domain Services

The procedure used to programmatically create and delete objects in Active Directory Domain Services is dependent upon the programming technology used. For more information about creating and deleting objects in Active Directory Domain Services with a specific programming technology, see the topics listed in the following table.



| Programming technology                                                                       | For more information                                                            |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [Active Directory Service Interfaces](/windows/desktop/ADSI/active-directory-service-interfaces-adsi)         | [Creating and Deleting Objects](/windows/desktop/ADSI/creating-and-deleting-objects)             |
| [Lightweight Directory Access Protocol](/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api) | [Modifying a Directory Entry](/previous-versions/windows/desktop/ldap/modifying-a-directory-entry)                 |
| [System.DirectoryServices](/dotnet/api/system.directoryservices) | [Create, Delete, Rename and Move Objects](https://msdn.microsoft.com/library/ms180850(v=VS.80).aspx) |



 

## Creating an Object

In general, the only attributes required for an object to be created are the **cn** and **objectClass** attributes. Just creating an object does not necessarily make it a functional object however. Certain types of objects, such as users and groups, have additional required attributes to make them functional. For more information about creating specific types of objects, see [Creating a User](creating-a-user.md) and [Creating Groups in a Domain](creating-groups-in-a-domain.md).

**Windows Server 2003:** When an object of the [**user**](/windows/desktop/ADSchema/c-user), [**group**](/windows/desktop/ADSchema/c-group), or [**computer**](/windows/desktop/ADSchema/c-computer) class is created on a domain controller that is running on WWindows Server 2003 or later, the domain controller automatically sets the [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) attribute for the object to a unique string, if one is not specified.

## Deleting an Object

The Active Directory server performs the following actions when an object is deleted:

-   The **isDeleted** attribute of the deleted object is set to **TRUE**. Objects with an **isDeleted** attribute value set to **TRUE** are called [*tombstones*](/previous-versions/windows/desktop/legacy/ms681941(v=vs.85)).
-   The deleted object is moved to the Deleted Objects container for its naming context. If the object **systemFlags** property contains the 0x02000000 flag, the object is not moved to the Deleted Objects container. For more information about binding to and enumerating the contents of the Deleted Objects container, see [Retrieving Deleted Objects](retrieving-deleted-objects.md).
-   The Deleted Objects container is flat, so all objects reside at the same level within the Deleted Objects container. Thus, the relative distinguished name of the deleted object is changed to ensure that the name is unique within the Deleted Objects container. If the original name is longer than 75 characters, it is truncated to 75 characters. The following are then appended to the new name:
    1.  A 0x0A character
    2.  The string "DEL:"
    3.  The string form of a unique GUID, such as "947e3228-70c9-4311-8b7a-e5c9b5bd4432"

    An example of a deleted object name is:
    ```C++
    Jeff Smith\0ADEL:947e3228-70c9-4311-8b7a-e5c9b5bd4432
    ```

    

-   Most attribute values for the deleted object are removed. The following attributes are automatically retained:

    -   **attributeID**
    -   **attributeSyntax**
    -   **distinguishedName**
    -   **dNReferenceUpdate**
    -   **flatName**
    -   **governsID**
    -   **groupType**
    -   **instanceType**
    -   **lDAPDisplayName**
    -   **legacyExchangeDN**
    -   **mS-DS-CreatorSID**
    -   **mSMQOwnerID**
    -   **name**
    -   **nCName**
    -   **objectClass**
    -   **objectGUID**
    -   **objectSid**
    -   **oMSyntax**
    -   **proxiedObjectName**
    -   **replPropertyMetaData**
    -   **sAMAccountName**
    -   **securityIdentifier**
    -   **subClassOf**
    -   **systemFlags**
    -   **trustAttributes**
    -   **trustDirection**
    -   **trustPartner**
    -   **trustType**
    -   **userAccountControl**
    -   **uSNChanged**
    -   **uSNCreated**
    -   **whenCreated**

    Other attributes that have a **searchFlags** attribute value that contains 0x00000008 are also retained.

    The following attribute values are always removed from a deleted object:

    -   **objectCategory**
    -   **samAccountType**

-   The security descriptor of the deleted object is retained and inheritable access control entries are not propagated. The security descriptor is retained as-is at the time the object is deleted.
-   Links to and from the deleted object are cleared. This is performed in the background after the object is deleted. If the deleted object is restored before all of the links are cleared, an error will be received.
-   If the object is deleted on a Windows Server 2003 domain controller, the **lastKnownParent** attribute of the deleted object is set to the distinguished name of the container where the object was contained when it was deleted.

The deleted object remains in the Deleted Objects container for a period of time known as the *tombstone lifetime*. By default, the tombstone lifetime is 60 days, but this value can be changed by the system administrator. After the tombstone lifetime expires, the object is permanently removed from the Directory Service. To avoid missing a delete operation, an application must perform incremental synchronizations more frequently than the tombstone lifetime.

Windows Server 2003 adds the ability to restore deleted objects. For more information about deleted object restoration, see [Restoring Deleted Objects](restoring-deleted-objects.md).

When an item is deleted, none of the attributes of the object can be modified. In Windows Server 2003, it is possible to modify the security descriptor (the **ntSecurityDescriptor** attribute) on a deleted object. This is to allow restoration of objects when the person restoring the object does not have write permissions to mandatory attributes. To update the security descriptor on a deleted object, the caller must have the "Reanimate Tombstone" control access right on the naming context, in addition to regular **WRITE\_DAC** and **WRITE\_OWNER** access. Even if the security descriptor is restrictive, the administrator can first take ownership of the object, assuming the administrator has the **SE\_TAKE\_OWNERSHIP\_NAME** privilege, and then modify the security descriptor. To do this, use the [**ldap\_modify\_ext\_s**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_modify_ext_s) function with the [**LDAP\_SERVER\_SHOW\_DELETED\_OID**](/previous-versions/windows/desktop/ldap/ldap-server-show-deleted-oid) control. The modification list must contain a single attribute replacement for the **ntSecurityDescriptor** attribute.

 

 