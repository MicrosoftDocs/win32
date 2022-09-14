---
title: Operating system version changes in Windows 8.1 and Windows Server 2012 R2
description: Operating system version changes in Windows 8.1 and Windows Server 2012 R2
ms.assetid: 3040262A-85EB-4F26-BE34-D2BBD5886E9E
ms.topic: article
ms.date: 05/31/2018
---

# Operating system version changes in Windows 8.1 and Windows Server 2012 R2

## Platforms

**Clients -** Windows 8.1

**Servers -** Windows Server 2012 R2

## Description

We have made some significant changes in how the GetVersion(Ex) APIs work in Windows 8.1 due to undesirable customer behaviors resulting from how the GetVersion(Ex) APIs have been used in the past.

In previous versions of Windows, calling the GetVersion(Ex) APIs would return the actual version of the operating system (OS), unless the process had been mitigated by an app compat shim to give it a different version. This was done on a provisional basis and was relatively incomplete in terms of the number of processes that Microsoft could reasonably shim in a release. Many applications fell through the cracks because they didn’t get shimmed due to poorly designed version checks.

The number one reason to do a version check is to warn the user that the application needs to run on a newer version of the OS. However due to poor checks, apps would often incorrectly warn that they needed to be run on Windows XP or later, which of course the newest OS is. More often than not, the newest OS would run the application without any issues if not for these checks.

## Manifestation

In Windows 8.1, the GetVersion(Ex) APIs have been deprecated. That means that while you can still call these API functions, if your app does not specifically target Windows 8.1, the functions will return the Windows 8 version (6.2).

## Solution

### Adding an app manifest

In order for your app to target Windows 8.1, you'll need to include an [app (executable) manifest](/windows/compatibility/application-executable-manifest) for the app's executable. Then, in the [**&lt;compatibility&gt;** section](../SbsCs/application-manifests.md#compatibility) of the manifest, you'll need to add a **&lt;supportedOS&gt;** element for each Windows version you want to declare that your app supports.

The following example shows an app manifest file for an app that supports all versions of Windows from Windows Vista to Windows 8.1:

```XML
<!-- example.exe.manifest -->
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
    <assemblyIdentity
        type="win32"
        name="Contoso.ExampleApplication.ExampleBinary"
        version="1.2.3.4"
        processorArchitecture="x86"
    />
    <description>Contoso Example Application</description>
    <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">
        <application>
            <!-- Windows 8.1 -->
            <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/> <!-- * ADD THIS LINE * -->
            <!-- Windows 8 -->
            <supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/>
            <!-- Windows 7 -->
            <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
            <!-- Windows Vista -->
            <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/> 
        </application>
    </compatibility>
</assembly>
```

The line above marked `* ADD THIS LINE *` shows how to accurately target your application for Windows 8.1.

Declaring support for Windows 8.1 in your app manifest will not have any effect when running your app on previous operating systems.

### Using VersionHelpers instead of GetVersion(Ex)

Windows 8.1 introduces new replacement API functions for GetVersion(Ex), known as VersionHelpers. They are extremely easy to use; all you have to do is `#include <VersionHelpers.h>`. The inline functions available in the VersionHelpers.h header file allow your code to ask whether the operating system is a given version of Windows or later.

**Example**
For example, if your application requires Windows 8 or later, use the following test:

```cpp
#include <VersionHelpers.h>
// ...
    if (!IsWindows8OrGreater())
    {
       MessageBox(NULL, "You need at least Windows 8", "Version Not Supported", MB_OK);
    }
```

The available VersionHelper API functions are:

```c
#define VERSIONHELPERAPI FORCEINLINE BOOL
VERSIONHELPERAPI IsWindowsXPOrGreater();
VERSIONHELPERAPI IsWindowsXPSP1OrGreater();
VERSIONHELPERAPI IsWindowsXPSP2OrGreater();
VERSIONHELPERAPI IsWindowsXPSP3OrGreater();
VERSIONHELPERAPI IsWindowsVistaOrGreater();
VERSIONHELPERAPI IsWindowsVistaSP1OrGreater();
VERSIONHELPERAPI IsWindowsVistaSP2OrGreater();
VERSIONHELPERAPI IsWindows7OrGreater();
VERSIONHELPERAPI IsWindows7SP1OrGreater();
VERSIONHELPERAPI IsWindows8OrGreater();
VERSIONHELPERAPI IsWindows8Point1OrGreater();
VERSIONHELPERAPI IsWindowsServer();
```

They will return TRUE or FALSE depending on the question you are asking, and you only need to define the minimum level operating system that you support.

## Resources

-   [Application Compatibility Toolkit Download](https://www.microsoft.com/downloads/details.aspx?FamilyId=24DA89E9-B581-47B0-B45E-492DD6DA2971)
-   [Known Compatibility Fixes, Compatibility Modes, and AppHelp Messages](/previous-versions/windows/it-pro/windows-7/cc765984(v=ws.10))
-   [VersionHelpers APIs](../sysinfo/version-helper-apis.md)