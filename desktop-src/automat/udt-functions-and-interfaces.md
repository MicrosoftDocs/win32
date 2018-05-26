---
title: UDT Functions and Interfaces
description: The support functions for user-defined data types help you store UDTs in VARIANTS.
ms.assetid: badf90a3-82b6-4f2d-8f85-da159e5a1988
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UDT Functions and Interfaces

The support functions for user-defined data types help you store UDTs in VARIANTS. The support functions help you create a self-describing array of records, without the need of loading the type library of the UDT. The [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) interface describes the structure of a UDT.

The following table describes the UDT functions and interfaces:

## In this section



| Topic                                                                     | Description                                                                                                                                                                      |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearCustData**](/windows/previous-versions/OleAuto/nf-oleauto-clearcustdata?branch=master)<br/>                         | Releases memory used to hold the custom data item.<br/>                                                                                                                    |
| [**GetRecordInfoFromGuids**](/windows/previous-versions/OleAuto/nf-oleauto-getrecordinfofromguids?branch=master)<br/>       | Returns a pointer to the [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) interface for a UDT by passing the GUID of the type information without having to load the type library. <br/> |
| [**GetRecordInfoFromTypeInfo**](/windows/previous-versions/OleAuto/nf-oleauto-getrecordinfofromtypeinfo?branch=master)<br/> | Returns a pointer to the [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) interface of the UDT by passing its type information.<br/>                                                     |
| [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master)<br/>                             | Describes the structure of a particular UDT.<br/>                                                                                                                          |



 

 

 





