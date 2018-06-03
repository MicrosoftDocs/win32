---
title: IrDA and WSAStartup
description: IrDA programmers must call the Windows Sockets WSAStartup function before making any other IrDA function calls.
ms.assetid: 014e5209-29f6-43d6-abcd-148488f0b479
keywords:
- IrDA and WSAStartup
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IrDA and WSAStartup

IrDA programmers must call the Windows Sockets [**WSAStartup**](https://msdn.microsoft.com/library/windows/desktop/ms742213) function before making any other IrDA function calls.

The following is an example of making a [**WSAStartup**](https://msdn.microsoft.com/library/windows/desktop/ms742213) function call for an IrDA application.

``` syntax
WORD        WSAVerReq = MAKEWORD(1,1);
WSADATA     WSAData;

if (WSAStartup(WSAVerReq, &WSAData) != 0)
{
    // wrong winsock DLLs?
}
```

 

 




