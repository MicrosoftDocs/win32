---
description: You can install entire products with Windows Installer functions. The following steps describe how to install a product.
ms.assetid: 03cc7abc-63bd-4a01-a05c-9f7928de8827
title: Installing an Application
ms.topic: article
ms.date: 05/31/2018
---

# Installing an Application

You can install entire products with Windows Installer functions. The following steps describe how to install a product.

**To install a product**

1.  Run a product through its installation or uninstallation sequence by calling the [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta) function.
2.  Specify the installation level by calling the [**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta) function.

    You can use the parameters of the [**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta) function to set the installation state. For example, you can set the state to install locally or to install from the source. You can set the range of product features to be included by setting the level.

For more information about installing an application, see [Resiliency](resiliency.md) and [Installation Mechanism](installation-mechanism.md).

 

 



