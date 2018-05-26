---
Description: You can use the following scripts in batch files to remove all AD RMS licenses and certificates from a client machine. The scripts will also deactivate the machine but will not uninstall the AD RMS client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cc5ae51c-ee67-40e0-8c77-732ba2b6822f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Restoring a Client Computer to a Clean State
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Restoring a Client Computer to a Clean State

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You can use the following scripts in batch files to remove all AD RMS licenses and certificates from a client machine. The scripts will also deactivate the machine but will not uninstall the AD RMS client.

-   If you are using AD RMS on Windows Vista or later, run the following script.

    ``` syntax
    @echo off
    @echo Deleting Licenses From License Store
    del /q /f "%USERPROFILE%\AppData\Local\Microsoft\Drm\*.*"
    del /q /f /s "%ALLUSERSPROFILE%\Microsoft\DRM\Server\*.*"
    ```

-   If you are using RMS 1.0 SP2, run the following script.

    ``` syntax
    @echo off
    del /q /f /s "%ALLUSERSPROFILE%\Application Data\Microsoft\DRM\Server\*.*"
    del /q /f "%USERPROFILE%\Application Data\Microsoft\DRM\*.*"
    del /q /f "%USERPROFILE%\Local Settings\Application Data\Microsoft\DRM\*.*"
    del /q /f "%SYSTEMROOT%\system32\secrep.dll"
    del /q /f "%SYSTEMROOT%\system32\secure*.sst"
    attrib -h -s "%SYSTEMROOT%\system32\clockfile.drm"
    del /q /f "%SYSTEMROOT%\system32\clockfile.drm"
    ```

## Related topics

<dl> <dt>

[Production Client Settings](production-client-settings.md)
</dt> <dt>

[Switching to the Production Environment](switching-to-the-production-environment.md)
</dt> </dl>

 

 



