---
title: Synchronization Points
description: When property sets are supported on the same object as IStorage, it is important to be aware of synchronization points between the base storage and the property storage.
ms.assetid: 34cc4338-b29f-43f9-946d-14b2b235ccec
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Synchronization Points

When property sets are supported on the same object as [**IStorage**](/windows/win32/Objidl/nn-objidl-istorage?branch=master), it is important to be aware of synchronization points between the base storage and the property storage.

The property set storage holds the property set stream in an internal buffer until that buffer is committed through the [**IPropertyStorage::Commit**](/windows/win32/Propidl/nf-propidl-ipropertystorage-commit?branch=master) method. This is true whether [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) was opened in transacted mode or in direct mode.

 

 




