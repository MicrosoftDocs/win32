---
description: The ITMedia interface is a representation of media in a Session Descriptor Protocol (SDP, see RFC 2327).
ms.assetid: f5cd7971-3456-4e2f-8808-deb16678099a
title: ITMedia interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMedia interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITMedia** interface is a representation of media in a Session Descriptor Protocol (SDP, see RFC 2327). This interface exports methods to get and set basic media properties, such as type. The [**ITMediaCollection::get\_Item**](itmediacollection-get-item.md) and [**ITMediaCollection::Create**](itmediacollection-create.md) methods create the **ITMedia** interface.

## Members

The **ITMedia** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITMedia** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITMedia** interface has these methods.



| Method                                                          | Description                                                                                      |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**get\_FormatCodes**](itmedia-get-formatcodes.md)             | Gets the list of media payload format codes.<br/>                                          |
| [**get\_MediaName**](itmedia-get-medianame.md)                 | Gets the media name.<br/>                                                                  |
| [**get\_MediaTitle**](itmedia-get-mediatitle.md)               | Gets the media title.<br/>                                                                 |
| [**get\_NumPorts**](itmedia-get-numports.md)                   | Gets the number of ports needed for the session.<br/>                                      |
| [**get\_StartPort**](itmedia-get-startport.md)                 | Gets the 16-bit port value for the first port.<br/>                                        |
| [**get\_TransportProtocol**](itmedia-get-transportprotocol.md) | Gets the transport protocol.<br/>                                                          |
| [**put\_FormatCodes**](itmedia-put-formatcodes.md)             | Sets the list of media payload format codes.<br/>                                          |
| [**put\_MediaName**](itmedia-put-medianame.md)                 | Sets the media name.<br/>                                                                  |
| [**put\_MediaTitle**](itmedia-put-mediatitle.md)               | Sets the media title.<br/>                                                                 |
| [**put\_TransportProtocol**](itmedia-put-transportprotocol.md) | Sets the transport protocol.<br/>                                                          |
| [**SetPortInfo**](itmedia-setportinfo.md)                      | Sets the 16-bit port value for the first port and number of ports needed for session.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> <dt>

[**ITMediaCollection**](itmediacollection.md)
</dt> <dt>

[**ITSDP**](itsdp.md)
</dt> <dt>

[**ITTime**](ittime.md)
</dt> </dl>

 

