---
Description: In Windows 8.1 and Windows 10, the GetVersion and GetVersionEx functions have been deprecated.
ms.assetid: E7A1A16A-95B3-4B45-81AD-A19E33F15AE4
title: Targeting your application for Windows
ms.topic: article
ms.date: 05/31/2018
---

# Targeting your application for Windows

In Windows 8.1 and Windows 10, the [**GetVersion**](https://msdn.microsoft.com/en-us/library/ms724439(v=VS.85).aspx) and [**GetVersionEx**](https://msdn.microsoft.com/en-us/library/ms724451(v=VS.85).aspx) functions have been deprecated. In Windows 10, the [**VerifyVersionInfo**](/windows/desktop/api/Winbase/nf-winbase-verifyversioninfoa) function has also been deprecated. While you can still call the deprecated functions, if your application does not specifically target Windows 8.1 or Windows 10, the functions will return the Windows 8 version (6.2).

> [!Note]  
> [**GetVersion**](https://msdn.microsoft.com/en-us/library/ms724439(v=VS.85).aspx), [**GetVersionEx**](https://msdn.microsoft.com/en-us/library/ms724451(v=VS.85).aspx), [**VerifyVersionInfo**](/windows/desktop/api/Winbase/nf-winbase-verifyversioninfoa), and the [Version Helper functions](version-helper-apis.md) are for desktop apps only. Universal Windows apps can use the [**AnalyticsInfo.VersionInfo**](https://docs.microsoft.com/uwp/api/windows.system.profile.analyticsinfo.versioninfo) property for telemetry and diagnostic logs.

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
</assembly>
```

Declaring support for Windows 8.1 or Windows 10 in your app manifest will not have any effect when running your app on previous operating systems.

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

 

 



