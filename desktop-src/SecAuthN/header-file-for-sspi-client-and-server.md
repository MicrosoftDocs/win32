---
description: The following header file should be included with both the client and the server SSPI samples as SspiExample.h. It declares functions that handle communication with the security package.
ms.assetid: 358c2cd6-674b-4d70-9657-800b0d1b2fe7
title: Header File for SSPI Client and Server
ms.topic: article
ms.date: 05/31/2018
---

# Header File for SSPI Client and Server

The following header file should be included with both the client and the server SSPI samples as SspiExample.h. It declares functions that handle communication with the security package.


```C++
//  SspiExample.h
#include <sspi.h>
#include <windows.h>

BOOL SendMsg (SOCKET s, PBYTE pBuf, DWORD cbBuf);
BOOL ReceiveMsg (SOCKET s, PBYTE pBuf, DWORD cbBuf, DWORD *pcbRead);
BOOL SendBytes (SOCKET s, PBYTE pBuf, DWORD cbBuf);
BOOL ReceiveBytes (SOCKET s, PBYTE pBuf, DWORD cbBuf, DWORD *pcbRead);
void cleanup();

BOOL GenClientContext (
    BYTE *pIn,
    DWORD cbIn,
    BYTE *pOut,
    DWORD *pcbOut,
    BOOL *pfDone,
    CHAR *pszTarget,
    CredHandle *hCred,
    struct _SecHandle *hcText
);

BOOL GenServerContext (
   BYTE *pIn,
   DWORD cbIn,
   BYTE *pOut,
   DWORD *pcbOut,
   BOOL *pfDone,
   BOOL  fNewCredential
);

BOOL EncryptThis (
         PBYTE pMessage, 
         ULONG cbMessage,
         BYTE ** ppOutput,
         LPDWORD pcbOutput,
         ULONG securityTrailer
    );

PBYTE DecryptThis(
         PBYTE achData, 
         LPDWORD pcbMessage,
         struct _SecHandle *hCtxt,
         ULONG   cbSecurityTrailer
);

BOOL 
SignThis (
         PBYTE pMessage, 
         ULONG cbMessage,
         BYTE ** ppOutput,
         LPDWORD pcbOutput
);

PBYTE VerifyThis(
          PBYTE pBuffer, 
          LPDWORD pcbMessage,
          struct _SecHandle *hCtxt,
          ULONG   cbMaxSignature
);

void PrintHexDump(DWORD length, PBYTE buffer);

BOOL ConnectAuthSocket (
   SOCKET *s, 
   CredHandle *hCred, 
   struct _SecHandle *hcText
);

BOOL CloseAuthSocket (SOCKET s);

BOOL DoAuthentication (SOCKET s);

void MyHandleError(char *s);

```



 

 



