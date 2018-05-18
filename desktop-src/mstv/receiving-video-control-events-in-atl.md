---
title: Receiving Video Control Events in ATL
description: Receiving Video Control Events in ATL
ms.assetid: 'cd62980f-5142-4805-9fc2-b2d272b91c5c'
---

# Receiving Video Control Events in ATL

This topic applies to Windows XP or later.

The Video Control sends events to the client through a dispinterface, [**\_IMSVidCtlEvents**](-imsvidctlevents.md). In ATL, you can create a dispinterface event sink by deriving from the **IDispEventImpl** or **IDispEventSimpleImpl** class template. One advantage of these classes is that you do not have to implement methods for all of the events. Instead, you can implement just the ones that you are interested in receiving.

This section gives a brief summary of this process. For details, consult the ATL documentation. The example uses **IDispEventSimpleImpl** to catch two events from the Video Control, [**\_IMSVidCtlEvents::Click**](-imsvidctlevents-click.md) and [**\_IMSVidCtlEvents::StateChange**](-imsvidctlevents-statechange.md).

First, include **IDispEventSimpleImpl** the class template in your client's inheritance list:


```C++
class ATL_NO_VTABLE CMyContainer :
    /* ... */
    public IDispEventSimpleImpl<IDC_MSVIDCTL1, CMyContainer, 
        &amp;__uuidof(_IMSVidCtlEvents)>
```



The first parameter is the resource ID of the video control in your form. The second parameter is the name of your composite control class. The third parameter is the IID of the event interface.

Next, define variables of type **\_ATL\_FUNC\_INFO** to hold the type information for the events you want to support. Declare the variables as `extern` in your header file:


```C++
/* In your header file: */
extern _ATL_FUNC_INFO OnClickInfo;       // Click event.
extern _ATL_FUNC_INFO OnStateChangeInfo; // StateChange event.

/* In your source file: */
_ATL_FUNC_INFO OnClickInfo = {CC_STDCALL, VT_EMPTY, 0};
_ATL_FUNC_INFO OnStateChangeInfo = {CC_STDCALL, VT_EMPTY, 2, { VT_I4, VT_I4} };
```



Each **\_ATL\_FUNCT\_INFO** variable specifies type information for one method in the event interface. The information consists of the calling convention (always CC\_STDCALL); the return type; the number of parameters; and an array of types, one for each parameter.

Now add entries for the two events in the event sink map:


```C++
BEGIN_SINK_MAP(CMyContainer)
   SINK_ENTRY_INFO(0, __uuidof(_IMSVidCtlEvents),
       DISPID_CLICK, OnClick, &amp;OnClickInfo)
   SINK_ENTRY_INFO(0, __uuidof(_IMSVidCtlEvents), 
       dispidStateChange, OnStateChange, &amp;OnStateChangeInfo)
END_SINK_MAP()
```



Define the event handler methods in your composite control class:


```C++
void __stdcall OnStateChange(MSVidCtlStateList PrevState, MSVidCtlStateList CurrState)
{
     // Call an application-defined function to update the UI.
     MyUpdateState(PrevState, CurrState);
}

void __stdcall OnClick()
{
     // Call an application-defined function to update the UI. 
     MyHandleClick();
}
```



ATL automatically sets up the connection when it shows the window, and automatically releases the connection when it unloads the control.

**Dual Interface Events**

Other Video Control objects, such as devices and features, send events through dual interfaces rather than dispinterfaces. (A *dispinterface* is invoked only through the **IDispatch::Invoke** method; it does not use a vtable. A *dual interface* can be invoked either through the **Invoke** method or through the vtable.)

In ATL, you can use the **IDispatchImpl** class template to handle dual interface events. The following discussion describes how to receive file playback events from the [MSVidFilePlaybackDevice](msvidfileplaybackdevice.md) object, using the [**IMSVidFilePlaybackEvent**](imsvidfileplaybackevent.md) interface.

First, add the **IDispatchImpl** class to your inheritance list:


```C++
    public IDispatchImpl<
       IMSVidFilePlaybackEvent,  // The event interface we're sinking.
       &amp;__uuidof(IMSVidPlaybackEvent), // The IID of the interface. 
       &amp;LIBID_MSVidCtlLib, /*wMajor =*/ 1, /*wMinor =*/ 0  // Typelib
    >
```



Add the **IMSVidFilePlaybackEvent** interface to your component's COM map:


```C++
BEGIN_COM_MAP(CMyControl)
    /* ... */
    COM_INTERFACE_ENTRY(IMSVidFilePlaybackEvent)
    /* ... */
END_COM_MAP()
```



If the COM map already has an entry for **IDispatch**, this change may cause a compile error similar to the following:


```C++
    error C2594: 'static_cast' : ambiguous conversions from
    'CMyControl::_ComMapClass *' to 'IDispatch *'
```



This error occurs if your control inherits **IDispatch** through more than one interface. You can fix this by using the **COM\_INTERFACE\_ENTRY2** macro to select one of the inheritance branches:


```C++
    COM_INTERFACE_ENTRY2(IDispatch, IMSVidFilePlaybackEvent)
```



Now implement the methods that are defined by the event interface. (You do not have to implement the **IDispatch** or **IUnknown** methods.) In the case of **IMSVidFilePlaybackEvent**, the interface defines one event, **EndOfMedia**.


```C++
STDMETHODIMP EndOfMedia(IMSVidPlayback *pPlayback)
{ 
    /* Perform any actions. */
    return S_OK;
}
```



To receive events, call the **AtlAdvise** function on the object that fires the events.


```C++
// Class member variables
CComPtr<IMSVidFilePlayback> m_pFilePlayback;
DWORD m_dwFileSinkCP; // Holds the connection point cookie.

// Here is the code to sink the events. First, check whether the
// MSVidFilePlaybackDevice object is the active input. If it is, you
// can query it for IMSVidFilePlayback.
CComPtr<IMSVidInputDevice> pInputDevice;
HRESULT hr = pVidControl->get_InputActive(&amp;pInputDevice);
if (SUCCEEDED(hr))
{
    m_pFilePlayback = pInputDevice; // Implicit QueryInterface.
    if (m_pFilePlayback)
    {
        // Query ourselves for the IUnknown interface.
        CComPtr<IUnknown> pUnk;
        this->QueryInterface(IID_IUnknown, (void**)&amp;pUnk);
        // Establish the connection point.
        hr = AtlAdvise(m_pFilePlayback, pUnk,
            __uuidof(IMSVidFilePlaybackEvent), &amp;m_dwFileSinkCP);
    }
}
```



Before you release the object, call **AtlUnadvise** to release the connection point:


```C++
if (m_pFilePlayback)
{
    AtlUnadvise(m_pFilePlayback, 
        __uuidof(IMSVidFilePlaybackEvent), m_dwFileSinkCP);
    m_pFilePlayback.Release();
}
```



 

 




