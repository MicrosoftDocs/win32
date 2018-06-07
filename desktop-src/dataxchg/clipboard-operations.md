---
title: Clipboard Operations
description: A window should use the clipboard when cutting, copying, or pasting data. A window places data on the clipboard for cut and copy operations and retrieves data from the clipboard for paste operations.
ms.assetid: 27f9142c-3154-4de5-aea6-3c53f7e940ec
keywords:
- Windows User Interface,clipboard
- clipboard,windows
- clipboard,cutting data
- clipboard,copying data
- clipboard,pasting data
- clipboard,owner window
- clipboard,delayed rendering
- clipboard,memory
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Clipboard Operations

A window should use the clipboard when cutting, copying, or pasting data. A window places data on the clipboard for cut and copy operations and retrieves data from the clipboard for paste operations. The following sections describe these operations and related issues.

To place data on or retrieve data from the clipboard, a window must first open the clipboard by using the [**OpenClipboard**](/windows/desktop/api/Winuser/nf-winuser-openclipboard) function. Only one window can have the clipboard open at a time. To find out which window has the clipboard open, call the [**GetOpenClipboardWindow**](/windows/desktop/api/Winuser/nf-winuser-getopenclipboardwindow) function. When it has finished, the window must close the clipboard by calling the [**CloseClipboard**](/windows/desktop/api/Winuser/nf-winuser-closeclipboard) function.

The following topics are discussed in this section.

-   [Cut and Copy Operations](#cut-and-copy-operations)
-   [Paste Operations](#paste-operations)
-   [Clipboard Ownership](#clipboard-ownership)
-   [Delayed Rendering](#delayed-rendering)
-   [Memory and the Clipboard](#memory-and-the-clipboard)

## Cut and Copy Operations

To place information on the clipboard, a window first clears any previous clipboard content by using the [**EmptyClipboard**](/windows/desktop/api/Winuser/nf-winuser-emptyclipboard) function. This function sends the [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message to the previous clipboard owner, frees resources associated with data on the clipboard, and assigns clipboard ownership to the window that has the clipboard open. To find out which window owns the clipboard, call the [**GetClipboardOwner**](/windows/desktop/api/Winuser/nf-winuser-getclipboardowner) function.

After emptying the clipboard, the window places data on the clipboard in as many clipboard formats as possible, ordered from the most descriptive clipboard format to the least descriptive. For each format, the window calls the [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function, specifying the format identifier and a global memory handle. The memory handle can be NULL, indicating that the window renders the data on request. For more information, see [Delayed Rendering](#delayed-rendering).

## Paste Operations

To retrieve paste information from the clipboard, a window first determines the clipboard format to retrieve. Typically, a window enumerates the available clipboard formats by using the [**EnumClipboardFormats**](/windows/desktop/api/Winuser/nf-winuser-enumclipboardformats) function and uses the first format it recognizes. This method selects the best available format according to the priority set when the data was placed on the clipboard.

Alternatively, a window can use the [**GetPriorityClipboardFormat**](/windows/desktop/api/Winuser/nf-winuser-getpriorityclipboardformat) function. This function identifies the best available clipboard format according to a specified priority. A window that recognizes only one clipboard format can simply determine whether that format is available by using the [**IsClipboardFormatAvailable**](/windows/desktop/api/Winuser/nf-winuser-isclipboardformatavailable) function.

After determining the clipboard format to use, a window calls the [**GetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-getclipboarddata) function. This function returns the handle to a global memory object containing data in the specified format. A window can briefly lock the memory object in order to examine or copy the data. However, a window should not free the object or leave it locked for a long period of time.

## Clipboard Ownership

The *clipboard owner* is the window associated with the information on the clipboard. A window becomes the clipboard owner when it places data on the clipboard specifically, when it calls the [**EmptyClipboard**](/windows/desktop/api/Winuser/nf-winuser-emptyclipboard) function. The window remains the clipboard owner until it is closed or another window empties the clipboard.

When the clipboard is emptied, the clipboard owner receives a [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message. Following are some reasons why a window might process this message:

-   The window delayed rendering of one or more clipboard formats. In response to the [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message, the window might free resources it had allocated in order to render data on request. For more information about the rendering of data, see [Delayed Rendering](#delayed-rendering).
-   The window placed data on the clipboard in a private clipboard format. The data for private clipboard formats is not freed by the system when the clipboard is emptied. Therefore, the clipboard owner should free the data upon receiving the [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message. For more information about private clipboard formats, see [Clipboard Formats](clipboard-formats.md).
-   The window placed data on the clipboard using the **CF\_OWNERDISPLAY** clipboard format. In response to the [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message, the window might free resources it had used to display information in the clipboard viewer window. For more information about this alternative format, see [Owner Display Format](about-the-clipboard.md).

## Delayed Rendering

When placing a clipboard format on the clipboard, a window can delay rendering the data in that format until the data is needed. To do so, an application can specify **NULL** for the *hData* parameter of the [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function. This is useful if the application supports several clipboard formats, some or all of which are time-consuming to render. By passing a **NULL** handle, a window renders complex clipboard formats only when and if they are needed.

If a window delays rendering a clipboard format, it must be prepared to render the format upon request for as long as it is the clipboard owner. The system sends the clipboard owner a [**WM\_RENDERFORMAT**](wm-renderformat.md) message when a request is received for a specific format that has not been rendered. Upon receiving this message, the window should call the [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function to place a global memory handle on the clipboard in the requested format.

If the clipboard owner is destroyed and has delayed rendering some or all clipboard formats, it receives the [**WM\_RENDERALLFORMATS**](wm-renderallformats.md) message. Upon receiving this message, the window should place valid memory handles on the clipboard for all clipboard formats that it provides. This ensures that these formats remain available after the clipboard owner is destroyed.

An application should not open the clipboard before calling [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) in response to the [**WM\_RENDERFORMAT**](wm-renderformat.md) or [**WM\_RENDERALLFORMATS**](wm-renderallformats.md) message.

Any clipboard formats that are not rendered in response to the [**WM\_RENDERALLFORMATS**](wm-renderallformats.md) message cease to be available to other applications and are no longer enumerated by the clipboard functions.

## Memory and the Clipboard

A memory object that is to be placed on the clipboard should be allocated by using the [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574) function with the **GMEM\_MOVEABLE** flag.

After a memory object is placed on the clipboard, ownership of that memory handle is transferred to the system. When the clipboard is emptied and the memory object has one of the following clipboard formats, the system frees the memory object by calling the specified function:



| Function to free object                             | Clipboard format                                                                                                                                               |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeleteMetaFile**](https://msdn.microsoft.com/library/windows/desktop/dd183537)<br/> | **CF\_DSPENHMETAFILE**<br/> **CF\_DSPMETAFILEPICT**<br/> **CF\_ENHMETAFILE**<br/> **CF\_METAFILEPICT**<br/>                            |
| [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539)<br/>     | **CF\_BITMAP**<br/> **CF\_DSPBITMAP**<br/> **CF\_PALETTE**<br/>                                                                              |
| [**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579)<br/>        | **CF\_DIB**<br/> **CF\_DIBV5**<br/> **CF\_DSPTEXT**<br/> **CF\_OEMTEXT**<br/> **CF\_TEXT**<br/> **CF\_UNICODETEXT**<br/>   |
| none<br/>                                     | **CF\_OWNERDISPLAY**<br/> When the clipboard is emptied of a **CF\_OWNERDISPLAY** object, the application itself must free the memory object.<br/> |



 

 

 





