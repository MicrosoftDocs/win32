---
description: An overloaded method that releases the memory that contains the path.
audience: developer
ms.assetid: 9164d7b2-15b8-4b73-ab8c-68ed45692ea0
ms.tgt_platform: multiple
title: CObjectPathParser::Free methods (ObjPath.h)
ms.date: 07/02/2019
ms.topic: reference
---

# CObjectPathParser::Free methods

\[The [**CObjectPathParser**](/windows/win32/api/objpath/nl-objpath-cobjectpathparser) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

An overloaded method that releases the memory that contains the path.

### Overload list



| Method                                                                     | Description                                                                          |
|:---------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**Free(LPWSTR)**](/windows/win32/api/objpath/nf-objpath-cobjectpathparser-free(lpwstr))                     | Releases the memory that contains the unparsed path.<br/>                      |
| [**Free(ParsedObjectPath)**](/windows/win32/api/objpath/nf-objpath-cobjectpathparser-free(parsedobjectpath)) | Releases the memory that contains the structure that has the parsed path.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ObjPath.h (include ObjPath.h)</dt> </dl>                                                      |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



## See also

<dl> <dt>

[**CObjectPathParser**](/windows/win32/api/objpath/nl-objpath-cobjectpathparser)
</dt> </dl>

�

�
