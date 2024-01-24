---
description: A physical consumer is a COM object that implements the IWbemUnboundObjectSink interface.
ms.assetid: 497457dc-61ca-4527-89fd-2af0383de5e9
ms.tgt_platform: multiple
title: Implementing a Physical Consumer
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Physical Consumer

A physical consumer is a COM object that implements the [**IWbemUnboundObjectSink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemunboundobjectsink) interface. WMI loads your physical consumer and passes events through **IWbemUnboundObjectSink** in response to one or more events, as defined by the associated logical consumer. Permanent consumers have special security requirements. For more information, see [Securing WMI Events](securing-wmi-events.md).

The following procedure describes how to implement a physical consumer for a permanent event consumer.

**To implement a physical consumer for a permanent event consumer**

1.  Create a COM object.

    You must implement a physical consumer as a local or remote server using the COM protocol.

2.  Determine if you want to support synchronous or asynchronous event notification.

    With asynchronous event notification, the sending thread is unrelated to the receiving thread. Therefore, neither WMI nor the event provider gets blocked while WMI delivers a notification to any consumer registered to receive the event. The disadvantage to asynchronous delivery is that a context switch occurs between the time the provider produces the event and the time the consumer receives the event. For more information about working asynchronously, see the [COM Fundamentals](../com/guide.md) topic in the COM section of the Microsoft Windows Software Development Kit (SDK). For more information about context switches, see the [Context Switches](../procthread/context-switches.md) topic in the DLLs, Processes, and Threads section of the Windows SDK.

    > [!Note]  
    > Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

     

    With synchronous notification, WMI delivers the notification on the same thread that the event provider used to deliver the event to WMI. In this case, when an event provider sends a notification, the event provider is blocked by WMI until WMI delivers the notification. Only if your consumer is extremely fast and can process an event in 100 microseconds or less should you consider supporting synchronous notification. Synchronous consumers that take too long to process events can seriously slow the delivery of events to all other consumers. Furthermore, they can inadvertently block the provider. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md).

3.  Implement the [**IWbemUnboundObjectSink::IndicateToConsumer**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemunboundobjectsink-indicatetoconsumer) function.

    WMI uses the [**IndicateToConsumer**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemunboundobjectsink-indicatetoconsumer) function to pass the necessary pointers and events to your physical consumer for both synchronous and asynchronous communications. Your implementation of **IndicateToConsumer** should contain all of the necessary code to respond to an event.

    Unlike a temporary event consumer, you do not need to call the [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator) interface to contact WMI. Instead, WMI locates a pointer to your consumer through the event consumer provider. For more information, see [Writing an Event Consumer Provider](writing-an-event-consumer-provider.md).

    However, if you wish to call back into WMI, use the [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator) and [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interfaces. The traditional method for connecting to WMI is during the initialization process of your COM object. For more information, see [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md).

    If you implement your physical consumer as an in-process COM server and connect to WMI separately from the initialization process, you must use the **CLSID\_WbemAdministrativeLocator** class identifier to access the [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator) interface in the call to [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance).

    The following example shows how to use the **CLSID\_WbemAdministrativeLocator** class identifier to access the [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator) interface.

    ```C++
    IWbemLocator *pLoc = 0;

    DWORD dwRes = CoCreateInstance(CLSID_WbemAdministrativeLocator, 0, 
        CLSCTX_INPROC_SERVER, IID_IWbemLocator, (LPVOID *) &pLoc);
    ```

    

    The [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator) interface obtains the initial namespace pointer to WMI on a particular host computer. Failure to use the **CLSID\_WbemAdministrativeLocator** identifier in the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) call results in an "access denied" error.

    Under usual circumstances, WMI delivers asynchronous events to the client one at a time. However, if a client cannot receive asynchronous event notifications as fast as the events arrive, WMI starts to automatically batch events into a single call. Automatic batching helps if the round-trip times are a problem, as is often the case in high-throughput scenarios. However, batching does not improve system performance if the client or the network bandwidth are at fault.

 

 
