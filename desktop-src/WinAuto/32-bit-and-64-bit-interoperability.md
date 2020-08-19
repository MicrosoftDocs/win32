---
title: 32-bit and 64-bit Interoperability
description: Assistive technology applications need to communicate across process boundaries to get UI information from Microsoft Active Accessibility servers and Microsoft UI Automation providers.
ms.assetid: 8b46daed-4fd9-430c-bb4d-24be9c8015b5
ms.topic: article
ms.date: 05/31/2018
---

# 32-bit and 64-bit Interoperability

Assistive technology applications need to communicate across process boundaries to get UI information from Microsoft Active Accessibility servers and Microsoft UI Automation providers. This topic describes the main interprocess communication issues that you need to keep in mind when developing Windows accessibility applications.

When applications use the Windows Automation API, the Microsoft Active Accessibility and UI Automation run-time components automatically handle all of the issues and complexities involved in performing interprocess communications (IPC), including the interoperability issues involved when one process is 32-bits and the other is 64-bits. Microsoft recognizes that there are occasions when an assistive technology application may need to use some form of IPC instead of the Windows Automation API to communicate with a Microsoft Active Accessibility server or UI Automation provider. On these occasions, Microsoft recommends that you use DCOM or Windows messages (those with values less than that of **WM\_USER**) to communicate with other processes. Like the Windows Automation API, DCOM and Windows messages automatically handle all IPC issues for you, including 32-bit to 64-bit interoperability.

When the Windows Automation API, DCOM, and Windows messages are not an option, keep the following issues in mind when implementing your chosen IPC method:

-   Shared Memory—When using shared memory, be aware that a structure in a 32-bit process may have a different size and layout than the same structure in a 64-bit process. This is especially true for structures that contain pointers or handles.
-   Pointer Truncation—Although a 32-bit application can use the **LONGLONG** data type to store a 64-bit value, there are instances where no Windows API element exists that would enable the 32-bit application to receive a 64-bit value from a 64-bit process, or to send a 64-bit value to a 64-bit process. For example, the [**GetWindowLongPtr**](/windows/desktop/api/winuser/nf-winuser-getwindowlongptra) and [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) functions truncate all pointer values, leaving the 32-bit application with a useless value.
-   Handles—Because kernel32 and user32 handles are only 32-bit significant in both 32-bit and 64-bit processes, they can be transferred between processes without a problem. However, some items that Windows defines as handles are really just wrapped pointers (for example, **HTREEITEM**). These "handles" will be truncated if they are passed from a 64-bit process to a 32-bit process.
-   [WinEvent](winevents-infrastructure.md) Hook Functions—To register an in-context hook function with a 32-bit server process, the hook function must reside in a 32-bit DLL. Similarly, to register an in-context hook function with a 64-bit server process, the hook function must reside in a 64-bit DLL. If an assistive technology application attempts to register an in-context hook function with a server that has a different bit-depth, events will still be delivered to the hook function, but they will be delivered out-of-context. For more information, see WinEvents and [In-Context and Out-of-Context Hook Functions](in-context-and-out-of-context-hook-functions.md).

For more information about 32-bit and 64-bit interoperability, see [Process Interoperability](/windows/desktop/WinProg64/process-interoperability).

## Related topics

<dl> <dt>

[Windows Automation API Overview](windows-automation-api-overview.md)
</dt> </dl>

 

 