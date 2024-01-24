---
description: Whenever making any changes to the package, authors of upgrade packages should always run validation on their packages before attempting to install the package for the first time and rerun validation.
ms.assetid: c578c020-18be-47ea-8f59-c1bbd45f1260
title: Validating an Installation Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Validating an Installation Upgrade

Whenever making any changes to the package, authors of upgrade packages should always run validation on their packages before attempting to install the package for the first time and rerun validation. Run validation on an upgrade package in the same way as for an installation package. For details, see [Validating an Installation Database](validating-an-installation-database.md).

This completes the sample upgrade package. To install the upgrade first install MNP2000.msi and then install MNP2001.msi. When you uninstall MNP2001 both the original and upgrade products are removed from your computer.

## Next example

[A Customization Transform Example](a-customization-transform-example.md)

 

 



