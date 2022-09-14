---
description: The CHString assignment (=) operator reinitializes an existing CHString object with new data.
ms.assetid: 6864aacf-ac18-4b5a-be3e-3a0d8bb31e74
ms.tgt_platform: multiple
title: CHString::operator= (ChString.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CHString::operator=

\[The [**CHString**](chstring.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The [**CHString**](chstring.md) assignment (=) operator reinitializes an existing CHString object with new data.

``` syntax
const CHString& operator =(
  const CHString& stringSrc )
throw( CHeap_Exception );

const CHString& operator =(
  WCHAR ch )
throw( CHeap_Exception );

const CHString& operator =(
  const unsigned char* psz )
throw( CHeap_Exception );

const CHString& operator =(
  LPCWSTR lpsz )
throw( CHeap_Exception );

const CHString& operator =(
  LPCSTR lpsz )
throw( CHeap_Exception );

const CHString& operator =(
  CHString *p )
throw( CHeap_Exception );

const CHString& operator =(
  char ch )
throw( CHeap_Exception );
```

## Parameters

<dl> <dt>

<span id="stringSrc__p"></span><span id="stringsrc__p"></span><span id="STRINGSRC__P"></span>*stringSrc*, *p*
</dt> <dd>

Assigns a [**CHString**](chstring.md) string to this object.

</dd> <dt>

<span id="ch"></span><span id="CH"></span>*ch*
</dt> <dd>

Assigns a character to this object.

</dd> <dt>

<span id="lpsz__psz"></span><span id="LPSZ__PSZ"></span>*lpsz*, *psz*
</dt> <dd>

Assigns a **NULL**-terminated string to this object.

</dd> </dl>

## Remarks

If the destination string (that is, the left side) is already large enough to store the new data, no new memory allocation is performed. However, memory exceptions can occur whenever you use the assignment operator because new storage is often allocated to hold the resulting [**CHString**](chstring.md) object.

## Examples

The following code example shows the use of **CHString::operator =**:


```C++
CHString s1, s2;        // Empty CHString objects

s1 = L"cat";            // s1 = "cat"
s2 = s1;                // s1 and s2 each = "cat"
s1 = L"the " + s1;      // Or expressions
s1 = 'x';               // Or just individual characters
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

 

