---
Description: The CInstance::SetCHString method sets a string property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a75b574d-9ee7-4930-a003-5d71c5f1d687
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CInstance::SetCHString methods
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CInstance::SetCHString methods

\[The [**CInstance**](/windows/desktop/api/Instance/nl-instance-cinstance) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The **CInstance::SetCHString** method sets a string property.

### Overload list



| Method                                                                                           | Description                        |
|:-------------------------------------------------------------------------------------------------|:-----------------------------------|
| [**SetCHString(LPCWSTR, LPCSTR)**](/windows/desktop/api/Instance/nf-instance-cinstance-setchstring(lpcwstr_lpcstr))                   | Sets a string property.<br/> |
| [**SetCHString(LPCWSTR, const CHString&)**](https://msdn.microsoft.com/en-us/library/Aa388996(v=VS.85).aspx) | Sets a string property.<br/> |



## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>Instance.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



## See also

<dl> <dt>

[**CInstance**](/windows/desktop/api/Instance/nl-instance-cinstance)
</dt> </dl>

 

 




