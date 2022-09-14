---
description: This is a per-machine system policy that can be used to apply upgrade component rules during small updates and minor upgrades.
ms.assetid: 0d39c059-d936-454c-aed8-efedd3da7473
title: EnforceUpgradeComponentRules
ms.topic: article
ms.date: 05/31/2018
---

# EnforceUpgradeComponentRules

This is a per-machine [system policy](system-policy.md) that can be used to apply upgrade component rules during [small updates](small-updates.md) and [minor upgrades](minor-upgrades.md).

Set the EnforceUpgradeComponentRules policy to 1 to apply upgrade component rules during [small updates](small-updates.md) and [minor upgrades](minor-upgrades.md) of all products on the computer. To apply the rules during small updates and minor upgrades of a particular product, set the [**MSIENFORCEUPGRADECOMPONENTRULES**](msienforceupgradecomponentrules.md) property to 1 on the command line or in the [Property table](property-table.md).

When the property or policy has been set to 1, [small updates](small-updates.md) and [minor upgrades](minor-upgrades.md) can fail because the update attempts to do the following:

-   Add a new feature to the top or middle of an existing feature tree.

    The new feature must be added as a new leaf feature to an existing feature tree.

    In this case, the [**ProductCode**](productcode.md) of the product can be changed and the updates can be treated as a [major upgrade](major-upgrades.md).

-   Remove a component from a feature.

    This can also occur if you change the GUID of a component. The component identified by the original GUID appears to be removed and the component as identified by the new GUID appears as a new component.

    **Windows Installer 4.5 and later:** The component can be removed correctly using Windows Installer 4.5 or later by setting the **msidbComponentAttributesUninstallOnSupersedence** attribute in the [Component table](component-table.md) or by setting the [**MSIUNINSTALLSUPERSEDEDCOMPONENTS**](msiuninstallsupersededcomponents.md) property.

    Alternatively, the [**ProductCode**](productcode.md) of the product can be changed and the updates can be treated as a [major upgrade](major-upgrades.md).

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



