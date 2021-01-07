---
description: An &\#0034;input context&\#0034; is an internal structure maintained by the IMM.
ms.assetid: 2b639e30-5368-45bb-943d-db1ab6b62582
title: Input Context
ms.topic: article
ms.date: 05/31/2018
---

# Input Context

An "input context" is an internal structure maintained by the IMM. It contains information about the status of the IME and is used by IME windows. By default, the operating system creates and assigns an input context to each thread. Within the thread, this default input context is a shared resource and is associated with each newly created window.

To retrieve or set information in the IME, an IME-aware application must first retrieve a handle to the input context associated with a specified window. The application retrieves the handle by using the [**ImmGetContext**](/windows/desktop/api/Imm/nf-imm-immgetcontext) function. It can use the retrieved handle in subsequent calls to the IMM functions to retrieve and set IME values, such as the composition window style, the composition style, and the status window position. Once the application has finished using the context, it must release the context using the [**ImmReleaseContext**](/windows/desktop/api/Imm/nf-imm-immreleasecontext) function.

Because the default input context is a shared resource, any changes the application makes to it apply to all windows in the thread. However, the application can override this default behavior by creating its own input context and associating it with one or more windows of the thread. The changes made to an application-specific input context apply only to the windows associated with the context.

Your application can create an input context by using the [**ImmCreateContext**](/windows/desktop/api/Imm/nf-imm-immcreatecontext) function. To assign the context to a window, the application calls the [**ImmAssociateContext**](/windows/desktop/api/Imm/nf-imm-immassociatecontext) function. This function returns a handle to the previously associated input context. If the application has not already associated an input context with the window, the returned handle is for the default input context. Typically, the application saves this handle and later reassociates it with the window when the customized input context is no longer needed.

Once an input context is associated with a window, the operating system automatically selects that context when the window is activated and receives the input focus. The style and other information in the input context affects subsequent keyboard input for that window, determining how the IME operates.

Your application must destroy any customized input context before it terminates. First, the application removes the input context from any association it has made with windows in the thread by using the [**ImmAssociateContext**](/windows/desktop/api/Imm/nf-imm-immassociatecontext) function. Then, it calls the [**ImmDestroyContext**](/windows/desktop/api/Imm/nf-imm-immdestroycontext) function.

## Related topics

<dl> <dt>

[About Input Method Manager](about-input-method-manager.md)
</dt> </dl>

 

 



