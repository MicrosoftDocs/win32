---
description: The UpgradedFile\_OptionalData table contains information about specific files in an upgraded image. This table is optional in the patch creation database (.pcp file) and is used by the UiCreatePatchPackageEx function.
ms.assetid: 8b96a83a-2bfa-47b7-bde0-896bdcc97d29
title: UpgradedFiles_OptionalData Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# UpgradedFiles\_OptionalData Table (Patchwiz.dll)

The UpgradedFile\_OptionalData table contains information about specific files in an upgraded image. This table is optional in the patch creation database (.pcp file) and is used by the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function.

The UpgradedFile\_OptionalData table has the following columns.



| Column                  | Type    | Key | Nullable |
|-------------------------|---------|-----|----------|
| Upgraded                | text    | Y   | N        |
| FTK                     | text    | Y   | N        |
| SymbolPaths             | text    |     | Y        |
| AllowIgnoreOnPatchError | integer |     | Y        |
| IncludeWholeFile        | integer |     | Y        |



 

## Columns

<dl> <dt>

<span id="Upgraded"></span><span id="upgraded"></span><span id="UPGRADED"></span>Upgraded
</dt> <dd>

Foreign key to the Upgraded column of the [UpgradedImages Table (Patchwiz.dll)](upgradedimages-table-patchwiz-dll-.md).

</dd> <dt>

<span id="FTK"></span><span id="ftk"></span>FTK
</dt> <dd>

File table key. Foreign key into [File table](file-table.md) of the .msi file of the upgraded image. If two or more upgraded images within a family have the same FTK value, the value must refer to the same file. Files shared by multiple upgrade images should have the same FTK to minimize cabinet file size.

</dd> <dt>

<span id="SymbolPaths"></span><span id="symbolpaths"></span><span id="SYMBOLPATHS"></span>SymbolPaths
</dt> <dd>

The value in this field is added to the semicolon-delimited list of folders in the SymbolPaths column of the [UpgradedImages Table (Patchwiz.dll)](upgradedimages-table-patchwiz-dll-.md) when the patch is generated, and can be used to add symbol files for a specific file.

</dd> <dt>

<span id="AllowIgnoreOnPatchError"></span><span id="allowignoreonpatcherror"></span><span id="ALLOWIGNOREONPATCHERROR"></span>AllowIgnoreOnPatchError
</dt> <dd>

Set to 1 to indicate that the patch is non-vital. Set to 0 to indicate that the patch is vital. If Windows Installer encounters a problem when applying this patch to the file specified in the FTK column, the value in this field determines whether the error message box includes an **Ignore** button to enable the user to continue the patching process.

</dd> <dt>

<span id="IncludeWholeFile"></span><span id="includewholefile"></span><span id="INCLUDEWHOLEFILE"></span>IncludeWholeFile
</dt> <dd>

Set to a nonzero value if the entire file specified in the FTK column should be installed rather than creating a binary patch.

</dd> </dl>

 

 



