---
description: The default queue callback routine can be specified to handle notifications sent by SetupCommitFileQueue, or it can be called by a custom callback routine that builds on the functionality of the default queue callback routine.
ms.assetid: df8ae7b5-f3a2-4343-a603-440ab5c02b88
title: Using the Default Queue Callback Routine
ms.topic: article
ms.date: 05/31/2018
---

# Using the Default Queue Callback Routine

The default queue callback routine can be specified to handle notifications sent by [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea), or it can be called by a custom callback routine that builds on the functionality of the default queue callback routine.

The following sections explain how to initialize and terminate the context used by a default queue callback routine. The sections also describe how to use the default queue callback routine with [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) or a custom callback routine.

-   [Initializing and Terminating the Callback Context](initializing-and-terminating-the-callback-context.md)
-   [Calling the Default Queue Callback Routine](calling-the-default-queue-callback-routine.md)

 

 



