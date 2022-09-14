---
description: Manipulates a textual conference description.
ms.assetid: b9ce61d1-3fc5-4963-8d2f-586a4b6a159d
title: ITConferenceBlob interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConferenceBlob interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITConferenceBlob** interface manipulates a textual conference description. The interface is intended to be independent of the format and syntax of the conference description. To manipulate specific aspects of the conference description, the application must query for another interface. Currently, only SDP conference descriptions are supported; the application must use **QueryInterface** for [**ITSdp**](itsdp.md) to access the various fields of the SDP conference description. The **ITConferenceBlob** interface is created by calling **QueryInterface** on [**ITDirectoryObject**](/windows/desktop/api/Rend/nn-rend-itdirectoryobject).

## Members

The **ITConferenceBlob** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITConferenceBlob** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITConferenceBlob** interface has these methods.



| Method                                                             | Description                                                                                                                                   |
|:-------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_CharacterSet**](itconferenceblob-get-characterset.md)     | Gets the [**BLOB\_CHARACTER\_SET**](blob-character-set.md) indicator of whether blob characters are in ASCII, Unicode, and so on.<br/> |
| [**get\_ConferenceBlob**](itconferenceblob-get-conferenceblob.md) | Gets a pointer to the conference blob.<br/>                                                                                             |
| [**Init**](itconferenceblob-init.md)                              | Initializes the conference blob.<br/>                                                                                                   |
| [**SetConferenceBlob**](itconferenceblob-setconferenceblob.md)    | Commits changes to the conference blob.<br/>                                                                                            |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

