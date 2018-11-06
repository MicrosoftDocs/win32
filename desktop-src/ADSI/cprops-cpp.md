---
title: CPROPS.CPP
description: In the example provider component, an example of a property cache implementation can be found in cprops.cpp. Supported methods are listed in the following table.
ms.assetid: 51c9aa05-ca30-4d61-b3e3-d2f17a02b28f
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CPROPS.CPP

In the example provider component, an example of a property cache implementation can be found in cprops.cpp. Supported methods are listed in the following table.



| Method                                           | Description                                                                                                         |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **CPropertyCache::addproperty**                  | Extend the property cache by adding a new one.                                                                      |
| **CPropertyCache::updateproperty**               | Look up the property, free its contents, and use new values instead; then mark the cache changed for this property. |
| **CPropertyCache::findproperty**                 | Look up this property by name; save its index.                                                                      |
| **CPropertyCache::getproperty**                  | Find the property in the cache if available, otherwise call **GetInfo**. Set the index and copy in the new values.  |
| **CPropertyCache::putproperty**                  | Find the property. Free what was there and put in new values.                                                       |
| **CPropertyCache::CPropertyCache**               | Standard constructor.                                                                                               |
| **CPropertyCache::~CPropertyCache**              | Standard destructor.                                                                                                |
| **CPropertyCache::createpropertycache**          | Create the cache.                                                                                                   |
| **CPropertyCache::unboundgetproperty**           | Find the property in the cache and set it to these values.                                                          |
| **CPropertyCache::SampleDSMarshallProperties**   | Marshal property data and values.                                                                                   |
| **CPropertyCache::marshallproperty**             | Marshal a property.                                                                                                 |
| **CPropertyCache::SampleDSUnMarshallProperties** | Unmarshal property data and values.                                                                                 |
| **CPropertyCache::unmarshallproperty**           | Unmarshal a property.                                                                                               |



 

 

 




