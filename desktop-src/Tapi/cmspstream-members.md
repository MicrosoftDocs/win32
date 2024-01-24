---
description: The following list contains the CMSPStream members.
ms.assetid: 792a29ac-ebbb-4bb2-bebf-fbf870b18e84
title: CMSPStream Members
ms.topic: article
ms.date: 05/31/2018
---

# CMSPStream Members



| Member type                     | Name                | Description                                                                                                                                |
|---------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| IUnknown                        | \*m\_pFTM           | Pointer to the free threaded marshaller.                                                                                                   |
| DWORD                           | m\_dwState          | The current state of the stream.                                                                                                           |
| HANDLE                          | m\_hAddress         | The address on which this stream is being used.                                                                                            |
| DWORD                           | m\_dwMediaType      | The [**media type**](tapimediatype--constants.md) of this stream (audio, video, etc.).                                                    |
| TERMINAL\_DIRECTION             | m\_Direction        | The [**direction**](/windows/desktop/api/Tapi3if/ne-tapi3if-terminal_direction) of this stream (incoming or outgoing).                                                         |
| CMSPCallBase                    | \*m\_pMSPCall       | Pointer to the call object.                                                                                                                |
| IGraphBuilder                   | \*m\_pIGraphBuilder | Pointer to graph object interfaces.                                                                                                        |
| IMediaControl                   | \*m\_pIMediaControl | Pointer to the media control interface.                                                                                                    |
| CMSPArray <ITTerminal \*> | m\_Terminals        | The list of terminals on the stream.                                                                                                       |
| CMSPCritSection                 | m\_lock             | The lock that protects the stream object. The stream object should never acquire the lock and then call an MSPCall method that might lock. |



 

## Related topics

<dl> <dt>

[**CMSPStream**](/windows/desktop/api/Mspstrm/nl-mspstrm-cmspstream)
</dt> </dl>

 

 



