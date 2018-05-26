---
Description: All pointers used by applications with Windows Sockets should be FAR, although this is only relevant to 16-bit applications and meaningless in a 32-bit. To facilitate this, data type definitions such as LPHOSTENT are provided.
ms.assetid: 49111309-1a2f-462c-b9f5-e6839e439ada
title: Pointers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pointers

All pointers used by applications with Windows Sockets should be FAR, although this is only relevant to 16-bit applications and meaningless in a 32-bit. To facilitate this, data type definitions such as **LPHOSTENT** are provided.

## Related topics

<dl> <dt>

[**hostent**](/windows/win32/winsock/ns-winsock-hostent?branch=master)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 



