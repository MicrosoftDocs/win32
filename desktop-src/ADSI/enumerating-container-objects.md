---
title: Enumerating Container Objects
description: By convention, all items in an enumeration in ADSI must be of the same Automation data type. For example, an enumeration should not return some items as a VARIANT of type VT\_I4 and others as a VARIANT of type VT\_BSTR.
ms.assetid: 155caa67-05db-432b-b813-0d891a502301
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Container Objects

By convention, all items in an enumeration in ADSI must be of the same Automation data type. For example, an enumeration should not return some items as a **VARIANT** of type **VT\_I4** and others as a **VARIANT** of type **VT\_BSTR**.

To enumerate a list of items that an object maintains, a client requests the creation of an enumeration object for the specific type of information being listed. In ADSI, the client may list the objects in namespace objects, generic container objects, collection objects, member objects, or schema objects. ADSI provides a filter that can be set and modified to limit the matches in any enumeration though the [**IADsContainer.Filter**](iadscontainer-property-methods.md) property. Examples of implementations of enumerator objects can be found in the example provider component code for the following ADs container objects.



| Object type         | code         |
|---------------------|--------------|
| Generic Container   | cenumobj.cpp |
| Namespace Container | cenumns.cpp  |
| Schema Container    | cenumsch.cpp |



 

For client-side information, see [Collections and Groups](collections-and-groups.md).

 

 




