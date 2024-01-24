---
description: The ITParticipant interface is implemented by the IPConf MSP. It allows an application to retrieve information on conference participants, and get pointers to the streams associated with those participants.
ms.assetid: 8c3edfc1-3165-48b7-9d83-8892c192498b
title: ITParticipant interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant interface

\[**ITParticipant** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITParticipant** interface is implemented by the [IPConf MSP](ipconf-msp.md). It allows an application to retrieve information on conference participants, and get pointers to the streams associated with those participants.

This interface is exposed on the call object when a call uses the IP Conferencing. A pointer can be obtained by calling **QueryInterface** using an [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo) pointer.

## Members

The **ITParticipant** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITParticipant** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITParticipant** interface has these methods.



| Method                                                                      | Description                                                                                                                                                             |
|:----------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumerateStreams**](itparticipant-enumeratestreams.md)                  | Enumerates streams associated with the current participant.<br/>                                                                                                  |
| [**get\_MediaTypes**](itparticipant-get-mediatypes.md)                     | Gets the [**media types**](tapimediatype--constants.md) associated with a participant.<br/>                                                                      |
| [**get\_ParticipantTypedInfo**](itparticipant-get-participanttypedinfo.md) | Gets a BSTR representation of the needed type of information, such as PTI\_EMAILADDRESS.<br/>                                                                     |
| [**get\_Status**](itparticipant-get-status.md)                             | Gets the status of the participant.<br/>                                                                                                                          |
| [**get\_Streams**](itparticipant-get-streams.md)                           | Creates a collection of streams associated with the current participant. Provided for Automation client applications, such as those written in Visual Basic.<br/> |
| [**put\_Status**](itparticipant-put-status.md)                             | Sets whether a stream associated with the participant is enabled.<br/>                                                                                            |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[IPConf MSP](ipconf-msp.md)
</dt> <dt>

[IPConf MSP Interfaces](ipconf-msp-interfaces.md)
</dt> <dt>

[**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo)
</dt> </dl>

 

