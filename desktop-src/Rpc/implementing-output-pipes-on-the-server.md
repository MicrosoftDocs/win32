---
title: Implementing Output Pipes on the Server
description: To begin receiving data from a server, a client calls one of the server's remote procedures.
ms.assetid: 5d791f4f-1d95-4bc0-b68f-db4fccc75ff8
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Output Pipes on the Server

To begin receiving data from a server, a client calls one of the server's remote procedures. This procedure must repeatedly call the push procedure in the server's stub. The MIDL compiler uses the application's IDL file to automatically generate the server's push procedure.

The remote server routine must fill the output pipe's buffer with data before it calls the push procedure. Each time the server program invokes the push procedure in its stub, the push procedure marshals the data and transmits it to the client. The loop continues until the server sends a buffer of zero length.

The following example is from the Pipedemo program contained in the samples that come with the Windows SDK. It illustrates a remote server procedure that uses a pipe to push data from the server to the client.


```C++
void OutPipe(LONG_PIPE *outputPipe )
{
    long *outputPipeData;
    ulong index = 0;
    ulong elementsToSend = PIPE_TRANSFER_SIZE;
 
    /* Allocate memory for the data to be passed back in the pipe */
    outputPipeData = (long *)malloc( sizeof(long) * PIPE_SIZE );
    
    while(elementsToSend >0) /* Loop to send pipe data elements */
    {
        if (index >= PIPE_SIZE)
            elementsToSend = 0;
        else
        {
            if ( (index + PIPE_TRANSFER_SIZE) > PIPE_SIZE )
                elementsToSend = PIPE_SIZE - index;
            else
                elementsToSend = PIPE_TRANSFER_SIZE;
        }
                    
        outputPipe->push( outputPipe->state,
                          &(outputPipeData[index]),
                          elementsToSend ); 
        index += elementsToSend;
 
    } //end while
 
    free((void *)outputPipeData);
 
}
```



## Related topics

<dl> <dt>

[pipe](/windows/desktop/Midl/pipe)
</dt> <dt>

[**/Oi**](/windows/desktop/Midl/-oi)
</dt> </dl>

 

 