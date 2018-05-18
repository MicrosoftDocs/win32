---
Description: 'You can install entire products with Windows Installer functions. The following steps describe how to install a product.'
ms.assetid: '03cc7abc-63bd-4a01-a05c-9f7928de8827'
title: Installing an Application
---

# Installing an Application

You can install entire products with Windows Installer functions. The following steps describe how to install a product.

**To install a product**

1.  Run a product through its installation or uninstallation sequence by calling the [**MsiInstallProduct**](msiinstallproduct.md) function.
2.  Specify the installation level by calling the [**MsiConfigureProduct**](msiconfigureproduct.md) function.

    You can use the parameters of the [**MsiConfigureProduct**](msiconfigureproduct.md) function to set the installation state. For example, you can set the state to install locally or to install from the source. You can set the range of product features to be included by setting the level.

For more information about installing an application, see [Resiliency](resiliency.md) and [Installation Mechanism](installation-mechanism.md).

 

 



