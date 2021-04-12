---
description: .
ms.assetid: 24617b5f-14f1-4f1b-a288-7d20a8166da0
title: NLS Sorting Changes
ms.topic: article
ms.date: 05/31/2018
---

# NLS Sorting Changes

## Affected Platforms

 **Clients** - Windows XP, Windows Vista, Windows 7  
**Servers** - Windows Server 2003, Windows Server 2008, Windows Server 2008 R2  










## Feature Impact

 **Severity** - High  
**Frequency** - Low (few apps impacted, but if impacted, always broken)  


## Description

The National Language Support (NLS) functions help applications support the different language- and locale-specific needs of users around the world. New Windows versions almost invariably include NLS changes. This change affects collation and sorting, and therefore applications that have persistent indexes.

A collation table has two numbers that identify its version (revision): the defined version and the NLS version. Both versions are DWORD values, composed of a major version and a minor version. The first byte of a value is reserved, the next two bytes represent the major version, and the last byte represents the minor version. In hexadecimal terms, the pattern is 0xRRMMMMmm, where R equals Reserved, M equals major, and m equals minor. For example, a major version of 3 with a minor version of 4 is represented as 0x304.

For a major version, one or more code points change so that the application must re-index all data for comparisons to be valid. For a minor version, nothing moves, but code points are added. For this type of version, the application only has to re-index strings with previously unsortable values. In summary, here is what the version numbers mean in relation to the data changes in the locale-specific exception tables and default tables:

**NLSVersion Major** – Changed code points in the 'exception,' or locale-specific tables  
**NLSVersion Minor** – Added new code points in the 'exception,' or locale-specific tables  
**DefinedVersion Major** – Changed code points in the default table  
**DefinedVersion Minor** – Added new code points in the default table  


**Sorting version numbers for released versions:**



| Operating System    | Release           | Version (0xRRMMMMmm)         |
|---------------------|-------------------|------------------------------|
| Windows XP          | RTM/SP1/SP2/SP3/… | N/A - no GetNLSVersion() API |
| Windows Server 2003 | RTM/SP1           | 0x00 0000 01                 |
| Windows Vista       | RTM/SP1           | 0x00 0405 00                 |
| Windows Server 2008 | RTM               | 0x00 0501 00 / 0x00 5001 00  |
| Windows 7           | RTM               | 0x00060100                   |



 

## Manifestation

Applications (such as databases) with persistent indexes that do not check the NLS version and re-index upon version change will fail to sort correctly or may fail to provide requested results.

In the case of user interfaces, lists (for example, alphabetical, numeric, alphanumeric, symbols, and so on) may sort incorrectly.

## Solution

Your application can call either **GetNLSVersionEx** (Windows Vista or later) or **GetNLSVersion** (prior to Windows Vista) to retrieve both the defined version and the NLS version for a collation table.

-   GetNLSVersionEx:

*Retrieves information about the current version of a specified NLS capability for a locale specified by name*  
This function allows an application such as Active Directory to determine whether an NLS change affects the locale used for a particular index table. If it does not, there is no need to re-index the table. For more information, see Handling Locale and Language Information.  
This function supports custom locales. If *lpLocaleName* specifies a supplemental locale, the data retrieved is the correct data for the collation order associated with that supplemental locale.  

**Note:** Versions of Windows prior to Windows Vista do not support **GetNLSVersionEx**.  


-   GetNLSVersion (use for applications running on versions of Windows prior to Windows Vista):

*Retrieves information about the current version of a specified NLS capability for a locale specified by identifier*  
This function allows an application such as Active Directory to determine if an NLS change affects the locale identifier used for a particular index table. If it does not, there is no need to re-index the table. For more information, see Handling Locale and Language Information.  
**Note:** This function retrieves information only about a locale specified by identifier. The **GetNLSVersionEx** function supports additional locales, features, and RFC 4646 names. However, versions of Windows prior to Windows Vista do not support **GetNLSVersionEx**.  
Applications meant to run only on Windows Vista and later should use **GetNLSVersionEx** in preference to this function. **GetNLSVersionEx** provides good support for supplemental locales.  


## Compatibility Test

**Steps to tell if a collation version changed (that is, you need to re-index):**

-   **Use GetNLSVersionEx()** to retrieve an **NLSVERSIONINFOEX** structure when doing the original indexing of your data.
-   Store the following properties with your index to identify the version:  **NLSVERSIONINFOEX.dwNLSVersion** and **NLSVERSIONINFOEX.dwDefinedVersion** – These two properties together specify the version of the sorting table you are using.  
    **NLSVERSIONINFOEX.dwEffectiveId** - This specifies the effective locale of your sort. A custom locale will point to an in-box locale's sort.  
    
-   When using the index use **GetNlsVersionEx()** to discover the version of your data.
-   If any of the three properties has changed, the sorting data you are using could return different results and any indexing you have may fail to find records.
-   If you KNOW that your data does not contain invalid Unicode code points (that is, all of your strings returned **TRUE** from a call to **IsNLSDefinedString()**), then you may consider them the same if ONLY the low byte of **dwNLSVersion** and **dwDefinedVersion** changed (the minor versions described above).

## Links to Other Resources

-   [Internationalization for Windows Applications](../intl/international-support.md)
-   [GetNLSVersionEx Function](/windows/win32/api/winnls/nf-winnls-getnlsversionex)
-   [GetNLSVersion Function](/windows/win32/api/winnls/nf-winnls-getnlsversion)
-   [How to tell if the collation version changed](/archive/blogs/shawnste/)

 

 
