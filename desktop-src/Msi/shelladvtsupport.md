---
Description: The ShellAdvtSupport property is set by the installer if the system's IShellLink interface supports installer descriptor resolution.
ms.assetid: 8c3503c5-2a9c-43ad-8cc5-ea10df39b24d
title: ShellAdvtSupport property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShellAdvtSupport property

The **ShellAdvtSupport** property is set by the installer if the system's [**IShellLink**](https://www.bing.com/search?q=**IShellLink**) interface supports installer descriptor resolution.

## Remarks

If this property is set, the system's [**IShellLink**](https://www.bing.com/search?q=**IShellLink**) interface supports installer descriptor resolution. This is supported by Windows 2000 and systems running Internet Explorer 4.01. If this property is not set, the installer has the default behavior of creating non-advertised features during installation, either locally or run from source.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Platform Support of Advertisement](platform-support-of-advertisement.md)
</dt> </dl>

 

 




