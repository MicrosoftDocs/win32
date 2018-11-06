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
-   If you are using the GetVersion API or other Version Helper functions such as [VerifyVersionInfo](https://msdn.microsoft.com/library/windows/desktop/ms725492.aspx), remember that the behavior of this API has changed since Windows 8.1. Please refer to [the API documentation](https://msdn.microsoft.com/library/windows/desktop/dn424972.aspx) for more details.
-   If you own apps such as antimalware or firewall, you should work through your usual feedback channels and via the Windows Insider program.

## App Manifest

Below is an example app manifest:


```
<exe>.manifest
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
    <assemblyIdentity 
        type="win32" 
        name=SXS_ASSEMBLY_NAME
        version=SXS_ASSEMBLY_VERSION
        processorArchitecture=SXS_PROCESSOR_ARCHITECTURE
    />
    <description> my app exe </description>
    <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
        <security>
            <requestedPrivileges>
                <requestedExecutionLevel
                    level="asInvoker"
                    uiAccess="false"
                />   
            </requestedPrivileges>
        </security>
    </trustInfo>
    <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"> 
        <application> 

      * <!-- Windows 10 --> 
      * <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/>
            <!-- Windows 8.1 -->
            <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/>
            <!-- Windows Vista -->
            <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/> 
            <!-- Windows 7 -->
            <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
            <!-- Windows 8 -->
            <supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/>
        </application> 
    </compatibility>
</assembly>
```



Add these variables to your sources:<dl> SXS\_MANIFEST\_RESOURCE\_ID=1  
SXS\_MANIFEST=foo.manifest  
SXS\_ASSEMBLY\_NAME=Microsoft.Windows.Foo  
SXS\_ASSEMBLY\_VERSION=1.0  
SXS\_ASSEMBLY\_LANGUAGE\_INDEPENDENT=1  
SXS\_MANIFEST\_IN\_RESOURCES=1  
</dl>For Windows 10, the two lines above marked with an asterisk (\*) show how to accurately target your application for the Windows 10 version of the OS. Manifesting the .exe for Windows 10 will not have any impact when run on previous versions of the Windows OS. You can also add this to your .rc file if you already have it defined.

Adding the trustInfo isn’t essential, but it is highly recommended. This will allow your .exe to always get the correct version, no matter whether the OS is Windows 10 or Windows 8.1.

## Resources

-   [Application Compatibility Toolkit Download: Download the Windows ADK for Windows 10](http://go.microsoft.com/fwlink/p/?LinkId=526740)
-   [Known Compatibility Fixes, Compatibility Modes, and AppHelp Messages](http://go.microsoft.com/fwlink/?LinkID=205039)
-   [Version Helpers API](http://go.microsoft.com/fwlink/p/?LinkId=325426)

 

 




