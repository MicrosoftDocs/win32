---
title: Displaying Modal User Interfaces
description: Displaying Modal User Interfaces
ms.assetid: 748a8db7-159d-4043-beac-e0516327bcef
keywords:
- Windows Media Player plug-ins,displaying dialog and message boxes
- plug-ins,displaying dialog and message boxes
- user interface plug-ins,displaying dialog and message boxes
- UI plug-ins,displaying dialog and message boxes
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Modal User Interfaces

UI plug-ins should not display modal dialog boxes or message boxes in response to method calls from Windows Media Player. For example, do not display a message box from your implementation of **IWMPPluginUI::Create**.

If you must display a dialog box or message box from a UI plug-in method implementation that is called by the Player, you must follow these steps:

1.  Register a new window message using **RegisterWindowMessage**.
2.  Send the window message you registered to your UI plug-in window using **PostMessage**.
3.  Show the dialog box or message box from the message handler for your new window message.

## Related topics

<dl> <dt>

[**UI Plug-in Overview**](ui-plug-in-overview.md)
</dt> </dl>

 

 




