---
Description: The event registration process take place when the terminal is selected by a stream.
ms.assetid: 03854b38-4dba-480e-b931-34299d04c551
title: Registering for Pluggable Terminal Events
ms.topic: article
ms.date: 05/31/2018
---

# Registering for Pluggable Terminal Events

The event registration process take place when the terminal is selected by a stream. In the terminal application's implementation of the [**SelectTerminal**](https://msdn.microsoft.com/en-us/library/ms732429(v=VS.85).aspx) method, we can use the [**ITTerminal**](https://msdn.microsoft.com/en-us/library/ms732646(v=VS.85).aspx) interface of the terminal that was attached to the stream, and call **QueryInterface** to find [**ITPluggableTerminalEventSinkRegistration**](/windows/desktop/api/msp/nn-msp-itpluggableterminaleventsinkregistration).

``` syntax
HRESULT hr = E_FAIL;
ITPluggableTerminalEventSinkRegistration* pEventRegistration = NULL;
hr = pTerminal->QueryInterface( 
    IID_ITPluggableTerminalEventSinkRegistration,
    (void**)& pEventRegistration
);
```

If the **QueryInterface** call succeeds, we can call the [**RegisterSink**](/windows/desktop/api/msp/nf-msp-itpluggableterminaleventsinkregistration-registersink) method. For this purpose, we should create an object that implements the [**ITPluggableTerminalEventSink**](/windows/desktop/api/msp/nn-msp-itpluggableterminaleventsink) interface. We pass this interface as a parameter of the **RegisterSink** method.

``` syntax
ITPluggableTerminalEventSink*    pEventSink;

HRESULT hr = CreateEventSink( &pEventSink);
// If (hr != S_OK) process the error here. 

hr = pEventRegistration->RegisterSink( pEventSink );
// If (hr != S_OK) process the error here. 
```

The terminal that implements the [**ITPluggableTerminalEventSinkRegistration**](/windows/desktop/api/msp/nn-msp-itpluggableterminaleventsinkregistration) call will store the interface. The pointer will be used when the terminal will fire an event.

The event sink can be unregistered using [**UnregisterSink**](/windows/desktop/api/msp/nf-msp-itpluggableterminaleventsinkregistration-unregistersink).

``` syntax
hr = pEventRegistration->UnregisterSink();
// If (hr != S_OK) process the error here.
```

 

 



