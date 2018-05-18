---
title: WDS Transport Provider Functions
description: User-defined content providers can expose the following callback functions to the multicast server.
ms.assetid: '30ec1969-4e90-458e-8a9f-39a7bbf4cd79'
---

# WDS Transport Provider Functions

User-defined content providers can expose the following callback functions to the multicast server.



| Function                                                                               | Description                                                                                                             |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [*WdsTransportProviderCloseContent*](wdstransportproviderclosecontent.md)             | Closes a content stream specified by a handle.                                                                          |
| [*WdsTransportProviderCloseInstance*](wdstransportprovidercloseinstance.md)           | Closes an instance of a content provider specified by a handle.                                                         |
| [*WdsTransportProviderCompareContent*](wdstransportprovidercomparecontent.md)         | Compares a specified content name and instance to an open content stream to determine if they are the same.             |
| [*WdsTransportProviderCreateInstance*](wdstransportprovidercreateinstance.md)         | Opens a new instance of a content provider.                                                                             |
| [*WdsTransportProviderDumpState*](wdstransportproviderdumpstate.md)                   | Instructs the transport provider to print a summary of its state and any other relevant information to the tracing log. |
| [*WdsTransportProviderGetContentMetadata*](wdstransportprovidergetcontentmetadata.md) | Retrieves metadata for an open content stream.                                                                          |
| [*WdsTransportProviderGetContentSize*](wdstransportprovidergetcontentsize.md)         | Retrieves the size of an open content stream.                                                                           |
| [*WdsTransportProviderInitialize*](wdstransportproviderinitialize.md)                 | Initializes a content provider.                                                                                         |
| [*WdsTransportProviderOpenContent*](wdstransportprovideropencontent.md)               | Opens a new static view of a content stream.                                                                            |
| [*WdsTransportProviderReadContent*](wdstransportproviderreadcontent.md)               | Reads content from an open content stream.                                                                              |
| [*WdsTransportProviderRefreshSettings*](wdstransportproviderrefreshsettings.md)       | Instructs the transport provider to reread any relevant settings.                                                       |
| [*WdsTransportProviderShutdown*](wdstransportprovidershutdown.md)                     | Shutsdown the content provider.                                                                                         |
| [*WdsTransportProviderUserAccessCheck*](wdstransportprovideruseraccesscheck.md)       | Specifies access to a content stream based on a user's token.                                                           |



 

 

 




