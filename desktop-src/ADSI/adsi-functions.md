---
title: ADSI Functions
description: Active Directory Service Interfaces expose the following helper functions to clients that do not use Automation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '4f0e90e2-afcc-4cf7-a731-9b38a83ca229'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADSI ADSI ,reference,functions", "function ADSI"]
---

# ADSI Functions

Active Directory Service Interfaces expose the following helper functions to clients that do not use Automation.



| Function                                           | Description                                                                                        |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**ADsBuildEnumerator**](adsbuildenumerator.md)   | Creates an enumerator object for the specified ADSI container object.                              |
| [**ADsBuildVarArrayInt**](adsbuildvararrayint.md) | Builds a variant array from an array of **DWORD**s.                                                |
| [**ADsBuildVarArrayStr**](adsbuildvararraystr.md) | Builds a variant array from an array of Unicode strings.                                           |
| [**ADsEncodeBinaryData**](adsencodebinarydata.md) | Converts a blob of binary data to the format suitable for a search filter.                         |
| [**ADsEnumerateNext**](adsenumeratenext.md)       | Populates a variant array with elements retrieved from the specified enumerator object.            |
| [**ADsFreeEnumerator**](adsfreeenumerator.md)     | Frees an enumerator object previously created by [**ADsBuildEnumerator**](adsbuildenumerator.md). |
| [**ADsGetLastError**](adsgetlasterror.md)         | Retrieves the last error code value of the calling thread.                                         |
| [**ADsGetObject**](adsgetobject.md)               | Binds to an ADSI object using the current credentials.                                             |
| [**ADsOpenObject**](adsopenobject.md)             | Binds to an ADSI object using specified credentials                                                |
| [**ADsSetLastError**](adssetlasterror.md)         | Sets the error code value of the calling thread.                                                   |
| [**AllocADsMem**](allocadsmem.md)                 | Allocates a block of memory.                                                                       |
| [**AllocADsStr**](allocadsstr.md)                 | Allocates memory for a given string.                                                               |
| [**FreeADsMem**](freeadsmem.md)                   | Frees the memory allocated by [**AllocADsMem**](allocadsmem.md).                                  |
| [**FreeADsStr**](freeadsstr.md)                   | Frees the memory allocated for the given string.                                                   |
| [**ReallocADsMem**](reallocadsmem.md)             | Assigns the existing memory content to a newly created memory location.                            |
| [**ReallocADsStr**](reallocadsstr.md)             | Replaces an existing string with a new one.                                                        |



 

The following ADSI functions are obsolete.



| Function                                                  | Description |
|-----------------------------------------------------------|-------------|
| [**AdsFreeAllErrorRecords**](obsolete-adsi-functions.md) | Obsolete.   |
| [**AdsDecodeBinaryData**](obsolete-adsi-functions.md)    | Obsolete.   |
| [**PropVariantToAdsType**](obsolete-adsi-functions.md)   | Obsolete.   |
| [**AdsTypeToPropVariant**](obsolete-adsi-functions.md)   | Obsolete.   |
| [**AdsFreeAdsValues**](obsolete-adsi-functions.md)       | Obsolete.   |
| [**InitAdsMem**](obsolete-adsi-functions.md)             | Obsolete.   |
| [**AssertAdsmemLeaks**](obsolete-adsi-functions.md)      | Obsolete.   |
| [**DumpMemorytracker**](obsolete-adsi-functions.md)      | Obsolete.   |



 

 

 




