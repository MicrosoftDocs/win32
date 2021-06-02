---
description: Shows using CryptEncodeObjectEx and CryptDecodeObjectEx.
ms.assetid: 78108cd5-531e-4d0c-96cf-6f6264b7716c
title: 'Example C Program: ASN.1 Encoding and Decoding'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: ASN.1 Encoding and Decoding

The following example shows using [**CryptEncodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobjectex) and [**CryptDecodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex). This example can easily be modified to use [**CryptEncodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobject) and [**CryptDecodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobject).

This example also uses a modified version of the function [**ByteToStr**](bytetostr.md) to print an [*Abstract Syntax Notation One*](../secgloss/a-gly.md) (ASN.1) encoded series of octets. It also uses [**MyHandleError**](myhandleerror.md). Code for these functions is included with the sample.


```C++
#include <stdio.h>
#include <windows.h>
#include "Wincrypt.h"
//-------------------------------------------------------------------
//  Copyright (C) Microsoft.  All rights reserved.
//  Only X509_ASN_ENCODING is needed with these
//  functions.
#pragma comment(lib, "crypt32.lib")

#define MY_TYPE   X509_ASN_ENCODING

//--------------------------------------------------------------------
//  Declare function ByteToString.

void ByteToStr(
     DWORD cb, 
     void* pv, 
     LPSTR sz);
//-------------------------------------------------------------------
//   Declare function MyHandleError.
void MyHandleError(char *s); 

//-------------------------------------------------------------------
//   Begin main.

void main(void)
{

//-------------------------------------------------------------------
//   Declare and initialize local variables.

char *Cert_Sub_Name ="Test User Name";

//-------------------------------------------------------------------
// Initialize a single RDN structure.

CERT_RDN_ATTR rgNameAttr = 
{
   szOID_COMMON_NAME,                // the OID
   CERT_RDN_PRINTABLE_STRING,        // type of string
   (DWORD)strlen(Cert_Sub_Name)+1,   // string length including
                                     // the terminating null 
                                     // character
   (BYTE *)Cert_Sub_Name             // pointer to the string
};
//-------------------------------------------------------------------
// Declare and initialize a structure to include
// the array of RDN structures.

CERT_RDN rgRDN[] = 
{
   1,               // the number of elements in the array
   &rgNameAttr      // pointer to the array
};

//-------------------------------------------------------------------
//  Declare and initialize a CERT_NAME_INFO 
//  structure that includes a CERT_RND.

CERT_NAME_INFO CertName = 
{
    1,          // number of elements in the CERT_RND's array
    rgRDN
};

//-------------------------------------------------------------------
//  Declare additional variables.

CERT_NAME_INFO *pDecodeName;  // point variable to hold
                              // the address of the decoded
                              // buffer
DWORD cbEncoded;              // variable to hold the
                              // length of the encoded string
DWORD cbDecoded;              // variable to hold the 
                              // length of the decoded buffer

BYTE *pbEncoded;              // variable to hold a pointer to the 
                              // encoded buffer
BYTE *pbDecoded;              // variable to hold a pointer to the
                              // decoded buffer
LPSTR sz;

//-------------------------------------------------------------------
//    Allocate memory for a large buffer.

if(sz=(char *)malloc(512))
{
     printf("Memory for sz allocated\n");
}
else
{
    MyHandleError("Memory allocation failed.");
}

//-------------------------------------------------------------------
// Call CrypteEncodeObjectEx to get 
// length to allocate for pbEncoded.

if( CryptEncodeObjectEx(
     MY_TYPE,        // the encoding/decoding type
     X509_NAME,    
     &CertName,
     0,                 
     NULL, 
     NULL,
     &cbEncoded))    // fill in the length needed for
                     // the encoded buffer
{
     printf("The number of bytes needed is %d \n",cbEncoded);
}
else
{
     MyHandleError("The first call to the function failed.\n");
}

if( pbEncoded = (BYTE*)malloc(cbEncoded))
{
     printf("Memory for pvEncoded has been allocated.\n");
}
else
{
    MyHandleError("Memory allocation failed.");
}

if(CryptEncodeObjectEx(
     MY_TYPE,
     X509_NAME,
     &CertName,
     0,
     NULL, 
     pbEncoded,
     &cbEncoded))
{
     ByteToStr(cbEncoded, pbEncoded,sz);
     printf("The Encoded octets are \n%s\n",sz);
}
else
{
     MyHandleError("Encoding failed.");
}

//-------------------------------------------------------------------
// Decode the encoded buffer.

//-------------------------------------------------------------------
//  Get the length needed for the decoded buffer.

if(CryptDecodeObjectEx(
     MY_TYPE,
     X509_NAME,
     pbEncoded,     // the buffer to be decoded
     cbEncoded,
     CRYPT_DECODE_NOCOPY_FLAG,
     NULL, 
     NULL,
     &cbDecoded))
{
     printf("The needed buffer length is %d\n",cbDecoded);
}
else
{
    MyHandleError("The first decode pass failed.");
}

//-------------------------------------------------------------------
// Allocate memory for the decoded information.

if(!(pbDecoded = (BYTE*)malloc(cbDecoded)))
{
     MyHandleError("Decode buffer memory allocation failed.");
}

//-------------------------------------------------------------------
// Decode the encoded buffer.

if(CryptDecodeObjectEx(
     MY_TYPE,
     X509_NAME,
     pbEncoded,     // the buffer to be decoded
     cbEncoded,
     CRYPT_DECODE_NOCOPY_FLAG,   
     NULL, 
     pbDecoded,
     &cbDecoded))
{
    pDecodeName = ( CERT_NAME_INFO     *)pbDecoded;
    printf("The cRDN is -> %d \n",pDecodeName->cRDN);
    printf("The OID is -> ");
    printf("%s\n",pDecodeName->rgRDN->rgRDNAttr->pszObjId);
    printf("The string is ->");
    printf(" %s\n",pDecodeName->rgRDN->rgRDNAttr->Value.pbData);}
else
{
     MyHandleError("Decode failed.");
}

// Clean up memory.

if(sz)
   free(sz);
if(pbEncoded)
   free(pbEncoded);
if(pbDecoded)
   free(pbDecoded);

printf("Processing completed without error.\n");
}  // end of main()

//-------------------------------------------------------------------
//  Define ByteToStr.

void ByteToStr(
     DWORD cb, 
     void* pv, 
     LPSTR sz)

//-------------------------------------------------------------------
// Parameters passed are:
//    pv -- the Array of BYTES to be converted.
//    cb -- the number of BYTEs in the array.
//    sz -- a pointer to the string to be returned.

{

//-------------------------------------------------------------------
//  Declare and initialize local variables.

BYTE* pb = (BYTE*) pv; // local pointer to a BYTE in the BYTE array
DWORD i;               // local loop counter
int b;                 // local variable

//  Ensure that sz is large enough to hold pv.
if(strlen(sz) < cb)
{
    MyHandleError("The array of bytes is too long for the "
        "allocated string.");
}

//-------------------------------------------------------------------
//  Begin processing loop.

for (i=0; i<cb; i++)
{
   b = (*pb & 0xF0) >> 4;
   *sz++ = (b <= 9) ? b + '0' : (b - 10) + 'A';
   b = *pb & 0x0F;
   *sz++ = (b <= 9) ? b + '0' : (b - 10) + 'A';
   pb++;
   *sz++=' ';
}
*sz++ = 0;
}  // end of ByteToStr
 
void MyHandleError(char *s) 
{ 
printf("An error occurred in running the program.\n"); 
    printf("%s\n",s); 
printf("Program terminating.\n"); 
exit(1); 
} // end of MyHandleError
```



 

 
