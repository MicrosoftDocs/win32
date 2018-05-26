---
Description: The CHString class exposes the following methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C064D6DE-14C4-4143-8164-B367C10CBF8E
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CHString Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CHString Methods

\[The [**CHString**](chstring.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The [**CHString**](chstring.md) class exposes the following methods.

## In this section

-   [**AllocSysString method**](/windows/win32/ChString/nf-chstring-chstring-allocsysstring?branch=master)
-   [**CHString constructors**](/windows/win32/ChString/nf-chstring-chstring-chstring(const chstring &)?branch=master)
-   [**Collate method**](/windows/win32/ChString/nf-chstring-chstring-collate?branch=master)
-   [**Compare method**](/windows/win32/ChString/nf-chstring-chstring-compare?branch=master)
-   [**CompareNoCase method**](/windows/win32/ChString/nf-chstring-chstring-comparenocase?branch=master)
-   [**Empty method**](/windows/win32/ChString/nf-chstring-chstring-empty?branch=master)
-   [**Find methods**](/windows/win32/ChString/nf-chstring-chstring-find?branch=master)
-   [**FindOneOf method**](/windows/win32/ChString/nf-chstring-chstring-findoneof?branch=master)
-   [**Format methods**](/windows/win32/ChString/nf-chstring-chstring-format(uint,---)?branch=master)
-   [**FormatMessageW methods**](/windows/win32/ChString/nf-chstring-chstring-formatmessagew(uint,---)?branch=master)
-   [**FormatV method**](/windows/win32/ChString/nf-chstring-chstring-formatv?branch=master)
-   [**FreeExtra method**](/windows/win32/ChString/nf-chstring-chstring-freeextra?branch=master)
-   [**GetAllocLength method**](/windows/win32/ChString/nf-chstring-chstring-getalloclength?branch=master)
-   [**GetAt method**](/windows/win32/ChString/nf-chstring-chstring-getat(int)?branch=master)
-   [**GetBuffer method**](/windows/win32/ChString/nf-chstring-chstring-getbuffer?branch=master)
-   [**GetBufferSetLength method**](/windows/win32/ChString/nf-chstring-chstring-getbuffersetlength?branch=master)
-   [**GetData method**](/windows/win32/ChString/nf-chstring-chstring-getdata?branch=master)
-   [**GetLength method**](/windows/win32/ChString/nf-chstring-chstring-getlength?branch=master)
-   [**IsEmpty method**](/windows/win32/ChString/nf-chstring-chstring-isempty?branch=master)
-   [**Left method**](/windows/win32/ChString/nf-chstring-chstring-left?branch=master)
-   [**LoadStringW method**](/windows/win32/ChString/nf-chstring-chstring-loadstringw(uint)?branch=master)
-   [**LockBuffer method**](/windows/win32/ChString/nf-chstring-chstring-lockbuffer?branch=master)
-   [**MakeLower method**](/windows/win32/ChString/nf-chstring-chstring-makelower?branch=master)
-   [**MakeReverse method**](/windows/win32/ChString/nf-chstring-chstring-makereverse?branch=master)
-   [**MakeUpper method**](/windows/win32/ChString/nf-chstring-chstring-makeupper?branch=master)
-   [**Mid methods**](/windows/win32/ChString/nf-chstring-chstring-mid?branch=master)
-   [**operator\[\] method**](/windows/win32/ChString/?branch=master)
-   [**CHString::operator+**](chstring--operator-plus.md)
-   [**CHString::operator+=**](chstring--operator-plus-equal.md)
-   [**CHString::operator=**](chstring--operator-equal.md)
-   [**operator==(constCHString&, constCHString&) method**](/windows/win32/ChString/?branch=master)
-   [**operator==(constCHString&, constLPCWSTR&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&gt;(constCHString&, constCHString&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&gt;(constCHString&, constLPCWSTR&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&gt;=(constCHString&, constCHString&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&gt;=(constCHString&, constLPCWSTR&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&lt;(constCHString&, constCHString&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&lt;(constCHString&, constLPCWSTR&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&lt;=(constCHString&, constCHString&) method**](/windows/win32/ChString/?branch=master)
-   [**operator&lt;=(constCHString&, constLPCWSTR&) method**](/windows/win32/ChString/?branch=master)
-   [**operator!=(constCHString&, constCHString&) method**](/windows/win32/ChString/?branch=master)
-   [**operator!=(constCHString&, constLPCWSTR&) method**](/windows/win32/ChString/?branch=master)
-   [**operator LPCWSTR method**](/windows/win32/ChString/nf-chstring-chstring-operator lpcwstr?branch=master)
-   [**ReleaseBuffer method**](/windows/win32/ChString/nf-chstring-chstring-releasebuffer?branch=master)
-   [**ReverseFind method**](/windows/win32/ChString/nf-chstring-chstring-reversefind?branch=master)
-   [**Right method**](/windows/win32/ChString/nf-chstring-chstring-right?branch=master)
-   [**SetAt method**](/windows/win32/ChString/nf-chstring-chstring-setat?branch=master)
-   [**SpanExcluding method**](/windows/win32/ChString/nf-chstring-chstring-spanexcluding?branch=master)
-   [**SpanIncluding method**](/windows/win32/ChString/nf-chstring-chstring-spanincluding?branch=master)
-   [**TrimLeft method**](/windows/win32/ChString/nf-chstring-chstring-trimleft?branch=master)
-   [**TrimRight method**](/windows/win32/ChString/nf-chstring-chstring-trimright?branch=master)
-   [**UnlockBuffer method**](/windows/win32/ChString/nf-chstring-chstring-unlockbuffer?branch=master)

 

 



