---
Description: 'The Job Object provider supports access to data about named kernel job objects.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '98407891-c628-40d9-9ec9-3e6934aaa2d2'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Job Object Provider
---

# Job Object Provider

The Job Object provider supports access to data about named kernel job objects. The Job Object provider does not report unnamed kernel job objects. This provider resides in the root\\cimv2 namespace and the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance is "NamedJobObjectProv". Finally, this provider is preinstalled.

The Job Object provider cannot create or modify named job objects. **CreateInstance** and **PutInstance** are not supported for any classes that belong to this provider.

The Job Object provider is implemented through the following instances of [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688):

-   "NamedJobObjectActgInfoProv"
-   "NamedJobObjectEventProv"
-   "NamedJobObjectLimitSettingProv"
-   "NamedJobObjectProv"
-   "NamedJobObjectSecLimitsettingProv"

The Job Object provider is an instance, method, and event provider that implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)

The Job Object provider uses the following standard classes:

-   [**Win32\_NamedJobObject**](win32-namedjobobject.md)
-   [**Win32\_NamedJobObjectActgInfo**](win32-namedjobobjectactginfo.md)
-   [**Win32\_NamedJobObjectLimitSetting**](win32-namedjobobjectlimitsetting.md)
-   [**Win32\_NamedJobObjectSecLimitSetting**](win32-namedjobobjectseclimitsetting.md)

The Job Object provider supports the following classes:

-   [**Win32\_NamedJobObjectStatistics**](win32-namedjobobjectstatistics.md)
-   [**Win32\_NamedJobObjectProcess**](win32-namedjobobjectprocess.md)
-   [**Win32\_NamedJobObjectLimit**](win32-namedjobobjectlimit.md)
-   [**Win32\_NamedJobObjectSecLimit**](win32-namedjobobjectseclimit.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 



