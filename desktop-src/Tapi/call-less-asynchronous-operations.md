---
Description: There are five asynchronous operations that are not related to any particular call.
ms.assetid: d7107834-07e4-40ed-91ea-2e6127597c13
title: Call-less Asynchronous Operations
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Call-less Asynchronous Operations

There are five asynchronous operations that are not related to any particular call. The TAPI 2.x [**lineDevSpecific**](https://msdn.microsoft.com/en-us/library/ms735604(v=VS.85).aspx), [**lineDevSpecificFeature**](https://msdn.microsoft.com/en-us/library/ms735607(v=VS.85).aspx), [**lineForward**](https://msdn.microsoft.com/en-us/library/ms735640(v=VS.85).aspx), [**lineSetTerminal**](https://msdn.microsoft.com/en-us/library/ms736110(v=VS.85).aspx), and [**lineUncompleteCall**](https://msdn.microsoft.com/en-us/library/ms736476(v=VS.85).aspx) functions initiate these operations. If an application initiates one of these asynchronous operations and calls [**lineClose**](https://msdn.microsoft.com/en-us/library/ms735573(v=VS.85).aspx), the service provider may receive no indication that the application has abandoned the function. This can occur if the application was not the only application to have the line open. If the application calls **lineClose** with one of these operations pending, and it is the only application with a handle to the line, TAPI calls the [**TSPI\_lineClose**](https://msdn.microsoft.com/en-us/library/ms725531(v=VS.85).aspx) function and the service provider should terminate the asynchronous operation, calling the [*Completion\_Proc*](https://msdn.microsoft.com/en-us/library/ms725180(v=VS.85).aspx) callback function for each such outstanding operation with the LINEERR\_OPERATIONFAILED error value.

 

 



