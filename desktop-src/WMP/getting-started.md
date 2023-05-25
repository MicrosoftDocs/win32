---
title: Getting Started with the Windows Media Player SDK
description: Getting Started with the Windows Media Player SDK
ms.assetid: 47c333dc-dad3-4430-a053-016d2c931f74
keywords:
- Windows Media Player Mobile,plug-ins
- Windows Media Player Mobile,user interface plug-ins
- Windows Media Player Mobile plug-ins
- plug-ins,user interface
- plug-ins,Windows Media Player Mobile
- user interface plug-ins,Windows Media Player Mobile
- UI plug-ins,Windows Media Player Mobile
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Getting Started with the Windows Media Player SDK

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To create your plug-in, you first need to install Microsoft eMbedded Visual C++ 4.0 and Visual Studio 2003. You must also install the Pocket PC 2003 SDK or the Smartphone 2003 SDK, which are separate downloads. To compile and run the project, a Pocket PC or Smartphone device running the Windows Mobile 2003 Second Edition operating system must be synchronized with the development computer by using Microsoft ActiveSync® 3.7.1 or later.

Because UI plug-ins on Windows Mobile devices use the same plug-in model as the desktop versions, you can use the Windows Media Player Plug-in Wizard as a starting point when creating a background UI plug-in that will work with Windows Media Player 10 Mobile.

To create UI plug-in code, do the following:

1.  Open Visual Studio 2003, and start a new project in Visual C++.
2.  Select **Windows Media Player Plug-in Wizard** from the **Templates** pane.
3.  Name your project NetworkPlugin and click **OK**.
4.  Select **UI Plug-in** and click **Next**.
5.  Select **Background** and click **Next**.
6.  Click **Next** to finish the wizard. If you are going to monitor events with your plug-in, you must check **Listen to events** before finishing the wizard, and you should read the documentation for the **IWMPEvents** interface to find out which events are supported on Windows Media Player 10 Mobile.

Now that you have created your UI plug-in code, you need to create an empty Windows CE DLL project in eMbedded Visual C++ 4.0. Then copy your wizard-generated source files to that new project so that they will compile with the ARM4 compiler.

To create an empty project

1.  Start a new project in eMbedded Visual C++, and then select **WCE Dynamic-Link Library** from the **Projects** pane.
2.  Name your project and click **OK**.
3.  Make sure **An empty Windows CE DLL project** is selected, and then click **Finish**.
4.  Click the **Project** menu item.
5.  Select **Add to Project**, and then click **Files**.
6.  Select the C++ files you created with the plug-in wizard, and then click **OK**.

## Related topics

<dl> <dt>

[**Creating a User Interface Plug-in for Windows Media Player 10 Mobile**](creating-a-user-interface-plug-in-for-windows-media-player-10-mobile.md)
</dt> <dt>

[**IWMPEvents Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents)
</dt> </dl>

 

 




