---
title: Server Development Using Context Handles
description: From the perspective of server program development, a context handle is an untyped pointer. Server programs initialize context handles by pointing them at data in memory or on some other form of storage (such as files on disks).
ms.assetid: 6a1aabca-4cb9-401c-90c7-0cff7a69b7b6
ms.topic: article
ms.date: 05/31/2018
---

# Server Development Using Context Handles

From the perspective of server program development, a context handle is an untyped pointer. Server programs initialize context handles by pointing them at data in memory or on some other form of storage (such as files on disks).

For instance, suppose that a client uses a context handle to request a series of updates to a record in a database. The client calls a remote procedure on the server and passes it a search key. The server program searches the database for the search key and obtains the integer record number of the matching record. The server can then point a pointer to void at a memory location containing the record number. When it returns, the remote procedure would need to return the pointer as a context handle through its return value or its parameter list. The client would need to pass the pointer to the server each time it called remote procedures to update the record. During each of these update operations, the server would cast the void pointer to be a pointer to an integer.

After the server program points the context handle at context data, the handle is considered opened. Handles containing a **NULL** value are closed. The server maintains an opened context handle until the client calls a remote procedure that closes it. If the client session terminates while the handle is open, the RPC run time calls the server run-down routine to free the handle.

The following code fragment demonstrates how a server might implement a context handle. In this example, the server maintains a data file that the client writes to using remote procedures. The context information is a file handle that keeps track of the current location in the file where the server will write data. The file handle is packaged as a context handle in the parameter list to remote procedure calls. A structure contains the file name and the file handle. The interface definition for this example is shown in [Interface Development Using Context Handles](interface-development-using-context-handles.md).


```C++
/* cxhndlp.c (fragment of file containing remote procedures) */
typedef struct 
{
     FILE* hFile;
     char   achFile[256];
} FILE_CONTEXT_TYPE;
```



The function RemoteOpen opens a file on the server:


```C++
short RemoteOpen(
    PPCONTEXT_HANDLE_TYPE pphContext,
    unsigned char *pszFileName)
{
    FILE               *hFile;
    FILE_CONTEXT_TYPE  *pFileContext;
 
    if ((hFile = fopen(pszFileName, "r")) == NULL) 
    {
        *pphContext = (PCONTEXT_HANDLE_TYPE) NULL;
        return(-1);
    }
    else 
    {
        pFileContext = (FILE_CONTEXT_TYPE *) 
                       MIDL_user_allocate(sizeof(FILE_CONTEXT_TYPE));
        pFileContext->hFile = hFile;
        // check if pszFileName is longer than 256 and if yes, return
        // an error
        strcpy_s(pFileContext->achFile, srlen(pszFileName), pszFileName);
        *pphContext = (PCONTEXT_HANDLE_TYPE) pFileContext;
        return(0);
    }
}
```



The function RemoteRead reads a file on the server.


```C++
short RemoteRead(
    PCONTEXT_HANDLE_TYPE phContext, 
    unsigned char *pbBuf, 
    short *pcbBuf) 
{ 
    FILE_CONTEXT_TYPE *pFileContext; 
    printf("in RemoteRead\n"); 
    pFileContext = (FILE_CONTEXT_TYPE *) phContext; 
    *pcbBuf = (short) fread(pbBuf, sizeof(char), 
                            BUFSIZE, 
                            pFileContext->hFile); 
    return(*pcbBuf); 
}
```



The function RemoteClose closes a file on the server. Note that the server application has to assign **NULL** to the context handle as part of the close function. This communicates to the server stub and the RPC run-time library that the context handle has been deleted. Otherwise, the connection will be kept open and eventually a context run-down will occur.


```C++
void RemoteClose(PPCONTEXT_HANDLE_TYPE pphContext)
{
    FILE_CONTEXT_TYPE *pFileContext;
 
    if (*pphContext == NULL)
    {
        //Log error, client tried to close a NULL handle.
        return;
    }
    pFileContext = (FILE_CONTEXT_TYPE *)*pphContext;
    printf("File %s closed.\n", pFileContext->achFile);
    fclose(pFileConext->hFile);
    MIDL_user_free(pFileContext);
 
    // This tells the run-time, when it is marshalling the out 
    // parameters, that the context handle has been closed normally.
    *pphContext = NULL;
}
```



> [!Note]  
> While it is expected the client passes a valid context handle to a call with \[in, out\] directional attributes, RPC does not reject **NULL** context handles for this combination of directional attributes. The **NULL** context handle is passed to the server as a **NULL** pointer. The server code for calls containing an \[in, out\] context handle should be written to avoid an access violation when a **NULL** pointer is received.

 

 

 




