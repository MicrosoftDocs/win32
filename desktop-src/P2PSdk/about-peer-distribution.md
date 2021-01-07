---
description: The Peer Distribution API, which supports the Branch Cache feature in Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012 offers a set of platform APIs that can increase network responsiveness of centralized applications when accessed from remote offices and aid in reducing overall wide area network (WAN) utilization without interfering with the network security technologies.
ms.assetid: feb9666e-563a-49f4-ad1c-f166a0faff31
title: About Peer Distribution
ms.topic: article
ms.date: 05/31/2018
---

# About Peer Distribution

The Peer Distribution API, which supports the Branch Cache feature in Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012 offers a set of platform APIs that can increase network responsiveness of centralized applications when accessed from remote offices and aid in reducing overall wide area network (WAN) utilization without interfering with the network security technologies.

The Peer Distribution system offers a set of platform APIs utilized by both the publishers that provide digital content and consumers that request it. To easily differentiate these roles, it may be easier to think of the publisher in a server role and the consumer in a client role. That aside, it is important to remember that aside from these conceptual roles, the Peer Distribution service is a true peer system, as indicated by the ability for any Peer Distribution node to both publish and consume digital content. The Peer Distribution platform APIs are exposed to publishers and consumers by a Win32 import library (**PeerDist.Lib**).

The lifecycle of content supplied by a publisher and retrieved by a consumer with the Peer Distribution service is composed of the following operations:



|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Content Publication** | Publishing is done to produce a description of content termed **Content Information**, or **Content Info** for short. This Content Info can then be used by an instance of the Peer Distribution service to authenticate and rebuild the content. When content is published by an application into the Peer Distribution service, which is conceptually a server-side operation, that content becomes associated with the Publisher Identity, which is based on the SID of the user associated with the thread access token. This binding is done to limit access to content by unauthorized entities. However, it is important to note that access to the content information is equivalent to access to the content itself, as the content information can be used to obtain the content from peers or a hosted cache.<br/> There is a new version of the content information data structure in Windows 8; however, the previous version is still supported. To interoperate with Windows 7 clients, an administrator may configure the Peer Distribution service to use the previous version of the content information data structure.<br/> |
| **Content Retrieval**   | For a consumer to retrieve content from the Peer Distribution service, access must be provided to the published Content Info associated with that content. The Peer Distribution service used to publish the content can provide the associated Content Info. Once the consumer has the Content Info, other Peer Distribution APIs can be used to request content from the Peer Distribution service. The Peer Distribution service will attempt to retrieve the content from the local network. If the content is not available, the client application is responsible for retrieving the content from the source server.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Publication Removal** | For applications that have published content into the Peer Distribution service, the [**PeerDistServerUnpublish**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverunpublish) function has been provided to allow content to be unpublished. Once content has been unpublished, the local Peer Distribution service will no longer provide the content info associated with that content.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Asynchronous Completions

The Peer Distribution API supports an asynchronous API model, and as a result Peer Distribution APIs allow for the use of either I/O Completion Ports or Events as the signaling mechanisms for processing asynchronous Peer Distribution operation completions. For either mechanism, Peer Distribution uses an [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure. In general, Peer Distribution takes the ownership of an **OVERLAPPED** structure and any out parameters that the Client passes to asynchronous API functions. The Client must not access these resources until the particular asynchronous function completes. As soon as the asynchronous functions completes, the Peer Distribution service will no longer require access to these resources and they may be reused as the calling application sees fit.

There will not be any asynchronous completion if the function returns any error code other than **ERROR\_IO\_PENDING**. The return of a value other than **ERROR\_IO\_PENDING** means that the call has failed synchronously. If the Peer Distribution API returns **ERROR\_IO\_PENDING**, the caller must wait for asynchronous completion.

The error code of the asynchronous completion can be retrieved in one of two ways:

**I/O Completion Port Based Completion**

User invokes the I/O completion port mechanism by providing a completion port handle and completion key to the following API functions:

<dl>

[**PeerDistRegisterForStatusChangeNotification**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistregisterforstatuschangenotification)  
[**PeerDistServerPublishStream**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverpublishstream)  
[**PeerDistServerOpenContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserveropencontentinformation)  
[**PeerDistClientOpenContent**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientopencontent)  
</dl>

The User creates a completion port by calling [**CreateIoCompletionPort**](/windows/desktop/FileIO/createiocompletionport). This completion port handle can be simultaneously used for other asynchronous I/O operations as well as Peer Distribution specific operations.

The caller should use [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function to manage asynchronous completion. If the asynchronous operation fails the **GetQueuedCompletionStatus** function will return **FALSE** and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the appropriate error code. The caller should ignore all the fields of the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure if the error code is anything other than **ERROR\_SUCCESS**. The asynchronous operation succeeds if the **GetQueuedCompletionStatus** function returns **TRUE**.

For more information see [I/O Completion Ports](/windows/desktop/FileIO/i-o-completion-ports).

**Event Based Completion**

If the caller sets a valid Event handle to the *hEvent* field of [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure, Peer Distribution uses it to signal that the associated asynchronous I/O operation has completed.

A thread caller can manage overlapped operations by specifying a handle to the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure's manual-reset event object in one of the wait functions. After the Event is signaled the caller must call [**PeerGetOverlappedResult**](https://www.bing.com/search?q=**PeerGetOverlappedResult**) passing in the appropriate **OVERLAPPED** structure. **PeerGetOverlappedResult** will return **FALSE** and the caller must call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) in order to retrieve the error code. The caller should ignore all the fields of the **OVERLAPPED** structure if the error code is anything other than **ERROR\_SUCCESS**. The asynchronous operation succeeds if the **PeerGetOverlappedResult** function returns **TRUE**.

If the caller provides a completion port along with an event, the event will be used as the completion mechanism.

**Windows 7:** Use the [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) function instead of [**PeerGetOverlappedResult**](https://www.bing.com/search?q=**PeerGetOverlappedResult**).

## Related topics

<dl> <dt>

[Peer Distribution API Reference](peer-distribution-api-reference.md)
</dt> </dl>

 

