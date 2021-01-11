---
description: Encodes and decodes simple, general data, and illustrates the following tasks and CryptoAPI functions.
ms.assetid: 7634bd05-fca0-4538-94da-7af6e3d8e6b8
title: 'Example C Program: Encoding and Decoding Data'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Encoding and Decoding Data

The following example encodes and decodes simple, general data, and illustrates the following tasks and CryptoAPI functions.

-   Determining the length needed for the buffer to hold the encoded data using [**CryptMsgCalculateEncodedLength**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcalculateencodedlength).
-   Opening a message for encoding using [**CryptMsgOpenToEncode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentoencode).
-   Adding content to the encoded message using [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate).
-   Copying the encoded message into a buffer using [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam).
-   Closing the encoded message using [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose).
-   Opening a message to decode using [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode).
-   Using [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) and [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam) to get the decoded data.

This example uses the function [**MyHandleError**](myhandleerror.md). The code for this function is included with the sample. Code for this and other auxiliary functions is also listed under [General Purpose Functions](general-purpose-functions.md).


```C++
//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// Example of encoding and decoding a message.
#pragma comment(lib, "crypt32.lib")

#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)
void MyHandleError(char *s);

void main(void)
{
//-------------------------------------------------------------------
// Declare and initialize variables. This includes getting a pointer 
// to the message content. This sample program creates the message 
// content and gets a pointer to it. In most situations, 
// the content will exist somewhere and a pointer to it
// will get passed to the application. 

HCRYPTMSG hMsg;
BYTE* pbContent;     // a byte pointer to the message
DWORD cbContent;     // the size of message
DWORD cbEncodedBlob;
BYTE *pbEncodedBlob;


//-------------------------------------------------------------------
//  The following variables are used only in the decoding phase.

DWORD cbDecoded;
BYTE *pbDecoded;

//-------------------------------------------------------------------
//  Begin processing. Display the original message.

pbContent = (BYTE*) "Security is our only business";
cbContent = strlen((char *) pbContent)+1;

printf("The original message => %s\n",pbContent);  

//-------------------------------------------------------------------
// Get the size of the encoded message BLOB.

if(cbEncodedBlob = CryptMsgCalculateEncodedLength(
             MY_ENCODING_TYPE,       // message encoding type
             0,                      // flags
             CMSG_DATA,              // message type
             NULL,                   // pointer to structure
             NULL,                   // inner content object ID
             cbContent))             // size of content
{
    printf("The length of the data has been calculated. \n");
}
else
{
    MyHandleError("Getting cbEncodedBlob length failed");
}
//-------------------------------------------------------------------
// Allocate memory for the encoded BLOB.

if(pbEncodedBlob = (BYTE *) malloc(cbEncodedBlob))
{
   printf("Memory has been allocated for the signed message. \n");
}
else
{
   MyHandleError("Memory allocation failed");
}
//-------------------------------------------------------------------
// Open a message to encode.

if(hMsg = CryptMsgOpenToEncode(
          MY_ENCODING_TYPE,        // encoding type
          0,                       // flags
          CMSG_DATA,               // message type
          NULL,                    // pointer to structure
          NULL,                    // inner content object ID
          NULL))                   // stream information (not used)
{
    printf("The message to be encoded has been opened. \n");
}
else
{
     MyHandleError("OpenToEncode failed");
}
//-------------------------------------------------------------------
// Update the message with the data.

if(CryptMsgUpdate(
        hMsg,         // handle to the message
        pbContent,    // pointer to the content
        cbContent,    // size of the content
        TRUE))        // last call
{
     printf("Content has been added to the encoded message. \n");
}
else
{
      MyHandleError("MsgUpdate failed");
}
//-------------------------------------------------------------------
// Get the resulting message.

if(CryptMsgGetParam(
               hMsg,                      // handle to the message
               CMSG_BARE_CONTENT_PARAM,   // parameter type
               0,                         // index
               pbEncodedBlob,             // pointer to the BLOB
               &cbEncodedBlob))           // size of the BLOB
{
    printf("Message encoded successfully. \n");
}
else
{
      MyHandleError("MsgGetParam failed");
}
//-------------------------------------------------------------------
// pbEncodedBlob now points to the encoded, signed content.

//-------------------------------------------------------------------
// Close the message.

if(hMsg)
    CryptMsgClose(hMsg);

//-------------------------------------------------------------------
// The following code decodes a message. 
// This code may be included here or could be used
// in a stand-alone program if the message 
// to be decoded and its size were input. 
// The encoded message BLOB and its length could be read 
// from a disk file or could be extracted from an email message 
// or other input source.

//-------------------------------------------------------------------
// Open a message for decoding.

if(hMsg = CryptMsgOpenToDecode(
               MY_ENCODING_TYPE,      // encoding type.
               0,                     // flags.
               CMSG_DATA,             // look for a data message.
               NULL,                  // cryptographic provider.
               NULL,                  // recipient information.
               NULL))                 // stream information.
{
     printf("The message to decode is open. \n");
}
else
{
    MyHandleError("OpenToDecode failed");
}
//-------------------------------------------------------------------
// Update the message with an encoded BLOB.
// Both pbEncodedBlob, the encoded data, 
// and cbEncodedBlob, the length of the encoded data,
// must be available. 

printf("\nThe length of the encoded message is %d.\n\n",
    cbEncodedBlob);

if(CryptMsgUpdate(
    hMsg,                 // handle to the message
    pbEncodedBlob,        // pointer to the encoded BLOB
    cbEncodedBlob,        // size of the encoded BLOB
    TRUE))                // last call
{
      printf("The encoded BLOB has been added to the message. \n");
}
else
{
    MyHandleError("Decode MsgUpdate failed");
}
//-------------------------------------------------------------------
// Get the size of the content.

if(CryptMsgGetParam(
                  hMsg,                  // handle to the message
                  CMSG_CONTENT_PARAM,    // parameter type
                  0,                     // index
                  NULL,                  // address for returned 
                                         // information
                  &cbDecoded))           // size of the returned
                                         // information
{
    printf("The decoded message size is %d. \n", cbDecoded);
}
else
{
    MyHandleError("Decode CMSG_CONTENT_PARAM failed");
}
//-------------------------------------------------------------------
// Allocate memory.

if(pbDecoded = (BYTE *) malloc(cbDecoded))
{
     printf("Memory has been allocated for the decoded message.\n");
}
else
{
    MyHandleError("Decoding memory allocation failed.");
}
//-------------------------------------------------------------------
// Get a pointer to the content.

if(CryptMsgGetParam(
                  hMsg,                  // handle to the message
                  CMSG_CONTENT_PARAM,    // parameter type
                  0,                     // index
                  pbDecoded,             // address for returned 
                                         // information
                  &cbDecoded))           // size of the returned 
                                         // information
{
     printf("The message is %s.\n",(LPSTR)pbDecoded);
}
else
{
     MyHandleError("Decode CMSG_CONTENT_PARAM #2 failed");
}
//-------------------------------------------------------------------
// Clean up.

if(pbEncodedBlob)
   free(pbEncodedBlob);
if(pbDecoded)
   free(pbDecoded);
if(hMsg)
    CryptMsgClose(hMsg);

printf("This program ran to completion without error. \n");

} //  End of main

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



 

 



