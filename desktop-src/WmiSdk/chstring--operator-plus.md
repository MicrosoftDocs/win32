---
description: The + concatenation operator joins two strings and returns a CHString object.
ms.assetid: b7ed6379-ccfa-40f9-9607-d9033179b674
ms.tgt_platform: multiple
title: CHString::operator+ (ChString.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CHString::operator+

\[The [**CHString**](chstring.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The + concatenation operator joins two strings and returns a [**CHString**](chstring.md) object.

``` syntax
friend CHString operator +(
  const CHString& str1,
  const CHString& str2 )
throw( CHeap_Exception );

friend CHString operator +(
  const CHString& str,
  WCHAR ch )
throw( CHeap_Exception );

friend CHString operator +(
  WCHAR ch,
  const CHString& str )
throw( CHeap_Exception );

friend CHString operator +(
  const CHString& str,
  LPCWSTR lpsz )
throw( CHeap_Exception );

friend CHString operator +(
  LPCWSTR lpsz,
  const CHString& str )
throw( CHeap_Exception );

friend CHString operator +(
  const CHString& str,
  char ch )
throw( CHeap_Exception );

friend CHString operator +(
  char ch,
  const CHString& str )
throw( CHeap_Exception );
```

## Parameters

<dl> <dt>

<span id="str__str1__str2"></span><span id="STR__STR1__STR2"></span>*str, str1, str2*
</dt> <dd>

[**CHString**](chstring.md) strings that are concatenated.

</dd> <dt>

<span id="ch"></span><span id="CH"></span>*ch*
</dt> <dd>

A character that concatenates to a string or a string that concatenates to a character.

</dd> <dt>

<span id="lpsz"></span><span id="LPSZ"></span>*lpsz*
</dt> <dd>

Pointer to a **NULL**-terminated character string.

</dd> </dl>

## Return Values

This concatenation operator returns a [**CHString**](chstring.md) object that is the temporary result of the concatenation. This return value makes it possible to combine several concatenations in the same expression.

## Remarks

One of the two argument strings must be a [**CHString**](chstring.md) object; the other can be a character pointer or a character. Be aware that memory exceptions can occur whenever you use the concatenation operator because new storage may be allocated to hold temporary data.

## Examples

The following code example shows the use of **CHString::operator +**:


```C++
CHString s1( L"abc" );
CHString s2( L"def" );
assert( (s1 + s2 ) == L"abcdef" );

CHString s3;
s3 = CHString( L"abc" ) + "def" ; // Correct
s3 = "abc" + "def"; // Wrong. The first argument must be a CHString.
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChString.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



## See also

<dl> <dt>

[**CHString**](chstring.md)
</dt> </dl>

 

