---
title: Receiving Video Control Events in C++
description: Receiving Video Control Events in C++
ms.assetid: aa9eacc7-a629-440e-a99a-a1f91a755609
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiving Video Control Events in C++

This topic applies to Windows XP or later.

In a television application, various objects send events, including the Video Control. The application can listen for these events and respond to them. For example, the Video Control sends an event when the video window is clicked or receives a keystroke.

Objects send events using COM connection points. To catch an event, the client implements an event interface. The object fires events by calling methods on that interface. For example, the Video Control sends events through the [**\_IMSVidCtlEvents**](/windows/previous-versions/msvidctl/?branch=master) interface. The mouse-click event is [**\_IMSVidCtlEvents::Click**](/windows/previous-versions/msvidctl/?branch=master). The following image illustrates this process.

![\-imsvidctlevents connection point](images/connection-point.gif)

In COM terminology, the event interface is the *outgoing* interface, the object that sends the events is the *source*, and any object that receives events is a *sink*. Typically the outgoing interface is a dispinterface, so the sink must implement **IDispatch**. The source fires events by calling **IDispatch::Invoke** with the dispatch identifier (dispid) of the method.

To receive events:

-   Implement the outgoing interface.
-   Call the **IConnectionPointContainer::FindConnectionPoint** method to retrieve a connection point from the Video Control. Pass in the interface identifier (IID) of the outgoing interface. The **FindConnectionPoint** method returns a pointer to the **IConnectionPoint** interface.
-   Call the **IConnectionPoint::Advise** method to establish the connection.

The following code sets up the connection point between the client and the Video Control:


```C++
HRESULT hr;
DWORD dwCookie;
CComPtr<IMSVidCtl> m_pVideoControl; // Pointer to the Video Control.

// Query the Video Control for IConnectionPointContainer.
CComQIPtr<IConnectionPointContainer> pContainer(m_pVideoControl);
if (pContainer)  
{
    // Find the connection point.
    CComPtr<IConnectionPoint> pConnectPt;
    hr = pContainer->FindConnectionPoint(DIID__IMSVidCtlEvents, 
            &amp;pConnectPt);
    if (SUCCEEDED(hr))
    {
        // Get the IUnknown pointer of the event sink, which is
        // typically the client itself.
        CComQIPtr<IUknown> pUnk;
        this->QueryInterface(IID_IUnknown, (void**)&amp;pUnk);
        hr = pConnectPt->Advise(pUnk, &amp;dwCookie);
    }
}
```



The **Advise** method returns a token (also called a *cookie*) that identifies the connection. The source object continues to fire events until the sink breaks the connection. To break the connection, call the **IConnectionPoint::Unadvise** method and pass in the same token:


```C++
hr = pConnectPt->Unadvise(dwCookie);
```



 

 




