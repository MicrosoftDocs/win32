---
description: The IMM includes thread identification checking that determines if a calling thread is the creator of a specified input method context handle (HIMC type) or window handle (HWND type).
ms.assetid: da55d6fe-a620-4ea7-9055-91bcd3233267
title: Developing IME-Aware Multiple-thread Applications
ms.topic: article
ms.date: 05/31/2018
---

# Developing IME-Aware Multiple-thread Applications

The IMM includes thread identification checking that determines if a calling thread is the creator of a specified input method context handle (HIMC type) or window handle (HWND type). If the thread is not the creator of the handle, the called IMM function fails and a subsequent call to [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INVALID\_ACCESS.

> [!Note]  
> The current IMM architecture does not provide a synchronization facility for access to IMM handles.

 

To use thread identification checking, your applications must adhere to the following guidelines:

-   A thread should not access the input context created by another thread.
-   A thread should not associate an input context with a window created by another thread, and vice versa.

## Related topics

<dl> <dt>

[Using Input Method Manager](using-input-method-manager.md)
</dt> </dl>

 

 
