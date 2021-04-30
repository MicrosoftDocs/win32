---
description: Each of the following constructors initializes a new CHString object with the specified data.
audience: developer
ms.assetid: d49e1600-d5d4-4c44-81c5-1b8c53b768de
ms.tgt_platform: multiple
title: CHString::CHString constructors (ChString.h)
ms.date: 07/02/2019
ms.topic: reference
---

# CHString::CHString constructors

\[The [**CHString**](chstring.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

Each of the following constructors initializes a new [**CHString**](chstring.md) object with the specified data.

### Overload list



| Constructor                                                                        | Description                                                  |
|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------|
| [**CHString()**](/windows/win32/api/rrascfg/nn-rrascfg-ieapproviderconfig)                                          | Creates an empty CHString object.<br/>                 |
| [**CHString(LPCSTR)**](/windows/win32/api/chstring/nf-chstring-chstring-chstring(lpcstr))                              | Initializes with the LPCSTR value.<br/>                |
| [**CHString(LPCWSTR)**](/windows/win32/api/chstring/nf-chstring-chstring-chstring(lpcwstr))                            | Initializes with the LPCWSTR value.<br/>               |
| [**CHString(WCHAR,int)**](/windows/win32/api/chstring/nf-chstring-chstring-chstring(wchar_int))                        | Initializes with int copies of the WCHAR value.<br/>   |
| [**CHString(LPCWSTR,int)**](/windows/win32/api/chstring/nf-chstring-chstring-chstring(lpcwstr_int))                    | Initializes with int copies of the LPCWSTR value.<br/> |
| [**CHString(const CHString&)**](/windows/win32/api/chstring/nf-chstring-chstring-chstring(constchstring_))            | Replicates the CHString parameter.<br/>                |
| [**CHString(const unsigned char\*)**](/windows/win32/api/chstring/nf-chstring-chstring-chstring(constunsignedchar)) | Initializes with the value pointed to by char\*.<br/>  |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChString.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



�

�
