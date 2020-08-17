---
title: Combining Pipe and Nonpipe Parameters
description: Combining pipe and nonpipe parameters in Remote Procedure Call (RPC).
ms.assetid: 52109ba9-4e10-4426-8dfc-e3052d403e9a
ms.topic: article
ms.date: 05/31/2018
---

# Combining Pipe and Nonpipe Parameters

When you combine pipe types and other types in a remote procedure call, the data is transmitted according to the direction of the parameter:

-   In the **\[in\]** direction, the data for all nonpipe arguments is transmitted first, followed by pipe data.
-   In the **\[out\]** direction, the server sends the pipe data first. After the manager routine returns, the server transmits the nonpipe data.
-   When there are **\[in,out\]** pipe arguments combined with **\[in,out\]** non-pipe arguments, first the input data is transmitted in its entirety, as previously described. Then, the output data is transmitted as previously described.

The following restriction applies to this (MIDL 3.0) implementation of pipes: When you combine pipe types and other types in a single remote procedure call, the nonpipe parameters must have a well-defined size in order to allow the MIDL compiler to calculate the buffer size needed. For example, you cannot combine pipe parameters with a \[ [unique](/windows/desktop/Midl/unique)\] pointer or a conformant structure, since their sizes cannot be determined at compile time.

## Related topics

<dl> <dt>

[pipe](/windows/desktop/Midl/pipe)
</dt> <dt>

[/Oi](/windows/desktop/Midl/-oi)
</dt> </dl>

 

 