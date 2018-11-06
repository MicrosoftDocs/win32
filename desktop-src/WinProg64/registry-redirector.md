---
title: Registry Redirector
description: The registry redirector isolates 32-bit and 64-bit applications by providing separate logical views of certain portions of the registry on WOW64.
ms.assetid: b3989f79-0439-485a-96c1-4f2227d48653
keywords:
- 64-bit Windows programming guide 64-bit Windows Programming , registry redirector
- registry redirector 64-bit Windows Programming
- redirection 64-bit Windows Programming
- WOW64 64-bit Windows Programming , registry redirector
ms.topic: article
ms.date: 05/31/2018
---

# Registry Redirector

The registry redirector isolates 32-bit and 64-bit applications by providing separate logical views of certain portions of the registry on WOW64. The registry redirector intercepts 32-bit and 64-bit registry calls to their respective logical registry views and maps them to the corresponding physical registry location. The redirection process is transparent to the application. Therefore, a 32-bit application can access registry data as if it were running on 32-bit Windows even if the data is stored in a different location on 64-bit Windows.

**Windows 10 on ARM:** In addition to the 32-bit logical view for x86 applications, Windows 10 on ARM includes a separate logical view for 32-bit ARM applications.

A subset of keys under redirected registry paths are shared. 32-bit registry calls to shared keys are not redirected. Instead, one physical copy of the key is mapped into each logical view of the registry. For a list of redirected keys and shared keys, see [Registry Keys Affected by WOW64](shared-registry-keys.md).

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** To enable application interoperability through COM and other mechanisms, a subset of redirected registry keys are also *reflected*. The process of registry reflection copies registry keys and values between two registry views to keep them synchronized. Registry reflection was removed starting with Windows 7 and Windows Server 2008 R2. For more information, see [Registry Reflection](registry-reflection.md).

The following scenario illustrates the use of these logical views:

-   A 32-bit x86 application checks for the existence of the following registry key: **HKEY\_LOCAL\_MACHINE\\Software\\Hello**. If the key does not exist, the application creates it with a default value of "Hello 32-bit x86 world"; otherwise, it reads and displays the value.
-   The same application is modified to write "Hello 64-bit world" instead of "Hello 32-bit x86 world" and recompiled as a 64-bit x64 or ARM64 application.
-   **Windows 10 on ARM:** The same application is modified to write “Hello 32-bit ARM world” and recompiled as a 32-bit ARM application.
-   When the 32-bit x86 application is run on 64-bit Windows, it displays "Hello 32-bit x86 world". When the 64-bit application is run, it displays "Hello 64-bit world". **Windows 10 on ARM:** When the 32-bit ARM application is run on 64-bit ARM64 Windows, it displays "Hello 32-bit ARM world". All applications call the same registry functions with the same predefined handle and the same key name; the difference is that each application operates on its logical view of registry, and each view is mapped to a separate physical location of the registry, which keeps all versions of the string intact.

Redirected keys are mapped to physical locations under **Wow6432Node**. For example, **HKEY\_LOCAL\_MACHINE\\Software** is redirected to **HKEY\_LOCAL\_MACHINE\\Software\\Wow6432Node**. However, the physical location of redirected keys should be considered reserved by the system. Applications should not access a key's physical location directly, because this location may change. For more information, see [Accessing an Alternate Registry View](accessing-an-alternate-registry-view.md).

**Windows 10 on ARM:** Redirected 32-bit ARM keys are mapped to physical locations under WowAA32Node.

To help 32-bit applications that write **REG\_SZ** or **REG\_EXPAND\_SZ** data containing %ProgramFiles% or %commonprogramfiles% to the registry, WOW64 intercepts these write operations and replaces them with "%ProgramFiles(x86)%" and "%commonprogramfiles(x86)%". For example, if the Program Files directory is on the C drive, then "%ProgramFiles(x86)%" expands to "C:\\Program Files (x86)". The replacement occurs only if the following conditions are met:

-   The string must begin with %ProgramFiles% or %commonprogramfiles%. If the string begins with a space or any character other than %, it is not replaced.
-   The case of %ProgramFiles% or %commonprogramfiles% must be exactly as shown because the string comparison is case-sensitive. For example, if the string begins with %CommonProgramFiles% instead of %commonprogramfiles%, it is not replaced.
-   The string cannot exceed MAX\_PATH\*2+15 characters. If it exceeds this length, it is not replaced.
-   The key cannot be opened with KEY\_WOW64\_64KEY. This flag specifies that operations on the key should be performed on the 64-bit registry view, so it is not replaced. For more information, see [Accessing an Alternate Registry View](accessing-an-alternate-registry-view.md).

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** The KEY\_WOW\_64\_64KEY flag does not affect whether a key is replaced. This flag affects replacement starting with Windows 7 and Windows Server 2008 R2.

In addition, REG\_SZ or REG\_EXPAND\_SZ keys containing system32 are replaced with syswow64. The string must begin with the path pointing to or under %windir%\\system32. The string comparison is not case-sensitive. Environment variables are expanded before matching the path, so all of the following paths are replaced: %windir%\\system32, %SystemRoot%\\system32, and C:\\windows\\system32. This patch is applied only to the keys that were reflected prior to Windows 7.

For more information, see the following topics:

-   [Registry Reflection](registry-reflection.md)
-   [Registry Keys Affected by WOW64](shared-registry-keys.md)
-   [Accessing an Alternate Registry View](accessing-an-alternate-registry-view.md)
-   [Example of Registry Redirection on WOW64](example-of-registry-reflection-and-redirection-on-wow64.md)
-   [Remote Registry Access in 64-bit Windows](remote-registry-access-in-64-bit-windows.md)

 

 




