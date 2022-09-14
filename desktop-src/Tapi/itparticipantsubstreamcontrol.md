---
description: The ITParticipantSubStreamControl interface is implemented by the IPConf MSP.
ms.assetid: d5af0fb1-af18-4efb-9b68-1fa60c1272f6
title: ITParticipantSubStreamControl interface (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantSubStreamControl interface

\[**ITParticipantSubStreamControl** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITParticipantSubStreamControl** interface is implemented by the IPConf MSP. This interface is exposed on the call object. This interface provides methods that allow an application to either discover or control the matching of substream to participant. The **ITParticipantSubStreamControl** interface is created by calling **QueryInterface** on [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo).

## Members

The **ITParticipantSubStreamControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITParticipantSubStreamControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITParticipantSubStreamControl** interface has these methods.



| Method                                                                                              | Description                                                     |
|:----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| [**get\_ParticipantFromSubStream**](itparticipantsubstreamcontrol-get-participantfromsubstream.md) | Gets participants associated with a given substream.<br/> |
| [**get\_SubStreamFromParticipant**](itparticipantsubstreamcontrol-get-substreamfromparticipant.md) | Gets substreams associated with a given participant.<br/> |
| [**SwitchTerminalToSubStream**](itparticipantsubstreamcontrol-switchterminaltosubstream.md)        | Sets a participant on a substream.<br/>                   |



 

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
</dt> </dl>

 

