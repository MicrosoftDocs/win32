---
description: Developing Queued Components
ms.assetid: 867b7512-82ad-4877-8675-aa2d7e62ff8a
title: Developing Queued Components
ms.topic: article
ms.date: 05/31/2018
---

# Developing Queued Components

The COM+ queued components service requires all application methods to contain only \[in\] parameters, with no return values. Because the server object is not necessarily available when the client makes the call, server results can be returned by sending a message that creates another object. In this way, two-way communication occurs not in every case but only when it is required, by a series of one-way messages between objects.

To use the COM+ queued components service, you must have the [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) service already installed. Message Queuing is not installed automatically. Message Queuing must be selected during the operating system setup or by using **Add/Remove programs**. An internal Message Queuing certificate is created automatically at logon.

The topics described in the following table provide additional considerations for more specialized situations.



| Topic                                                                                           | Description                                                                                            |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [Passing Objects as Parameter](passing-objects-as-parameters.md)s<br/>                   | Describes how to pass objects as \[in\] parameters to queued components.<br/>                    |
| [Security Limitations in Workgroup Mode](security-limitations-in-workgroup-mode.md)<br/> | Describes limitations on the use of Message Queuing authentication in workgroup mode.<br/>       |
| [Threading Considerations](threading-considerations.md)<br/>                             | Describes specific concerns related to passing recorder interface pointers between threads.<br/> |
| [Receiving a Response](receiving-a-response.md)<br/>                                     | Describes how to construct a response to a queued component call.<br/>                           |



 

 

 




