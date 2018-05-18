---
title: Using the Event Service
description: Using the Event Service
ms.assetid: '0e989af3-1378-4a15-b6be-df79512a702f'
---

# Using the Event Service

Windows 7 offers new features for defining custom events and event services for media graphs. The following new interfaces implement these features:



| Interface                                                            | Features                                                                                                                                                                                         |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IESEvent**](iesevent.md)                                         | Defines a generic event interface that can deliver and encapsulate events raised by devices in a media graph.                                                                                    |
| [**IESEvents**](iesevents.md)                                       | Defines event handling features for devices in a media graph. Devices register to receive specific types of events sent by other devices, and are required to handle only those types of events. |
| [**IESEventService**](ieseventservice.md)                           | Defines a custom event service that is attached to the media graph with the service id of **SID\_ESEventService**.                                                                               |
| [**IESEventServiceConfiguration**](ieseventserviceconfiguration.md) | Configures a custom event service.                                                                                                                                                               |



 

The rest of this document uses the term Event Service for a Windows event service that implements the [**IESEvent**](iesevent.md) and [**IESEvents**](iesevents.md) interfaces. Although the Event Service was initially developed to support the Protected Broadcast Driver Architecture (PBDA) in Windows 7, it is a generic event interface that can be used with non-PBDA media graphs, and non-PBDA events in Windows 7 implement these interfaces. For more information about PBDA, download the specification from <http://go.microsoft.com/fwlink/p/?linkid=132926>.

### Registering to Receive Events

An object that receives events from an Event Service must first register for the types of events it wants to receive. To register for events, the object must follow this procedure:

1.  Query the media graph object to obtain a pointer to the media graph's service provider object. A pointer to the **IServiceProvider** interface is returned in the second parameter of the **QueryInterface** call.
2.  Query the media graph's service provider object to obtain a pointer to the event service object. A pointer to [**IESEventService**](ieseventservice.md) interface is returned in the third parameter of the **QueryService** call.
3.  Use the [**IESEventService**](ieseventservice.md) pointer from step 2 to obtain a pointer to the connection point container object. A pointer to the **IConnectionPointContainer** interface is returned in the second parameter of the **QueryInterface** call.
4.  Use the **IConnectionPointContainer** pointer from step 3 to find a connection point for each event type that the object wants to receive. The event type is specified as the first argument to the **FindConnectionPoint** method. A pointer to the corresponding **IConnectionPoint** interface is returned in the second argument to **FindConnectionPoint**.
5.  Use the connection point pointer from step 4 to set up the standard COM advise mechanism, which notifies the object when the desired event is raised.

The following example shows how an object of class **CListener** would register to receive the [**OpenMMIEvent**](iesopenmmievent.md) event (error checking code omitted for brevity):


```C++
//
// Definitions of the event types that we are interested in.

// {85DAC915-E593-410d-8471-D6812105F28E}
const GUID EVENTTYPE_OpenMMI =
{ 0x85DAC915, 0xE593, 0x410d, { 0x84, 0x71, 0xD6, 0x81, 0x21, 0x05, 0xF2, 0x8E } };

//
// CListerner defines an object that receives IESEvent.
// This class must derive from IESEvents
//
class CListener :
   public CComObjectRootEx<CComMultiThreadModel>,
    public IESEvents
{
public:
    CListener();
    ~CListener();

BEGIN_COM_MAP(CListener)
   COM_INTERFACE_ENTRY_IID(IID_IESEvents, IESEvents)
END_COM_MAP()


    // Internal function to provide the object with the graph to listen to
    HRESULT StartListening (IFilterGraph* pGraph);

private:
    IFilterGraph*   m_pGraph;
    DWORD           m_dwOpenMMICookie;
 
    HRESULT RegisterForEvents (bool bListen);
};


HRESULT CListener::RegisterForEvents (bool bListen)
{
    //
    // Register with the graph to listen or stop listening to the events
    //
    HRESULT                     hr = S_OK;
    IServiceProvider*           pServiceProvider = NULL;
    IESEventService*            pEventService = NULL;
    IConnectionPointContainer*  pCPContainer = NULL;
    IConnectionPoint*           pOpenMMICP = NULL;

    //
    // Get the Eventing Service object from the graph's Service Provider.
    // This will succeed if the graph contain PBDA class driver filter.
    //
    hr = m_pGraph->QueryInterface (IID_IServiceProvider, (void**)&amp;pServiceProvider);

    if (SUCCEEDED(hr))
    {
        hr = pServiceProvider->QueryService (SID_ESEventService, IID_IESEventService, 
                (void**)&amp;pEventService);
    }

    //
    // Get the IConnectionPointContainer from the Eventing Service object
    //
    if (SUCCEEDED(hr))
    {
        hr = pEventService->QueryInterface (IID_IConnectionPointContainer, 
                (void**)&amp;pCPContainer);
    }

    //
    // Get the IConnectionPoint for the type of event that we're interested in.
    //
    if (SUCCEEDED(hr))
    {
        //
        // The trick here is to pass the EVENTTYPE_OpenMmi in the first parameter
        // instead of an interface IID. 
        //
        hr = pCPContainer->FindConnectionPoint (EVENTTYPE_OpenMMI, &amp;pOpenMMICP);
    }

    if (SUCCEEDED(hr))
    {
        if (bListen)
            hr = pOpenMMICP->Advise (static_cast< IESEvents* >(this), &amp;m_dwOpenMMICookie);
        else
            hr = pOpenMMICP->Unadvise (m_dwOpenMMICookie);
    }
    return hr;
}


```



