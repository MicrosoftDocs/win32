---
title: Internet-Aware Objects
description: Internet-Aware Objects
ms.assetid: a8228431-5a07-4816-938d-c789ab6a8eaa
ms.topic: article
ms.date: 05/31/2018
---

# Internet-Aware Objects

There are certain categories identified to cover the persistency interfaces; these have been identified as a result of defining how controls function across the Internet. A container that does not support the full range of persistency interfaces should ensure that it does not host a control that requires a combination of interfaces that it does not support.

The following tables describe the meaning for various categories as both implemented and required categories.



| Required Categories                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CATID\_PersistsToMoniker, CATID\_PersistsToStreamInit, CATID\_PersisitsToStream, CATID\_PersistsToStorage, CATID\_PersistsToMemory, CATID\_PersistsToFile, CATID\_PersistsToPropertyBag<br/> | Each of these categories is mutually exclusive and only used when an object supports only one persistence mechanism at all (hence the mutual exclusion). Containers that do not support the persistence mechanism described by one of these categories should prevent themselves from creating any objects of classes so marked.<br/> |
| CATID\_RequiresDataPathHost<br/>                                                                                                                                                             | The object requires the ability to save data to one or more paths and requires container involvement, therefore requiring container support for [**IBindHost**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775076(v=vs.85)).<br/>                                                                                                                                  |



 



| Implemented Categories                                                                                                                                                                            | Description                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| CATID\_PersistsToMoniker, CATID\_PersistsToStreamInit, CATID\_PersistsToStream, CATID\_PersistsToStorage, CATID\_PersistsToMemory, CATID\_PersistsToFile, CATID\_PersistsToPropertyBag<br/> | Object supports the corresponding IPersist\* mechanism for the category.<br/> |



 

The following table provides the exact CATIDs assigned to each category:



| Category                                | CATID                                           |
|-----------------------------------------|-------------------------------------------------|
| CATID\_RequiresDataPathHost<br/>  | 0de86a50-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToMoniker <br/>    | 0de86a51-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToStorage <br/>    | 0de86a52-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToStreamInit <br/> | 0de86a53-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToStream <br/>     | 0de86a54-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToMemory <br/>     | 0de86a55-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToFile <br/>       | 0de86a56-2baa-11cf-a229-00aa003d7352<br/> |
| CATID\_PersistsToPropertyBag<br/> | 0de86a57-2baa-11cf-a229-00aa003d7352<br/> |



 

## Related topics

<dl> <dt>

[Component Categories](component-categories.md)
</dt> </dl>

 

