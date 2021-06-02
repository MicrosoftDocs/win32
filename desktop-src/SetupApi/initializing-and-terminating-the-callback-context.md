---
description: Before the default queue callback routine can be used, either by specifying it as the callback routine when committing a file queue, or by calling it from a custom callback routine, it must be initialized.
ms.assetid: e25a9787-a4a3-4d06-bf55-f6f7cfb23481
title: Initializing and Terminating the Callback Context
ms.topic: article
ms.date: 05/31/2018
---

# Initializing and Terminating the Callback Context

Before the default queue callback routine can be used, either by specifying it as the callback routine when committing a file queue, or by calling it from a custom callback routine, it must be initialized.

The [**SetupInitDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallback) function builds the context structure that is used by the default queue callback routine. It returns a void pointer to that structure. This structure is essential for the default callback routine's operation and must be passed to the callback routine. You do can this either by specifying the void pointer as the context in a call to [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea), or by specifying the void pointer as the context parameter when calling [**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka) from a custom callback routine. This context structure must not be altered or referenced by the setup application.

The [**SetupInitDefaultQueueCallbackEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex) function also initializes a context for the default queue callback routine, but it specifies a second window to receive a caller-specified progress message each time the queue sends a notification. This enables you to use the default disk prompting and error dialog boxes, and to also embed a progress bar in a second window, for example, in a page of an installation wizard.

Regardless of whether you initialized the context used by the default queue callback routine with [**SetupInitDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallback) or [**SetupInitDefaultQueueCallbackEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex), after the queued operations have finished processing, call [**SetupTermDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setuptermdefaultqueuecallback) to release the resources allocated in initializing the context structure.

 

 



