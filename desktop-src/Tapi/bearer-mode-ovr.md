---
Description: The bearer mode corresponds to the quality of transmission requested from the network for establishing a call.
ms.assetid: 5276e1e7-7a91-4b74-b8c2-c0c7cebb203f
title: Bearer Mode
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Bearer Mode

The [**bearer mode**](https://msdn.microsoft.com/en-us/library/ms735508(v=VS.85).aspx) corresponds to the quality of transmission requested from the network for establishing a call. It is important to keep the concept of bearer mode separate from that of [**media type**](tapimediatype--constants.md). As an example, the analog telephone network (PSTN) provides only a 3.1 kHz voice-grade bearer mode but calls using it can support media types such as voice, fax, or data modem.

The bearer mode of a call is specified when the call is set up, or is provided when the call is offered. With line devices able to represent channel pools, it is possible for a service provider to allow calls to be established with wider bandwidth.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineSetCallParams**](https://msdn.microsoft.com/en-us/library/ms736086(v=VS.85).aspx), [**lineGetCallInfo**](https://msdn.microsoft.com/en-us/library/ms735720(v=VS.85).aspx), **dwBearerMode** member of [**LINECALLINFO**](https://msdn.microsoft.com/en-us/library/ms735527(v=VS.85).aspx).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong), [**ITCallInfo::put\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-put_callinfolong), **CIL\_BEARERMODE** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long).

**TSPI:** See [**LINE\_CALLINFO**](https://msdn.microsoft.com/library/ms725218) message, with *dwParam1* set to LINECALLINFOSTATE\_BEARERMODE.

 

 



