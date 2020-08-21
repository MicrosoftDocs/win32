---
title: CENUMOBJ.CPP
description: In the example provider component, the enumeration of a container object uses the routines, from cenumobj.cpp, listed in the following table.
ms.assetid: 7166230d-0bf8-4f7d-9781-72f125a3dd21
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CENUMOBJ.CPP

In the example provider component, the enumeration of a container object uses the routines, from cenumobj.cpp, listed in the following table.



| Method                                                 | Description                                                                                                                                                           |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CSampleDSGenObjectEnum::Create**                     | Create an object to enable enumeration of generic Active Directory objects.                                                                                           |
| **CSampleDSGenObjectEnum::CSampleDSGenObjectEnum**     | Initialization.                                                                                                                                                       |
| **CSampleDSGenObjectEnum::EnumGenericObjects**         | Manage retrieval of objects.                                                                                                                                          |
| **CSampleDSGenObjectEnum::FetchObjects**               | Retrieve the set of [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointers that match the filter.                                                             |
| **CSampleDSGenObjectEnum::FetchNextObject**            | Retrieve an object and match against the filter. If it matches, wrap it in generic object and return a [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. |
| **CSampleDSGenObjectEnum::EnumGenericObjects**         | Manage retrieving the objects.                                                                                                                                        |
| **CSampleDSGenObjectEnum::Next**                       | Retrieve the specified number of elements from the enumeration object indicated.                                                                                      |
| **CSampleDSGenObjectEnum::IsValidDSFilter**            | Verify that object class matches one in the filter list.                                                                                                              |
| **CSampleDSGenObjectEnum::BuildDSFilterArray**         | Manage the filter array.                                                                                                                                              |
| **CSampleDSGenObjectEnum::CreateAndAppendFilterEntry** | Add a new object class to the filter and set the filter as contiguous.                                                                                                |
| **FreeFilterList**                                     | Free the filter.                                                                                                                                                      |



 

 

 