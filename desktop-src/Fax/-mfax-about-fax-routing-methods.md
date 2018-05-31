---
Description: A fax routing method is a procedure defined by a fax routing extension.
ms.assetid: 3da25944-514e-4a69-955f-90b10bd4f60b
title: About Fax Routing Methods
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Fax Routing Methods

A fax routing method is a procedure defined by a fax routing extension. Fax routing methods can include, but are not limited to, printing faxes, storing faxes, and manipulating received fax files. The fax service calls the fax routing methods, in order of priority, when the service receives a fax document.

A fax routing extension can support multiple fax routing methods, but the extension must export one uniquely named [**FaxRouteMethod**](-mfax-faxroutemethod.md) function for each routing method. For more information, see [Routing a Fax](-mfax-routing-a-fax.md).

A fax routing method can perform multiple operations; for example, the method can read the received fax file and convert it from a graphics file to an editable text file. A fax routing method cannot delete or modify the original Tagged Image File Format Class F (TIFF Class F) file. For more information about TIFF Class F files, see [Fax Image Format](-mfax-fax-image-format.md).

 

 



