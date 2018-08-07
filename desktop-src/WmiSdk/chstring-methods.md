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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CHString Methods

\[The [**CHString**](chstring.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The [**CHString**](chstring.md) class exposes the following methods.

## In this section

-   [**AllocSysString method**](/windows/desktop/api/ChString/nf-chstring-chstring-allocsysstring)
-   [**CHString constructors**](/windows/desktop/api/ChString/nf-chstring-chstring-chstring(const chstring &))
-   [**Collate method**](/windows/desktop/api/ChString/nf-chstring-chstring-collate)
-   [**Compare method**](/windows/desktop/api/ChString/nf-chstring-chstring-compare)
-   [**CompareNoCase method**](/windows/desktop/api/ChString/nf-chstring-chstring-comparenocase)
-   [**Empty method**](/windows/desktop/api/ChString/nf-chstring-chstring-empty)
-   [**Find methods**](/windows/desktop/api/ChString/nf-chstring-chstring-find)
-   [**FindOneOf method**](/windows/desktop/api/ChString/nf-chstring-chstring-findoneof)
-   [**Format methods**](/windows/desktop/api/ChString/nf-chstring-chstring-format(uint_---))
-   [**FormatMessageW methods**](/windows/desktop/api/ChString/nf-chstring-chstring-formatmessagew(uint_---))
-   [**FormatV method**](/windows/desktop/api/ChString/nf-chstring-chstring-formatv)
-   [**FreeExtra method**](/windows/desktop/api/ChString/nf-chstring-chstring-freeextra)
-   [**GetAllocLength method**](/windows/desktop/api/ChString/nf-chstring-chstring-getalloclength)
-   [**GetAt method**](/windows/desktop/api/ChString/nf-chstring-chstring-getat(int))
-   [**GetBuffer method**](/windows/desktop/api/ChString/nf-chstring-chstring-getbuffer)
-   [**GetBufferSetLength method**](/windows/desktop/api/ChString/nf-chstring-chstring-getbuffersetlength)
-   [**GetData method**](/windows/desktop/api/ChString/nf-chstring-chstring-getdata)
-   [**GetLength method**](/windows/desktop/api/ChString/nf-chstring-chstring-getlength)
-   [**IsEmpty method**](/windows/desktop/api/ChString/nf-chstring-chstring-isempty)
-   [**Left method**](/windows/desktop/api/ChString/nf-chstring-chstring-left)
-   [**LoadStringW method**](/windows/desktop/api/ChString/nf-chstring-chstring-loadstringw(uint))
-   [**LockBuffer method**](/windows/desktop/api/ChString/nf-chstring-chstring-lockbuffer)
-   [**MakeLower method**](/windows/desktop/api/ChString/nf-chstring-chstring-makelower)
-   [**MakeReverse method**](/windows/desktop/api/ChString/nf-chstring-chstring-makereverse)
-   [**MakeUpper method**](/windows/desktop/api/ChString/nf-chstring-chstring-makeupper)
-   [**Mid methods**](/windows/desktop/api/ChString/nf-chstring-chstring-mid)
-   [**operator\[\] method**](https://msdn.microsoft.com/en-us/library/Aa386162(v=VS.85).aspx)
-   [**CHString::operator+**](chstring--operator-plus.md)
-   [**CHString::operator+=**](chstring--operator-plus-equal.md)
-   [**CHString::operator=**](chstring--operator-equal.md)
-   [**operator==(constCHString&, constCHString&) method**](https://msdn.microsoft.com/en-us/library/Aa385641(v=VS.85).aspx)
-   [**operator==(constCHString&, constLPCWSTR&) method**](https://msdn.microsoft.com/en-us/library/Aa385645(v=VS.85).aspx)
-   [**operator>(constCHString&, constCHString&) method**](https://msdn.microsoft.com/en-us/library/Aa385665(v=VS.85).aspx)
-   [**operator>(constCHString&, constLPCWSTR&) method**](https://msdn.microsoft.com/en-us/library/Aa385672(v=VS.85).aspx)
-   [**operator>=(constCHString&, constCHString&) method**](https://msdn.microsoft.com/en-us/library/Aa385652(v=VS.85).aspx)
-   [**operator>=(constCHString&, constLPCWSTR&) method**](https://msdn.microsoft.com/en-us/library/Aa385661(v=VS.85).aspx)
-   [**operator<(constCHString&, constCHString&) method**](https://msdn.microsoft.com/en-us/library/Aa385689(v=VS.85).aspx)
-   [**operator<(constCHString&, constLPCWSTR&) method**](https://msdn.microsoft.com/en-us/library/Aa385695(v=VS.85).aspx)
-   [**operator<=(constCHString&, constCHString&) method**](https://msdn.microsoft.com/en-us/library/Aa385676(v=VS.85).aspx)
-   [**operator<=(constCHString&, constLPCWSTR&) method**](https://msdn.microsoft.com/en-us/library/Aa385683(v=VS.85).aspx)
-   [**operator!=(constCHString&, constCHString&) method**](https://msdn.microsoft.com/en-us/library/Aa385704(v=VS.85).aspx)
-   [**operator!=(constCHString&, constLPCWSTR&) method**](https://msdn.microsoft.com/en-us/library/Aa385763(v=VS.85).aspx)
-   [**operator LPCWSTR method**](/windows/desktop/api/ChString/nf-chstring-chstring-operator lpcwstr)
-   [**ReleaseBuffer method**](/windows/desktop/api/ChString/nf-chstring-chstring-releasebuffer)
-   [**ReverseFind method**](/windows/desktop/api/ChString/nf-chstring-chstring-reversefind)
-   [**Right method**](/windows/desktop/api/ChString/nf-chstring-chstring-right)
-   [**SetAt method**](/windows/desktop/api/ChString/nf-chstring-chstring-setat)
-   [**SpanExcluding method**](/windows/desktop/api/ChString/nf-chstring-chstring-spanexcluding)
-   [**SpanIncluding method**](/windows/desktop/api/ChString/nf-chstring-chstring-spanincluding)
-   [**TrimLeft method**](/windows/desktop/api/ChString/nf-chstring-chstring-trimleft)
-   [**TrimRight method**](/windows/desktop/api/ChString/nf-chstring-chstring-trimright)
-   [**UnlockBuffer method**](/windows/desktop/api/ChString/nf-chstring-chstring-unlockbuffer)

 

 



