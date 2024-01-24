---
description: There are five asynchronous operations that are not related to any particular call.
ms.assetid: d7107834-07e4-40ed-91ea-2e6127597c13
title: Call-less Asynchronous Operations
ms.topic: article
ms.date: 05/31/2018
---

# Call-less Asynchronous Operations

There are five asynchronous operations that are not related to any particular call. The TAPI 2.x [**lineDevSpecific**](/windows/win32/api/tapi/nf-tapi-linedevspecific), [**lineDevSpecificFeature**](/windows/win32/api/tapi/nf-tapi-linedevspecificfeature), [**lineForward**](/windows/win32/api/tapi/nf-tapi-lineforward), [**lineSetTerminal**](/windows/win32/api/tapi/nf-tapi-linesetterminal), and [**lineUncompleteCall**](/windows/win32/api/tapi/nf-tapi-lineuncompletecall) functions initiate these operations. If an application initiates one of these asynchronous operations and calls [**lineClose**](/windows/win32/api/tapi/nf-tapi-lineclose), the service provider may receive no indication that the application has abandoned the function. This can occur if the application was not the only application to have the line open. If the application calls **lineClose** with one of these operations pending, and it is the only application with a handle to the line, TAPI calls the [**TSPI\_lineClose**](/windows/win32/api/tspi/nf-tspi-tspi_lineclose) function and the service provider should terminate the asynchronous operation, calling the [*Completion\_Proc*](/windows/win32/api/tspi/nc-tspi-async_completion) callback function for each such outstanding operation with the LINEERR\_OPERATIONFAILED error value.

 

 
