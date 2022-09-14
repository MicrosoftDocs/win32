---
title: The SetInfo Method
description: The IADs SetInfo method saves the current values for the properties for this Active Directory object from the property cache to the underlying directory store. This is analogous to flushing a buffer out to disk.
ms.assetid: e4152b3d-3a59-4f69-9765-03cdf6286459
ms.tgt_platform: multiple
keywords:
- SetInfo ADSI ,using
- properties ADSI ,save the current values for properties
ms.topic: article
ms.date: 05/31/2018
---

# The SetInfo Method

The [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method saves the current values for the properties for this Active Directory object from the property cache to the underlying directory store. This is analogous to flushing a buffer out to disk.

[**SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) updates objects that already exist in the directory, or create a new directory entry for newly created objects.

At the time of the [**SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) call, if any property cache values have been written with a [**PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) control code, such as ADS\_PROPERTY\_UPDATE or ADS\_PROPERTY\_CLEAR, then the appropriate requests are passed on to the underlying directory service.

 

 




