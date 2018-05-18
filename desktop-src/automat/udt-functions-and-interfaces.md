---
title: UDT Functions and Interfaces
description: The support functions for user-defined data types help you store UDTs in VARIANTS.
ms.assetid: 'badf90a3-82b6-4f2d-8f85-da159e5a1988'
---

# UDT Functions and Interfaces

The support functions for user-defined data types help you store UDTs in VARIANTS. The support functions help you create a self-describing array of records, without the need of loading the type library of the UDT. The [**IRecordInfo**](irecordinfo.md) interface describes the structure of a UDT.

The following table describes the UDT functions and interfaces:

## In this section



| Topic                                                                     | Description                                                                                                                                                                      |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearCustData**](clearcustdata.md)<br/>                         | Releases memory used to hold the custom data item.<br/>                                                                                                                    |
| [**GetRecordInfoFromGuids**](getrecordinfofromguids.md)<br/>       | Returns a pointer to the [**IRecordInfo**](irecordinfo.md) interface for a UDT by passing the GUID of the type information without having to load the type library. <br/> |
| [**GetRecordInfoFromTypeInfo**](getrecordinfofromtypeinfo.md)<br/> | Returns a pointer to the [**IRecordInfo**](irecordinfo.md) interface of the UDT by passing its type information.<br/>                                                     |
| [**IRecordInfo**](irecordinfo.md)<br/>                             | Describes the structure of a particular UDT.<br/>                                                                                                                          |



 

 

 





