---
title: WDS Transport Provider Functions
description: User-defined content providers can expose the following callback functions to the multicast server.
ms.assetid: 30ec1969-4e90-458e-8a9f-39a7bbf4cd79
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WDS Transport Provider Functions

User-defined content providers can expose the following callback functions to the multicast server.



| Function                                                                               | Description                                                                                                             |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [*WdsTransportProviderCloseContent*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderclosecontent?branch=master)             | Closes a content stream specified by a handle.                                                                          |
| [*WdsTransportProviderCloseInstance*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovidercloseinstance?branch=master)           | Closes an instance of a content provider specified by a handle.                                                         |
| [*WdsTransportProviderCompareContent*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovidercomparecontent?branch=master)         | Compares a specified content name and instance to an open content stream to determine if they are the same.             |
| [*WdsTransportProviderCreateInstance*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovidercreateinstance?branch=master)         | Opens a new instance of a content provider.                                                                             |
| [*WdsTransportProviderDumpState*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderdumpstate?branch=master)                   | Instructs the transport provider to print a summary of its state and any other relevant information to the tracing log. |
| [*WdsTransportProviderGetContentMetadata*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovidergetcontentmetadata?branch=master) | Retrieves metadata for an open content stream.                                                                          |
| [*WdsTransportProviderGetContentSize*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovidergetcontentsize?branch=master)         | Retrieves the size of an open content stream.                                                                           |
| [*WdsTransportProviderInitialize*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderinitialize?branch=master)                 | Initializes a content provider.                                                                                         |
| [*WdsTransportProviderOpenContent*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovideropencontent?branch=master)               | Opens a new static view of a content stream.                                                                            |
| [*WdsTransportProviderReadContent*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderreadcontent?branch=master)               | Reads content from an open content stream.                                                                              |
| [*WdsTransportProviderRefreshSettings*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderrefreshsettings?branch=master)       | Instructs the transport provider to reread any relevant settings.                                                       |
| [*WdsTransportProviderShutdown*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovidershutdown?branch=master)                     | Shutsdown the content provider.                                                                                         |
| [*WdsTransportProviderUserAccessCheck*](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportprovideruseraccesscheck?branch=master)       | Specifies access to a content stream based on a user's token.                                                           |



 

 

 




