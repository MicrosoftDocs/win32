---
description: The UpgradedFilesToIgnore table prevents the updating of specific files that are in fact changed in the upgraded image relative to the target images.
ms.assetid: 3b5f4360-887a-4a21-8f16-faa84da34328
title: UpgradedFilesToIgnore Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# UpgradedFilesToIgnore Table (Patchwiz.dll)

The UpgradedFilesToIgnore table prevents the updating of specific files that are in fact changed in the upgraded image relative to the target images. It may be useful to do this in certain cases. For example, a patch package intended only for use with non-administrative installations does not need to include patching files that are only part of administrative images. Excluding such files used only in administrative images can reduce the size of the patch package; however, administrators should be informed on how to update these files separately. This table is optional in the patch creation database (.pcp file) and is used by the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function.

The UpgradedFilesToIgnore table has the following columns.



| Column   | Type | Key | Nullable |
|----------|------|-----|----------|
| Upgraded | text | Y   | N        |
| FTK      | text | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Upgraded"></span><span id="upgraded"></span><span id="UPGRADED"></span>Upgraded
</dt> <dd>

Foreign key to the Upgraded column of the [UpgradedImages Table (Patchwiz.dll)](upgradedimages-table-patchwiz-dll-.md). The patch creation tool excludes updating the file specified in the FTK column of the UpgradedFilesToIgnore table when upgrading a target to the image specified in the Upgraded field. Enter a value of "\*" in the Upgraded field to exclude updating the file for all upgraded images.

</dd> <dt>

<span id="FTK"></span><span id="ftk"></span>FTK
</dt> <dd>

Foreign key into the [File table](file-table.md) of the upgraded image. A value of the form "&lt;prefix&gt;\*" matches all file table keys in the File table that begin with that prefix. No text can follow the asterisk.

</dd> </dl>

 

 



