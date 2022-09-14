---
description: Shows how to properly create a DACL.
ms.assetid: f8ec202f-4f34-4123-8f3c-cfc5960b4dc2
title: Creating a DACL
ms.topic: article
ms.date: 05/31/2018
---

# Creating a DACL

Creating a proper [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) is a necessary and important part of application development. Because a **NULL** DACL permits all types of access to all users, do not use **NULL** DACLs.

The following example shows how to properly create a DACL. The example contains a function, CreateMyDACL, that uses the [security descriptor definition language](/windows/desktop/SecAuthZ/security-descriptor-definition-language) (SDDL) to define the granted and denied access control in a DACL. To provide different access for your application's objects, modify the CreateMyDACL function as needed.

In the example:

1.  The main function passes an address of a [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure to the CreateMyDACL function.
2.  The CreateMyDACL function uses SDDL strings to:
    -   Deny access to guest and anonymous logon users.
    -   Allow read/write/execute access to authenticated users.
    -   Allow full control to administrators.

    For more information about the SDDL string formats, see [Security Descriptor String Format](/windows/desktop/SecAuthZ/security-descriptor-string-format).
3.  The CreateMyDACL function calls the [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) function to convert the SDDL strings to a [*security descriptor*](/windows/desktop/SecGloss/s-gly). The security descriptor is pointed to by the **lpSecurityDescriptor** member of the [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure. CreateMyDACL sends the return value from **ConvertStringSecurityDescriptorToSecurityDescriptor** to the main function.
4.  The main function uses the updated [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure to specify the DACL for a new folder that is created by the [**CreateDirectory**](/windows/desktop/api/fileapi/nf-fileapi-createdirectorya) function.
5.  When the main function is finished using the [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure, the main function frees the memory allocated for the **lpSecurityDescriptor** member by calling the [**LocalFree**](/windows/desktop/api/winbase/nf-winbase-localfree) function.

> [!Note]  
> To successfully compile SDDL functions such as [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora), you must define the \_WIN32\_WINNT constant as 0x0500 or greater.

 


```C++
#define _WIN32_WINNT 0x0500

#include <windows.h>
#include <sddl.h>
#include <stdio.h>

#pragma comment(lib, "advapi32.lib")

BOOL CreateMyDACL(SECURITY_ATTRIBUTES *);

void main()
{
     SECURITY_ATTRIBUTES  sa;
      
     sa.nLength = sizeof(SECURITY_ATTRIBUTES);
     sa.bInheritHandle = FALSE;  

     // Call function to set the DACL. The DACL
     // is set in the SECURITY_ATTRIBUTES 
     // lpSecurityDescriptor member.
     if (!CreateMyDACL(&sa))
     {
         // Error encountered; generate message and exit.
         printf("Failed CreateMyDACL\n");
         exit(1);
     }

     // Use the updated SECURITY_ATTRIBUTES to specify
     // security attributes for securable objects.
     // This example uses security attributes during
     // creation of a new directory.
     if (0 == CreateDirectory(TEXT("C:\\MyFolder"), &sa))
     {
         // Error encountered; generate message and exit.
         printf("Failed CreateDirectory\n");
         exit(1);
     }

     // Free the memory allocated for the SECURITY_DESCRIPTOR.
     if (NULL != LocalFree(sa.lpSecurityDescriptor))
     {
         // Error encountered; generate message and exit.
         printf("Failed LocalFree\n");
         exit(1);
     }
}


// CreateMyDACL.
//    Create a security descriptor that contains the DACL 
//    you want.
//    This function uses SDDL to make Deny and Allow ACEs.
//
// Parameter:
//    SECURITY_ATTRIBUTES * pSA
//    Pointer to a SECURITY_ATTRIBUTES structure. It is your
//    responsibility to properly initialize the 
//    structure and to free the structure's 
//    lpSecurityDescriptor member when you have
//    finished using it. To free the structure's 
//    lpSecurityDescriptor member, call the 
//    LocalFree function.
// 
// Return value:
//    FALSE if the address to the structure is NULL. 
//    Otherwise, this function returns the value from the
//    ConvertStringSecurityDescriptorToSecurityDescriptor 
//    function.
BOOL CreateMyDACL(SECURITY_ATTRIBUTES * pSA)
{
     // Define the SDDL for the DACL. This example sets 
     // the following access:
     //     Built-in guests are denied all access.
     //     Anonymous logon is denied all access.
     //     Authenticated users are allowed 
     //     read/write/execute access.
     //     Administrators are allowed full control.
     // Modify these values as needed to generate the proper
     // DACL for your application. 
     TCHAR * szSD = TEXT("D:")       // Discretionary ACL
        TEXT("(D;OICI;GA;;;BG)")     // Deny access to 
                                     // built-in guests
        TEXT("(D;OICI;GA;;;AN)")     // Deny access to 
                                     // anonymous logon
        TEXT("(A;OICI;GRGWGX;;;AU)") // Allow 
                                     // read/write/execute 
                                     // to authenticated 
                                     // users
        TEXT("(A;OICI;GA;;;BA)");    // Allow full control 
                                     // to administrators

    if (NULL == pSA)
        return FALSE;

     return ConvertStringSecurityDescriptorToSecurityDescriptor(
                szSD,
                SDDL_REVISION_1,
                &(pSA->lpSecurityDescriptor),
                NULL);
}
```



 

 
