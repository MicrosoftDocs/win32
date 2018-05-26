---
Description: The following example creates a random session key, duplicates the key, sets some additional parameters on the original key, and destroys both the original and the duplicate keys.
ms.assetid: e57274cf-42d3-445b-97f1-dd574010290f
title: Example C Program Duplicating a Session Key
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Example C Program: Duplicating a Session Key

The following example creates a random [*session key*](security.s_gly#-security-session-key-gly), duplicates the key, sets some additional parameters on the original key, and destroys both the original and the duplicate keys. This example illustrates the use of [**CryptDuplicateKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptduplicatekey?branch=master) and related functions.

This example illustrates the following tasks and CryptoAPI functions:

-   Accessing a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) using [**CryptAcquireContext**](/windows/win32/Wincrypt/nf-wincrypt-cryptacquirecontexta?branch=master).
-   Creating a session key using [**CryptGenKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptgenkey?branch=master).
-   Duplicating the key created using [**CryptDuplicateKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptduplicatekey?branch=master).
-   Using [**CryptSetKeyParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptsetkeyparam?branch=master) to alter the key generation process in two different ways.
-   Filling a buffer with random bytes using [**CryptGenRandom**](/windows/win32/Wincrypt/nf-wincrypt-cryptgenrandom?branch=master).
-   Destroying the keys using [**CryptDestroyKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptdestroykey?branch=master).
-   Releasing the CSP with [**CryptReleaseContext**](/windows/win32/Wincrypt/nf-wincrypt-cryptreleasecontext?branch=master).

This example uses the function [**MyHandleError**](myhandleerror.md). The code for this function is included with the sample. Code for this and other auxiliary functions is also listed under [General Purpose Functions](general-purpose-functions.md).


```C++
#pragma comment(lib, "crypt32.lib")

#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)
void MyHandleError(char *s);

//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// Begin main.

void main()
{
//-------------------------------------------------------------------
// Declare and initialize variables.

HCRYPTPROV   hCryptProv;
HCRYPTKEY    hOriginalKey;
HCRYPTKEY    hDuplicateKey;
DWORD        dwMode;
BYTE         pbData[16];

//-------------------------------------------------------------------
// Begin processing.

printf("This program creates a session key and duplicates \n");
printf("that key. Next, parameters are added to the original \n");
printf("key. Finally, both keys are destroyed. \n\n");

//-------------------------------------------------------------------
// Acquire a cryptographic provider context handle.

if(CryptAcquireContext(    
   &amp;hCryptProv,
   NULL,
   NULL,
   PROV_RSA_FULL,
   0)) 
{    
    printf("CryptAcquireContext succeeded. \n");
}
else
{
    MyHandleError("Error during CryptAcquireContext!\n");
}
//-------------------------------------------------------------------
// Generate a key.
if (CryptGenKey(
     hCryptProv, 
     CALG_RC4, 
     0, 
     &amp;hOriginalKey))
{
   printf("Original session key is created. \n");
}
else
{
   MyHandleError("ERROR - CryptGenKey.");
}
//-------------------------------------------------------------------
// Duplicate the key.

if (CryptDuplicateKey(
     hOriginalKey, 
     NULL, 
     0, 
     &amp;hDuplicateKey))
{
   printf("The session key has been duplicated. \n");
}
else
{
   MyHandleError("ERROR - CryptDuplicateKey");
}
//-------------------------------------------------------------------
// Set additional parameters on the original key.
// First, set the cipher mode.

dwMode = CRYPT_MODE_ECB;
if(CryptSetKeyParam(
   hOriginalKey, 
   KP_MODE, 
   (BYTE*)&amp;dwMode, 
   0)) 
{
     printf("Key Parameters set. \n");
}
else
{
     MyHandleError("Error during CryptSetKeyParam.");
}
// Generate a random initialization vector.
if(CryptGenRandom(
   hCryptProv, 
   8, 
   pbData)) 
{
     printf("Random sequence generated. \n");
}
else
{
     MyHandleError("Error during CryptGenRandom.");
}
//-------------------------------------------------------------------
// Set the initialization vector.
if(CryptSetKeyParam(
   hOriginalKey, 
   KP_IV, 
   pbData, 
   0)) 
{
     printf("Parameter set with random sequence as "
         "initialization vector. \n");
}
else
{
     MyHandleError("Error during CryptSetKeyParam.");
}
//-------------------------------------------------------------------
// Clean up.

if (hOriginalKey)
    if (!CryptDestroyKey(hOriginalKey))
        MyHandleError("Failed CryptDestroyKey\n");

if (hDuplicateKey)
    if (!CryptDestroyKey(hDuplicateKey))
            MyHandleError("Failed CryptDestroyKey\n");

if(hCryptProv)
    if (!CryptReleaseContext(hCryptProv, 0))
        MyHandleError("Failed CryptReleaseContext\n");

printf("\nThe program ran to completion without error. \n");

} // End of main.

//-------------------------------------------------------------------
//  This example uses the function MyHandleError, a simple error
//  handling function, to print an error message and exit 
//  the program. 
//  For most applications, replace this function with one 
//  that does more extensive error reporting.

void MyHandleError(char *s)
{
    printf("An error occurred in running the program.\n");
    printf("%s\n",s);
    printf("Error number %x\n.",GetLastError());
    printf("Program terminating.\n");
    exit(1);
}
```



 

 



