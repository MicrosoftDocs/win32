---
title: ADSI Functions
description: Active Directory Service Interfaces expose the following helper functions to clients that do not use Automation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4f0e90e2-afcc-4cf7-a731-9b38a83ca229
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,reference,functions
- function ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Functions

Active Directory Service Interfaces expose the following helper functions to clients that do not use Automation.



| Function                                           | Description                                                                                        |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**ADsBuildEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsbuildenumerator?branch=master)   | Creates an enumerator object for the specified ADSI container object.                              |
| [**ADsBuildVarArrayInt**](/windows/win32/Adshlp/nf-adshlp-adsbuildvararrayint?branch=master) | Builds a variant array from an array of **DWORD**s.                                                |
| [**ADsBuildVarArrayStr**](/windows/win32/Adshlp/nf-adshlp-adsbuildvararraystr?branch=master) | Builds a variant array from an array of Unicode strings.                                           |
| [**ADsEncodeBinaryData**](/windows/win32/Adshlp/nf-adshlp-adsencodebinarydata?branch=master) | Converts a blob of binary data to the format suitable for a search filter.                         |
| [**ADsEnumerateNext**](/windows/win32/Adshlp/nf-adshlp-adsenumeratenext?branch=master)       | Populates a variant array with elements retrieved from the specified enumerator object.            |
| [**ADsFreeEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsfreeenumerator?branch=master)     | Frees an enumerator object previously created by [**ADsBuildEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsbuildenumerator?branch=master). |
| [**ADsGetLastError**](/windows/win32/Adshlp/nf-adshlp-adsgetlasterror?branch=master)         | Retrieves the last error code value of the calling thread.                                         |
| [**ADsGetObject**](/windows/win32/Adshlp/nf-adshlp-adsgetobject?branch=master)               | Binds to an ADSI object using the current credentials.                                             |
| [**ADsOpenObject**](/windows/win32/Adshlp/nf-adshlp-adsopenobject?branch=master)             | Binds to an ADSI object using specified credentials                                                |
| [**ADsSetLastError**](/windows/win32/Adshlp/nf-adshlp-adssetlasterror?branch=master)         | Sets the error code value of the calling thread.                                                   |
| [**AllocADsMem**](/windows/win32/Adshlp/nf-adshlp-allocadsmem?branch=master)                 | Allocates a block of memory.                                                                       |
| [**AllocADsStr**](/windows/win32/Adshlp/nf-adshlp-allocadsstr?branch=master)                 | Allocates memory for a given string.                                                               |
| [**FreeADsMem**](/windows/win32/Adshlp/nf-adshlp-freeadsmem?branch=master)                   | Frees the memory allocated by [**AllocADsMem**](/windows/win32/Adshlp/nf-adshlp-allocadsmem?branch=master).                                  |
| [**FreeADsStr**](/windows/win32/Adshlp/nf-adshlp-freeadsstr?branch=master)                   | Frees the memory allocated for the given string.                                                   |
| [**ReallocADsMem**](/windows/win32/Adshlp/nf-adshlp-reallocadsmem?branch=master)             | Assigns the existing memory content to a newly created memory location.                            |
| [**ReallocADsStr**](/windows/win32/Adshlp/nf-adshlp-reallocadsstr?branch=master)             | Replaces an existing string with a new one.                                                        |



 

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



 

 

 




