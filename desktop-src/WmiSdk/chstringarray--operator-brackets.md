---
Description: These subscript operators set or get the element at the specified index. These operators are a convenient substitute for the SetAt and GetAt methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93b10bef-908e-4c5e-aac3-b13051b2e7c9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CHStringArray::operator \[ \]
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CHStringArray::operator \[ \]

\[The [**CHStringArray**](/windows/desktop/api/ChStrArr/nl-chstrarr-chstringarray) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

These subscript operators set or get the element at the specified index. These operators are a convenient substitute for the [**SetAt**](/windows/desktop/api/ChStrArr/nf-chstrarr-chstringarray-setat(int,lpcwstr)) and [**GetAt**](/windows/desktop/api/ChStrArr/nf-chstrarr-chstringarray-getat(int)) methods.

``` syntax
CHString& operator []( 
  int nIndex
);

CHString operator []( 
  int nIndex
) const;
```

## Parameters

<dl> <dt>

<span id="nIndex"></span><span id="nindex"></span><span id="NINDEX"></span>*nIndex*
</dt> <dd>

An integer index that is greater than or equal to zero and less than or equal to the value returned by [**GetUpperBound**](/windows/desktop/api/ChStrArr/nf-chstrarr-chstringarray-getupperbound)

</dd> </dl>

## Return Values

The subscript operators return the [**CHString**](chstring.md) pointer element currently at this index.

## Remarks

You can use the first operator, which calls for arrays that are not **const**, on either the right (r-value) or the left (l-value) side of an assignment statement. The second, which calls for **const** arrays, can be used only on the right.

The debug version of the library asserts if the subscript (either on the left or right side of an assignment statement) is out of bounds.

## Examples

The following code example shows the use of [**CHStringArray::operator \[\]**](/windows/desktop/api/ChPtrArr/).


```C++
CHStringArray array;
CHString s;

array.Add( L"String 1" ); // Element 0 
array.Add( L"String 2" ); // Element 1 
s = array[0]; // Get element 0
assert( s == L"String 1" ); 

array[0] = L"String 3"; // Replace element 0 
assert( array[0] == L"String 3" );
```



## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChStrArr.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



## See also

<dl> <dt>

[**CHStringArray::Add**](/windows/desktop/api/ChStrArr/nf-chstrarr-chstringarray-add)
</dt> <dt>

[**CHStringArray::GetAt**](/windows/desktop/api/ChStrArr/nf-chstrarr-chstringarray-getat(int))
</dt> <dt>

[**CHStringArray::SetAt**](/windows/desktop/api/ChStrArr/nf-chstrarr-chstringarray-setat(int,lpcwstr))
</dt> </dl>

 

 




