---
title: Synchronization Points
description: When property sets are supported on the same object as IStorage, it is important to be aware of synchronization points between the base storage and the property storage.
ms.assetid: 34cc4338-b29f-43f9-946d-14b2b235ccec
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Points

When property sets are supported on the same object as [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage), it is important to be aware of synchronization points between the base storage and the property storage.

The property set storage holds the property set stream in an internal buffer until that buffer is committed through the [**IPropertyStorage::Commit**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-commit) method. This is true whether [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) was opened in transacted mode or in direct mode.

 

 




