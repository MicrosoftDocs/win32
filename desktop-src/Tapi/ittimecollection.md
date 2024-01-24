---
description: The ITTimeCollection interface is a provider-specific interface for the Session Descriptor Protocol (SDP) conference blob object.
ms.assetid: 6309e9f2-8a73-4d42-ae0a-2165352d6244
title: ITTimeCollection interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITTimeCollection interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITTimeCollection** interface is a provider-specific interface for the Session Descriptor Protocol (SDP) conference blob object. This interface allows access to [**ITTime**](ittime.md) interfaces by index, and also enable the creation and deletion of time components. The [**ITSdp::get\_TimeCollection**](itsdp-get-timecollection.md) method creates the **ITTimeCollection** interface.

## Members

The **ITTimeCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITTimeCollection** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITTimeCollection** interface has these methods.



| Method                                                           | Description                                                                                                           |
|:-----------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**Create**](ittimecollection-create.md)                        | Creates an [**ITTime**](ittime.md) component.<br/>                                                             |
| [**Delete**](ittimecollection-delete.md)                        | Deletes an [**ITTime**](ittime.md) component.<br/>                                                             |
| [**get\_\_NewEnum**](ittimecollection-get--newenum.md)          | Returns an enumerator for the collection.<br/>                                                                  |
| [**get\_Count**](ittimecollection-get-count.md)                 | Gets number of items in collection.<br/>                                                                        |
| [**get\_EnumerationIf**](ittimecollection-get-enumerationif.md) | Returns the [**IEnumTime**](ienumtime.md) enumeration interface that enumerates [**ITTime**](ittime.md).<br/> |
| [**get\_Item**](ittimecollection-get-item.md)                   | Given an index, returns an item in the collection.<br/>                                                         |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

