---
title: Developing Applications for Previous Versions of Windows
description: Explains what to do to develop applications that run on previous versions of Windows and take advantage of the API that are supported with the Platform Update for Windows Vista and the Platform Update for Windows Server 2008.
ms.assetid: 9c46f894-e5cd-46a1-81c8-f63b09504735
ms.topic: article
ms.date: 05/31/2018
---

# Developing Applications for Previous Versions of Windows

Explains what to do to develop applications that run on previous versions of Windows and take advantage of the API that are supported with the Platform Update for Windows Vista and the Platform Update for Windows Server 2008.

## Required Downloads

Download and installation of the packages described in the following sections is required if you want to develop applications that use API that are introduced with the Microsoft Windows Software Development Kit (SDK) for Windows 7.

### Microsoft Windows SDK

The Windows SDK for Windows 7 is required for creating applications that use APIs supported with the Platform Update for Windows Vista and the Platform Update for Windows Server 2008.

For access to additional resources and information, such as downloads, forum posts, and the Windows SDK team blog, see the [Windows SDK Developer Center](https://msdn.microsoft.com/bb980924.aspx) (https://msdn.microsoft.com/bb980924.aspx).

### .NET Framework

The .NET Framework 3.5 Service Pack 1 is required for creating applications that use APIs supported by the Platform Update for Windows Vista and the Platform Update for Windows Server 2008.

For additional resources and information, see the [.NET Framework Developer Center](https://msdn.microsoft.com/netframework/default.aspx) (https://msdn.microsoft.com/netframework/default.aspx).

### DirectX SDK Required When Using Direct3D

If you create applications that use Direct3D, the [DirectX SDK](/previous-versions/windows/apps/hh452744(v=win.10)) (https://msdn.microsoft.com/directx/aa937788.aspx) is required for creating applications that use APIs supported by the Platform Update for Windows Vista and the Platform Update for Windows Server 2008.

### Update Your Development Computer

Ensure that your development computer has all of the latest updates from Windows Update.

If you are developing applications on a previous version of Windows, you must obtain the Platform Update for Windows Vista or the Platform Update for Windows Server 2008 update from Windows Update. Installing either of these updates will enable you to take advantage of the new API provided by the Windows SDK for Windows 7.

For more information about how to obtain updates from Windows Update see the [Knowledge Base article about the Platform Update for Windows Vista (KB 971644)](https://support.microsoft.com/kb/971644) (https://support.microsoft.com/kb/971644).

## Development Environment

### Set the Build Target to Windows 7

All applications that use libraries in the Platform Update for Windows Vista must be built against the Windows 7 target platform.

Setting WINVER to the Windows 7 target platform value enables you to develop applications that use APIs supported with the Platform Update for Windows Vista or the Platform Update for Windows Server 2008 on a development machine running Windows Vista.

You can set the target platform to Windows 7 either in your source code or by using the /D option with the Visual Studio compiler.

The following example shows how to set WINVER in your source code.


```C++
#define WINVER 0x0601
```



The following example shows how to set WINVER using the /D compiler option.

``` syntax
/DWINVER=0x0601
```

## Application Deployment

If you build your application using the headers and libraries provided by the Windows SDK for Windows 7, supported APIs will run on any Windows version that has the Platform Update for Windows Vista or the Platform Update for Windows Server 2008 installed.

> [!Note]  
> The behavior, performance, or requirements for some APIs that are supported with the Platform Update for Windows Vista or the Platform Update for Windows Server 2008 may vary across different versions of Windows. For details about a specific API that is supported by the updates, see [About Platform Update for Windows Vista](platform-update-for-windows-vista-overview.md).

 

### No Redistributable Components

Your application does not need to install redistributable components, such as DLLs or other run-time files.

### Requires Updated End-User Computer

Because Platform Update for Windows Vista and Platform Update for Windows Server 2008 are hosted by Windows Update, end-users with automatic updates enabled are highly likely to already have these updates as well as the required service packs.

If the end-user's computer does not have Platform Update for Windows Vista or Platform Update for Windows Server 2008 installed and your application requires APIs that are supported with these updates, your application may not be able to run on the end-user's computer or may encounter errors during execution.

To avoid the problems that could be caused by your user's computer being out-of-date, you want to verify that your user's computer has the Platform Update for Windows Vista or the Platform Update for Windows Server 2008 update during the installation of your application. You can use the [Windows Update Agent API](/windows/desktop/Wua_Sdk/portal-client) to check your end-user's computer for installed updates. You can also use the Windows Update Agent API to download and install required updates during application installation if the end-user has not already installed the updates.

For an example of an installer that demonstrates how to use the [Windows Update Agent API](/windows/desktop/Wua_Sdk/portal-client), see [Direct3D 11 Deployment for Game Developers](../direct3darticles/direct3d11-deployment.md) in the [DirectX SDK](/previous-versions/windows/apps/hh452744(v=win.10)) (https://msdn.microsoft.com/directx/aa937788.aspx).

Although the D3D11InstallHelper installer sample that is discussed in [Direct3D 11 Deployment for Game Developers](../direct3darticles/direct3d11-deployment.md), was written for applications that use Direct3D 11, it provides a good example of how to interact with the [Windows Update Agent API](/windows/desktop/Wua_Sdk/portal-client) to initiate and track the download and installation of updates that are hosted by Windows Update. Compiling this sample may require the Windows SDK for Windows 7. For additional information about the D3D11InstallHelper sample, including known issues, see the [DirectX SDK](/previous-versions/windows/apps/hh452744(v=win.10)) (https://msdn.microsoft.com/directx/aa937788.aspx) Release Notes for August 2009.Platform Update for Windows Vista

## Related topics

<dl> <dt>

[Platform Update for Windows Vista](platform-update-for-windows-vista-portal.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[About Platform Update for Windows Vista](platform-update-for-windows-vista-overview.md)
</dt> <dt>

[Knowledge Base article about the Platform Update for Windows Vista (KB 971644)](https://support.microsoft.com/kb/971644)
</dt> </dl>

 

 