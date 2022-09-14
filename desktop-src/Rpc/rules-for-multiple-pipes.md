---
title: Rules for Multiple Pipes
description: Rules for multiple pipes in a single call in Remote Procedure Call (RPC).
ms.assetid: 1d0b2aed-27cc-4e74-9307-ada86bda4596
ms.topic: article
ms.date: 05/31/2018
---

# Rules for Multiple Pipes

You can combine \[[**in**](/windows/desktop/Midl/in)\], \[[**out**](/windows/desktop/Midl/out-idl)\], and \[**in, out**\] pipe parameters in any combination in a single call, but you must process the pipes in a specific order, as shown in the following pseudocode example:

> [!Note]  
> This feature is no longer supported in Windows Vista and later platforms.

 

-   Get the data from every input pipe, starting with the first (leftmost) \[**in**\] parameter, and continuing in order, draining each pipe before beginning to process the next.
-   After every input pipe has been completely processed, send the data for the output pipes, again starting with the first \[**out**\] parameter, and continuing in order, filling each pipe before beginning to process the next.

``` syntax
//in .IDL file:
void InOutUCharPipe( [in,out] UCHAR_PIPE *uchar_pipe_1, 
                     [out] UCHAR_PIPE * uchar_pipe_2, 
                     [in] UCHAR_PIPE uchar_pipe_3);
 
//remote procedure:
void InOutUCharPipe( UCHAR_PIPE *param1,
                     UCHAR_PIPE *param2,
                     UCHAR_PIPE  param3)
{
    while(!END_OF_PIPE1)
    {
        param1->pull (. . .);
        . . .
    };

    while(!END_OF_PIPE3)
    {
        param3.pull (. . .);
        . . .
    };

    while(!END_OF_PIPE1)
    {
        param1->push (. . .);
        . . .
    };

    while(!END_OF_PIPE2)
    {
        param2->push(. . .);
        . . .
    };
} //end InOutUCharPipe
```

 

 