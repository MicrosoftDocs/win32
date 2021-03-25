---
description: The ITTime interface is a provider-specific interface for a Session Descriptor Protocol (SDP) conference blob object.
ms.assetid: '24d33259-dcbe-47e4-9c71-fcc25f6e9a76'
title: ITTime interface (Sdpblb.h)
ms.topic: interface
ms.date: 05/31/2018
---

# ITTime interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITTime** interface is a provider-specific interface for a Session Descriptor Protocol (SDP) conference blob object. It provides access to a set of activation times for the session. The [**IEnumTime::Next**](ienumtime-next.md) and [**ITTimeCollection::Create**](ittimecollection-create.md) methods create the **ITTime** interface.

## Members

The **ITTime** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITTime** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITTime** interface has these methods.



| Method                                         | Description                                                                 |
|:-----------------------------------------------|:----------------------------------------------------------------------------|
| [**get\_StartTime**](ittime-get-starttime.md) | Gets the 32-bit NTP (Network Time Protocol) starting time value.<br/> |
| [**get\_StopTime**](ittime-get-stoptime.md)   | Gets the NTP ending time value.<br/>                                  |
| [**put\_StartTime**](ittime-put-starttime.md) | Sets the 32-bit NTP starting time value.<br/>                         |
| [**put\_StopTime**](ittime-put-stoptime.md)   | Sets the NTP ending time value.<br/>                                  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

