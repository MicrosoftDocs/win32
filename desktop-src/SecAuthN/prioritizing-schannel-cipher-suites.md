---
description: 'Cryptography API: Next Generation (CNG) provides functions that query, add, remove, and prioritize the cipher suites that a provider supports. Changes made by using these functions take effect immediately and do not require restarting an active server.'
ms.assetid: e919be5c-ac2c-446c-a422-971805b1f672
title: Prioritizing Schannel Cipher Suites
ms.topic: article
ms.date: 05/31/2018
---

# Prioritizing Schannel Cipher Suites

[Cryptography API: Next Generation](../seccng/cng-portal.md) (CNG) provides functions that query, add, remove, and prioritize the cipher suites that a provider supports. Changes made by using these functions take effect immediately and do not require restarting an active server.

> [!Note]
> You can also modify the list of cipher suites by configuring the **SSL Cipher Suite Order** group policy settings using the Group Policy Object snap-in in Microsoft Management Console.
> 
> **To configure the **SSL Cipher Suite Order** group policy setting**
> 
> 1.  At a command prompt, enter **gpedit.msc**. The **Group Policy Object Editor** appears.
> 2.  Expand **Computer Configuration**, **Administrative Templates**, **Network**, and then click **SSL Configuration Settings**.
> 3.  Under **SSL Configuration Settings**, click the **SSL Cipher Suite Order** setting.
> 4.  In the **SSL Cipher Suite Order** pane, scroll to the bottom of the pane.
> 5.  Follow the instructions labeled **How to modify this setting**.
> 
> It is necessary to restart the computer after modifying this setting for the changes to take effect.

 

The list of cipher suites is limited to 1023 characters.

To prioritize Schannel cipher suites, see the following examples.

-   [Listing Supported Cipher Suites](#listing-supported-cipher-suites)
-   [Adding, Removing, and Prioritizing Cipher Suites](#adding-removing-and-prioritizing-cipher-suites)

## Listing Supported Cipher Suites

Call the [**BCryptEnumContextFunctions**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumcontextfunctions) function to list the cipher suites that a provider supports in order of priority.

The following example demonstrates how to use the [**BCryptEnumContextFunctions**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumcontextfunctions) function to list supported cipher suites.


```C++
#include <stdio.h>
#include <windows.h>
#include <bcrypt.h>


void main()
{

   HRESULT Status = ERROR_SUCCESS;
   DWORD   cbBuffer = 0;
   PCRYPT_CONTEXT_FUNCTIONS pBuffer = NULL;

    Status = BCryptEnumContextFunctions(
        CRYPT_LOCAL,
        L"SSL",
        NCRYPT_SCHANNEL_INTERFACE,
        &cbBuffer,
        &pBuffer);
    if(FAILED(Status))
    {
        printf_s("\n**** Error 0x%x returned by BCryptEnumContextFunctions\n", Status);
        goto Cleanup;
    }
                
    if(pBuffer == NULL)
    {
        printf_s("\n**** Error pBuffer returned from BCryptEnumContextFunctions is null");
        goto Cleanup;
    }

    printf_s("\n\n Listing Cipher Suites ");
    for(UINT index = 0; index < pBuffer->cFunctions; ++index)
    {
        printf_s("\n%S", pBuffer->rgpszFunctions[index]);
    }

Cleanup:
    if (pBuffer != NULL)
    {
        BCryptFreeBuffer(pBuffer);
    }
}


```



## Adding, Removing, and Prioritizing Cipher Suites

Call the [**BCryptAddContextFunction**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptaddcontextfunction) and [**BCryptRemoveContextFunction**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptremovecontextfunction) functions to add and remove cipher suites from the list of supported cipher suites.

When adding a cipher suite, set the value of the *dwPosition* parameter of the [**BCryptAddContextFunction**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptaddcontextfunction) function to **CRYPT\_PRIORITY\_TOP** to add it to the top of the prioritized list, or to **CRYPT\_PRIORITY\_BOTTOM** to add it to the bottom of the list.

To prioritize the list of cipher suites, remove all of the cipher suites from the list, and then add cipher suites to the list in the order you want them.

The following example shows how to add a cipher suite to the top of the prioritized list for the default Microsoft Schannel Provider.


```C++
#include <stdio.h>
#include <windows.h>
#include <bcrypt.h>


void main()
{
    
    SECURITY_STATUS Status = ERROR_SUCCESS;
    LPWSTR wszCipher = (L"RSA_EXPORT1024_DES_CBC_SHA");
       
    Status = BCryptAddContextFunction(
                CRYPT_LOCAL,
                L"SSL",
                NCRYPT_SCHANNEL_INTERFACE,
                wszCipher,
                CRYPT_PRIORITY_TOP);
}


```



The following example shows how to remove a cipher suite from the prioritized list for the default Microsoft Schannel Provider.


```C++
#include <stdio.h>
#include <windows.h>
#include <bcrypt.h>


void main()
{
    
    SECURITY_STATUS Status = ERROR_SUCCESS;
      LPWSTR wszCipher = (L"TLS_RSA_WITH_RC4_128_SHA");
       
    Status = BCryptRemoveContextFunction(
                CRYPT_LOCAL,
                L"SSL",
                NCRYPT_SCHANNEL_INTERFACE,
                wszCipher);
}


```



 

 
