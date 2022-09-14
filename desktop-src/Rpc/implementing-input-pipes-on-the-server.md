---
title: Implementing Input Pipes on the Server
description: To begin sending data to a server, a client calls one of the server's remote procedures.
ms.assetid: 6abaa851-41bf-4a03-8d12-cd595d74c8c9
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Input Pipes on the Server

To begin sending data to a server, a client calls one of the server's remote procedures. This procedure must repeatedly call the pull procedure in the server's stub. The MIDL compiler uses the application's IDL file to automatically generate the server's pull procedure.

Each time the server program invokes the pull procedure in its stub, the pull procedure receives blocks of data from the client. It unmarshals the data into the server's buffer. The server's remote procedure can then process this data in any way required. The loop continues until the server receives a buffer of zero length.

The following example is from the Pipedemo program contained in the samples that come with the Platform Software Development Kit (SDK). It illustrates a remote server procedure that uses a pipe to pull data from the client to the server.

``` syntax
//file: server.c (fragment)
#include uc_server.c
#define PIPE_TRANSFER_SIZE 100 /* Transfer 100 pipe elements at one time */
 
void InPipe(LONG_PIPE     long_pipe )
{
    long local_pipe_buf[PIPE_TRANSFER_SIZE];
    ulong actual_transfer_count = PIPE_TRANSFER_SIZE;
 
    while(actual_transfer_count > 0) /* Loop to get all 
                                        the pipe data elements */
    {
        long_pipe.pull( long_pipe.state,
                        local_pipe_buf,
                        PIPE_TRANSFER_SIZE,
                        &actual_transfer_count);
        /* process the elements */
    } // end while
} //end InPipe
```

 

 




