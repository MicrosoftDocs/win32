---
title: Out-Only Unique or Full Pointer Parameters Not Accepted
description: Unique or full pointers that are \ out\ -only are not accepted by the MIDL compiler. Such specifications cause the MIDL compiler to generate an error message.
ms.assetid: 0477980e-d76e-452f-9ab1-71a8ed8642d9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Out-Only Unique or Full Pointer Parameters Not Accepted

Unique or full pointers that are \[ [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\]-only are not accepted by the MIDL compiler. Such specifications cause the MIDL compiler to generate an error message.

The automatically generated server stub has to allocate memory for the pointer referent so that the server application can store data in that memory area. According to the definition of an **\[out\]**-only parameter, no information about the parameter is transmitted from client to server. In the case of a unique pointer, which can take the value null, the server stub does not have enough information to correctly duplicate the unique pointer in the server's address space, nor does the stub have any information about whether the pointer should point to a valid address or whether it should be set to null. Therefore, this combination is not allowed.

Rather than \[**out**, [unique](https://msdn.microsoft.com/library/windows/desktop/aa367294)\] or \[**out**, [ptr](https://msdn.microsoft.com/library/windows/desktop/aa367149)\] pointers, use \[**in**, **out**, **unique**\] or \[**in**, **out**, **ptr**\] pointers, or use another level of indirection such as a reference pointer that points to the valid unique or full pointer.

 

 




