---
title: Packaging, deployment, and query of Windows apps
description: Programmatically create app packages for Windows apps, and install, update, query, and uninstall app packages.
ms.assetid: 4ea65e62-4878-41fd-9ad8-424b1546f02a
ms.topic: article
ms.date: 05/31/2018
---

# Packaging, deployment, and query of Windows apps

You deploy, manage, and service Windows apps (including UWPs and desktop apps) through .msix/.appx app packages based on the OPC format. Each app package contains the files that constitute the app, and a manifest file that describes the software to Windows.

## Introduction

Typically, developers create and sign app packages using Visual Studio. For more info, see [Package a UWP app with Visual Studio](/windows/msix/package/packaging-uwp-apps).

The Microsoft Store makes it easy to build, submit, and sell your apps to customers around the world. For more info, see [App submissions](/windows/uwp/publish/app-submissions).

Windows PowerShell cmdlets enable you to install and manage line-of-business Windows apps without using the Store. For more info, see [Appx Module Cmdlets](/powershell/module/appx/index).

Using the packaging, deployment, and query APIs, you can programmatically perform these tasks:

-   Create an app package for a Windows app
-   Deploy a packaged Windows app
-   Enumerate the app packages installed on a system and get information about them from their manifest
-   Consume the contents of an app package

## In this section



| Topic                                                                                                    | Description                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [How to create an app package (C++)](how-to-create-a-package.md)                                        | Learn how to create an app package using the packaging API.                                                                                                                           |
| [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md)      | Learn how to use [**MakeCert**](/windows-hardware/drivers/devtest/makecert) and [**Pvk2Pfx**](/windows-hardware/drivers/devtest/pvk2pfx) to create a test code signing certificate, so that you can sign your app packages. |
| [How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md)                    | Learn how to use [**SignTool**](/windows-hardware/drivers/devtest/signtool) to sign your app packages so they can be deployed.                                                                    |
| [How to troubleshoot app package signature errors](how-to-troubleshoot-app-package-signature-errors.md) | An app deployment failure can be caused by a failure to validate the digital signature of the app package. Learn how to recognize these failures, and what to do about them.          |
| [How to programmatically sign an app package (C++)](how-to-programmatically-sign-a-package.md)          | Learn how to sign an app package by using the [**SignerSignEx2**](/windows/desktop/SecCrypto/signersignex2) function.                                                                                   |
| [How to develop an OEM app that uses a custom file](how-to-develop-oem-app-with-custom-file.md)         | Learn how to develop an app that uses a custom file to pass info from the OEM to the app.                                                                                             |
| [Extract app package contents (C++)](how-to-extract-content-from-a-package.md)                          | Learn how to extract files from an app package using the packaging API.                                                                                                               |
| [Query app package manifest info (C++)](how-to-query-package-identity-information.md)                   | Learn how to get info from an app package manifest using the packaging API                                                                                                            |
| [Troubleshooting](troubleshooting.md)                                                                   | Provides info to help you troubleshoot problems you experience when packaging, deploying, or querying an app package.                                                                 |
| [Packaging API reference](interfaces.md)                                                                | The packaging API creates, reads, and writes app packages.                                                                                                                            |
| [Deployment API reference](package-deployment-api.md)                                                   | The deployment API installs, updates, and uninstalls app packages.                                                                                                                    |
| [Query API reference](functions.md)                                                                     | The query API gets info about the app packages installed on the system.                                                                                                               |
| [Tools and PowerShell cmdlets](appx-packaging-tools.md)                                                 | Use these tools and cmdlets to create, install, and manage app packages.                                                                                                              |
| [SDK samples](appx-packaging-samples.md)                                                                | Download SDK samples that demonstrate the packaging, deployment, and query APIs for Windows apps.                                                                               |
| [Glossary](appx-packaging-glossary.md)                                                                  | Learn about the terms related to packaging, deployment, and query of Windows apps.                                                                                              |



 

## Related topics

<dl> <dt>

**Concepts**
</dt> <dt>

[App packages and deployment](/previous-versions/windows/apps/hh464929(v=win.10))
</dt> <dt>

**Other Reference**
</dt> <dt>

[App package manifest schema](/uwp/schemas/appxpackage/appx-package-manifest)
</dt> <dt>

[**Windows.ApplicationModel.Package**](/uwp/api/Windows.ApplicationModel.Package)
</dt> <dt>

[**Windows.ApplicationModel.PackageId**](/uwp/api/Windows.ApplicationModel.PackageId)
</dt> <dt>

[**Windows.Management.Deployment.PackageManager**](/uwp/api/Windows.Management.Deployment.PackageManager)
</dt> <dt>

[**Windows.Management.Deployment.PackageUserInformation**](/uwp/api/Windows.Management.Deployment.PackageUserInformation)
</dt> </dl>

 

 