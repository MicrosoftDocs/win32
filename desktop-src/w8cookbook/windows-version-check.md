---
title: Windows version check
description: The OS version has been incremented with the Windows 10 OS release.
ms.assetid: 55BB7B44-1AFD-456D-9380-38B4D26E5EF6
ms.topic: article
ms.date: 05/31/2018
---

# Windows version check

The OS version has been incremented with the Windows 10 OS release. This means that the internal version number for Windows 10 has also been changed to 10.0. As in the past, we go to great lengths to maintain application and device compatibility after an OS version change. For most app categories (without any kernel dependencies) the change will not negatively impact app functionality, and existing apps will continue to work fine on Windows 10.

## Manifestations

The manifestation of this change is app-specific. This means any app that specifically checks for the OS version will get a higher version number, which can lead to one or more of the following situations:

-   App installers might not be able to install the app, and apps might not be able to start.
-   Apps might become unstable or crash.
-   Apps might generate error messages, but continue to function properly.

Some apps perform a version check and simply pass a warning to users. However, there are apps that are bound very tightly to a version check (in the drivers, or in kernel mode to avoid detection). In these cases, the app will fail if an incorrect version is found. Rather than a version check, we recommend one of the following approaches:

-   If the app is dependent on specific API functionality, ensure you target the correct API version.
-   NTDDI (NT device driver interface) version number will increment only if target functionality in the API changes. Ensure you detect the change via APISet or other exposed API as created by the feature team, and do not use the version as a proxy for some feature or fix. If there are breaking changes and a proper check is not exposed, then that is a bug.
-   Ensure the app does NOT check for version in odd ways, such as via the registry, file versions, offsets, kernel mode, drivers or other means. If the app absolutely needs to check the version, use the GetVersion APIs, which should return the major, minor and build number.
-   If you are using the GetVersion API or other Version Helper functions such as [VerifyVersionInfo](/windows/desktop/api/winbase/nf-winbase-verifyversioninfoa), remember that the behavior of this API has changed starting with Windows 8.1. Please refer to [the API documentation](../SysInfo/version-helper-apis.md) for more details.
-   If you own apps such as antimalware or firewall, you should work through your usual feedback channels and via the Windows Insider program.

## Declaring Windows 10 Compatibility With An App Manifest

If your app is compatible with Windows 10, it can declare this fact in the [app (executable) manifest](/windows/compatibility/application-executable-manifest) for the app's executable. This tells the system that your app understands Windows 10's system version number of 10.0 (so the GetVersion API does not return an earlier version), and also lets the system turn off other compatibility behaviors applied to apps that don't declare Windows 10 compatibility.

To declare Windows 10 compatibility in an app manifest, you'll need to add a [**&lt;compatibility&gt;** section](../SbsCs/application-manifests.md#compatibility) of the manifest if one does not already exist, and then add **&lt;supportedOS&gt;** elements for Windows 10 and every other Windows version you want to declare that your app supports.

The following example shows an app manifest file for an app that supports all versions of Windows from Windows Vista to Windows 10:

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
            <!-- Windows 10 -->
            <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/> <!-- * ADD THIS LINE * -->
            <!-- Windows 8.1 -->
            <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/>
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

The line above marked `* ADD THIS LINE *` shows how to accurately target your application for Windows 10.

Declaring support for Windows 10 in your app manifest will not have any effect when running your app on previous operating systems.

## Resources

-   [Application Compatibility Toolkit Download: Download the Windows ADK for Windows 10](https://download.microsoft.com/download/9/A/E/9AE69DD5-BA93-44E0-864E-180F5E700AB4/adk/adksetup.exe)
-   [Known Compatibility Fixes, Compatibility Modes, and AppHelp Messages](/previous-versions/windows/it-pro/windows-7/cc765984(v=ws.10))
-   [Version Helpers API](../sysinfo/version-helper-apis.md)