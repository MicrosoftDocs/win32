---
title: Collections and Groups
description: ADSI uses collection objects to represent any arbitrary set of items in a directory service that can be represented using the same data type.
ms.assetid: 03257cc9-f354-4e1c-8880-936a7acac3ef
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,using,collections and groups
- collections ADSI
- groups ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Collections and Groups

ADSI uses collection objects to represent any arbitrary set of items in a directory service that can be represented using the same data type. Collection objects are defined as a set of **VARIANT** values, representing any of the valid Automation data types. Collection objects can represent both persistent information such as access-control lists and volatile information such as print jobs in a print queue.

The standard COM convention for listing the contents of a collection (or container) object is to create an enumerator object that supports [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant), which has methods to step through the list of collection objects. The interfaces in ADSI that supply the **get\_\_NewEnum** method (note the two underscores) are [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer), [**IADsMembers**](/windows/desktop/api/Iads/nn-iads-iadsmembers) and [**IADsCollection**](/windows/desktop/api/Iads/nn-iads-iadscollection). ADSI also supplies the helper functions [**ADsBuildEnumerator**](/windows/desktop/api/Adshlp/nf-adshlp-adsbuildenumerator) and [**ADsEnumerateNext**](/windows/desktop/api/Adshlp/nf-adshlp-adsenumeratenext) for C and C++ programs to simplify enumeration. Automation clients use enumeration implicitly when they call **Next** in a **For** loop.

Groups are simply collections of objects supporting the [**IADsMembers**](/windows/desktop/api/Iads/nn-iads-iadsmembers) interface.

 

 