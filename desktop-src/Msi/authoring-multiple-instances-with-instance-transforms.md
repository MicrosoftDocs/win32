---
description: To install multiple instances of a product from one Windows Installer package, you need to author a base installation package for the product and an instance transform for each instance to be installed in addition to the base instance.
ms.assetid: fef49dda-503f-4b13-8763-70cb2ee0df5d
title: Authoring Multiple Instances with Instance Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Multiple Instances with Instance Transforms

To install multiple instances of a product from one Windows Installer package, you need to author a base installation package for the product and an instance transform for each instance to be installed in addition to the base instance. Use the following guidelines when authoring your base package and transforms:

-   Your setup application can check for the presence of the installer running on a version of Windows Vista, Windows Server 2003, Windows XP with Service Pack 1 (SP1), and the Windows Installer 3.0 redistributable. Any of these installer versions (or later) are required to install multiple instances from a single package using a product code–changing transform.
-   Each instance must have a unique product code and instance identifier. You may define a property in the base package, the value of which can be set to the instance identifier.
-   To keep the files of each instance isolated, the base package should install files into a directory location that depends on the instance identifier.
-   To keep the nonfile data of each instance isolated, the base package should collect nonfile data into sets of components for each instance. The appropriate components should then be installed based on conditional statements that depend on the instance identifier.
-   Author an instance transform for each instance being installed in addition to the base instance. The base package may install its own instance.
-   The instance transform must change the product code and identifier for each instance.
-   It is recommended that the product transform also change the product name so that the instance is readily distinguished in Add/Remove Programs through Control Panel.
-   If the instance transform installs files, they should be installed in a directory that depends on the instance identifier.
-   All nonfile data, such as registry keys, should include the instance name in their path to prevent collisions. This can be accomplished by using the property whose value is the instance identifier in the path as shown by the following example of a [Registry Table](registry-table.md).



| Registry | Root | Key                                            | Name         | Value           | Component\_      |
|----------|------|------------------------------------------------|--------------|-----------------|------------------|
| Reg1     | 1    | Software\\Microsoft\\MyProduct\\\[InstanceId\] | InstanceGuid | \[ProductCode\] | NonFileDataComp1 |



 

For more information, see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md) and [Installing Multiple Instances with Instance Transforms](installing-multiple-instances-with-instance-transforms.md).

 

 



