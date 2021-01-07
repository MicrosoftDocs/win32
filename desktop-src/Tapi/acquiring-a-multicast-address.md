---
description: The following code fragment illustrates how to request and set a multicast address for a conference.
ms.assetid: faff57a9-88b3-45ce-bf9e-3f7087dfd1fd
title: Acquiring a Multicast Address
ms.topic: article
ms.date: 05/31/2018
---

# Acquiring a Multicast Address

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The following code fragment illustrates how to request and set a multicast address for a conference.

For the sake of simplicity, this fragment shows the assignment of one multicast address to one media item. In actuality, the selection of a scope, the multicast address request, and the assignment will be performed for every media item involved in the conference.

This fragment assumes that [connecting to an ILS server](connecting-to-an-ils-server.md) has already been performed. The operations shown here would be performed in the "Modify the settings if necessary" section of [Creating a Conference Announcement](creating-a-conference-announcement.md).


```C++
// If ( hr != S_OK ) process the error here.
```



## Related topics

<dl> <dt>

[Multicast COM Interfaces](multicast-com-interfaces.md)
</dt> <dt>

[**IMcastAddressAllocation**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastaddressallocation)
</dt> <dt>

[**IMcastScope**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastscope)
</dt> <dt>

[**IMcastLeaseInfo**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastleaseinfo)
</dt> <dt>

[**IEnumMcastScope**](/windows/desktop/api/Mdhcp/nn-mdhcp-ienummcastscope)
</dt> <dt>

[**ITConferenceBlob**](itconferenceblob.md)
</dt> <dt>

[**ITSdp**](itsdp.md)
</dt> <dt>

[**ITMediaCollection**](itmediacollection.md)
</dt> <dt>

[**IEnumBstr**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumbstr)
</dt> <dt>

[**ITMedia**](itmedia.md)
</dt> <dt>

[**ITConnection**](itconnection.md)
</dt> </dl>

 

 



