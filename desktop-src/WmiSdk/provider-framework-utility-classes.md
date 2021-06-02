---
description: WMI C++ classes that are part of the WMI Provider Framework are no longer recommended for use.
ms.assetid: d2414a72-3435-4035-bcd9-b3ec87f5709c
ms.tgt_platform: multiple
title: Provider Framework Utility Classes
ms.topic: article
ms.date: 05/31/2018
---

# Provider Framework Utility Classes

\[WMI C++ classes that are part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The provider framework libraries Framedyd.dll (debug version) and Framedyn.dll (release version) implement several provider helper classes. Some functions in Framedyn.dll have been removed from the header files. To continue to use these functions, add `#define FRAMEWORK_ALLOW_DEPRECATED` to your code before including Fwcommon.h.

You can unload individual providers that are no longer required.

To use this capability, you must make the three following changes to your provider in MainDll.cpp:

-   In the function **DllMain** where you call [**CWbemProviderGlue::FrameworkLoginDLL**](/windows/desktop/api/WbemGlue/nf-wbemglue-cwbemproviderglue-frameworklogindll(lpcwstr_plong)), you must add a second parameter which is a pointer to a long.
-   In the function **DllCanUnloadNow** where you call [**CWbemProviderGlue::FrameworkLogoffDLL**](/windows/desktop/api/WbemGlue/nf-wbemglue-cwbemproviderglue-frameworklogoffdll(lpcwstr_plong)), you must add a second parameter which is a pointer to a long.
-   In the function **DllGetClassObject** where you create an instance of **CWbemGlueFactory**, you must add a parameter which is a pointer to a long.

In all three cases, the pointer to a long must be the same pointer.

> [!Note]  
> In Maindll.cpp, **DllGetClassObject**, **DllCanUnloadNow**, **DllRegisterServer**, **DllUnregisterServer** and **DllMain** routines must be wrapped in a try/catch block.

 

> [!Caution]  
> Provider debug builds link with Framedyd.lib for Framedyd.dll. Framedyd.dll is in the Microsoft Windows Software Development Kit (SDK) \\bin directory which is not included in the system path. When a debug build of a provider is tested with the Windows Management service, the framework provider will fail to load because Framedyd.dll or one of its dependencies will not be located. Therefore, you must either copy Framedyd.dll from the Windows SDK \\bin directory to the \\system32\\wbem directory or add the Windows SDK \\bin directory to the system search path.

 

The following table lists the provider framework utility classes.



| Utility class                                          | Description                                                                                                                     |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**CHString**](chstring.md)                           | Provides string comparison and manipulation functions for WMI.                                                                  |
| [**CHStringArray**](/windows/desktop/api/ChStrArr/nl-chstrarr-chstringarray)                 | Contains for creating and manipulating arrays of CHString.                                                                      |
| [**TRefPointerCollection**](/windows/desktop/api/RefPtrCo/nl-refptrco-trefpointercollection) | Grants access to a container class for pointers.                                                                                |
| [**WBEMTime**](wbemtime.md)                           | Facilitates conversions between various Windows and ANSI C run-time time formats.                                               |
| [**WBEMTimeSpan**](/windows/desktop/api/WbemTime/nl-wbemtime-wbemtimespan)                   | Contains helper functions used to calculate and hold the time span difference between two [**WBEMTime**](wbemtime.md) objects. |



 

> [!Note]  
> The [**CHString**](chstring.md) and [**CHStringArray**](/windows/desktop/api/ChStrArr/nl-chstrarr-chstringarray) classes are similar to the Microsoft Foundation Classes (MFC) **CString** and **CStringArray**. The WMI versions exist so that developers can access to string manipulation and comparison methods without having to access MFC. The [**WBEMTime**](wbemtime.md) and [**WBEMTimeSpan**](/windows/desktop/api/WbemTime/nl-wbemtime-wbemtimespan) classes are also similar to the MFC **CTime** and **CTimeSpan** classes. The WMI versions are capable of storing time to nanosecond accuracy, and can also convert to and from **BSTR**. For more information about the CString, CStringArray, CTime, and CTimeSpan classes, see the [Microsoft Foundation Classes](https://msdn.microsoft.com/library/d06h2x6e(VS.71).aspx) on MSDN.

 

**BSTR** values returned by [**WBEMTime**](wbemtime.md) methods are in [Date and Time Format](date-and-time-format.md): "yyyymmddHHMMSS.mmmmmmsUUU"

**BSTR** values returned by [**WBEMTimeSpan**](/windows/desktop/api/WbemTime/nl-wbemtime-wbemtimespan) methods are in [Interval Format](interval-format.md): "ddddddddHHMMSS.mmmmmm:000"

Although times and time spans are stored internally as nanoseconds, they are not necessarily stored with nanosecond accuracy. This is because [**WBEMTime**](wbemtime.md) objects can be constructed using time formats that are accurate to a second (**struct tm**, and **time\_t**). Adding artificial decimal places does not increase the accuracy.

 

 
