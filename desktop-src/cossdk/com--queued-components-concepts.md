---
description: COM+ Queued Components Concepts
ms.assetid: ff11e251-311f-4612-8f0d-a4cbc5b4d872
title: COM+ Queued Components Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Queued Components Concepts

Based on [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) services, the COM+ queued components service provides an easy way to invoke and execute components asynchronously. Processing can occur without regard to the availability or accessibility of either the sender or the receiver.

In COM terms, a *queue* is a storage area that saves messages for later retrieval. Queuing provides a mechanism for connectionless communication. That is, the sender and receiver are not connected directly and communicate only through queues. Queuing provides a way to hold the information until the receiver is ready to obtain it. The sender and receiver are indirectly communicating so that each can operate independently, unaffected by the other.

In the past, an in-depth knowledge of marshaling was necessary to queue, send, and receive asynchronous messages. Now, using method calls that are easily understood and used by component developers, the COM+ queued components service automatically marshals data in the form of a Message Queuing message. And because the queued components service offers built-in support for transactions, an inconsistent state cannot compromise data if a server failure occurs.

The following topics in this section contain background information about designing and writing queued components.



| Topic                                                                           | Description                                                                                                           |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [Benefits of Queued Processing](benefits-of-queued-processing.md)<br/>   | Describes the benefits of programming with COM+ queued components.<br/>                                         |
| [Queued Components Architecture](queued-components-architecture.md)<br/> | Describes the architecture of the COM+ queued components service.<br/>                                          |
| [Transactional Message Queuing](transactional-message-queuing.md)<br/>   | Describes how transactions are handled by the COM+ queued components service.<br/>                              |
| [Queued Components Security](queued-components-security.md)<br/>         | Describes the policy options for authentication of client messages and their implications.<br/>                 |
| [Developing Queued Components](developing-queued-components.md)<br/>     | Describes programming considerations when writing queuable components.<br/>                                     |
| [Queued Components Errors](queued-components-errors.md)<br/>             | Describes the most common types of errors you may encounter when using the COM+ queued components service.<br/> |



 

## Related topics

<dl> <dt>

[COM+ Queued Components Tasks](com--queued-components-tasks.md)
</dt> </dl>

 

 




