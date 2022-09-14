---
title: Restoring Deleted Objects
description: Windows Server 2003 includes the \ 0034;restore deleted objects \ 0034; feature.
ms.assetid: b64c5c91-fb76-4323-b78d-f692aa887c96
ms.tgt_platform: multiple
keywords:
- Restoring Deleted Objects AD
- Active Directory, using, restoring deleted objects
- objects AD , restoring deleted objects
ms.topic: article
ms.date: 05/31/2018
---

# Restoring Deleted Objects

Windows Server 2003 includes the "restore deleted objects" feature.

To enable deleted object restoration, at least one domain controller in the domain must be running on Windows Server 2003 or a later version of Windows. By default, only domain administrators can restore deleted objects, though this can be delegated to others.

The following limitations apply to restoring deleted objects:

-   An object cannot be restored when the tombstone lifetime for the object has expired because when the tombstone lifetime has expired, the object is permanently deleted.
-   Objects that exist at the root of the naming context, such as a domain or application partition, cannot be restored.
-   Schema objects cannot be restored. Schema objects should never be deleted.
-   It is possible to restore deleted containers, but the restoration of the deleted objects that were in the container before the deletion is difficult because the tree structure under the container must be manually reconstructed.

## Permissions Required to Restore a Deleted Object

When an object is deleted, the object security descriptor is retained. Although the owner is identifiable from the security descriptor, for security reasons, only domain administrators are allowed to restore deleted objects. Domain administrators can grant the permission to restore delete objects to other users and groups by granting the user or group the "Reanimate Tombstone" control access right. The "Reanimate Tombstone" control access right is granted at the Naming Context root. Only users that had read access permission on an object and its attributes are permitted to read the object and accessible attributes after the object is deleted.

> [!Note]  
> Granting a user this permission can be a security risk because it could permit the user to restore an account object that has access to resources that the user would not normally have access to. By restoring an account, the user essentially gains control of this account because the user must set the initial password on the account when the account is restored.

 

To completely restore a deleted object, the user must:

-   Have, or be a member of a group that has, the "Reanimate Tombstone" control access right.

-   Have write access for each mandatory attribute that requires updating.

-   Have write access to the Relative Distinguished Name (RDN).

-   Have write access to each optional attribute that needs to be updated.

-   Have child-creation rights on the destination container for the object class of restored object.

    > [!Note]  
    > The **isDeleted** attribute is not verified during the restore operation. Neither will the delete-child permission on the "Deleted Objects" container be verified.

     

## Restoring a Deleted Object

To restore a deleted object, the object must first be located in the Deleted Objects container. For more information about retrieving deleted objects, see [Retrieving Deleted Objects](retrieving-deleted-objects.md).

When the object has been located, the following operations must be completed in a single LDAP operation. This requires the use of the [**ldap\_modify\_ext\_s**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_modify_ext_s) function with the [**LDAP\_SERVER\_SHOW\_DELETED\_OID**](/previous-versions/windows/desktop/ldap/ldap-server-show-deleted-oid) control.

-   Remove the **isDeleted** attribute value. The **isDeleted** attribute value must be removed, not set to **FALSE**.
-   Replace the distinguished name of the object so that it is moved to a container other than the Deleted Objects container. This can be any container that can normally contain the object. The distinguished name of the previous container of the object can be found in the deleted object's **lastKnownParent** attribute. The **lastKnownParent** attribute is only set if the object was deleted on a Windows Server 2003 domain controller. Thus, it is possible that the content of the **lastKnownParent** attribute is inaccurate.
-   Restore the mandatory attributes for the object that were cleared during deletion.

> [!Note]  
> The **objectCategory** attribute can also be set when the object is restored, but is not required. If no **objectCategory** value is specified, the default **objectCategory** for the object's **objectClass** is used.

 

After the object is restored, it can be accessed as it was before it was deleted. At this point, any optional attributes that are important should be restored. Any references to the object from other objects in the directory must also be restored.

As a security measure, user objects are disabled when they are restored. User objects must be enabled after restoring the optional attributes to allow the user object to be used.

For more information and a code example that shows how to restore a deleted object, see the RestoreDeletedObject function below.

## RestoreDeletedObject

The following C++ code example shows how to restore a deleted object.


