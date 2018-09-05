---
title: ' in, string and  out, string Prototype'
description: The following function prototype uses two parameters an \ in, string\ parameter and an \ out, string\ parameter.
ms.assetid: acb0ec4f-1846-4fa2-98c2-2081b52a8260
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \[in, string\] and \[out, string\] Prototype

The following function prototype uses two parameters: an \[[**in**](https://msdn.microsoft.com/library/windows/desktop/aa367051), [**string**](https://msdn.microsoft.com/library/windows/desktop/aa367270)\] parameter and an \[[**out**](https://msdn.microsoft.com/library/windows/desktop/aa367136), **string**\] parameter.

``` syntax
void Analyze(
    [in, string]                       *pszInput,
    [out, string, size_is(STRSIZE)]    *pszOutput);
```

The first parameter is \[[**in**](https://msdn.microsoft.com/library/windows/desktop/aa367051)\] only. This input string is only transmitted from the client to the server. The server uses it as the basis for further processing. The string is not modified and is not required again by the client, so it does not have to be returned to the client.

The second parameter, representing the doctor's response, is \[[**out**](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] only. This response string is only transmitted from the server to the client. The allocation size is provided so that the server stubs can allocate memory for it. Since *pszOutput* is a \[[**ref**](https://msdn.microsoft.com/library/windows/desktop/aa367153)\] pointer, the client must have sufficient memory allocated for the string before the call. The response string is written into this area of memory when the remote procedure returns.

 

 




