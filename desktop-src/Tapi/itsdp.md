---
description: The ITSdp interface provides methods for the manipulation of a Session Descriptor Protocol (SDP, see RFC 2327) conference blob component.
ms.assetid: 77c1e302-6290-4eeb-b7c9-462a13b29dcd
title: ITSdp interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITSdp** interface provides methods for the manipulation of a Session Descriptor Protocol (SDP, see RFC 2327) conference blob component. It provides the following functionality:

-   Provides access to some of the properties that are common to all the media. These include attributes pertaining to the creator's personal information, session description, and address type information.
-   Provides the starting point for accessing the time and media collections through properties.

The **ITSdp** interface is created by calling **QueryInterface** on [**ITConferenceBlob**](itconferenceblob.md).

## Members

The **ITSdp** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITSdp** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITSdp** interface has these methods.



| Method                                                    | Description                                                                                         |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**get\_Description**](itsdp-get-description.md)         | Gets the session description.<br/>                                                            |
| [**get\_IsValid**](itsdp-get-isvalid.md)                 | Validates the SDP blob for structure and field values.<br/>                                   |
| [**get\_MachineAddress**](itsdp-get-machineaddress.md)   | Gets the machine address of the originating host.<br/>                                        |
| [**get\_MediaCollection**](itsdp-get-mediacollection.md) | Gets pointer to [**ITMediaCollection**](itmediacollection.md) interface for conference.<br/> |
| [**get\_Name**](itsdp-get-name.md)                       | Gets the session name.<br/>                                                                   |
| [**get\_Originator**](itsdp-get-originator.md)           | Gets conference originator.<br/>                                                              |
| [**get\_ProtocolVersion**](itsdp-get-protocolversion.md) | Gets the SDP protocol version.<br/>                                                           |
| [**get\_SessionId**](itsdp-get-sessionid.md)             | Gets the 32-bit NTP (Network Time Protocol) value that serves as the session identifier.<br/> |
| [**get\_SessionVersion**](itsdp-get-sessionversion.md)   | Gets the 32-bit (ideally NTP) value that serves as the session version.<br/>                  |
| [**get\_TimeCollection**](itsdp-get-timecollection.md)   | Gets pointer to [**ITTimeCollection**](ittimecollection.md) interface for conference.<br/>   |
| [**get\_Url**](itsdp-get-url.md)                         | Gets the URL.<br/>                                                                            |
| [**GetEmailNames**](itsdp-getemailnames.md)              | Gets array of e-mail names and addresses associated with conference blob.<br/>                |
| [**GetPhoneNumbers**](itsdp-getphonenumbers.md)          | Gets the phone numbers.<br/>                                                                  |
| [**put\_Description**](itsdp-put-description.md)         | Sets the session description.<br/>                                                            |
| [**put\_MachineAddress**](itsdp-put-machineaddress.md)   | Sets the machine address of the originating host.<br/>                                        |
| [**put\_Name**](itsdp-put-name.md)                       | Sets the session name.<br/>                                                                   |
| [**put\_Originator**](itsdp-put-originator.md)           | Gets conference originator.<br/>                                                              |
| [**put\_SessionVersion**](itsdp-put-sessionversion.md)   | Sets session version.<br/>                                                                    |
| [**put\_Url**](itsdp-put-url.md)                         | Sets the URL.<br/>                                                                            |
| [**SetEmailNames**](itsdp-setemailnames.md)              | Sets array of email names and addresses associated with conference blob.<br/>                 |
| [**SetPhoneNumbers**](itsdp-setphonenumbers.md)          | Sets the phone numbers.<br/>                                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

