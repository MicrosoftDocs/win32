---
title: Synchronization Points
description: When property sets are supported on the same object as IStorage, it is important to be aware of synchronization points between the base storage and the property storage.
ms.assetid: '34cc4338-b29f-43f9-946d-14b2b235ccec'
---

# Synchronization Points

When property sets are supported on the same object as [**IStorage**](istorage.md), it is important to be aware of synchronization points between the base storage and the property storage.

The property set storage holds the property set stream in an internal buffer until that buffer is committed through the [**IPropertyStorage::Commit**](ipropertystorage-commit.md) method. This is true whether [**IPropertyStorage**](ipropertystorage.md) was opened in transacted mode or in direct mode.

 

 




