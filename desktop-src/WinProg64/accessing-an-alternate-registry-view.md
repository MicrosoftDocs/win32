---
title: Accessing an Alternate Registry View
description: By default, a 32-bit application running on WOW64 accesses the 32-bit registry view and a 64-bit application accesses the 64-bit registry view.
ms.assetid: 2c5fd3de-998c-44ab-863e-8e0e90d56e5d
keywords:
- registry views 64-bit Windows Programming
- WOW64 64-bit Windows Programming , registry views
ms.topic: article
ms.date: 05/31/2018
---

# Accessing an Alternate Registry View

By default, a 32-bit application running on WOW64 accesses the 32-bit registry view and a 64-bit application accesses the 64-bit registry view. The following flags enable 32-bit applications to access redirected keys in the 64-bit registry view and 64-bit applications to access redirected keys in the 32-bit registry view. These flags have no effect on shared registry keys. For more information, see [Registry Keys Affected by WOW64](shared-registry-keys.md).



| Flag name         | Value  | Description                                                                                                                                                                                                                                       |
|-------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KEY\_WOW64\_64KEY | 0x0100 | Access a 64-bit key from either a 32-bit or 64-bit application.                                                                                                                                                                                   |
| KEY\_WOW64\_32KEY | 0x0200 | Access a 32-bit key from either a 32-bit or 64-bit application.<br/>**Windows 10 on ARM:** This refers to the 32-bit ARM registry view for 32-bit ARM processes and the 32-bit x86 registry view for 32-bit x86 and 64-bit ARM64 processes. |



 

These flags can be specified in the *samDesired* parameter of the following registry functions:

-   [**RegCreateKeyEx**](/windows/desktop/api/winreg/nf-winreg-regcreatekeyexa)
-   [**RegDeleteKeyEx**](/windows/desktop/api/winreg/nf-winreg-regdeletekeyexa)
-   [**RegOpenKeyEx**](/windows/desktop/api/winreg/nf-winreg-regopenkeyexa)

Either KEY\_WOW64\_32KEY or KEY\_WOW64\_64KEY can be specified. If both flags are specified, the function fails with ERROR\_INVALID\_PARAMETER.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** If both flags are specified, the function s behavior is undefined.

The [**RegDeleteKey**](/windows/desktop/api/winreg/nf-winreg-regdeletekeya) function cannot be used to access an alternate registry view.

The following are best practices when accessing the registry from an application:

-   After the application has accessed an alternate registry view using one of the flags, all subsequent operations (create, delete, or open) on child registry keys must explicitly use the same flag. Otherwise, there can be unexpected behavior.
-   To accurately enumerate all keys in both views, perform the enumeration in two passes. The first pass should use a handle opened with one of the flags, and the other pass should use a handle opened with the other flag.

> [!Note]  
> The **Wow6432Node** and **WowAA32Node** keys are reserved. For compatibility, applications should not use these keys directly.

 

For information about accessing the alternate registry view through WMI, see [Requesting WMI Data on a 64-bit Platform](/windows/desktop/WmiSdk/requesting-wmi-data-on-a-64-bit-platform).

## Related topics

<dl> <dt>

[Registry Redirector](registry-redirector.md)
</dt> <dt>

[Registry Reflection](registry-reflection.md)
</dt> </dl>

 

