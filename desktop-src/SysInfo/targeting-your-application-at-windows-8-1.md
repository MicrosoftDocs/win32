---
description: In Windows 8.1 and Windows 10, the GetVersion and GetVersionEx functions have been deprecated.
ms.assetid: E7A1A16A-95B3-4B45-81AD-A19E33F15AE4
title: Targeting your application for Windows
ms.topic: article
ms.date: 05/31/2018
---

# Targeting your application for Windows

In Windows 8.1 and Windows 10, the [**GetVersion**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversion) and [**GetVersionEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa) functions have been deprecated. In Windows 10, the [**VerifyVersionInfo**](/windows/win32/api/winbase/nf-winbase-verifyversioninfoa) function has also been deprecated. While you can still call the deprecated functions, if your application does not specifically target Windows 8.1 or Windows 10, the functions will return the Windows 8 version (6.2).

> [!Note]  
> [**GetVersion**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversion), [**GetVersionEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa), [**VerifyVersionInfo**](/windows/win32/api/winbase/nf-winbase-verifyversioninfoa), and the [Version Helper functions](version-helper-apis.md) are for desktop apps only. Universal Windows apps can use the [**AnalyticsInfo.VersionInfo**](/uwp/api/windows.system.profile.analyticsinfo.versioninfo) property for telemetry and diagnostic logs.

In order for your app to target Windows 8.1 or Windows 10, you'll need to include an [app (executable) manifest](/windows/compatibility/application-executable-manifest) for the app's executable. Then, in the [**&lt;compatibility&gt;** section](../SbsCs/application-manifests.md#compatibility) of the manifest, you'll need to add a **&lt;supportedOS&gt;** element for each Windows version you want to declare that your app supports.

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
            <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/>
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
    <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
        <security>
            <requestedPrivileges>
                <!--
                  UAC settings:
                  - app should run at same integrity level as calling process
                  - app does not need to manipulate windows belonging to
                    higher-integrity-level processes
                  -->
                <requestedExecutionLevel
                    level="asInvoker"
                    uiAccess="false"
                />   
            </requestedPrivileges>
        </security>
    </trustInfo>
</assembly>
```

Declaring support for Windows 8.1 or Windows 10 in your app manifest will not have any effect when running your app on previous operating systems.

The above app manifest also includes a [**&lt;trustInfo&gt;** section](/previous-versions/bb756929(v=msdn.10)), which specifies how the system should treat it with respect to [User Account Control (UAC)](/windows/security/identity-protection/user-account-control/how-user-account-control-works). Adding **trustInfo** isn't essential, but it is highly recommended, even when your app doesn't need any particular UAC-related behavior. In particular, if you don't add **trustInfo** at all, then 32-bit x86 versions of your app will be subject to [UAC file virtualization](/windows/security/identity-protection/user-account-control/how-user-account-control-works#virtualization), which allows writes to administrator-privileged folders like the Windows system folders to succeed when they would otherwise fail, but redirects them to a user-specific "VirtualStore" folder.

## Related topics

<dl> <dt>

[Getting the system version](getting-the-system-version.md)
</dt> <dt>

[Version Helper functions](version-helper-apis.md)
</dt> <dt>

[OSVERSIONINFO](/windows/desktop/api/winnt/ns-winnt-osversioninfoa)
</dt> <dt>

[OSVERSIONINFOEX](/windows/desktop/api/winnt/ns-winnt-osversioninfoexa)
</dt> </dl>