```C++
//***************************************************************************
//
//  RestoreDeletedObject()
//
//  Restores a deleted object. 
//
//  pwszDeletedDN - Contains the fully qualified distinguished name of the 
//  deleted object.
//
//  pwszDestContainerDN - Contains the fully qualified distinguished name of 
//  the folder that the deleted object should be moved to.
//
//  Returns S_OK if successful or an HRESULT or LDAP error code otherwise.
//
//***************************************************************************

HRESULT RestoreDeletedObject(LPCWSTR pwszDeletedDN, LPCWSTR pwszDestContainerDN)
{
    if((NULL == pwszDeletedDN) || (NULL == pwszDestContainerDN))
    {
        return E_POINTER;
    }
    
    HRESULT hr = E_FAIL;

    // Build the new distinguished name.
    LPWSTR pwszNewDN = new WCHAR[lstrlenW(pwszDeletedDN) + lstrlenW(pwszDestContainerDN) + 1];
    if(pwszNewDN)
    {
        wcscpy_s(pwszNewDN, pwszDeletedDN);

        // Search for the first 0x0A character. This is the delimiter in the deleted object name.
        LPWSTR pwszChar;
        for(pwszChar = pwszNewDN; *pwszChar; pwszChar = CharNextW(pwszChar))
        {
            if(('\\' == *pwszChar) && ('0' == *(pwszChar + 1)) && ('A' == *(pwszChar + 2)))
            {
                break;
            }
            
        }

        if(0 != *pwszChar)
        {
            // Truncate the name string at the delimiter.
            *pwszChar = 0;

            // Add the last known parent DN to complete the DN.
            wcscat_s(pwszNewDN, L",");
            wcscat_s(pwszNewDN, pwszDestContainerDN);

            PLDAP ld;

            // Initialize LDAP.
            ld = ldap_init(NULL, LDAP_PORT);
            if(NULL != ld) 
            {
                ULONG ulRC;
                ULONG version = LDAP_VERSION3;

                // Set the LDAP version.
                ulRC = ldap_set_option(ld, LDAP_OPT_PROTOCOL_VERSION, (void*)&version);
                if(LDAP_SUCCESS == ulRC)
                {
                    // Establish a connection with the server.
                    ulRC = ldap_connect(ld, NULL);
                    if(LDAP_SUCCESS == ulRC)
                    {                    
                        // Bind to the LDAP server.
                        ulRC = ldap_bind_s(ld, NULL, NULL, LDAP_AUTH_NEGOTIATE);
                        if(LDAP_SUCCESS == ulRC)
                        {
                            // Setup the new values.
                            LPWSTR rgNewVals[] = {pwszNewDN, NULL};

                            /*
                            Remove the isDeleted attribute. This cannot be set 
                            to FALSE or the restore operation will not work.
                            */
                            LDAPModW modIsDeleted = { LDAP_MOD_DELETE, L"isDeleted", NULL };

                            /*
                            Set the new DN, in effect, moving the deleted 
                            object to where it resided before the deletion.
                            */
                            LDAPModW modDN = { LDAP_MOD_REPLACE, L"distinguishedName", rgNewVals };
                            
                            // Initialize the LDAPMod structure.
                            PLDAPModW ldapMods[] = 
                            {
                                &modIsDeleted,
                                &modDN,
                                NULL
                            };

                            /*
                            Use the LDAP_SERVER_SHOW_DELETED_OID control to 
                            modify deleted objects.
                            */
                            LDAPControlW showDeletedControl;
                            showDeletedControl.ldctl_oid = LDAP_SERVER_SHOW_DELETED_OID_W;
                            showDeletedControl.ldctl_value.bv_len = 0;
                            showDeletedControl.ldctl_value.bv_val = NULL;
                            showDeletedControl.ldctl_iscritical = TRUE;

                            // Initialzie the LDAPControl structure
                            PLDAPControlW ldapControls[] = { &showDeletedControl, NULL };

                            /*
                            Modify the specified attributes. This must performed 
                            in one step, which is why the LDAP APIs must be used 
                            to restore a deleted object.
                            */
                            ulRC = ldap_modify_ext_sW(ld, (PWCHAR)pwszDeletedDN, ldapMods, ldapControls, NULL);
                            if(LDAP_SUCCESS == ulRC)
                            {
                                hr = S_OK;
                            }
                            else if(LDAP_ALREADY_EXISTS == ulRC)
                            {
                                /*
                                An object already exists with the specified name 
                                in the specified target container. At this point, 
                                a new name must be selected.
                                */
                            }
                        }
                    }
                }

                if(LDAP_SUCCESS != ulRC)
                {
                    hr = ulRC;
                    
                    OutputDebugString(ldap_err2string(ulRC));
                }

                // Release the LDAP session.
                ldap_unbind(ld);
            }
        }
        else
        {
            /*
            If the end of the string is reached before the delimiter is found, just 
            end and fail.
            */
            hr = E_INVALIDARG;
        }
    
        delete pwszNewDN;
    }
    else
    {
        hr = E_OUTOFMEMORY;
    }

    return hr;
}

```



 

 