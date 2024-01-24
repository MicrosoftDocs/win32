---
description: The installer sets the PATCH property to a list of patches being applied by calling MsiApplyPatch, MsiApplyMultiplePatches or the /p Command Line Option.
ms.assetid: 'f2993544-2124-4fb0-8bb3-59f5d8e76b83'
title: PATCH property
ms.topic: article
ms.date: 05/31/2018
---

# PATCH property

The installer sets the **PATCH** property to a list of patches being applied by calling [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha), [**MsiApplyMultiplePatches**](/windows/desktop/api/Msi/nf-msi-msiapplymultiplepatchesa) or the /p [Command Line Option](command-line-options.md). You can also set the **PATCH** property on the command line while installing a package using [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta) or the /i Command Line Option.

The value of the **PATCH** property is a list of the patches that are being installed. Each patch in the list is represented by the full path to the patch's package (.msp file.) The full paths in the list are separated by semicolons.

**Windows Installer 2.0:** Multiple patches are not supported. Windows Installer 3.0 is required to apply multiple patches.

## Remarks

If you create a patch package using [Msimsp.exe](msimsp-exe.md) and [Patchwiz.dll](patchwiz-dll.md) you can specify that an action or a dialog box only run when a particular patch is being applied. When you create the patch package, for example test.msp, you author an upgraded image of the product and a patch creation properties file. When authoring the patch creation properties file you can enter a property name, for example PATCHFORTEST, in the MediaSrcPropName field of the [ImageFamilies](imagefamilies-table-patchwiz-dll-.md) table. When you author the sequence tables of the upgraded image of the product, you can include in the Condition column of the sequence table a conditional statement for the action or dialog box you want to make conditional.

For example, you can use the following conditional statement to run an action or dialog box only when test.msp is being applied.

<dl> PATCH AND PATCHFORTEST AND PATCH >< PATCHFORTEST  
</dl>

> [!Note]  
> Because the **PATCH** property can contain multiple patches, use the substring operator "><" to test for the presence of a particular patch rather than the equals operator "=". For more information about conditional statements see the [Conditional Statement Syntax](conditional-statement-syntax.md) section.

 

The installer sets both properties if you apply a list of patches that includes test.msp. For example, you can use the /p [Command Line Option](command-line-options.md) to apply a list of two patches.

**msiexec /qb /p \\\\scratch\\scratch\\XYZ\\Patches\\test.msp;\\\\scratch\\scratch\\XYZ\\bar.msp**

The installer sets the **PATCH** and PATCHFORTEST properties as follows.

<dl> PATCH=\\\\scratch\\scratch\\XYZ\\Patches\\test.msp;\\\\scratch\\scratch\\XYZ\\bar.msp  
PATCHFORTEST=\\\\scratch\\scratch\\XYZ\\Patches\\test.msp  
</dl>

In this case, the condition is TRUE and the above conditional action or dialog box can run for each patch being installed, test.msp and bar.msp.

If test.msp is not being applied, the installer does not include it in the **PATCH** property and does not set PATCHFORTEST. In this case, the condition above is FALSE and the conditional action or dialog box does not run.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Conditional Statement Syntax](conditional-statement-syntax.md)
</dt> <dt>

[Examples of Conditional Statement Syntax](examples-of-conditional-statement-syntax.md)
</dt> </dl>

 

 




