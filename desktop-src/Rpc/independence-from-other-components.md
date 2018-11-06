---
title: Independence From Other Components
description: Extended error data is useful even when the server or application through which the chain passed does not recognize extended error data, or does not take advantage of it. Recommended approaches for such situations are provided at the end of this section.
ms.assetid: 32c52afd-cd79-4df3-bf30-72a17ce22089
keywords:
- Independence From Other Components
ms.topic: article
ms.date: 05/31/2018
---

# Independence From Other Components

Extended error data is useful even when the server or application through which the chain passed does not recognize extended error data, or does not take advantage of it. Recommended approaches for such situations are provided at the end of this section.

Extended error data is most useful when applications or servers using RPC take advantage of extended error information. When investigating an RPC\_S\_\* error code and the servers or applications involved do not make extended error data available, consider the following approaches:

-   Take a sniff.

    Reproduce the scenario while taking the sniff. The sniff of the wire will contain the extended error data.

-   Examine it from the debugger.

    If taking a sniff of the problem does not work, because the call is local or because the error originates locally, attach a debugger to the process returning the error and put a breakpoint immediately after the RPC call generating the error. RPC often indicates errors by throwing exceptions, so if you are looking for error 1825 (RPC\_S\_SEC\_PKG\_ERROR), enable exception 1825 and when the debugger breaks on that exception, examine the extended error information for the thread.

 

 




