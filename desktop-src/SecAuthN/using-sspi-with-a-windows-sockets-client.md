---
description: This sample program works with the server program Using SSPI with a Windows Sockets Server.
ms.assetid: 7ec15770-d3bd-4488-abe8-058115fec071
title: Using SSPI with a Windows Sockets Client
ms.topic: article
ms.date: 05/31/2018
---

# Using SSPI with a Windows Sockets Client

This sample program works with the server program [Using SSPI with a Windows Sockets Server](using-sspi-with-a-windows-sockets-server.md). The client and server sample programs are designed to work together. Both programs use the header file SspiExample.h, which can be found in [Header File for SSPI Client and Server Samples](header-file-for-sspi-client-and-server.md). This program includes calls to functions in Secur32.lib and Ws2\_32.lib, which must be included among the link libraries.

This program demonstrates the following:

-   Establishing a Windows Sockets connection with a server.
-   Initializing an authenticated SSPI session with the Negotiate SSP.
-   Connecting with a server and establishing a secure communication session.
-   Receiving and decrypt a message from the server within the secure session.

This sample program uses limited error handling.


```C++
//--------------------------------------------------------------------
//  Client-side program to establish an SSPI socket connection
//  with a server and exchange messages.

//--------------------------------------------------------------------
//  Define macros and constants.

#define SECURITY_WIN32
#define BIG_BUFF   2048
#define SEC_SUCCESS(Status) ((Status) >= 0)
#define g_usPort 2000

#define cbMaxMessage 12000
#define MessageAttribute ISC_REQ_CONFIDENTIALITY 

#include <windows.h>
#include <winsock.h>
#include <stdio.h>
#include <stdlib.h>
#include "SspiExample.h"

CredHandle hCred;
struct _SecHandle  hcText;

//  The following #define statement must be changed. ServerName must
//  be defined as the name of the computer running the server sample.
//  TargetName must be defined as the logon name of the user running 
//  the server program.
#define ServerName  "Server_Computer_Name"
#define TargetName  "Server_User_Logon_Name"

void main()
{

    SOCKET            Client_Socket;
    BYTE              Data[BIG_BUFF];
    PCHAR             pMessage;
    WSADATA           wsaData;
    CredHandle        hCred;
    struct _SecHandle hCtxt;
    SECURITY_STATUS   ss;
    DWORD             cbRead;
    ULONG             cbMaxSignature;
    ULONG             cbSecurityTrailer;
    SecPkgContext_Sizes            SecPkgContextSizes;
    SecPkgContext_NegotiationInfo  SecPkgNegInfo;
    BOOL DoAuthentication (SOCKET s);

    //-------------------------------------------------------------------
    //  Initialize the socket and the SSP security package.

    if(WSAStartup (0x0101, &wsaData))
    {
        MyHandleError("Could not initialize winsock ");
    }

    //--------------------------------------------------------------------
    //  Connect to a server.

    if (!ConnectAuthSocket (
        &Client_Socket,
        &hCred,
        &hCtxt))
    {
        MyHandleError("Authenticated server connection ");
    }

    //--------------------------------------------------------------------
    //   An authenticated session with a server has been established.
    //   Receive and manage a message from the server.
    //   First, find and display the name of the negotiated
    //   SSP and the size of the signature and the encryption 
    //   trailer blocks for this SSP.

    ss = QueryContextAttributes(
        &hCtxt,
        SECPKG_ATTR_NEGOTIATION_INFO,
        &SecPkgNegInfo );

    if (!SEC_SUCCESS(ss))  
    {
        MyHandleError("QueryContextAttributes failed ");
    }
    else
    {
        printf("Package Name: %s\n", SecPkgNegInfo.PackageInfo->Name);
    }

    ss = QueryContextAttributes(
        &hCtxt,
        SECPKG_ATTR_SIZES,
        &SecPkgContextSizes );

    if (!SEC_SUCCESS(ss))  
    {
        MyHandleError("Query context ");
    }

    cbMaxSignature = SecPkgContextSizes.cbMaxSignature;
    cbSecurityTrailer = SecPkgContextSizes.cbSecurityTrailer;

    printf("InitializeSecurityContext result = 0x%08x\n", ss);

    //--------------------------------------------------------------------
    //   Decrypt and display the message from the server.

    if (!ReceiveBytes(
        Client_Socket, 
        Data, 
        BIG_BUFF, 
        &cbRead))
    {
        MyHandleError("No response from server ");
    }

    if (0 == cbRead)
    {
        MyHandleError("Zero bytes received ");
    }

    pMessage = (PCHAR) DecryptThis(
        Data, 
        &cbRead,
        &hCtxt,
        cbSecurityTrailer);

    printf ("The message from the server is \n ->  %.*s \n",
        cbRead, pMessage);

    //--------------------------------------------------------------------
    //  Terminate socket and security package.

    DeleteSecurityContext (&hCtxt);
    FreeCredentialHandle (&hCred); 
    shutdown (Client_Socket, 2);
    closesocket (Client_Socket);
    if (SOCKET_ERROR == WSACleanup ())
    {
        MyHandleError("Problem with socket cleanup ");
    }

    exit (EXIT_SUCCESS);
}  // end main

//--------------------------------------------------------------------
//  ConnectAuthSocket establishes an authenticated socket connection 
//  with a server and initializes needed security package resources.

BOOL ConnectAuthSocket (
    SOCKET            *s,
    CredHandle        *hCred, 
struct _SecHandle *hcText)
{
    unsigned long  ulAddress;
    struct hostent *pHost;
    SOCKADDR_IN    sin;

    //--------------------------------------------------------------------
    //  Lookup the server's address.

    ulAddress = inet_addr (ServerName);

    if (INADDR_NONE == ulAddress) 
    {
        pHost = gethostbyname (ServerName);
        if (NULL == pHost) 
        {
            MyHandleError("Unable to resolve host name ");
        }
        memcpy((char FAR *)&ulAddress, pHost->h_addr, pHost->h_length);
    }

    //--------------------------------------------------------------------
    //  Create the socket.

    *s = socket (
        PF_INET, 
        SOCK_STREAM, 
        0);

    if (INVALID_SOCKET ==  *s) 
    {
        MyHandleError("Unable to create socket");
    }
    else
    {
        printf("Socket created.\n");
    }

    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = ulAddress;
    sin.sin_port = htons (g_usPort);

    //--------------------------------------------------------------------
    //  Connect to the server.

    if (connect (*s, (LPSOCKADDR) &sin, sizeof (sin))) 
    {
        closesocket (*s);
        MyHandleError( "Connect failed ");
    }

    //--------------------------------------------------------------------
    //  Authenticate the connection. 

    if (!DoAuthentication (*s)) 
    {
        closesocket (*s);
        MyHandleError("Authentication ");
    }

    return(TRUE);
}  // end ConnectAuthSocket 

BOOL DoAuthentication (SOCKET s)

{
    BOOL        fDone = FALSE;
    DWORD       cbOut = 0;
    DWORD       cbIn = 0;
    PBYTE       pInBuf;
    PBYTE       pOutBuf;


    if(!(pInBuf = (PBYTE) malloc(cbMaxMessage)))
    {
        MyHandleError("Memory allocation ");
    }

    if(!(pOutBuf = (PBYTE) malloc(cbMaxMessage)))
    {
        MyHandleError("Memory allocation ");
    }

    cbOut = cbMaxMessage;
    if (!GenClientContext (
        NULL, 
        0, 
        pOutBuf,  
        &cbOut, 
        &fDone, 
        TargetName,
        &hCred,
        &hcText
        ))
    {
        return(FALSE);
    }

    if (!SendMsg (s, pOutBuf, cbOut )) 
    {
        MyHandleError("Send message failed ");
    }

    while (!fDone) 
    {
        if (!ReceiveMsg (
            s, 
            pInBuf,  
            cbMaxMessage, 
            &cbIn))
        {
            MyHandleError("Receive message failed ");
        }

        cbOut = cbMaxMessage;

        if (!GenClientContext (
            pInBuf,  
            cbIn, 
            pOutBuf, 
            &cbOut, 
            &fDone, 
            TargetName,
            &hCred,
            &hcText))
        {
            MyHandleError("GenClientContext failed");
        }
        if (!SendMsg (
            s, 
            pOutBuf, 
            cbOut))
        {
            MyHandleError("Send message 2  failed ");
        }
    }

    free(pInBuf); 
    free(pOutBuf);
    return(TRUE);
}

BOOL GenClientContext (
    BYTE       *pIn,
    DWORD       cbIn,
    BYTE       *pOut,
    DWORD      *pcbOut,
    BOOL       *pfDone,
    CHAR       *pszTarget,
    CredHandle *hCred,
struct _SecHandle *hcText)
{
    SECURITY_STATUS   ss;
    TimeStamp         Lifetime;
    SecBufferDesc     OutBuffDesc;
    SecBuffer         OutSecBuff;
    SecBufferDesc     InBuffDesc;
    SecBuffer         InSecBuff;
    ULONG             ContextAttributes;
    static TCHAR      lpPackageName[1024];

    if( NULL == pIn )  
    {   
        strcpy_s(lpPackageName, 1024 * sizeof(TCHAR), "Negotiate");
        ss = AcquireCredentialsHandle (
            NULL, 
            lpPackageName,
            SECPKG_CRED_OUTBOUND,
            NULL, 
            NULL, 
            NULL, 
            NULL, 
            hCred,
            &Lifetime);

        if (!(SEC_SUCCESS (ss)))
        {
            MyHandleError("AcquireCreds failed ");
        }
    }

    //--------------------------------------------------------------------
    //  Prepare the buffers.

    OutBuffDesc.ulVersion = 0;
    OutBuffDesc.cBuffers  = 1;
    OutBuffDesc.pBuffers  = &OutSecBuff;

    OutSecBuff.cbBuffer   = *pcbOut;
    OutSecBuff.BufferType = SECBUFFER_TOKEN;
    OutSecBuff.pvBuffer   = pOut;

    //-------------------------------------------------------------------
    //  The input buffer is created only if a message has been received 
    //  from the server.

    if (pIn)   
    {
        InBuffDesc.ulVersion = 0;
        InBuffDesc.cBuffers  = 1;
        InBuffDesc.pBuffers  = &InSecBuff;

        InSecBuff.cbBuffer   = cbIn;
        InSecBuff.BufferType = SECBUFFER_TOKEN;
        InSecBuff.pvBuffer   = pIn;

        ss = InitializeSecurityContext (
            hCred,
            hcText,
            pszTarget,
            MessageAttribute, 
            0,
            SECURITY_NATIVE_DREP,
            &InBuffDesc,
            0, 
            hcText,
            &OutBuffDesc,
            &ContextAttributes,
            &Lifetime);
    }
    else
    {
        ss = InitializeSecurityContext (
            hCred,
            NULL,
            pszTarget,
            MessageAttribute, 
            0, 
            SECURITY_NATIVE_DREP,
            NULL,
            0, 
            hcText,
            &OutBuffDesc,
            &ContextAttributes,
            &Lifetime);
    }

    if (!SEC_SUCCESS (ss))  
    {
        MyHandleError ("InitializeSecurityContext failed " );
    }

    //-------------------------------------------------------------------
    //  If necessary, complete the token.

    if ((SEC_I_COMPLETE_NEEDED == ss) 
        || (SEC_I_COMPLETE_AND_CONTINUE == ss))  
    {
        ss = CompleteAuthToken (hcText, &OutBuffDesc);
        if (!SEC_SUCCESS(ss))  
        {
            fprintf (stderr, "complete failed: 0x%08x\n", ss);
            return FALSE;
        }
    }

    *pcbOut = OutSecBuff.cbBuffer;

    *pfDone = !((SEC_I_CONTINUE_NEEDED == ss) ||
        (SEC_I_COMPLETE_AND_CONTINUE == ss));

    printf ("Token buffer generated (%lu bytes):\n", OutSecBuff.cbBuffer);
    PrintHexDump (OutSecBuff.cbBuffer, (PBYTE)OutSecBuff.pvBuffer);
    return TRUE;

}

PBYTE DecryptThis(
    PBYTE              pBuffer, 
    LPDWORD            pcbMessage,
struct _SecHandle *hCtxt,
    ULONG              cbSecurityTrailer)
{
    SECURITY_STATUS   ss;
    SecBufferDesc     BuffDesc;
    SecBuffer         SecBuff[2];
    ULONG             ulQop = 0;
    PBYTE             pSigBuffer;
    PBYTE             pDataBuffer;
    DWORD             SigBufferSize;

    //-------------------------------------------------------------------
    //  By agreement, the server encrypted the message and set the size
    //  of the trailer block to be just what it needed. DecryptMessage 
    //  needs the size of the trailer block. 
    //  The size of the trailer is in the first DWORD of the
    //  message received. 

    SigBufferSize = *((DWORD *) pBuffer);
    printf ("data before decryption including trailer (%lu bytes):\n",
        *pcbMessage);
    PrintHexDump (*pcbMessage, (PBYTE) pBuffer);

    //--------------------------------------------------------------------
    //  By agreement, the server placed the trailer at the beginning 
    //  of the message that was sent immediately following the trailer 
    //  size DWORD.

    pSigBuffer = pBuffer + sizeof(DWORD);

    //--------------------------------------------------------------------
    //  The data comes after the trailer.

    pDataBuffer = pSigBuffer + SigBufferSize;

    //--------------------------------------------------------------------
    //  *pcbMessage is reset to the size of just the encrypted bytes.

    *pcbMessage = *pcbMessage - SigBufferSize - sizeof(DWORD);

    //--------------------------------------------------------------------
    //  Prepare the buffers to be passed to the DecryptMessage function.

    BuffDesc.ulVersion    = 0;
    BuffDesc.cBuffers     = 2;
    BuffDesc.pBuffers     = SecBuff;

    SecBuff[0].cbBuffer   = SigBufferSize;
    SecBuff[0].BufferType = SECBUFFER_TOKEN;
    SecBuff[0].pvBuffer   = pSigBuffer;

    SecBuff[1].cbBuffer   = *pcbMessage;
    SecBuff[1].BufferType = SECBUFFER_DATA;
    SecBuff[1].pvBuffer   = pDataBuffer;

    ss = DecryptMessage(
        hCtxt,
        &BuffDesc,
        0,
        &ulQop);

    if (!SEC_SUCCESS(ss)) 
    {
        fprintf(stderr, "DecryptMessage failed");
    }

    //-------------------------------------------------------------------
    //  Return a pointer to the decrypted data. The trailer data
    //  is discarded.

    return pDataBuffer;

}

PBYTE VerifyThis(
    PBYTE   pBuffer, 
    LPDWORD pcbMessage,
struct _SecHandle *hCtxt,
    ULONG   cbMaxSignature)
{

    SECURITY_STATUS   ss;
    SecBufferDesc     BuffDesc;
    SecBuffer         SecBuff[2];
    ULONG             ulQop = 0;
    PBYTE             pSigBuffer;
    PBYTE             pDataBuffer;

    //-------------------------------------------------------------------
    //  The global cbMaxSignature is the size of the signature
    //  in the message received.

    printf ("data before verifying (including signature):\n");
    PrintHexDump (*pcbMessage, pBuffer);

    //--------------------------------------------------------------------
    //  By agreement with the server, 
    //  the signature is at the beginning of the message received,
    //  and the data that was signed comes after the signature.

    pSigBuffer = pBuffer;
    pDataBuffer = pBuffer + cbMaxSignature;

    //-------------------------------------------------------------------
    //  The size of the message is reset to the size of the data only.

    *pcbMessage = *pcbMessage - (cbMaxSignature);

    //--------------------------------------------------------------------
    //  Prepare the buffers to be passed to the signature verification 
    //  function.

    BuffDesc.ulVersion    = 0;
    BuffDesc.cBuffers     = 2;
    BuffDesc.pBuffers     = SecBuff;

    SecBuff[0].cbBuffer   = cbMaxSignature;
    SecBuff[0].BufferType = SECBUFFER_TOKEN;
    SecBuff[0].pvBuffer   = pSigBuffer;

    SecBuff[1].cbBuffer   = *pcbMessage;
    SecBuff[1].BufferType = SECBUFFER_DATA;
    SecBuff[1].pvBuffer   = pDataBuffer;

    ss = VerifySignature(
        hCtxt,
        &BuffDesc,
        0,
        &ulQop
        );

    if (!SEC_SUCCESS(ss)) 
    {
        fprintf(stderr, "VerifyMessage failed");
    }
    else
    {
        printf("Message was properly signed.\n");
    }

    return pDataBuffer;

}  // end VerifyThis


void PrintHexDump(
    DWORD length, 
    PBYTE buffer)
{
    DWORD i,count,index;
    CHAR rgbDigits[]="0123456789abcdef";
    CHAR rgbLine[100];
    char cbLine;

    for(index = 0; length;
        length -= count, buffer += count, index += count) 
    {
        count = (length > 16) ? 16:length;

        sprintf_s(rgbLine, 100, "%4.4x  ",index);
        cbLine = 6;

        for(i=0;i<count;i++) 
        {
            rgbLine[cbLine++] = rgbDigits[buffer[i] >> 4];
            rgbLine[cbLine++] = rgbDigits[buffer[i] & 0x0f];
            if(i == 7) 
            {
                rgbLine[cbLine++] = ':';
            } 
            else 
            {
                rgbLine[cbLine++] = ' ';
            }
        }
        for(; i < 16; i++) 
        {
            rgbLine[cbLine++] = ' ';
            rgbLine[cbLine++] = ' ';
            rgbLine[cbLine++] = ' ';
        }

        rgbLine[cbLine++] = ' ';

        for(i = 0; i < count; i++) 
        {
            if(buffer[i] < 32 || buffer[i] > 126) 
            {
                rgbLine[cbLine++] = '.';
            } 
            else 
            {
                rgbLine[cbLine++] = buffer[i];
            }
        }

        rgbLine[cbLine++] = 0;
        printf("%s\n", rgbLine);
    }
}

BOOL SendMsg (
    SOCKET  s, 
    PBYTE   pBuf, 
    DWORD   cbBuf)
{
    if (0 == cbBuf)
        return(TRUE);

    //----------------------------------------------------------
    //  Send the size of the message.

    if (!SendBytes (s, (PBYTE)&cbBuf, sizeof (cbBuf)))
        return(FALSE);

    //----------------------------------------------------------
    //  Send the body of the message.

    if (!SendBytes (
        s, 
        pBuf, 
        cbBuf))
    {
        return(FALSE);
    }

    return(TRUE);
}    

BOOL ReceiveMsg (
    SOCKET  s, 
    PBYTE   pBuf, 
    DWORD   cbBuf, 
    DWORD  *pcbRead)

{
    DWORD cbRead;
    DWORD cbData;

    //----------------------------------------------------------
    //  Receive the number of bytes in the message.

    if (!ReceiveBytes (
        s, 
        (PBYTE)&cbData, 
        sizeof (cbData), 
        &cbRead))
    {
        return(FALSE);
    }

    if (sizeof (cbData) != cbRead)
        return(FALSE);
    //----------------------------------------------------------
    //  Read the full message.

    if (!ReceiveBytes (
        s, 
        pBuf, 
        cbData, 
        &cbRead))
    {
        return(FALSE);
    }

    if (cbRead != cbData)
        return(FALSE);

    *pcbRead = cbRead;
    return(TRUE);
}  // end ReceiveMessage    

BOOL SendBytes (
    SOCKET  s, 
    PBYTE   pBuf, 
    DWORD   cbBuf)
{
    PBYTE pTemp = pBuf;
    int   cbSent;
    int   cbRemaining = cbBuf;

    if (0 == cbBuf)
        return(TRUE);

    while (cbRemaining) 
    {
        cbSent = send (
            s, 
            (const char *)pTemp, 
            cbRemaining, 
            0);
        if (SOCKET_ERROR == cbSent) 
        {
            fprintf (stderr, "send failed: %u\n", GetLastError ());
            return FALSE;
        }

        pTemp += cbSent;
        cbRemaining -= cbSent;
    }

    return TRUE;
}

BOOL ReceiveBytes (
    SOCKET  s, 
    PBYTE   pBuf, 
    DWORD   cbBuf, 
    DWORD  *pcbRead)
{
    PBYTE pTemp = pBuf;
    int cbRead, cbRemaining = cbBuf;

    while (cbRemaining) 
    {
        cbRead = recv (
            s, 
            (char *)pTemp, 
            cbRemaining, 
            0);
        if (0 == cbRead)
            break;
        if (SOCKET_ERROR == cbRead) 
        {
            fprintf (stderr, "recv failed: %u\n", GetLastError ());
            return FALSE;
        }

        cbRemaining -= cbRead;
        pTemp += cbRead;
    }

    *pcbRead = cbBuf - cbRemaining;

    return TRUE;
}  // end ReceiveBytes


void MyHandleError(char *s)
{

    fprintf(stderr,"%s error. Exiting.\n",s);
    exit (EXIT_FAILURE);
}
```



 

 



