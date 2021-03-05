---
description: The ITConnection interface functionality is shown below.
ms.assetid: 44dc39cf-3222-41ed-b29c-df2d32615500
title: ITConnection interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITConnection** interface provides the following functionality:

-   Provides access to the address and time to live (TTL) information for the session.
-   Provides access to the bandwidth information.
-   Enables manipulation of the encryption key.

The **ITConnection** interface is created by calling **QueryInterface** on [**ITConferenceBlob**](itconferenceblob.md).

## Members

The **ITConnection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITConnection** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITConnection** interface has these methods.



| Method                                                               | Description                                                                                                                                    |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_AddressType**](itconnection-get-addresstype.md)             | Gets the address type.<br/>                                                                                                              |
| [**get\_Bandwidth**](itconnection-get-bandwidth.md)                 | Gets bandwidth value.<br/>                                                                                                               |
| [**get\_BandwidthModifier**](itconnection-get-bandwidthmodifier.md) | Gets the bandwidth modifier.<br/>                                                                                                        |
| [**get\_NetworkType**](itconnection-get-networktype.md)             | Gets the network type.<br/>                                                                                                              |
| [**get\_NumAddresses**](itconnection-get-numaddresses.md)           | Gets the number of addresses to be used for the session.<br/>                                                                            |
| [**get\_StartAddress**](itconnection-get-startaddress.md)           | Gets the first address to be used for the session.<br/>                                                                                  |
| [**get\_Ttl**](itconnection-get-ttl.md)                             | Gets the [*time to live*](t-tapgloss.md) (TTL) scope for transmissions on the addresses.<br/> |
| [**GetEncryptionKey**](itconnection-getencryptionkey.md)            | Gets the encryption key.<br/>                                                                                                            |
| [**put\_AddressType**](itconnection-put-addresstype.md)             | Sets the address type.<br/>                                                                                                              |
| [**put\_NetworkType**](itconnection-put-networktype.md)             | Sets the network type.<br/>                                                                                                              |
| [**SetAddressInfo**](itconnection-setaddressinfo.md)                | Sets address information.<br/>                                                                                                           |
| [**SetBandwidthInfo**](itconnection-setbandwidthinfo.md)            | Sets the bandwidth value.<br/>                                                                                                           |
| [**SetEncryptionKey**](itconnection-setencryptionkey.md)            | Sets the encryption key needed to decrypt the session or an indication to a mechanism to obtain a usable key by external means.<br/>     |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

