---
title: Call Synchronization
description: Call Synchronization
ms.assetid: e74407ef-f500-4d13-aef4-ca6bb37d5858
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

When sending asynchronous notifications, the caller does not wait for the reply. COM uses [**PostMessage**](_win32_PostMessage_cpp) or high-level events to send asynchronous notifications, depending on the platform. COM defines five asynchronous methods of [**IAdviseSink**](/windows/win32/ObjIdl/nn-objidl-iadvisesink?branch=master):

-   [**OnDataChange**](/windows/win32/ObjIdl/nf-objidl-iadvisesink-ondatachange?branch=master)
-   [**OnViewChange**](/windows/win32/ObjIdl/nf-objidl-iadvisesink-onviewchange?branch=master)
-   [**OnRename**](/windows/win32/ObjIdl/nf-objidl-iadvisesink-onrename?branch=master)
-   [**OnSave**](/windows/win32/ObjIdl/nf-objidl-iadvisesink-onsave?branch=master)
-   [**OnClose**](/windows/win32/ObjIdl/nf-objidl-iadvisesink-onclose?branch=master)

> [!Note]  
> While COM is processing an asynchronous call, synchronous calls cannot be made. For example, a container application's implementation of [**OnDataChange**](/windows/win32/ObjIdl/nf-objidl-iadvisesink-ondatachange?branch=master) cannot contain a call to [**IPersistStorage::Save**](/windows/win32/ObjIdl/nf-objidl-ipersiststorage-save?branch=master). These calls are the only asynchronous calls supported by COM. There is no way to create a custom interface that is asynchronous at this time.

 

</dd> <dt>

<span id="Input-synchronized_calls"></span><span id="input-synchronized_calls"></span><span id="INPUT-SYNCHRONIZED_CALLS"></span>*Input-synchronized calls*
</dt> <dd>

When making input-synchronized calls, the object called must complete the call before yielding control. This helps ensure that focus management works correctly and that data entered by the user is processed appropriately. These calls are made by COM through the [**SendMessage**](_win32_SendMessage_cpp) function, without entering a modal loop. While processing an input-synchronized call, the object called must not call any function or method (including synchronous methods) that might yield control. The following methods are input synchronized

-   [**IOleWindow::GetWindow**](/windows/win32/OleIdl/nf-oleidl-iolewindow-getwindow?branch=master)
-   [**IOleInPlaceActiveObject::OnFrameWindowActivate**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceactiveobject-onframewindowactivate?branch=master)
-   [**IOleInPlaceActiveObject::OnDocWindowActivate**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceactiveobject-ondocwindowactivate?branch=master)
-   [**IOleInPlaceActiveObject::ResizeBorder**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceactiveobject-resizeborder?branch=master)
-   [**IOleInPlaceUIWindow::GetBorder**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceuiwindow-getborder?branch=master)
-   [**IOleInPlaceUIWindow::RequestBorderSpace**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceuiwindow-requestborderspace?branch=master)
-   [**IOleInPlaceUIWindow::SetBorderSpace**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceuiwindow-setborderspace?branch=master)
-   [**IOleInPlaceFrame::SetMenu**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-setmenu?branch=master)
-   [**IOleInPlaceFrame::SetStatusText**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-setstatustext?branch=master)
-   [**IOleInPlaceObject::SetObjectRects**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceobject-setobjectrects?branch=master)

</dd> </dl>

To minimize problems that can arise from asynchronous message processing, the majority of COM method calls are synchronous. With synchronous communication, there is no need for special code to dispatch and handle incoming messages. When an application makes a synchronous method call, COM enters a modal wait loop that handles the required replies and dispatches incoming messages to applications capable of processing them.

COM manages method calls by assigning an identifier called a *logical thread ID*. A new one is assigned when a user selects a menu command or when the application initiates a new COM operation. Subsequent calls that relate to the initial COM call are assigned the same logical thread ID as the initial call.

 

 




