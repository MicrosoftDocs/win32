---
Description: A process may call WSPCloseSocket on a duplicated socket and the descriptor will become deallocated. The underlying socket, however, will remain open until WSPCloseSocket is called on the last remaining descriptor.
ms.assetid: dff1e932-5e87-4ec5-995d-686d20ba6236
title: Reference Counting
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reference Counting

A process may call [**WSPCloseSocket**](/windows/win32/Ws2spi/?branch=master) on a duplicated socket and the descriptor will become deallocated. The underlying socket, however, will remain open until **WSPCloseSocket** is called on the last remaining descriptor.

 

 



