---
description: The status, composition, and candidates windows form the user interface for the IME.
ms.assetid: a0e52743-f9be-4934-9469-71d3cb5a768a
title: Status, Composition, and Candidates Windows
ms.topic: article
ms.date: 05/31/2018
---

# Status, Composition, and Candidates Windows

The status, composition, and candidates windows form the user interface for the IME. The status window indicates that the IME is open and provides the user with the means to set the conversion modes. The composition window appears when the user enters text and, depending on the conversion mode, either displays the text as entered or displays converted text. The candidates window appears in conjunction with the composition window. It contains a list of "candidates" (alternative characters) for the selected character or characters in the composition window. The user can scroll through the candidates list and select the desired characters, then return to the composition window. The user can compose the desired text in this way until the composition string is finalized and the window is closed.

The IME sends the composed characters to the IME-aware application in the form of [**WM\_IME\_CHAR**](wm-ime-char.md) or [**WM\_IME\_COMPOSITION**](wm-ime-composition.md)/GCS\_RESULT messages. If the application does not process these messages, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function translates them into one or more [**WM\_CHAR**](../inputdev/wm-char.md) messages.

By default, the operating system automatically creates and manages status, composition, and candidates windows for text input requirements. For many applications, this default processing is sufficient. These applications rely entirely on the operating system for IME support and are said to be "IME-unaware" because they are unaware of the many tasks the operating system carries out to manage the IME windows.

An IME-aware application, on the other hand, participates in the creation and management of IME windows. Such applications control the operation, position, and appearance of the default windows by sending messages to these windows and by intercepting and processing messages from the windows. In some cases, applications create their own IME windows and provide complete processing for their custom status, composition, and candidates windows.

## Related topics

<dl> <dt>

[About Input Method Manager](about-input-method-manager.md)
</dt> </dl>

 

 
