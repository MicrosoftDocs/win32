---
title: Debugging (Windows Web Services)
description: A set of functions is only available in the DEBUG build, and are intended for testing and debugging.
ms.assetid: 23c01420-3f51-4c3f-9ee1-2614de3a278f
keywords:
- Debugging Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Debugging (Windows Web Services)

A set of functions is only available in the DEBUG build, and are intended for testing and debugging.


There are a number of functions and environment variables available in the DEBUG mode only. They can be used to help with testing and debugging.

-   Setting WsTimeout=0 will cause all timeouts to be INFINITE. This is useful when stepping through the debugger during time sensitive operations.
-   Setting WsFailCount has the same effect as calling WsSetAutoFail.
-   WsFlags allows you to set various flags that modify the runtime behavior. The syntax is WsFlags=a,b,c. The supported flags are ModifyTimestamp, ModifyInclusivePrefixes, ModifyTimestampDigest, ModifyToHeaderDigest and ModifySignatureValue.

The following functions are used with debugging:

-   [**WsDumpMemory**](wsdumpmemory.md)
-   [**WsSetAutoFail**](wssetautofail.md)

 

 




