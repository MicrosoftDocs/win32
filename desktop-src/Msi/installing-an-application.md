---
Description: You can install entire products with Windows Installer functions. The following steps describe how to install a product.
ms.assetid: 03cc7abc-63bd-4a01-a05c-9f7928de8827
title: Installing an Application
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installing an Application

You can install entire products with Windows Installer functions. The following steps describe how to install a product.

**To install a product**

1.  Run a product through its installation or uninstallation sequence by calling the [**MsiInstallProduct**](/windows/win32/Msi/nf-msi-msiinstallproducta?branch=master) function.
2.  Specify the installation level by calling the [**MsiConfigureProduct**](/windows/win32/Msi/nf-msi-msiconfigureproducta?branch=master) function.

    You can use the parameters of the [**MsiConfigureProduct**](/windows/win32/Msi/nf-msi-msiconfigureproducta?branch=master) function to set the installation state. For example, you can set the state to install locally or to install from the source. You can set the range of product features to be included by setting the level.

For more information about installing an application, see [Resiliency](resiliency.md) and [Installation Mechanism](installation-mechanism.md).

 

 



