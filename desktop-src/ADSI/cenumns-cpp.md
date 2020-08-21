---
title: CENUMNS.CPP
description: In the example provider component, the enumeration of a namespace object uses the methods, from cenumns.cpp, listed in the following table.
ms.assetid: 52e23977-8df6-44a4-9a5e-a7896471c17e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CENUMNS.CPP

In the example provider component, the enumeration of a namespace object uses the methods, from cenumns.cpp, listed in the following table.



| Method                                              | Description                                                                                                                                               |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CSampleDSNamespaceEnum::Create**                  | Create an object to allow enumeration of an ADS namespace object.                                                                                         |
| **CSampleDSNamespaceEnum::CSampleDSNamespaceEnum**  | Standard constructor.                                                                                                                                     |
| **CSampleDSNamespaceEnum::~CSampleDSNamespaceEnum** | Standard destructor.                                                                                                                                      |
| **CSampleDSNamespaceEnum::Next**                    | Retrieve the specified number of elements from the namespace object indicated.                                                                            |
| **CSampleDSNamespaceEnum::EnumObjects**             | Manage retrieving the interface pointers to the objects.                                                                                                  |
| **CSampleDSNamespaceEnum::FetchObjects**            | Fetch the set of [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointers.                                                                          |
| **CSampleDSNamespaceEnum::FetchNextObject**         | Fetch the next object. If found, create a generic Active Directory object and retrieve its [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. |



 

 

 