Once you have the registration process defined, the object can start listening for registered events by calling the registration method. The following example shows how a CListener object would start listening for an [**OpenMMIEvent**](iesopenmmievent.md) event by calling the **RegisterForEvents** method defined in the previous example:


```C++
HRESULT CListener::StartListening (IFilterGraph* pGraph)
{
    pGraph->AddRef();
    m_pGraph = pGraph;

    //
    // Register to listen to the events
    //
    RegisterForEvents(true);

    return S_OK;
}

```



### Receiving and Handling Events

To handle events from the Event Service, an object must implement the [**IESEvents**](iesevents.md) interface, which defines a single event handler method named [**OnESEventReceived**](iesevents-oneseventreceived.md). The object must implement **OnESEventReceived** for each type of event it has registered to receive. The following example illustrates how the CListener object from the previous example would receive an [**OpenMMIEvent**](iesopenmmievent.md) event:


```C++
HRESULT CListener::OnESEventReceived(GUID guidEventType, IESEvent* pESEvent)
{
    //
    // When the Eventing Service dispatches OpenMMI events,
    // this function would receive them.
    //
    if (IsEqualGUID (guidEventType, EVENTTYPE_OpenMMI))
    {
        // 
        // Process OpenMMI event here.
        //
    } 
    return S_OK;
}
```



### Getting Data from an Event

To obtain data from an event, a receiving object must implement the [**IESEvent**](iesevent.md) interface. This interface defines the following methods for obtaining event data:



| Method                                          | Feature                                            |
|-------------------------------------------------|----------------------------------------------------|
| [**GetEventType**](iesevent-geteventtype.md)   | Returns a GUID that indicates the event type.      |
| [**GetData**](idvb-st-getdata.md)              | Returns a byte array that contains the event data. |
| [**GetStringData**](iesevent-getstringdata.md) | Gets the event data in Unicode string format.      |
| [**GetEventId**](iesevent-geteventid.md)       | Gets the unique identifier for the event.          |



 

The following example shows how an object would implement the [**IESEvent**](iesevent.md) interface to obtain data from an event of type **MyEvent**:


```C++
#include <windows.h>
#include <atlbase.h>
#include <atlcom.h>
#include <atlsafe.h>
#include <tuner.h>

//
// CMyEvent defines an object representing an event.
// This event is identified by event type guid.
//
// Note about thread model:
// The Eventing Service is running in multiple threaded apartment.
// If the event object is running in single-threaded apartment,
// make sure to provide appropriate COM interface marshaling.
//
// This example assumes it is running in a multithreaded apartment.
//

//
// Define an event type for this event
// {CC81F18F-3E14-4024-AB1F-E4DC159D6D00}
const GUID EVENTTYPE_MyEvent =
{ 0xcc81f18f, 0x3e14, 0x4024, { 0xab, 0x1f, 0xe4, 0xdc, 0x15, 0x9d, 0x6d, 0x00 } };

class CMyEvent :
    public CComObjectRootEx<CComMultiThreadModel>,
    public IESEvent
{
    CMyEvent();

BEGIN_COM_MAP(CMyEvent)
   COM_INTERFACE_ENTRY_IID(IID_IESEvent, IESEvent)
END_COM_MAP()

    // IESEvent interface
   HRESULT GetEventType (GUID* pguidEventType);
   HRESULT GetData (LPSAFEARRAY* pbData);
   HRESULT GetStringData (BSTR* pbstrData);
    HRESULT GetEventId (DWORD* pdwEventId);
    HRESULT SetCompletionStatus (DWORD dwResult);

private:
    WCHAR   m_data[16];
};

CMyEvent::CMyEvent()
{
    wcscpy_s (m_data, _countof (m_data), L"Example");
}

HRESULT CMyEvent::GetEventType(GUID* pguidEventType)
{
    //
    // Return event type of this event.
    //
    *pguidEventType = EVENTTYPE_MyEvent;
    return S_OK;
}

HRESULT CMyEvent::GetData (LPSAFEARRAY* pbData)
{
    //
    // Return the data associated with this event, if any.
    //
    CComSafeArray<BYTE> data (sizeof(m_data));
    BYTE*               pData   = (BYTE*) m_data;    
    
    for (int I = 0; I < sizeof(m_data); I++)
    {
        data[i] = pData[i];
    }

    *pbData = data.Detach();
    return S_OK;
}

HRESULT CMyEvent::GetStringData (BSTR* pbstrData)
{
    //
    // Return the string data associated with this event, if any.
    // This should be the same data as returned in GetData,
    // except using string representation.
    //
    CComBSTR    bstrData (m_data);

    *pbstrData = bstrData.Detach();
    return S_OK;
}

HRESULT CMyEvent::GetEventId (DWORD* pdwEventId)
{
    //
    // The event id is a PBDA concept.  See PBDA spec.
    // For this custom event, we don't need to supply this.
    //
    *pdwEventId = 0;
    return S_OK;
}

HRESULT CMyEvent::SetCompletionStatus (DWORD dwResult)
{
    //
    // The completion status is a PBDA concept.  See PBDA spec.
    // For this custom event, we don't need to do anything here.
    //
    return S_OK;
}

```



