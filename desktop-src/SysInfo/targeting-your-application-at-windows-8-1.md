---
Description: In Windows 8.1 and Windows 10, the GetVersion and GetVersionEx functions have been deprecated.
ms.assetid: E7A1A16A-95B3-4B45-81AD-A19E33F15AE4
title: Targeting your application for Windows
ms.topic: article
ms.date: 05/31/2018
---

# Targeting your application for Windows

In Windows 8.1 and Windows 10, the [**GetVersion**](https://msdn.microsoft.com/en-us/library/ms724439(v=VS.85).aspx) and [**GetVersionEx**](https://msdn.microsoft.com/en-us/library/ms724451(v=VS.85).aspx) functions have been deprecated. In Windows 10, the [**VerifyVersionInfo**](/windows/desktop/api/Winbase/nf-winbase-verifyversioninfoa) function has also been deprecated. While you can still call the deprecated functions, if your application does not specifically target Windows 8.1 or Windows 10, you will get Windows 8 version (6.2.0.0).

> [!Note]  
> [**GetVersion**](https://msdn.microsoft.com/en-us/library/ms724439(v=VS.85).aspx), [**GetVersionEx**](https://msdn.microsoft.com/en-us/library/ms724451(v=VS.85).aspx), [**VerifyVersionInfo**](/windows/desktop/api/Winbase/nf-winbase-verifyversioninfoa), and the [Version Helper functions](version-helper-apis.md) are for desktop apps only. Universal Windows apps can use the [**AnalyticsInfo.VersionInfo**](https://msdn.microsoft.com/library/windows/apps/dn960164) property for telemetry and diagnostic logs.

 

In order to target Windows 8.1 or Windows 10, you need to include the app manifest in the source file. The following example shows an app manifest file.


```XML
<exe>.manifest
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
    <assemblyIdentity 
        type="win32" 
        name=SXS_ASSEMBLY_NAME
        version=SXS_ASSEMBLY_VERSION
        processorArchitecture=SXS_PROCESSOR_ARCHITECTURE
    />
    <description> my exe </description>
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
            <!-- Windows 10 --> 
            <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/>
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



Next, add the following to your sources:

``` syntax
SXS_MANIFEST_RESOURCE_ID=1
SXS_MANIFEST=foo.manifest
SXS_ASSEMBLY_NAME=Microsoft.Windows.Foo
SXS_ASSEMBLY_VERSION=1.0    
SXS_ASSEMBLY_LANGUAGE_INDEPENDENT=1
SXS_MANIFEST_IN_RESOURCES=1
```

Manifesting the **.exe** for Windows 8.1 or Windows 10 will not have any impact when run on previous operating systems. You can also add this to your **.rc** file if you already have it defined.

Adding the **trustInfo** isn’t essential, but it is highly recommended. This will allow your **.exe** to always get the correct version, whether the operating system is Windows 10, Windows 8.1, or Windows 8.

## Related topics

<dl> <dt>

[Getting the system version](https://docs.microsoft.com/windows)
</dt> <dt>

[Version Helper functions](version-helper-apis.md)
</dt> <dt>

[OSVERSIONINFO](https://docs.microsoft.com/windows)
</dt> <dt>

[OSVERSIONINFOEX](https://docs.microsoft.com/windows)
</dt> </dl>

 

 



