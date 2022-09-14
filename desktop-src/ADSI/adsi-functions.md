---
title: ADSI Functions
description: Active Directory Service Interfaces expose the following helper functions to clients that do not use Automation.
ms.assetid: 4f0e90e2-afcc-4cf7-a731-9b38a83ca229
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,reference,functions
- function ADSI
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Functions

Active Directory Service Interfaces expose the following helper functions to clients that do not use Automation.



| Function                                           | Description                                                                                        |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**ADsBuildEnumerator**](/windows/desktop/api/Adshlp/nf-adshlp-adsbuildenumerator)   | Creates an enumerator object for the specified ADSI container object.                              |
| [**ADsBuildVarArrayInt**](/windows/desktop/api/Adshlp/nf-adshlp-adsbuildvararrayint) | Builds a variant array from an array of **DWORD**s.                                                |
| [**ADsBuildVarArrayStr**](/windows/desktop/api/Adshlp/nf-adshlp-adsbuildvararraystr) | Builds a variant array from an array of Unicode strings.                                           |
| [**ADsEncodeBinaryData**](/windows/desktop/api/Adshlp/nf-adshlp-adsencodebinarydata) | Converts a blob of binary data to the format suitable for a search filter.                         |
| [**ADsEnumerateNext**](/windows/desktop/api/Adshlp/nf-adshlp-adsenumeratenext)       | Populates a variant array with elements retrieved from the specified enumerator object.            |
| [**ADsFreeEnumerator**](/windows/desktop/api/Adshlp/nf-adshlp-adsfreeenumerator)     | Frees an enumerator object previously created by [**ADsBuildEnumerator**](/windows/desktop/api/Adshlp/nf-adshlp-adsbuildenumerator). |
| [**ADsGetLastError**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetlasterror)         | Retrieves the last error code value of the calling thread.                                         |
| [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject)               | Binds to an ADSI object using the current credentials.                                             |
| [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject)             | Binds to an ADSI object using specified credentials                                                |
| [**ADsSetLastError**](/windows/desktop/api/Adshlp/nf-adshlp-adssetlasterror)         | Sets the error code value of the calling thread.                                                   |
| [**AllocADsMem**](/windows/desktop/api/Adshlp/nf-adshlp-allocadsmem)                 | Allocates a block of memory.                                                                       |
| [**AllocADsStr**](/windows/desktop/api/Adshlp/nf-adshlp-allocadsstr)                 | Allocates memory for a given string.                                                               |
| [**FreeADsMem**](/windows/desktop/api/Adshlp/nf-adshlp-freeadsmem)                   | Frees the memory allocated by [**AllocADsMem**](/windows/desktop/api/Adshlp/nf-adshlp-allocadsmem).                                  |
| [**FreeADsStr**](/windows/desktop/api/Adshlp/nf-adshlp-freeadsstr)                   | Frees the memory allocated for the given string.                                                   |
| [**ReallocADsMem**](/windows/desktop/api/Adshlp/nf-adshlp-reallocadsmem)             | Assigns the existing memory content to a newly created memory location.                            |
| [**ReallocADsStr**](/windows/desktop/api/Adshlp/nf-adshlp-reallocadsstr)             | Replaces an existing string with a new one.                                                        |



 

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



 

 

 




