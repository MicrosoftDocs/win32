---
description: The summary information stream contains information about the package that can be viewed through Microsoft Windows Explorer.
ms.assetid: b909955f-ddd6-4cf1-8e86-fcf89be80b41
title: About the Summary Information Stream
ms.topic: article
ms.date: 05/31/2018
---

# About the Summary Information Stream

The summary information stream contains information about the package that can be viewed through Microsoft Windows Explorer. This information is accessible through the **IStream** interface. It is up to the author to provide the values for each of these properties.

The summary information stream uses COM to provide structured storage of databases. COM supports the concept of structured storage accessible through the **IStream** interface. Structured storage, in turn, supports the concept of property sets as a flexible method for serializing almost any information. The COM specification defines a single standard property set, summary information, which is used to populate property sheets viewable from Windows Explorer. So, information stored in the summary information stream can be viewed by users when they right-click an installer database or transform and select [Properties](about-properties.md).

For a list of the summary property set see [Summary Information Stream Property Set](summary-information-stream-property-set.md).

For brief descriptions of the Summary Information properties used with databases, transforms, and patches, see [Summary Property Descriptions](summary-property-descriptions.md).

 

 



