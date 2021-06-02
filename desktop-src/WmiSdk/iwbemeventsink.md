---
description: Initiates communication with an event provider using a restricted set of queries.
ms.assetid: dd076dd0-ed39-47a2-86fb-a595baf3f464
ms.tgt_platform: multiple
title: IWbemEventSink interface (Wbemprov.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWbemEventSink
api_type: 
- COM
api_location: 
- Wbemsvc.dll
---

# IWbemEventSink interface

The **IWbemEventSink** interface initiates communication with an event provider using a restricted set of queries. This interface extends [**IWbemObjectSink**](iwbemobjectsink.md), providing new methods dealing with security and performance. For more information about using this interface, see [Writing an Event Provider](writing-an-event-provider.md) and [Securing WMI Events](securing-wmi-events.md).

## Members

The **IWbemEventSink** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWbemEventSink** interface has these methods.



| Method                                                                | Description                                                           |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**GetRestrictedSink**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-getrestrictedsink)         | Called by the consumer to set up restricted event queries.<br/> |
| [**IsActive**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-isactive)                           | Checks status of event sink.<br/>                               |
| [**SetBatchingParameters**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-setbatchingparameters) | Called by the consumer to set batching parameters.<br/>         |
| [**SetSinkSecurity**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-setsinksecurity)             | Used to update the security descriptor on an event sink.<br/>   |



 

## Remarks

When implementing an event subscription sink ([**IWbemObjectSink**](iwbemobjectsink.md) or **IWbemEventSink**), do not call into WMI from within the methods on the sink object. For example, calling [**IWbemServices::CancelAsyncCall**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-cancelasynccall) to cancel the sink from within an implementation of [**IWbemEventSink::SetSinkSecurity**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-setsinksecurity) can interfere with the WMI state. To cancel an event subscription, set a flag and call **IWbemServices::CancelAsyncCall** from another thread or object. For implementations that are not related to an event sink, such as object, enum, and query retrievals, you can call back into WMI.

Sink implementations should process the event notification within 100 MSEC because the WMI thread that delivers the event notification cannot do other work until the sink object has completed processing. If the notification requires a large amount of processing, the sink can use an internal queue for another thread to handle the processing.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                            |
| Header<br/>                   | <dl> <dt>Wbemprov.h (include Wbemidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Wbemuuid.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Wbemsvc.dll</dt> </dl>                    |



## See also

<dl> <dt>

[COM API for WMI](com-api-for-wmi.md)
</dt> </dl>

 

 




