---
description: The ITParticipantEvent interface contains methods that retrieve the description of participant events.
ms.assetid: 1199ec91-ee06-4e6c-8d8f-1585a3da3db0
title: ITParticipantEvent interface (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantEvent interface

\[**ITParticipantEvent** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITParticipantEvent** interface contains methods that retrieve the description of participant events. When the application's implementation of the [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event) method indicates a [**TAPI\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-tapi_event) equal to **TE\_PRIVATE**, the method's *pEvent* parameter is an **IDispatch** pointer for the **ITParticipantEvent** interface. The methods of this interface can be used to retrieve information concerning a participant change that has occurred.

> [!Note]  
> You must call the [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method and set an event filter mask that includes the **TE\_PRIVATE** event to enable reception of participant events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events. For more information, see the [Events](events.md) overview.

 

## Members

The **ITParticipantEvent** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITParticipantEvent** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITParticipantEvent** interface has these methods.



| Method                                                         | Description                                                                                                                                     |
|:---------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_Event**](itparticipantevent-get-event.md)             | Gets the [**PARTICIPANT\_EVENT**](participant-event.md) descriptor of the event.<br/>                                                    |
| [**get\_Participant**](itparticipantevent-get-participant.md) | Gets a pointer to an array of [**ITParticipant**](itparticipant.md) interfaces representing the participants involved in the event.<br/> |
| [**get\_SubStream**](itparticipantevent-get-substream.md)     | Gets a pointer to an array of [**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream) interfaces representing the substreams involved in the event.<br/>       |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipant**](itparticipant.md)
</dt> <dt>

[**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream)
</dt> <dt>

[**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo)
</dt> <dt>

[**PARTICIPANT\_EVENT**](participant-event.md)
</dt> <dt>

[**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event)
</dt> <dt>

[**TAPI\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-tapi_event)
</dt> <dt>

[Register Events code snippet](register-events.md)
</dt> </dl>

 

