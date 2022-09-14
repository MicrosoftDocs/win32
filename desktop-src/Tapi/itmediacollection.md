---
description: The ITMediaCollection interface provides access to the set of media information in an SDP (RFC 2327) conference description.
ms.assetid: a7e7a07d-239e-432e-9984-7763f11c59ce
title: ITMediaCollection interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMediaCollection interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITMediaCollection** interface provides access to the set of media information in an SDP (RFC 2327) conference description. Each Media description in the SDP is described by an [**ITMedia**](itmedia.md) interface. **ITMediaCollection** allows manipulation of the set of **ITMedia** information for the SDP, including:

-   Allows media access by index.
-   Enables creation and deletion of media.

The [**ITSdp::get\_MediaCollection**](itsdp-get-mediacollection.md) method creates the **ITMediaCollection** interface.

## Members

The **ITMediaCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITMediaCollection** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITMediaCollection** interface has these methods.



| Method                                                            | Description                                                            |
|:------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**Create**](itmediacollection-create.md)                        | Creates a new media with default properties and returns it.<br/> |
| [**Delete**](itmediacollection-delete.md)                        | Deletes the media corresponding to the specified index.<br/>     |
| [**get\_\_NewEnum**](itmediacollection-get--newenum.md)          | Returns an enumerator for the collection.<br/>                   |
| [**get\_Count**](itmediacollection-get-count.md)                 | Gets the number of media in the session.<br/>                    |
| [**get\_EnumerationIf**](itmediacollection-get-enumerationif.md) | Gets pointer to enumeration interface.<br/>                      |
| [**get\_Item**](itmediacollection-get-item.md)                   | Returns the media corresponding to the specified index.<br/>     |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

