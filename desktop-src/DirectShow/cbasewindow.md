---
description: The CBaseWindow class is a base class for managing windows.
ms.assetid: 212d179e-5b5e-49fb-bf0a-a12e0317c96a
title: CBaseWindow class (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseWindow class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CBaseWindow` class is a base class for managing windows. Video renderers can use this class to create video windows. To use this class, create a derived class that inherits from `CBaseWindow`. In the derived class:

-   Implement the pure virtual method [**CBaseWindow::GetClassWindowStyles**](cbasewindow-getclasswindowstyles.md), which defines the window styles.
-   Override the [**CBaseWindow::OnReceiveMessage**](cbasewindow-onreceivemessage.md) method, which handles window messages.
-   Implement a destructor that calls the [**CBaseWindow::DoneWithWindow**](cbasewindow-donewithwindow.md) method.

Before using an instance of the derived class, call the [**CBaseWindow::PrepareWindow**](cbasewindow-preparewindow.md) method.



| Protected Member Variables                                           | Description                                                                    |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**m\_hInstance**](cbasewindow-m-hinstance.md)                      | Handle to the module instance.                                                 |
| [**m\_hwnd**](cbasewindow-m-hwnd.md)                                | Handle to the object's window.                                                 |
| [**m\_hdc**](cbasewindow-m-hdc.md)                                  | Handle to the window's device context.                                         |
| [**m\_Width**](cbasewindow-m-width.md)                              | Width of the client area, in pixels.                                           |
| [**m\_Height**](cbasewindow-m-height.md)                            | Height of the client area, in pixels.                                          |
| [**m\_bActivated**](cbasewindow-m-bactivated.md)                    | Flag that specifies whether the window has been activated.                     |
| [**m\_pClassName**](cbasewindow-m-pclassname.md)                    | Static string that contains the name of the window class.                      |
| [**m\_ClassStyles**](cbasewindow-m-classstyles.md)                  | Class styles for the window.                                                   |
| [**m\_WindowStyles**](cbasewindow-m-windowstyles.md)                | Window styles for the window.                                                  |
| [**m\_WindowStylesEx**](cbasewindow-m-windowstylesex.md)            | Extended window styles for the window.                                         |
| [**m\_ShowStageMessage**](cbasewindow-m-showstagemessage.md)        | Private message that brings the window to the foreground.                      |
| [**m\_ShowStageTop**](cbasewindow-m-showstagetop.md)                | Private message that sets the window style to WS\_EX\_TOPMOST.                 |
| [**m\_RealizePalette**](cbasewindow-m-realizepalette.md)            | Private message that realizes the palette.                                     |
| [**m\_MemoryDC**](cbasewindow-m-memorydc.md)                        | Handle to the memory device context.                                           |
| [**m\_hPalette**](cbasewindow-m-hpalette.md)                        | Handle to the window's palette.                                                |
| [**m\_bNoRealize**](cbasewindow-m-bnorealize.md)                    | Flag that specifies whether the window should realize its palette.             |
| [**m\_bBackground**](cbasewindow-m-bbackground.md)                  | Flag that specifies whether the palette should be a background palette.        |
| [**m\_bRealizing**](cbasewindow-m-brealizing.md)                    | Flag that specifies whether a new palette is being realized.                   |
| [**m\_WindowLock**](cbasewindow-m-windowlock.md)                    | Critical section, to serialize access to the object.                           |
| [**m\_bDoGetDC**](cbasewindow-m-bdogetdc.md)                        | Flag that specifies whether to retrieve the device context.                    |
| [**m\_bDoPostToDestroy**](cbasewindow-m-bdoposttodestroy.md)        | Flag that specifies whether the window posts or sends its destruction message. |
| Protected Methods                                                    | Description                                                                    |
| [**OnPaletteChange**](cbasewindow-onpalettechange.md)               | Handles palette-change messages. Virtual.                                      |
| Public Methods                                                       | Description                                                                    |
| [**CBaseWindow**](cbasewindow-cbasewindow.md)                       | Constructor method.                                                            |
| [**DoneWithWindow**](cbasewindow-donewithwindow.md)                 | Destroys the window. Virtual.                                                  |
| [**PrepareWindow**](cbasewindow-preparewindow.md)                   | Creates the window. Virtual.                                                   |
| [**InactivateWindow**](cbasewindow-inactivatewindow.md)             | Inactivates the window. Virtual.                                               |
| [**ActivateWindow**](cbasewindow-activatewindow.md)                 | Sizes the window according to the requirements of the derived class. Virtual.  |
| [**OnSize**](cbasewindow-onsize.md)                                 | Handles WM\_SIZE messages. Virtual.                                            |
| [**OnClose**](cbasewindow-onclose.md)                               | Handles WM\_CLOSE messages. Virtual.                                           |
| [**GetDefaultRect**](cbasewindow-getdefaultrect.md)                 | Retrieves the default size of the client area. Virtual.                        |
| [**UninitialiseWindow**](cbasewindow-uninitialisewindow.md)         | Releases the window's resources. Virtual.                                      |
| [**InitialiseWindow**](cbasewindow-initialisewindow.md)             | Initializes the window. Virtual.                                               |
| [**CompleteConnect**](cbasewindow-completeconnect.md)               | Notifies the window that the renderer's input pin has been connected.          |
| [**DoCreateWindow**](cbasewindow-docreatewindow.md)                 | Creates the window.                                                            |
| [**PerformanceAlignWindow**](cbasewindow-performancealignwindow.md) | Aligns the window to a **DWORD** boundary, for maximum performance.            |
| [**DoShowWindow**](cbasewindow-doshowwindow.md)                     | Sets the window's show state.                                                  |
| [**PaintWindow**](cbasewindow-paintwindow.md)                       | Causes the window to be repainted.                                             |
| [**DoSetWindowForeground**](cbasewindow-dosetwindowforeground.md)   | Brings the window to the foreground.                                           |
| [**SetPalette**](cbasewindow-setpalette.md)                         | Installs a palette for the window. Virtual.                                    |
| [**SetRealize**](cbasewindow-setrealize.md)                         | Specifies whether the window realizes palettes.                                |
| [**DoRealisePalette**](cbasewindow-dorealisepalette.md)             | Realizes the window's current palette. Virtual.                                |
| [**PossiblyEatMessage**](cbasewindow-possiblyeatmessage.md)         | Enables a derived class to forward messages to another window. Virtual.        |
| [**GetWindowWidth**](cbasewindow-getwindowwidth.md)                 | Retrieves the current width of the window.                                     |
| [**GetWindowHeight**](cbasewindow-getwindowheight.md)               | Retrieves the current height of the window.                                    |
| [**GetWindowHWND**](cbasewindow-getwindowhwnd.md)                   | Retrieves a handle to the window.                                              |
| [**GetMemoryHDC**](cbasewindow-getmemoryhdc.md)                     | Retrieves a handle to the memory device context.                               |
| [**GetWindowHDC**](cbasewindow-getwindowhdc.md)                     | Retrieves a handle to the window's device context.                             |
| [**OnReceiveMessage**](cbasewindow-onreceivemessage.md)             | Handles window messages. Virtual.                                              |
| [**UnsetPalette**](cbasewindow-unsetpalette.md)                     | Deletes the window's current palette and restores the default system palette.  |
| Pure Virtual Methods                                                 | Description                                                                    |
| [**GetClassWindowStyles**](cbasewindow-getclasswindowstyles.md)     | Retrieves the window's class styles and window styles.                         |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




