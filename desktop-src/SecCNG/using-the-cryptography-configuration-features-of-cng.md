---
description: Provides functions to enumerate and obtain information about registered providers.
ms.assetid: 5b07060e-0c66-4bf2-b697-05231cb38375
title: Using the Cryptography Configuration Features of CNG
ms.topic: article
ms.date: 05/31/2018
---

# Using the Cryptography Configuration Features of CNG

The CNG API provides functions to enumerate and obtain information about registered providers.

-   [Enumerating Providers](#enumerating-providers)
-   [Getting Provider Registration Information](#getting-provider-registration-information)

## Enumerating Providers

You use the [**BCryptEnumRegisteredProviders**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptenumregisteredproviders) function to enumerate the registered providers. The **BCryptEnumRegisteredProviders** function can be called in one of two ways:

1.  The first is to have the [**BCryptEnumRegisteredProviders**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptenumregisteredproviders) function allocate the memory. This is accomplished by passing the address of a **NULL** pointer for the *ppBuffer* parameter. This code will allocate the memory required for the [**CRYPT\_PROVIDERS**](/windows/desktop/api/Bcrypt/ns-bcrypt-crypt_providers) structure and the associated strings. When the **BCryptEnumRegisteredProviders** function is used in this manner, you must free the memory when it is no longer needed by passing *ppBuffer* to the [**BCryptFreeBuffer**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptfreebuffer) function.

    The following example shows how to use the [**BCryptEnumRegisteredProviders**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptenumregisteredproviders) function to allocate the buffer for you.

    ```C++
    #include <windows.h>

    #ifndef NT_SUCCESS
    #define NT_SUCCESS(Status) ((NTSTATUS)(Status) >= 0)
    #endif

    void EnumProviders1()
    {
        NTSTATUS status;
        ULONG cbBuffer = 0;
        PCRYPT_PROVIDERS pBuffer = NULL;

        /*
        Get the providers, letting the BCryptEnumRegisteredProviders 
        function allocate the memory.
        */
        status = BCryptEnumRegisteredProviders(&cbBuffer, &pBuffer);

        if (NT_SUCCESS(status))
        {
            if (pBuffer != NULL)
            {
                // Enumerate the providers.
                for (ULONG i = 0; i < pBuffer->cProviders; i++)
                {
                    printf("%S\n", pBuffer->rgpszProviders[i]);
                }
            }
        }
        else
        {
            printf("BCryptEnumRegisteredProviders failed with error " 
                "code 0x%08x\n", status);
        }

        if (NULL != pBuffer)
        {
            /*
            Free the memory allocated by the 
            BCryptEnumRegisteredProviders function.
            */
            BCryptFreeBuffer(pBuffer);
        }
    }
    
    ```

    

2.  The second method is to allocate the required memory yourself. This is accomplished by calling the [**BCryptEnumRegisteredProviders**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptenumregisteredproviders) function with **NULL** for the *ppBuffer* parameter. The **BCryptEnumRegisteredProviders** function will place in the value pointed to by the *pcbBuffer* parameter, the required size, in bytes, of the [**CRYPT\_PROVIDERS**](/windows/desktop/api/Bcrypt/ns-bcrypt-crypt_providers) structure and all strings. You then allocate the required memory and pass the address of this buffer pointer for the *ppBuffer* parameter in a second call to the **BCryptEnumRegisteredProviders** function.

    The following example shows how to use the [**BCryptEnumRegisteredProviders**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptenumregisteredproviders) function to allocate and use your own buffer.

    ```C++
    #include <windows.h>
    #include <stdio.h>

    #ifndef NT_SUCCESS
    #define NT_SUCCESS(Status) ((NTSTATUS)(Status) >= 0)
    #endif

    void EnumProviders2()
    {
        NTSTATUS status;
        ULONG cbBuffer = 0;

        // Get the required size of the buffer.
        status = BCryptEnumRegisteredProviders(&cbBuffer, NULL);

        if (STATUS_BUFFER_TOO_SMALL == status)
        {
            // Allocate the buffer.
            PCRYPT_PROVIDERS pBuffer = 
                (PCRYPT_PROVIDERS)LocalAlloc(LPTR, cbBuffer);
            if (NULL != pBuffer)
            {
                // Get the providers in the buffer that was allocated.
                status = BCryptEnumRegisteredProviders(
                    &cbBuffer, 
                    &pBuffer);
                if (NT_SUCCESS(status))
                {
                    for (ULONG i = 0; i < pBuffer->cProviders; i++)
                    {
                        // Enumerate the providers.
                        printf("%S\n", pBuffer->rgpszProviders[i]);
                    }
                }

                // Free the memory that was allocated.
                LocalFree(pBuffer);
            }
        }
    }
    
    ```

    

## Getting Provider Registration Information

The [**BCryptQueryProviderRegistration**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptqueryproviderregistration) function is used to obtain additional, registration-specific information about a provider. This function takes the name of the provider that you want to obtain information for, the desired provider mode (kernel mode, user mode, or both), and the identifier of the provider interface to retrieve the registration information for. For example, to obtain the user mode registration information for the cipher interface for the "Microsoft Primitive Provider" provider, you would make a call similar to the following.


```C++
BCryptQueryProviderRegistration(
    MS_PRIMITIVE_PROVIDER,
    CRYPT_UM,
    BCRYPT_CIPHER_INTERFACE,
    //...
    );

```



Like the [**BCryptEnumRegisteredProviders**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptenumregisteredproviders) function, the [**BCryptQueryProviderRegistration**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptqueryproviderregistration) function can either allocate memory for you or you can allocate the memory yourself. The process is the same for the two functions.

 

 



