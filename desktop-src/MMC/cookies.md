---
title: Cookies
description: Shows how cookies can be used by a snap-in to share data objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3b48fb0b-d2c7-41e6-a5bf-277e6f92488b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- cookies MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cookies

Cookies are pointer-sized identifiers within an instance of a snap-in and are associated with a particular scope or result item. When inserting an item in the scope or result pane, a snap-in passes to MMC the value that will be used as the item's cookie value. The value is solely determined by the snap-in. MMC does not care whether the cookie is a pointer, an index, a hash, or any other type of reference. However, most snap-ins will use as cookies pointers to the internal C++ or COM objects that represent these items. When MMC needs a data object for a particular item, it uses the item's cookie value to uniquely identify the item.

**NULL** (0) is a special cookie value. MMC uses this cookie value to refer to the static node of a stand-alone snap-in. Because a stand-alone snap-in does not explicitly add the static node, MMC passes a **NULL** cookie value instead. A stand-alone snap-in should be able to handle **NULL** when MMC passes it a cookie value.

MMC passes the cookie of an item only to the snap-in that created that item. Extension snap-ins get a data object rather than a cookie. Most notifications also specify a data object rather than a cookie — even those notifications that are sent to the snap-in that inserted the item.

Because MMC usually identifies items with data objects rather than cookies, most snap-in developers implement a clipboard format that quickly retrieves the cookie from the data object. It is important that this clipboard format not be published or used by extension snap-ins, because the internal structure that the cookie points to is subject to change. Instead, the snap-in extended should publish other clipboard formats that provide the necessary information in a cleaner fashion.

 

 




