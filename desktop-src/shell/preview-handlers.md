---
description: Preview handlers are called when an item is selected to show a lightweight, rich, read-only preview of the file's contents in the view's reading pane. This is done without launching the file's associated application.
ms.assetid: '166a4001-d237-44a4-a457-e320e995639c'
title: Preview Handlers and Shell Preview Host
ms.topic: article
ms.date: 05/31/2018
---

# Preview Handlers and Shell Preview Host

Preview handlers are called when an item is selected to show a lightweight, rich, *read-only* preview of the file's contents in the view's reading pane. This is done without launching the file's associated application.

This topic discusses the following topics:

-   [Preview Handler Architecture](#preview-handler-architecture)
-   [Server Model Options](#server-model-options)
-   [Initialization](#initialization)
-   [Preview Handler Data Flow](#preview-handler-data-flow)
-   [Debugging a Preview Handler](#debugging-a-preview-handler)
-   [Providing Your Own Process for a Preview Handler](#providing-your-own-process-for-a-preview-handler)
-   [Related topics](#related-topics)

## Preview Handler Architecture

A preview handler is a hosted application. Hosts include the Windows Explorer in Windows Vista or Microsoft Outlook 2007. Hosts implement [**IPreviewHandlerFrame**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandlerframe) as a method of communication between the preview handler and the host.

The preview handler itself implements these interfaces:

-   [**IInitializeWithStream**](/windows/desktop/api/Propsys/nn-propsys-iinitializewithstream)
-   [**IObjectWithSite**](/windows/win32/api/ocidl/nn-ocidl-iobjectwithsite)
-   [**IOleWindow**](/windows/win32/api/oleidl/nn-oleidl-iolewindow)
-   [**IPreviewHandler**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandler)
-   [**IPreviewHandlerVisuals**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandlervisuals) (Optional)

Your handler is called through its [**IObjectWithSite**](/windows/win32/api/ocidl/nn-ocidl-iobjectwithsite), which returns an [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer through which you request an [**IPreviewHandlerFrame**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipreviewhandlerframe) object to interact with the host.

## Server Model Options

Preview handlers always run out of process. There are two methods of implementing this:

1.  A preview handler can be built as an in-process server but run through an out-of-process surrogate host. This is the preferred method. The system provides a surrogate host for this in the Prevhost.exe file. Preview handlers built by this method are not compatible with Outlook 2007 on Windows XP. However, these same handlers will work in Windows Explorer and Outlook 2007 running on Windows Vista.
2.  A preview handler can be built as a local Component Object Model (COM) server. This is not recommended for several reasons. First, implementation of an in-process server is easier. More importantly, implementation as an in-process server provides greater control over the lifetime of the handler object, which allows for better cleanup and efficiency.

By default, preview handlers run in a low integrity level (IL) process for security reasons. You can optionally disable running as a low IL process by setting the following value in the registry. However, it is not recommended to do so. Systems could eventually be configured to reject any process that is not low IL.

```
HKEY_CLASSES_ROOT
   CLSID
      {YOUR HANDLER'S CLSID}
         DisableLowILProcessIsolation [DWORD] = 1
```

Different preview handlers share the same process by default. Two instances of Prevhost.exe can be running simultaneously; one for handlers running as low IL processes, one for handlers that have opted out of that behavior.

## Initialization

As with thumbnail and property handlers, it is strongly recommended that you initialize your handler with a stream. You can initialize through a file or item if necessary, but streams provide the most secure way to implement a handler. Initialization through a stream ensures file integrity and the stability benefits to the system of running the handler as a low IL process, such as protecting the system from buffer overruns, limiting where a handler can write information, and limiting communication with other windows.

If you must initialize with a file or Shell item, store the file path or a reference to the [**IShellItem**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem). Do not read data from these sources until [**IPreviewHandler::DoPreview**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-dopreview) is called.

In general, initialization should not do any heavy work such as composing and storing a preview image. For optimal efficiency, that sort of processing should not be done until the preview is called for.

## Preview Handler Data Flow

The data flow in the preview process follows the general path shown here. The host can be thought of as Windows Explorer in Windows Vista or Outlook 2007.

1.  The preview handler is initialized, preferably with a stream.
2.  The view window is passed from the host to the handler through [**IPreviewHandler::SetWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-setwindow).
3.  At this point, the handler should do nothing more until [**IPreviewHandler::DoPreview**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-dopreview) is called.
4.  The preview is displayed in the reading pane through a call to [**IPreviewHandler::DoPreview**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-dopreview).
5.  The size of the window is set through [**IPreviewHandler::SetRect**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-setrect).
6.  The window is resized when needed through [**IPreviewHandler::SetRect**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-setrect).
7.  The preview is unloaded and its resources released when it is no longer needed, through a call to [**IPreviewHandler::Unload**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandler-unload).

## Debugging a Preview Handler

If you have followed the recommendations to implement your preview handler as an in-process server, to debug your preview handler, you can attach to Prevhost.exe. As mentioned earlier, be aware that there could be two instances of Prevhost.exe, one for normal low IL processes and one for those handlers that have opted out of running as a low IL process.

If you do not find Prevhost.exe in your list of available processes, it probably has not been loaded at that point. Clicking on a file for a preview loads the surrogate and it should then appear as an attachable process.

## Providing Your Own Process for a Preview Handler

If you want to force the creation of a new process for your handler rather than running under the default process, create a new subkey for your handler under **AppID** and set its DllSurrogate entry to "Prevhost.exe". Use that **AppID** subkey instead of the default Prevhost.exe **AppID**.

By providing a new process, the handler can avoid running under a shared process as it would do by default. This could allow you, for example, to ensure the specific version of the common language runtime (CLR) in the process. This is required if you are building a managed implementation of a preview handler.

> [!Note]  
> 32-bit preview handlers should use **AppID** {534A1E02-D58F-44f0-B58B-36CBED287C7C} when installed on 64-bit operating systems.

 

## Related topics

<dl> <dt>

[Building Preview Handlers](building-preview-handlers.md)
</dt> <dt>

[How to Register a Preview Handler](how-to-register-a-preview-handler.md)
</dt> <dt>

[Preview Handler Guidelines](preview-handler-guidelines.md)
</dt> </dl>

 

 
