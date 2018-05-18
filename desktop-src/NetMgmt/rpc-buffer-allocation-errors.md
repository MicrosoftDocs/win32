---
title: RPC Buffer Allocation Errors
description: Because the RPC run-time library allocates memory for send and receive buffers, the function should expect RPC allocation errors.
ms.assetid: 'be9105df-1183-48d6-8cea-391ca628c8b7'
---

# RPC Buffer Allocation Errors

Because the RPC run-time library allocates memory for send and receive buffers, the function should expect RPC allocation errors. In the event of an RPC allocation error, a resumable handle is invalidated. This is a requirement because resumable functions are not rewindable.

 

 




