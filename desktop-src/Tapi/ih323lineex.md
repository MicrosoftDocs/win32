---
description: The IH323LineEx interface is implemented by the H323 MSP and is available only on H.323 address objects. This interface exposes methods that enable creation and manipulation of terminals that can communicate between H323 and SDP clients.
ms.assetid: 2ab57343-8cf5-4af2-91f7-46926cfce6dd
title: IH323LineEx interface (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IH323LineEx interface

\[**IH323LineEx** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **IH323LineEx** interface is implemented by the [H323 MSP](h323-msp.md) and is available only on H.323 address objects. This interface exposes methods that enable creation and manipulation of terminals that can communicate between H323 and SDP clients.

> [!Note]  
> All methods in this interface should be called only after registering for incoming calls on this address.

 

## Members

The **IH323LineEx** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IH323LineEx** also has these types of members:

-   [Methods](#methods)

### Methods

The **IH323LineEx** interface has these methods.



| Method                                                                                 | Description                                                              |
|:---------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**SetAlias**](ih323lineex-setalias.md)                                               | Configures a default H.323 alias for the address.<br/>             |
| [**SetDefaultCapabilityPreferrence**](ih323lineex-setdefaultcapabilitypreferrence.md) | Configures the preference weighting for default capabilities.<br/> |
| [**SetExternalT120Address**](ih323lineex-setexternalt120address.md)                   | Configures an external T.120 address for data exchange.<br/>       |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[H323 MSP](h323-msp.md)
</dt> </dl>

 

