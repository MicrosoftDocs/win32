---
title: Handling Events in C++
description: Handling Events in C++
ms.assetid: 5d9eb1c7-7022-4442-b67a-6a96fe5ce97f
keywords:
- Windows Media Player,C++
- Windows Media Player object model,C++
- object model,C++
- Windows Media Player Mobile,C++
- Windows Media Player ActiveX control,C++
- Windows Media Player Mobile ActiveX control,C++
- ActiveX control,C++
- C++ program embedding
- embedding,C++ programs
- Windows Media Player ActiveX control,event handling
- Windows Media Player Mobile ActiveX control,event handling
- ActiveX control,event handling
- events,C++
ms.topic: article
ms.date: 05/31/2018
---

# Handling Events in C++

You can receive events from Windows Media Player in two ways.

-   Through **IDispatch** by using the **\_WMPOCXEvents** interface. This is the interface to use for most embedding scenarios.
-   Through the **IWMPEvents** interface. This interface is available when your code is connected to the full mode Player, such as when remoting the Windows Media Player control or in a UI plug-in.

In each scenario, you start listening to events by using COM connection points.

The following example code uses three member variables:


```C++
CComPtr<IWMPPlayer>         m_spWMPPlayer;
CComPtr<IConnectionPoint>   m_spConnectionPoint;
DWORD                       m_dwAdviseCookie;

```



To retrieve a connection point, you first **QueryInterface** for the connection point container.


```C++
HRESULT  hr = S_OK;
// Smart pointer to IConnectionPointContainer
CComPtr<IConnectionPointContainer>  spConnectionContainer;

hr = m_spWMPPlayer->QueryInterface(&spConnectionContainer);

```



Next, request the connection point for the event interface you want to use. The following example code first attempts to use **IWMPEvents**. If that interface isn't available, it uses **\_WMPOCXEvents**.


```C++
// Test whether the control supports the IWMPEvents interface.
if(SUCCEEDED(hr))
{
    hr = spConnectionContainer->FindConnectionPoint(__uuidof(IWMPEvents), &m_spConnectionPoint);
    if (FAILED(hr))
    {
        // If not, try the _WMPOCXEvents interface, which uses IDispatch.
        hr = spConnectionContainer->FindConnectionPoint(__uuidof(_WMPOCXEvents), &m_spConnectionPoint);
    }
}

```



Finally, call **IConnectionPoint::Advise** to request events.


```C++
if(SUCCEEDED(hr))
{
    hr = m_spConnectionPoint->Advise(this, &m_dwAdviseCookie);
}

```



In the preceding example, the first parameter assumes that the calling class implements both **IWMPEvents** and **\_WMPOCXEvents**. The second parameter is a return value that you use to stop listening to events, such as when your program exits, using code similar to the following:


```C++
// Stop listening to events
if (m_spConnectionPoint)
{
    if (0 != m_dwAdviseCookie)
        m_spConnectionPoint->Unadvise(m_dwAdviseCookie);
        m_spConnectionPoint.Release();
}

```



Implementing the event handlers for **IWMPEvents** and **\_WMPOCXEvents** differs. For **IWMPEvents**, you must implement a function to handle every event defined by the interface, even if you don't intend to use the event.


```C++
// IWMPEvents methods
void STDMETHODCALLTYPE OpenStateChange( long NewState ){ return; }
void STDMETHODCALLTYPE PlayStateChange( long NewState ){ return; }
void STDMETHODCALLTYPE AudioLanguageChange( long LangID ){ return; }
// And so on...

```



To implement **\_WMPOCXEvents** handlers, you must use **IDispatch::Invoke**, which is a single event handler implementation for all the events happening on the **IDispatch** interface. This means that you can choose to handle only certain events and ignore others. The following example code shows a **\_WMPOCXEvents** handler, using **Invoke**, that handles only the **OpenStateChange** and **PlayStateChange** events:


```C++
HRESULT CMyClass::Invoke(
    DISPID  dispIdMember,      
    REFIID  riid,              
    LCID  lcid,                
    WORD  wFlags,              
    DISPPARAMS FAR*  pDispParams,  
    VARIANT FAR*  pVarResult,  
    EXCEPINFO FAR*  pExcepInfo,  
    unsigned int FAR*  puArgErr )
{
    if (!pDispParams)
        return E_POINTER;

    if (pDispParams->cNamedArgs != 0)
        return DISP_E_NONAMEDARGS;

    HRESULT hr = DISP_E_MEMBERNOTFOUND;

    switch (dispIdMember)
    {
        case DISPID_WMPCOREEVENT_OPENSTATECHANGE:
            OpenStateChange(pDispParams->rgvarg[0].lVal /* NewState */ );
            break;

        case DISPID_WMPCOREEVENT_PLAYSTATECHANGE:
            PlayStateChange(pDispParams->rgvarg[0].lVal /* NewState */);
            break;

        // Other cases can handle additional events by using DISPIDs.
    }

    return( hr );
}

```



In the preceding example code, each case simply calls through to the **IWMPEvents** handler for the corresponding event. If your code only handles **\_WMPOCXEvents**, you can simply call a custom function or handle the event inline after the **case** statement.

## Receiving Events from Windows Media Player 10 Mobile

The Windows Media Player 10 Mobile control only supports receiving certain events through **\_WMPOCXEvents** and **IWMPEvents**. For more information, please see the documentation for **IWMPEvents**.

## Samples

The Windows Media Player setup package installs a sample that demonstrates event handling. See the WMPHost sample for more information.

## Related topics

<dl> <dt>

[**Samples**](samples.md)
</dt> <dt>

[**Using the Windows Media Player Control in a C++ Program**](using-the-windows-media-player-control-in-a-c---program.md)
</dt> </dl>

 

 




