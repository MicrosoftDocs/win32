---
title: WFP Version-Independent Names and Targeting Specific Versions of Windows
description: In many cases, the Windows Filtering Platform (WFP) API provides more than one version of a function or structure.
ms.assetid: FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670
ms.topic: article
ms.date: 05/31/2018
---

# WFP Version-Independent Names and Targeting Specific Versions of Windows

In many cases, the Windows Filtering Platform (WFP) API provides more than one version of a function or structure.

Most data and function names in the WFP API end with a version number, such as "0" or "1", even if there is only one version.

## Version Mapping in fwpvi.h

The fwpvi.h header file is included starting with the Windows 7 SDK and WDK. This header file maps the versionless API name to the version that is appropriate for use with a given operating system.

For example, here is a brief excerpt from the version of fwpvi.h included in the Windows 8 SDK.


```C++
#define FwpmNetEventCreateEnumHandle FwpmNetEventCreateEnumHandle0
#if (NTDDI_VERSION >= NTDDI_WIN8)
#define FwpmNetEventEnum FwpmNetEventEnum2
#elif (NTDDI_VERSION >= NTDDI_WIN7)
#define FwpmNetEventEnum FwpmNetEventEnum1
#else
#define FwpmNetEventEnum FwpmNetEventEnum0
#endif
```



As shown above, there is only one version of **FwpmNetEventCreateEnumHandle** – [**FwpmNetEventCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventcreateenumhandle0) – so any call to **FwpmNetEventCreateEnumHandle** will always call **FwpmNetEventCreateEnumHandle0**, regardless of the operating system targeted.

However, there are three versions of of **FwpmNetEventEnum**: [**FwpmNetEventEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum0), [**FwpmNetEventEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum1), and [**FwpmNetEventEnum2**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum2). The fwpvi.h header file ensures that a call to **FwpmNetEventEnum** will call the version most appropriate to the targeted operating system:

-   [**FwpmNetEventEnum2**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum2) for Windows 8 (or later)
-   [**FwpmNetEventEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum1) for Windows 7 is targeted
-   [**FwpmNetEventEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum0) for earlier operating systems (such as Windows Vista or Windows Vista with Service Pack 1 (SP1))

## Calling Version-Independent Functions and Structures

WFP developers targeting a particular operating system or WDK version are encouraged to always program against the version-independent macros. This will automatically select the latest version supported in the operating system you are targeting. Use of the most recent header files is recommended, even when targeting an earlier operating system. Doing this consistently will ensure the latest supported version is used, and can also make it easier to maintain and update your code.

The [WFP API reference documentation](fwp-reference.md) describes each version of a numbered API. If more than one version exists, the targeted operating system is noted. However, developers will generally want to call the version-independent (numberless) APIs, and indicate the targeted operating system (such as **NTDDI\_WIN6** for Windows Vista or **NTDDI\_WIN8** for Windows 8).

To ensure proper handling of functions that take different parameters in different versions, you can include conditional blocks such as `#if (NTDDI_VERSION >= NTDDI_WIN7)`.

 

 




