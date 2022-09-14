---
description: Using public symbols for your target and upgrade image binaries can reduce binary patch sizes by approximately one half.
ms.assetid: 83351a1b-ba70-4f0b-bacf-71ad7993a5aa
title: Using Symbols to Reduce Binary Patch Size
ms.topic: article
ms.date: 05/31/2018
---

# Using Symbols to Reduce Binary Patch Size

Using public symbols for your target and upgrade image binaries can reduce binary patch sizes by approximately one half. The actual reduction depends upon the symbols used. Note that using symbols can result in slower patch creation times because it takes longer to process the symbol files.

To reduce the size of a binary patch using symbols, you must provide symbols for both the target and upgrade image binaries. Specify the symbols in the SymbolPaths column of the [TargetImages](targetimages-table-patchwiz-dll-.md) table and the SymbolPaths column of the [UpgradedImages](upgradedimages-table-patchwiz-dll-.md) table. You must use Visual C++ to generate symbols in the program database (PDB) file format. Newer versions of Visual C++ provide all of the necessary information in the PDB file. Older versions of Visual C++ also generate the debug (DBG) file format. In this case, the SymbolsPaths value should specify the location of both the PDB and DBG files.

For example, the TargetImage for a patch might be the installation package that shipped with Windows 2000 and that installs the 1.1.1029.0 version of MSI.DLL. The UpgradedImage might be the updated installation package that shipped with Windows 2000 with Service Pack 1 (SP1) and that installs the 1.11.1314.0 version of MSI.DLL. Two Patch Creation Properties (PCP) files would then have to be created, one with the SymbolPaths column of both the [TargetImages](targetimages-table-patchwiz-dll-.md) and [UpgradedImages](upgradedimages-table-patchwiz-dll-.md) tables left NULL (blank) and the other with the SymbolPaths column of both the TargetImages and UpgradedImages tables populated with the location of the symbols for the binaries. In this case, the size of the patch generated without using symbols can be approximately three times the size of the patch generated using symbols.

The Mpatch.exe utility can be used to test the generation of binary patches for a single file and to check whether or not the symbols are valid. The Mpatch.exe utility is included in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). The output of Mpatch.exe will indicate if the symbols do not match.

For example, enter the following command line to check whether or not the symbols are valid.

**mpatch.exe -NEWSYMPATH:d:\\update -OLDSYMPATH:d:\\target d:\\target\\example.dll d:\\update\\example.dll example.pat**

If the symbols are not in the correct location, the output of Mpatch.exe may include the following warning.

``` syntax
WARNING: no debug symbols for d:\update\example.dll
```

 

 



