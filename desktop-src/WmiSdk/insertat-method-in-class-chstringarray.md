---
description: The InsertAt method inserts an element (or multiple copies of an element) or all the elements of another array at a specified index.
audience: developer
ms.assetid: 1d6355bc-7df2-4aa3-8e47-0239d726ed7d
ms.tgt_platform: multiple
title: CHStringArray::InsertAt methods (ChStrArr.h)
ms.date: 07/02/2019
ms.topic: reference
---

# CHStringArray::InsertAt methods

\[The [**CHStringArray**](/windows/win32/api/chstrarr/nl-chstrarr-chstringarray) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The **InsertAt** method inserts an element (or multiple copies of an element) or all the elements of another array at a specified index.

### Overload list



| Method                                                                               | Description                                                                                                             |
|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**InsertAt(int,LPCWSTR,int)**](/previous-versions/windows/desktop/legacy/aa385383(v=vs.85))       | Inserts one or more elements at a specified index in an array.<br/>                                               |
| [**InsertAt(int,CHStringArray\*)**](/windows/win32/api/chstrarr/nf-chstrarr-chstringarray-insertat(int_chstringarray)) | Inserts all the elements of another [**CHStringArray**](/windows/win32/api/chstrarr/nl-chstrarr-chstringarray) at a specified index in an array.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChStrArr.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



## See also

<dl> <dt>

[**CHStringArray**](/windows/win32/api/chstrarr/nl-chstrarr-chstringarray)
</dt> </dl>

�

�
