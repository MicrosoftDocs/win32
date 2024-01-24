---
title: Embedding the Windows Media Player Control in a Custom Program
description: Embedding the Windows Media Player Control in a Custom Program
ms.assetid: 2a5f0cd7-e3fa-4d4f-9203-bcb13362c9ab
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- Windows Media Player Mobile,embedding ActiveX control
- embedding,custom programs
- custom program embedding
- embedding,Visual Basic-based programs
- Visual Basic-based program embedding
- embedding,manually using COM methods
- manual embedding using COM methods
- embedding,C++ programs
- C++ program embedding
- embedding,Visual Studio programs
- Visual Studio,program embedding
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Embedding the Windows Media Player Control in a Custom Program

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Because the Windows Media Player ActiveX control is based on Microsoft Component Object Model (COM) technology, you can embed it in programs written with many different programming languages. The Windows Media Player control represents an easy way to add sophisticated digital media functionality to any program.

In Microsoft Visual Basic, you can add the control to the control toolbox, place it on a form, and adjust the control properties in the properties window. If you want a custom user interface, you can place command buttons on the form and add code that manages the Windows Media Player control. Embedding the control in a Visual Basic-based program is very similar to embedding it in an Office document and programming it with VBA.

Alternately, you can embed the control manually using COM methods to instantiate the control and access the COM interfaces documented in [Object Model Reference for C++](object-model-reference-for-c.md).

When you embed the Windows Media Player control in a C++ program, you have the option of implementing COM interfaces that allow the control to run in remote mode. This means that the embedded control shares the same playback engine as the full mode of the Player, and users can switch back and forth between the full mode and the docked state without interrupting digital media playback. You can also control what is displayed in the various panes of the full mode Player when your users switch to the undocked state.

With C++ embedding, you also have the option of applying a skin definition file to the embedded Player control. This is an easy way to create lightweight user interface code that you can maintain separately from your main program code.

Microsoft Visual Studio supports embedding ActiveX controls, including the Windows Media Player control. When you choose to do this, Visual Studio creates a new alternate interoperability (interop) assembly to manage interoperability between the .NET Framework and the Windows Media Player control. Visual Studio uses the .NET Framework tlbimp.exe tool to create the interop assembly. This means that the signatures displayed when using the IntelliSense feature in Visual Studio use semantics determined by the current version of tlbimp.

## Related topics

<dl> <dt>

[**Embedding the Windows Media Player Control**](embedding-the-windows-media-player-control.md)
</dt> <dt>

[**Using the Windows Media Player Control in a C++ Program**](using-the-windows-media-player-control-in-a-c---program.md)
</dt> <dt>

[**Using the Windows Media Player Control in a .NET Framework Solution**](using-the-windows-media-player-control-in-a--net-framework-solution.md)
</dt> <dt>

[**Using the Windows Media Player Control with Visual Basic**](using-the-windows-media-player-control-with-visual-basic.md)
</dt> </dl>

 

 




