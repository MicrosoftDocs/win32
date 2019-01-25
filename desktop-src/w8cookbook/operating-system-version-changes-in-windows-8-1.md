---
title: Operating system version changes in Windows 8.1 and Windows Server 2012 R2
description: Operating system version changes in Windows 8.1 and Windows Server 2012 R2
ms.assetid: 3040262A-85EB-4F26-BE34-D2BBD5886E9E
ms.topic: article
ms.date: 05/31/2018
---

# Operating system version changes in Windows 8.1 and Windows Server 2012 R2

## Platforms

<dl> **Clients -** Windows 8.1  
**Servers -** Windows Server 2012 R2  
</dl>

## Description

We have made some significant changes in how the GetVersion(Ex) APIs work in Windows 8.1 due to undesirable customer behaviors resulting from how the GetVersion(Ex) APIs have been used in the past.

In previous versions of Windows, calling the GetVersion(Ex) APIs would return the actual version of the operating system (OS), unless the process had been mitigated by an app compat shim to give it a different version. This was done on a provisional basis and was relatively incomplete in terms of the number of processes that Microsoft could reasonably shim in a release. Many applications fell through the cracks because they didn’t get shimmed due to poorly designed version checks.

The number one reason to do a version check is to show some message of OS supportability for the application. However due to the poor checks, the message would often show that the app needed to be run on XP or later, which of course the newest OS is. More often than not, the newest OS would run the application without any issues if not for these checks.

## Manifestation

In Windows 8.1, the GetVersion(Ex) APIs have been deprecated. That means that while you can still call the APIs, if your app does not specifically target Windows 8.1, you will get Windows 8 versioning (6.2.0.0).

## Solution

In order to target Windows 8.1, you need to either include the app manifest or include \_NT\_TARGET\_VERSION=$ (\_NT\_TARGET\_VERSION\_LATEST) in the source file.

This is what the app manifest would look like:


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
         *  <!-- Windows 8.1 -->
         *  <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/>
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



And then add this to your sources:

<dl> SXS\_MANIFEST\_RESOURCE\_ID=1  
SXS\_MANIFEST=foo.manifest  
SXS\_ASSEMBLY\_NAME=Microsoft.Windows.Foo  
SXS\_ASSEMBLY\_VERSION=1.0  
SXS\_ASSEMBLY\_LANGUAGE\_INDEPENDENT=1  
SXS\_MANIFEST\_IN\_RESOURCES=1  
</dl>

For Windows 8.1, the two lines above marked with an asterisk (\*) show how to accurately target your application for the Windows 8.1 version of the operating system. Manifesting the .exe for Windows 8.1 will not have any impact when run on previous operating systems. You can also add this to your .rc file if you already have it defined.

Adding the trustInfo isn’t essential, but it is highly recommended. This will allow your .exe to always get the correct version, no matter whether the operating system is Windows 8.1 or Windows 8.

The replacement APIs are known as VersionHelpers. They are extremely easy to use; all you have to do is \#include <VersionHelpers.h>.

**Example**

The inline functions available in the VersionHelpers.h header file enable you to verify the version of the operating system by returning a Boolean value when testing for the version of Windows. For example, if your application requires Windows 8 or later, use the following test:


```
C++
#include <VersionHelpers.h>
…
    if (!IsWindows8OrGreater())
    {
       MessageBox(NULL, "You need at least Windows 8", "Version Not Supported", MB_OK);
    }
```



The available APIs are:

<dl> \#define VERSIONHELPERAPI FORCEINLINE BOOL  
VERSIONHELPERAPI IsWindowsXPOrGreater()  
VERSIONHELPERAPI IsWindowsXPSP1OrGreater()  
VERSIONHELPERAPI IsWindowsXPSP2OrGreater()  
VERSIONHELPERAPI IsWindowsXPSP3OrGreater()  
VERSIONHELPERAPI IsWindowsVistaOrGreater()  
VERSIONHELPERAPI IsWindowsVistaSP1OrGreater()  
VERSIONHELPERAPI IsWindowsVistaSP2OrGreater()  
VERSIONHELPERAPI IsWindows7OrGreater()  
VERSIONHELPERAPI IsWindows7SP1OrGreater()  
VERSIONHELPERAPI IsWindows8OrGreater()  
VERSIONHELPERAPI IsWindows8\_1OrGreater()  
VERSIONHELPERAPI IsWindowsServer()  
</dl>

They will return TRUE or FALSE depending on the question you are asking, and you only need to define the minimum level operating system that you support.

## Resources

-   [Application Compatibility Toolkit Download](https://go.microsoft.com/fwlink/p/?LinkID=205020)
-   [Known Compatibility Fixes, Compatibility Modes, and AppHelp Messages](https://go.microsoft.com/fwlink/p/?LinkID=205039)
-   [VersionHelpers APIs](https://go.microsoft.com/fwlink/p/?LinkId=325426)

 

 




