---
title: Collections and Groups
description: ADSI uses collection objects to represent any arbitrary set of items in a directory service that can be represented using the same data type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '03257cc9-f354-4e1c-8880-936a7acac3ef'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADSI ADSI ,using,collections and groups", "collections ADSI", "groups ADSI"]
---

# Collections and Groups

ADSI uses collection objects to represent any arbitrary set of items in a directory service that can be represented using the same data type. Collection objects are defined as a set of **VARIANT** values, representing any of the valid Automation data types. Collection objects can represent both persistent information such as access-control lists and volatile information such as print jobs in a print queue.

The standard COM convention for listing the contents of a collection (or container) object is to create an enumerator object that supports [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e), which has methods to step through the list of collection objects. The interfaces in ADSI that supply the **get\_\_NewEnum** method (note the two underscores) are [**IADsContainer**](iadscontainer.md), [**IADsMembers**](iadsmembers.md) and [**IADsCollection**](iadscollection.md). ADSI also supplies the helper functions [**ADsBuildEnumerator**](adsbuildenumerator.md) and [**ADsEnumerateNext**](adsenumeratenext.md) for C and C++ programs to simplify enumeration. Automation clients use enumeration implicitly when they call **Next** in a **For** loop.

Groups are simply collections of objects supporting the [**IADsMembers**](iadsmembers.md) interface.

 

 




