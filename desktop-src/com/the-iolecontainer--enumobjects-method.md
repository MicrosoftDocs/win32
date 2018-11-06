---
title: The IOleContainer EnumObjects Method
description: The IOleContainer EnumObjects Method
ms.assetid: 29562d0e-dc8b-49cd-a58f-1f3125a438ed
ms.topic: article
ms.date: 05/31/2018
---

# The IOleContainer::EnumObjects Method

This method is used to enumerate over all the OLE objects contained in a document or form, returning an interface pointer for each OLE object. The container must return pointers to each OLE object that shares the same container. Nested forms or nested controls must also be enumerated.

Some containers implement extender controls, which wrap non-ActiveX controls, and then return pointers to these extender controls as a form is enumerated. This behavior enables ActiveX controls and ActiveX control containers to integrate well with non-ActiveX controls, and is thus recommended, but not required.

 

 




