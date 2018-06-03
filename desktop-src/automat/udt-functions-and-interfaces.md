---
title: UDT Functions and Interfaces
description: The support functions for user-defined data types help you store UDTs in VARIANTS.
ms.assetid: badf90a3-82b6-4f2d-8f85-da159e5a1988
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UDT Functions and Interfaces

The support functions for user-defined data types help you store UDTs in VARIANTS. The support functions help you create a self-describing array of records, without the need of loading the type library of the UDT. The [**IRecordInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-irecordinfo) interface describes the structure of a UDT.

The following table describes the UDT functions and interfaces:

## In this section



| Topic                                                                     | Description                                                                                                                                                                      |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearCustData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-clearcustdata)<br/>                         | Releases memory used to hold the custom data item.<br/>                                                                                                                    |
| [**GetRecordInfoFromGuids**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-getrecordinfofromguids)<br/>       | Returns a pointer to the [**IRecordInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-irecordinfo) interface for a UDT by passing the GUID of the type information without having to load the type library. <br/> |
| [**GetRecordInfoFromTypeInfo**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-getrecordinfofromtypeinfo)<br/> | Returns a pointer to the [**IRecordInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-irecordinfo) interface of the UDT by passing its type information.<br/>                                                     |
| [**IRecordInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-irecordinfo)<br/>                             | Describes the structure of a particular UDT.<br/>                                                                                                                          |



 

 

 





