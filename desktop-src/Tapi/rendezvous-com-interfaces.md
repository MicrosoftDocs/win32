---
description: The following table lists COM objects and interfaces associated with the Rendezvous conferencing controls.
ms.assetid: d9634586-8315-46d3-9ffc-bfa9a4d7738e
title: Rendezvous COM Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Rendezvous COM Interfaces

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The following table lists COM objects and interfaces associated with the Rendezvous conferencing controls.

For additional information on the Component Object Model (COM), please refer to the relevant sections in the Platform Software Development Kit (SDK).



| Interfaces                                                         | Description                                                                                                               |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**IEnumDialableAddrs**](/windows/desktop/api/Rend/nn-rend-ienumdialableaddrs)                   | Enumerates the dialable addresses available in the current directory.                                                     |
| [**IEnumDirectory**](/windows/desktop/api/Rend/nn-rend-ienumdirectory)                           | Enumerates [**ITDirectory**](/windows/desktop/api/Rend/nn-rend-itdirectory) objects.                                                                    |
| [**IEnumDirectoryObject**](/windows/desktop/api/Rend/nn-rend-ienumdirectoryobject)               | Enumerates [**ITDirectoryObject**](/windows/desktop/api/Rend/nn-rend-itdirectoryobject) objects.                                                        |
| [**IEnumMcastScope**](/windows/desktop/api/Mdhcp/nn-mdhcp-ienummcastscope)                         | Enumerates [**IMcastScope**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastscope) objects.                                                                    |
| [**IEnumMedia**](ienummedia.md)                                   | Enumerates [**ITMedia**](itmedia.md) objects.                                                                            |
| [**IEnumTime**](ienumtime.md)                                     | Enumerates [**ITTime**](ittime.md) objects.                                                                              |
| [**IMcastAddressAllocation**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastaddressallocation)         | Main interface for COM wrapper of multicast address allocation.                                                           |
| [**IMcastLeaseInfo**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastleaseinfo)                         | Provides methods to retrieve and set address lease information.                                                           |
| [**IMcastScope**](/windows/desktop/api/Mdhcp/nn-mdhcp-imcastscope)                                 | Encapsulates all the properties of a multicast scope and provides methods to get information about the scope.             |
| [**ITAttributeList**](itattributelist.md)                         | Allows getting and setting of uninterpreted attributes.                                                                   |
| [**ITConferenceBlob**](itconferenceblob.md)                       | Provides access to provider-specific conference information.                                                              |
| [**ITConnection**](itconnection.md)                               | Provides methods to manipulate connection factors such as conference address, scope, and bandwidth.                       |
| [**ITDirectory**](/windows/desktop/api/Rend/nn-rend-itdirectory)                                 | Gets and sets directory information, and provides access to a particular directory object.                                |
| [**ITDirectoryObject**](/windows/desktop/api/Rend/nn-rend-itdirectoryobject)                     | Gets and sets generic information for a conference or user within a directory.                                            |
| [**ITDirectoryObjectConference**](/windows/desktop/api/Rend/nn-rend-itdirectoryobjectconference) | Gets and sets generic information specific to a conference, such as start and stop times.                                 |
| [**ITDirectoryObjectUser**](/windows/desktop/api/Rend/nn-rend-itdirectoryobjectuser)             | Gets and sets generic information specific to a user, such as the name of a computer that is the user's primary IP phone. |
| [**ITILSConfig**](/windows/desktop/api/Rend/nn-rend-itilsconfig)                                 | Gets and sets information specific to the server of a given ILS directory.                                                |
| [**ITMedia**](itmedia.md)                                         | Gets and sets basic media properties such as the media name and transport protocol.                                       |
| [**ITMediaCollection**](itmediacollection.md)                     | Allows media access by index. Enables creation and deletion of media.                                                     |
| [**ITRendezvous**](/windows/desktop/api/Rend/nn-rend-itrendezvous)                               | Main interface for the Rendezvous control.                                                                                |
| [**ITSdp**](itsdp.md)                                             | Manipulates the SDP (Session Description Protocol) blob. Reference: RFC 2327.                                             |
| [**ITTime**](ittime.md)                                           | Provides access to a set of activation times for the session.                                                             |
| [**ITTimeCollection**](ittimecollection.md)                       | Allows time-component access by index. Enables creation and deletion of time components.                                  |



 

 

 



