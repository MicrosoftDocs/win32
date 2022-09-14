---
description: The following example adds an access control entry (ACE) to the discretionary access control list (DACL) of an object.
ms.assetid: 0c168bb7-996f-42a8-96cd-2ba7870a3333
title: Modifying the ACLs of an Object in C++
ms.topic: article
ms.date: 05/31/2018
---

# Modifying the ACLs of an Object in C++

The following example adds an [*access control entry*](/windows/desktop/SecGloss/a-gly) (ACE) to the [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) of an object.

The *AccessMode* parameter determines the type of new ACE and how the new ACE is combined with any existing ACEs for the specified trustee. Use the GRANT\_ACCESS, SET\_ACCESS, DENY\_ACCESS, or REVOKE\_ACCESS flags in the *AccessMode* parameter. For information about these flags, see [**ACCESS\_MODE**](/windows/win32/api/accctrl/ne-accctrl-access_mode).

Similar code can be used to work with a [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). Specify SACL\_SECURITY\_INFORMATION in the [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa) and [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) functions to get and set the SACL for the object. Use the SET\_AUDIT\_SUCCESS, SET\_AUDIT\_FAILURE, and REVOKE\_ACCESS flags in the *AccessMode* parameter. For information about these flags, see [**ACCESS\_MODE**](/windows/win32/api/accctrl/ne-accctrl-access_mode).

Use this code to add an [object-specific ACE](object-specific-aces.md) to the DACL of a directory service object. To specify the GUIDs in an object-specific ACE, set the *TrusteeForm* parameter to TRUSTEE\_IS\_OBJECTS\_AND\_NAME or TRUSTEE\_IS\_OBJECTS\_AND\_SID and set the *pszTrustee* parameter to be a pointer to an [**OBJECTS\_AND\_NAME**](/windows/desktop/api/AccCtrl/ns-accctrl-objects_and_name_a) or [**OBJECTS\_AND\_SID**](/windows/desktop/api/AccCtrl/ns-accctrl-objects_and_sid) structure.

This example uses the [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa) function to get the existing DACL. Then it fills an [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structure with information about an ACE and uses the [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla) function to merge the new ACE with any existing ACEs in the DACL. Finally, the example calls the [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) function to attach the new DACL to the [*security descriptor*](/windows/desktop/SecGloss/s-gly) of the object.


```C++
#include <windows.h>
#include <stdio.h>

DWORD AddAceToObjectsSecurityDescriptor (
    LPTSTR pszObjName,          // name of object
    SE_OBJECT_TYPE ObjectType,  // type of object
    LPTSTR pszTrustee,          // trustee for new ACE
    TRUSTEE_FORM TrusteeForm,   // format of trustee structure
    DWORD dwAccessRights,       // access mask for new ACE
    ACCESS_MODE AccessMode,     // type of ACE
    DWORD dwInheritance         // inheritance flags for new ACE
) 
{
    DWORD dwRes = 0;
    PACL pOldDACL = NULL, pNewDACL = NULL;
    PSECURITY_DESCRIPTOR pSD = NULL;
    EXPLICIT_ACCESS ea;

    if (NULL == pszObjName) 
        return ERROR_INVALID_PARAMETER;

    // Get a pointer to the existing DACL.

    dwRes = GetNamedSecurityInfo(pszObjName, ObjectType, 
          DACL_SECURITY_INFORMATION,
          NULL, NULL, &pOldDACL, NULL, &pSD);
    if (ERROR_SUCCESS != dwRes) {
        printf( "GetNamedSecurityInfo Error %u\n", dwRes );
        goto Cleanup; 
    }  

    // Initialize an EXPLICIT_ACCESS structure for the new ACE. 

    ZeroMemory(&ea, sizeof(EXPLICIT_ACCESS));
    ea.grfAccessPermissions = dwAccessRights;
    ea.grfAccessMode = AccessMode;
    ea.grfInheritance= dwInheritance;
    ea.Trustee.TrusteeForm = TrusteeForm;
    ea.Trustee.ptstrName = pszTrustee;

    // Create a new ACL that merges the new ACE
    // into the existing DACL.

    dwRes = SetEntriesInAcl(1, &ea, pOldDACL, &pNewDACL);
    if (ERROR_SUCCESS != dwRes)  {
        printf( "SetEntriesInAcl Error %u\n", dwRes );
        goto Cleanup; 
    }  

    // Attach the new ACL as the object's DACL.

    dwRes = SetNamedSecurityInfo(pszObjName, ObjectType, 
          DACL_SECURITY_INFORMATION,
          NULL, NULL, pNewDACL, NULL);
    if (ERROR_SUCCESS != dwRes)  {
        printf( "SetNamedSecurityInfo Error %u\n", dwRes );
        goto Cleanup; 
    }  

    Cleanup:

        if(pSD != NULL) 
            LocalFree((HLOCAL) pSD); 
        if(pNewDACL != NULL) 
            LocalFree((HLOCAL) pNewDACL); 

        return dwRes;
}

```



 

 
