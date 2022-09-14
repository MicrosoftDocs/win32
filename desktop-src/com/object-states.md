---
title: Object States
description: Object States
ms.assetid: 8ebef6d6-7a2f-4b95-91ca-999646cde82d
ms.topic: article
ms.date: 05/31/2018
---

# Object States

A compound object exists in one of three states: passive, loaded, or running. A compound-document object's state describes the relationship between the object in its container and the application responsible for its creation. The following table summarizes these states.



| Object state       | Description                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Passive<br/> | The compound-document object exists only in storage, either on disk or in a database. In this state, the object is unavailable for viewing or editing.<br/>                                                                                                                                                                                                                                   |
| Loaded<br/>  | The object's data structures created by the object handler are in the container's memory. The container has established communication with the object handler and there is cached presentation data available for rendering the object. Calls are processed by the object handler. This state, because of its low overhead, is used when a user is simply viewing or printing an object.<br/> |
| Running<br/> | The objects that control remoting have been created and the OLE server application is running. The object's interfaces are accessible, and the container can receive notification of changes. In this state, an end user can edit or otherwise manipulate the object.<br/>                                                                                                                    |



 

For more information, see the following topics:

-   [Entering the Loaded State](entering-the-loaded-state.md)
-   [Entering the Running State](entering-the-running-state.md)
-   [Entering the Passive State](entering-the-passive-state.md)

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 





