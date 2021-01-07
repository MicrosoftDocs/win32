---
description: Windows Installer permits one instance of a product code to be installed per context, and the two possible types of context are the following:MachineUser If a product code remains unchanged, only one instance can be installed in the machine context and only one instance can be installed in each user context. For multiple instances to remain isolated, they must have different product codes and cannot share file data or nonfile data. The Windows Installer cannot install multiple instances of products using concurrent installations. However, you can install multiple instances of a product if you have a separate installation package for each instance of a product or patch. Then each package can keep its own set of data and have its own unique product code. Starting with the installer running Windows Server 2003 and Windows XP with Service Pack 1 (SP1), you can install multiple instances of a product by using product code transforms and one .msi package or one patch. You can also use product code transforms to install multiple instances of a product with Windows 2000 with Service Pack 4 (SP4) and Windows Installer&\#160; 3.0. The only way to install more than one instance of a product with previous versions of the installer is to have a separate installation package for each instance. Using instance transforms significantly reduces the effort needed to support multiple instances of a product. You can author one base Windows Installer package for a product and then multiple instance transforms that change the product code and manage data for each instance.For more information, see Authoring Multiple Instances with Instance Transforms and Installing Multiple Instances with Instance Transforms.
ms.assetid: 5147ecbd-c395-4a8f-972d-f5c5b2173eff
title: Installing Multiple Instances of Products and Patches
ms.topic: article
ms.date: 05/31/2018
---

# Installing Multiple Instances of Products and Patches

Windows Installer permits one instance of a product code to be installed per context, and the two possible types of context are the following:

-   Machine
-   User

If a product code remains unchanged, only one instance can be installed in the machine context and only one instance can be installed in each user context.

For multiple instances to remain isolated, they must have different product codes and cannot share file data or nonfile data. The Windows Installer cannot install multiple instances of products using [concurrent installations](concurrent-installations.md). However, you can install multiple instances of a product if you have a separate installation package for each instance of a product or patch. Then each package can keep its own set of data and have its own unique product code.

Starting with the installer running Windows Server 2003 and Windows XP with Service Pack 1 (SP1), you can install multiple instances of a product by using product code transforms and one .msi package or one patch. You can also use product code transforms to install multiple instances of a product with Windows 2000 with Service Pack 4 (SP4) and Windows Installer  3.0. The only way to install more than one instance of a product with previous versions of the installer is to have a separate installation package for each instance.

Using instance transforms significantly reduces the effort needed to support multiple instances of a product. You can author one base Windows Installer package for a product and then multiple instance transforms that change the product code and manage data for each instance.

For more information, see [Authoring Multiple Instances with Instance Transforms](authoring-multiple-instances-with-instance-transforms.md) and [Installing Multiple Instances with Instance Transforms](installing-multiple-instances-with-instance-transforms.md).

 

 