### Raising Event Service Events

An object that raises events in an Event Service must follow this procedure:

1.  Query the media graph object to obtain a pointer to the media graph's service provider object. A pointer to the **IServiceProvider** interface is returned in the second parameter of the **QueryInterface** call.
2.  Query the media graph's service provider object to obtain a pointer to the event service object. A pointer to the [**IESEventService**](ieseventservice.md) interface is returned in the third parameter of the **QueryService** call.
3.  Use the [**IESEventService**](ieseventservice.md) pointer from step 1 to call the [**FireESEvent**](ieseventservice-fireesevent.md) method and raise the desired event.

The following example shows how an object of class CMyEvent would raise a custom event of type **MyEvent**. Error checking and cleanup code are not included here.


```C++
//
// Example code to send an event through Eventing Service
//

#include <windows.h>
#include <atlbase.h>
#include <atlcom.h>
#include <atlsafe.h>
#include <tuner.h>

//
// CMyEvent defines an object representing an event.
// This event is identified by event type guid.
//
// Note about thread model:
// The Eventing Service is running in multiple threaded apartment.
// If the event object is running in single-threaded apartment,
// make sure to provide appropriate COM interface marshaling.
//
// This example assumes it is running in a multithreaded apartment.
//

//
// Define an event type for this event
// {CC81F18F-3E14-4024-AB1F-E4DC159D6D00}
const GUID EVENTTYPE_MyEvent =
{ 0xcc81f18f, 0x3e14, 0x4024, { 0xab, 0x1f, 0xe4, 0xdc, 0x15, 0x9d, 0x6d, 0x00 } };

class CMyEvent :
    public CComObjectRootEx<CComMultiThreadModel>,
    public IESEvent
{
    CMyEvent();

HRESULT CMyEvent::FireESEvent (IFilterGraph* pGraph)
{
    HRESULT             hr = S_OK;
    IServiceProvider*   pServiceProvider = NULL;
    IESEventService*    pEventService = NULL;

    //
    // Get the Eventing Service object from the graph's Service Provider.
    // This will succeed if the graph contain PBDA class driver filter.
    //
    hr = pGraph->QueryInterface (IID_IServiceProvider, (void**)&amp;pServiceProvider);

    if (SUCCEEDED(hr))
    {
        hr = pServiceProvider->QueryService (SID_ESEventService, IID_IESEventService, 
             (void**)&amp;pEventService);
    }

    if (SUCCEEDED(hr))
    {
        //
        // Now we send this event through the Eventing Service.
        // This is an asynchronous operation.  The call returns immediately.
        // The event is queued up to be actually sent in another thread.
        //
        hr  = pEventService->FireESEvent (static_cast< IESEvent* >(this));
    }

    return hr;
}
```



### Advanced Event Service Use

The Event Service allows you to define a custom event service to handle events that are sent by another event service. This process is known as *chaining* event services. The following process is used to define a custom event service and chain it to an existing Event Service:

