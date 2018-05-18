---
title: Call Synchronization
description: Call Synchronization
ms.assetid: 'e74407ef-f500-4d13-aef4-ca6bb37d5858'
---

# Call Synchronization

COM applications must be able to deal correctly with user input while processing one or more calls from COM or the operating system. COM provides call synchronization for single-threaded apartments only. Multithreaded apartments (containing free-threaded threads) do not receive calls while making calls (on the same thread). Multithreaded apartments cannot make input synchronized calls. Asynchronous calls are converted to synchronous calls in multithreaded apartments. The message filter is not called for any thread in a multithreaded apartment. For more information about threading issues, see [Processes, Threads, and Apartments](processes--threads--and-apartments.md).

COM calls between processes fall into three categories, as follows:

<dl> <dt>

<span id="Synchronous_calls"></span><span id="synchronous_calls"></span><span id="SYNCHRONOUS_CALLS"></span>*Synchronous calls*
</dt> <dd>

Most of the communication that takes place within COM is synchronous. When making synchronous calls, the caller waits for the reply before continuing and can receive incoming messages while waiting. COM enters a modal loop to wait for the reply, receiving and dispatching other messages in a controlled manner.

</dd> <dt>

<span id="Asynchronous_notifications"></span><span id="asynchronous_notifications"></span><span id="ASYNCHRONOUS_NOTIFICATIONS"></span>*Asynchronous notifications*
</dt> <dd>

When sending asynchronous notifications, the caller does not wait for the reply. COM uses [**PostMessage**](_win32_PostMessage_cpp) or high-level events to send asynchronous notifications, depending on the platform. COM defines five asynchronous methods of [**IAdviseSink**](iadvisesink.md):

-   [**OnDataChange**](iadvisesink-ondatachange.md)
-   [**OnViewChange**](iadvisesink-onviewchange.md)
-   [**OnRename**](iadvisesink-onrename.md)
-   [**OnSave**](iadvisesink-onsave.md)
-   [**OnClose**](iadvisesink-onclose.md)

> [!Note]  
> While COM is processing an asynchronous call, synchronous calls cannot be made. For example, a container application's implementation of [**OnDataChange**](iadvisesink-ondatachange.md) cannot contain a call to [**IPersistStorage::Save**](ipersiststorage-save.md). These calls are the only asynchronous calls supported by COM. There is no way to create a custom interface that is asynchronous at this time.

 

</dd> <dt>

<span id="Input-synchronized_calls"></span><span id="input-synchronized_calls"></span><span id="INPUT-SYNCHRONIZED_CALLS"></span>*Input-synchronized calls*
</dt> <dd>

When making input-synchronized calls, the object called must complete the call before yielding control. This helps ensure that focus management works correctly and that data entered by the user is processed appropriately. These calls are made by COM through the [**SendMessage**](_win32_SendMessage_cpp) function, without entering a modal loop. While processing an input-synchronized call, the object called must not call any function or method (including synchronous methods) that might yield control. The following methods are input synchronized

-   [**IOleWindow::GetWindow**](iolewindow-getwindow.md)
-   [**IOleInPlaceActiveObject::OnFrameWindowActivate**](ioleinplaceactiveobject-onframewindowactivate.md)
-   [**IOleInPlaceActiveObject::OnDocWindowActivate**](ioleinplaceactiveobject-ondocwindowactivate.md)
-   [**IOleInPlaceActiveObject::ResizeBorder**](ioleinplaceactiveobject-resizeborder.md)
-   [**IOleInPlaceUIWindow::GetBorder**](ioleinplaceuiwindow-getborder.md)
-   [**IOleInPlaceUIWindow::RequestBorderSpace**](ioleinplaceuiwindow-requestborderspace.md)
-   [**IOleInPlaceUIWindow::SetBorderSpace**](ioleinplaceuiwindow-setborderspace.md)
-   [**IOleInPlaceFrame::SetMenu**](ioleinplaceframe-setmenu.md)
-   [**IOleInPlaceFrame::SetStatusText**](ioleinplaceframe-setstatustext.md)
-   [**IOleInPlaceObject::SetObjectRects**](ioleinplaceobject-setobjectrects.md)

</dd> </dl>

To minimize problems that can arise from asynchronous message processing, the majority of COM method calls are synchronous. With synchronous communication, there is no need for special code to dispatch and handle incoming messages. When an application makes a synchronous method call, COM enters a modal wait loop that handles the required replies and dispatches incoming messages to applications capable of processing them.

COM manages method calls by assigning an identifier called a *logical thread ID*. A new one is assigned when a user selects a menu command or when the application initiates a new COM operation. Subsequent calls that relate to the initial COM call are assigned the same logical thread ID as the initial call.

 

 




