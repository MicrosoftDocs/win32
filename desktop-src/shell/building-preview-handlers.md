---
Description: 'This topic discusses the specific interfaces and methods required to create a preview handler.'
ms.assetid: '6c240a63-c184-4b65-9483-794f5de4d695'
title: Building Preview Handlers
---

# Building Preview Handlers

This topic discusses the specific interfaces and methods required to create a preview handler.

A preview handler must implement the following interfaces:

-   [IInitializeWithStream::Initialize](#iinitializewithstreaminitialize) (strongly preferred), [**IInitializeWithFile**](iinitializewithfile.md), or [**IInitializeWithItem**](iinitializewithitem.md)
-   [IObjectWithSite](#iobjectwithsite)
-   [IOleWindow](#iolewindow)
-   [IPreviewHandler](#ipreviewhandler)

If your preview handler supports visual settings provided by the host such as background color and font, it must also implement the following interface:

-   [IPreviewHandlerVisuals](#ipreviewhandlervisuals)

This topic assumes that the preview handler is initialized with a stream and is registered for a particular file name extension.

## IInitializeWithStream::Initialize

Store the [**IStream**](stg.istream) and mode parameters so that you can read the item's data when you are ready to preview the item. Do not load the data in [**Initialize**](iinitializewithstream-initialize.md). Load the data in [**IPreviewHandler::DoPreview**](ipreviewhandler-dopreview.md) just before you render.

## IObjectWithSite

-   [IObjectWithSite::SetSite](#iobjectwithsitesetsite)
-   [IObjectWithSite::GetSite](#iobjectwithsitegetsite)

### IObjectWithSite::SetSite

Store the [**IUnknown**](com.iunknown) pointer for later access.

If you currently have a reference to an [**IPreviewHandlerFrame**](ipreviewhandlerframe.md) object, release it. Use the stored [**IUnknown**](com.iunknown) pointer to call [**QueryInterface**](com.iunknown_queryinterface) on the site for a new **IPreviewHandlerFrame** reference.

If you currently have an accelerator table, destroy it. Call [**IPreviewHandlerFrame::GetWindowContext**](ipreviewhandlerframe-getwindowcontext.md) to get a new accelerator table. Store this table. Note that it is used only as a list of accelerator keys that the frame supports. Commands in the accelerator entries are ignored.

### IObjectWithSite::GetSite

Return the site pointer, whatever it is.

## IOleWindow

-   [IOleWindow::ContextSensitiveHelp](#iolewindowcontextsensitivehelp)
-   [IOleWindow::GetWindow](#iolewindowgetwindow)

### IOleWindow::ContextSensitiveHelp

Return E\_NOTIMPL for this method.

### IOleWindow::GetWindow

If the preview handler's window currently exists, return the **HWND** of that window and S\_OK. If the window does not exist, return E\_FAIL.

## IPreviewHandler

-   [IPreviewHandler::SetWindow](#ipreviewhandlersetwindow)
-   [IPreviewHandler::SetRect](#ipreviewhandlersetrect)
-   [IPreviewHandler::DoPreview](#ipreviewhandlerdopreview)
-   [IPreviewHandler::SetFocus](#ipreviewhandlersetfocus)
-   [IPreviewHandler::QueryFocus](#ipreviewhandlerqueryfocus)
-   [IPreviewHandler::TranslateAccelerator](#ipreviewhandlertranslateaccelerator)
-   [IPreviewHandler::Unload](#ipreviewhandlerunload)

### IPreviewHandler::SetWindow

Set the *hwnd* parameter of this method to the parent of your preview handler's **HWND**. This method can be called multiple times. Resize your preview so that it renders only in the area described by the *prc* parameter.

If the previewer is in the process of rendering, use the [**IPreviewHandler::SetWindow**](ipreviewhandler-setwindow.md) method to change the parent of the previewer. Also change the area in which the previewer is rendering.

### IPreviewHandler::SetRect

Resize your preview so that it only renders in the area described by this method's *prc*.

If the previewer is in the process of rendering, change the area in which your previewer renders.

### IPreviewHandler::DoPreview

This is where the real work is done. Since a preview is dynamic, the preview content should only be loaded when it is needed. Do not load content in the initialization.

If the preview handler window does not exist, create it. Your preview handler's windows should be children of the window provided by [**IPreviewHandler::SetWindow**](ipreviewhandler-setwindow.md). They should be the size provided by **IPreviewHandler::SetWindow** and [**IPreviewHandler::SetRect**](ipreviewhandler-setrect.md) (whichever was called most recently).

Once you have a window, load the data from the [**IStream**](stg.istream) that the preview handler was initialized with, and render that data to your preview handler's window.

### IPreviewHandler::SetFocus

This method is called when the focus enters the reading pane through a tab action. Since it can be entered as a forward tab or reverse tab, use the current state of the SHIFT key to decide whether the first or last tab stop in the reading pane should receive the focus.

### IPreviewHandler::QueryFocus

This method should call the [**GetFocus**](inputdev.getfocus) function and return the result of that call in the *phwnd* parameter.

### IPreviewHandler::TranslateAccelerator

This method is called by the message pump of the preview handler's process (whether prevhost.exe or a custom local server) in response to user keystrokes. Preview handlers should handle these keystrokes or forward them to their host according to the algorithm detailed below.

However, because previews are read-only, keyboard input should be minimal and optimizations such as this are not needed in many cases.

If the keyboard accelerator passed to this method through the message pump is an accelerator that your preview handler accepts, then process it and return S\_OK. If your handler does not accept that accelerator, the accelerator message can be sent back as far as the frame to be handled.

There are two options for forwarding keyboard accelerators back to the frame:

The simplest model is to forward all keystrokes to the host using [**IPreviewHandlerFrame::TranslateAccelerator**](ipreviewhandlerframe-translateaccelerator.md). This is done in the preview handler sample provided with the Windows Software Development Kit (SDK). All low-integrity preview handlers must use this model. If the accelerator is not handled by your preview handler, call **IPreviewHandlerFrame::TranslateAccelerator** and return its result.

The other model is to use an accelerator table as an optimization to avoid sending too many keystrokes across process boundaries:

1.  When [**IObjectWithSite::SetSite**](com.iobjectwithsite_setsite) is called on your preview handler, acquire the accelerator table through [**IPreviewHandlerFrame::GetWindowContext**](ipreviewhandlerframe-getwindowcontext.md). (Be sure to free the handle to the accelerator table when your previewer is destroyed.)
2.  If the accelerator is handled by your preview handler, handle it and return S\_OK.
3.  If the accelerator is not handled by your preview handler, compare the message using [**IsAccelerator**](com.isaccelerator) against the accelerator table acquired.
4.  If the accelerator matches an entry in that accelerator table, call [**IPreviewHandlerFrame::TranslateAccelerator**](ipreviewhandlerframe-translateaccelerator.md) and return its result.
5.  If the accelerator does not match any entry in the accelerator table, return S\_FALSE.

### IPreviewHandler::Unload

When this method is called, stop any rendering, release any resources allocated by reading data from the stream, and release the [**IStream**](stg.istream) itself.

Once this method is called, the handler must be reinitialized before any attempt to call [**IPreviewHandler::DoPreview**](ipreviewhandler-dopreview.md) again.

## IPreviewHandlerVisuals

-   [IPreviewHandlerVisuals::SetBackgroundColor](#ipreviewhandlervisualssetbackgroundcolor)
-   [IPreviewHandlerVisuals::SetFont](#ipreviewhandlervisualssetfont)
-   [IPreviewHandlerVisuals::SetTextColor](#ipreviewhandlervisualssettextcolor)

These methods should be implemented when directing the preview handler to respond to the host's color and font schemes. The host queries the handler for [**IPreviewHandlerVisuals**](ipreviewhandlervisuals.md). If found to be supported, the host provides it with color, font, and text color.

### IPreviewHandlerVisuals::SetBackgroundColor

Store this color and use it during rendering when you want to provide a background color. For instance, to fill the window when the handler renders to an area smaller than the area provided by [**IPreviewHandler::SetWindow**](ipreviewhandler-setwindow.md) and [**IPreviewHandler::SetRect**](ipreviewhandler-setrect.md). Note, however, that you should not draw outside the area provided by those methods.

If this method is called while the preview is already being rendered, the rendering should be restarted using this background color.

### IPreviewHandlerVisuals::SetFont

Store this font information and use it during rendering when you want to display text consistent with the current Windows Vista settings.

### IPreviewHandlerVisuals::SetTextColor

Store this text color information and use it during rendering when you want to display text consistent with the current Windows Vista settings.

## Related topics

<dl> <dt>

[Preview Handlers and Shell Preview Host](preview-handlers.md)
</dt> <dt>

[How to Register a Preview Handler](how-to-register-a-preview-handler.md)
</dt> <dt>

[Preview Handler Guidelines](preview-handler-guidelines.md)
</dt> </dl>

 

 