1.  Query the media graph object that implements the event service to which you are chaining your custom event service, and obtain a pointer to the media graph's service provider object. A pointer to **IServiceProvider** interface is returned in the second parameter of the **QueryInterface** call.
2.  Instantiate an object that implements the [**IESEventService**](ieseventservice.md) interface for your custom event service. A pointer to the **IESEventService** interface for the custom event service is returned in the last parameter of the **CoCreateInstance** call that creates the custom event service object.
3.  Query the event service object you created in step 2 to obtain a pointer to the event service configuration object for your custom event service. A pointer to the [**IESEventServiceConfiguration**](ieseventservice.md) interface is returned in the second parameter of the **QueryInterface** call.
4.  Use the [**IESEventServiceConfiguration**](ieseventserviceconfiguration.md) pointer from step 3 to make the event service you are chaining to the parent or owner of your custom event service.
    -   Use the [**IESEventServiceConfiguration::SetParent**](ieseventserviceconfiguration-setparent.md) method to make the chained-to event service the parent. The *parent* event service can pass events to your custom event service so that you can pass them to your clients.
    -   If you make an object an *owner* of your custom event service, the owner object can examine data from any events it passes to your custom event service. Use the [**IESEventServiceConfiguration::SetOwner**](ieseventserviceconfiguration-setparent.md) method to make the object an owner. The object must implement the [**IESEvents**](iesevents.md) interface so that it can handle events that the parent event service passes to it.

A parent event service calls the [**IESEvents::OnESEventReceived**](iesevents-oneseventreceived.md) method of the owner object to allow the owner to examine the events. The can do can do any or any combination of the following:

-   Handle the event itself.
-   Pass the event to your custom event system without changes for handling. The owner returns "S\_OK" from the [**OnESEventReceived**](iesevents-oneseventreceived.md) method to accomplish this.
-   Modify the event or raise a different event before passing it to your custom event system.
-   Prevent the event from passing through to your custom event system. The owner returns "S\_FALSE" from the [**OnESEventReceived**](iesevents-oneseventreceived.md) method to accomplish this.

The following example shows how to implement a simple custom event service named **MyEventService**, and set the filter graph's event service as the parent and set itself as the owner of the service. Error checking and cleanup code are not included here.


```C++
//
// Example code to create a new Eventing Service
// and chain with existing one.
//

#include <windows.h>
#include <atlbase.h>
#include <atlcom.h>
#include <tuner.h>

class MyEventService :
    public CComObjectRootEx<CComMultiThreadModel>,
    public IESEvents
{
public:

BEGIN_COM_MAP(MyEventService)
   COM_INTERFACE_ENTRY_IID(IID_IESEvents, IESEvents)
END_COM_MAP()

    // IESEvents
   HRESULT OnESEventReceived(GUID guidEventType, IESEvent* pESEvent);

    // Initialize the object
    HRESULT Initialize (IFilterGraph* pGraph);

private:
    CComPtr<IESEventService> m_pESEventService;
};

HRESULT MyEventService::Initialize(IFilterGraph* pGraph)
{
    //
    // Initialize the object by creating a new Eventing Service
    // and chain with the graph's Eventing Service.
    //

    HRESULT                         hr = S_OK;
    IServiceProvider*               pServiceProvider = NULL;
    IESEventService*                pGraphEventService = NULL;
    IESEventServiceConfiguration*   pEventServiceConfig = NULL;

    //
    // Get the Eventing Service object from the graph's Service Provider.
    // This will succeed if the graph contain PBDA class driver filter.
    //
    hr = pGraph->QueryInterface (IID_IServiceProvider, (void**)&amp;pServiceProvider);

    if (SUCCEEDED(hr))
    {
        hr = pServiceProvider->QueryService (SID_ESEventService, IID_IESEventService, 
                 (void**)&amp;pGraphEventService);
    }

    //
    // Create own Eventing Service
    //
    if (SUCCEEDED(hr))
    {
        hr = CoCreateInstance(CLSID_ESEventService,
                                0,
                                CLSCTX_INPROC_SERVER,
                                IID_IESEventService,
                                (LPVOID*) &amp;m_pESEventService );
    }

    //
    // Configure parent and owner
    //
    if (SUCCEEDED(hr))
    {
        hr = m_pESEventService->QueryInterface (IID_IESEventServiceConfiguration, 
              (void**)&amp;pEventServiceConfig);
    }

    if (SUCCEEDED(hr))
    {
        //
        // When setting parent service, this will allow all events
        // from the parent to be sent through this service.  So
        // the clients to this service will get the event as well.
        //
        hr = pEventServiceConfig->SetParent (pGraphEventService);
    }

    if (SUCCEEDED(hr))
    {
        //
        // If the owner is set, then this service is allowed to
        // examine the event before sending it to the clients.
        //
        hr = pEventServiceConfig->SetOwner (static_cast< IESEvents* >(this));
    }

    return hr;
}
```



 

 




