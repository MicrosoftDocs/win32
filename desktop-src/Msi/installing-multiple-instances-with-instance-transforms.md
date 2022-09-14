---
description: This topic provides guidelines for installing or reinstalling a multiple instance installation that uses instance transforms.
ms.assetid: cf9076b1-5674-4ba8-9890-e981221d7b03
title: Installing Multiple Instances with Instance Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Installing Multiple Instances with Instance Transforms

This topic provides guidelines for installing or reinstalling a multiple instance installation that uses instance transforms.

-   When installing a new instance with an instance transform, include the **MSINEWINSTANCE** property and set **MSINEWINSTANCE**=1.
-   When installing a new instance with an instance transform, include the TRANSFORMS property and set the first transform in the list of transforms to the instance transform that changes the product code. Any customization transforms should follow the instance transform at the beginning of this list.
-   The easiest way to initiate a maintenance installation, and reinstall an instance, is to reference the product code of the instance. If you initiate the maintenance installation by using the package path, you must also specify the product code of the instance. From the command line, use the /n {Product Code} option. From code or script, use the **MSIINSTANCEGUID** property.

The following example shows installing a new instance from a command line where the instance transform is prefixed by a colon which specifies that the transform is embedded in the package.

**msiexec /I mypackage.msi TRANSFORMS=:instance.mst MSINEWINSTANCE=1 /qb**

The following example shows installing a new instance using [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta).

``` syntax
UINT uiStat = MsiInstallProduct(_T("path to mypackage.msi"), _T("TRANSFORMS=:instance.mst MSINEWINSTANCE=1"));
```

The following example shows installing the new instance from script.

``` syntax
Dim Installer As Object
Set Installer = CreateObject("WindowsInstaller.Installer")
Installer.InstallProduct "path to mypackage.msi", "TRANSFORMS=:instance.mst MSINEWINSTANCE=1"
```

The following example reinstalls an instance without re-caching the package. The instance is referred to by its product code {00000001-0002-0000-0000-624474736554}.

**msiexec /I {00000001-0002-0000-0000-624474736554} REINSTALL=ALL REINSTALLMODE=omus /qb**

The following example reinstalls an instance and re-caches the package from the command line. The instance is referred to by the package path. You are only required to include the /n {Product Code} option if the product is originally installed with an instance transform.

**msiexec /I c:\\newpath\\mypackage.msi /n {00000001-0002-0000-0000-624474736554} REINSTALL=ALL REINSTALLMODE=vomus /qb**

The following example reinstalls an instance and caches the package using **MsiInstallProduct**. The instance is referred to by the package path. Use the **MSIINSTANCEGUID** property to provide the product code of the instance.

``` syntax
UINT uiStat = MsiInstallProduct(_T("path to mypackage.msi"), _T("MSIINSTANCEGUID={00000001-0002-0000-0000-624474736554}  REINSTALL=ALL REINSTALLMODE=vomus"));
```

The following example reinstalls an instance and caches the package using script. Use the **MSIINSTANCEGUID** property to provide the product code of the instance.

``` syntax
Dim Installer As Object
Set Installer = CreateObject("WindowsInstaller.Installer")
Installer.InstallProduct "path to mypackage.msi", "MSIINSTANCEGUID={00000001-0002-0000-0000-624474736554}  REINSTALL=ALL REINSTALLMODE=vomus"
```

The following example shows how to advertise an instance using the command line.

**msiexec /jm mypackage.msi /t :instance.mst /c /qb**

The following example shows how to install to advertise an instance using **MsiAdvertiseProductEx**.

``` syntax
UINT uiStat = MsiAdvertiseProductEx(_T("path to mypackage.msi"), NULL, _T(":instance.mst"), 0, 0, MSIADVERTISEOPTIONS_INSTANCE);
```

The following example shows how to apply a patch to an instance from a command line. You are only required to include the /n {Product Code} option if the product was originally installed with an instance transform.

**msiexec /p mypatch.msp /n {00000001-0002-0000-0000-624474736554} /qb**

The following example shows how to apply a patch to an instance installation using [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha).

``` syntax
UINT uiStat = MsiApplyPatch(_T("path to mypatch.msp"), _T("{00000001-0002-0000-0000-624474736554}"), INSTALLTYPE_SINGLE_INSTANCE, _T("REINSTALL=ALL REINSTALLMODE=omus"));
```

For more information, see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md) and [Authoring Multiple Instances with Instance Transforms](authoring-multiple-instances-with-instance-transforms.md).

 

 



