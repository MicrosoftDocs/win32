---
title: Collections and Groups
description: ADSI uses collection objects to represent any arbitrary set of items in a directory service that can be represented using the same data type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 03257cc9-f354-4e1c-8880-936a7acac3ef
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,using,collections and groups
- collections ADSI
- groups ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Collections and Groups

ADSI uses collection objects to represent any arbitrary set of items in a directory service that can be represented using the same data type. Collection objects are defined as a set of **VARIANT** values, representing any of the valid Automation data types. Collection objects can represent both persistent information such as access-control lists and volatile information such as print jobs in a print queue.

The standard COM convention for listing the contents of a collection (or container) object is to create an enumerator object that supports [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e), which has methods to step through the list of collection objects. The interfaces in ADSI that supply the **get\_\_NewEnum** method (note the two underscores) are [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master), [**IADsMembers**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master) and [**IADsCollection**](/windows/win32/Iads/nn-iads-iadscollection?branch=master). ADSI also supplies the helper functions [**ADsBuildEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsbuildenumerator?branch=master) and [**ADsEnumerateNext**](/windows/win32/Adshlp/nf-adshlp-adsenumeratenext?branch=master) for C and C++ programs to simplify enumeration. Automation clients use enumeration implicitly when they call **Next** in a **For** loop.

Groups are simply collections of objects supporting the [**IADsMembers**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master) interface.

 

 




