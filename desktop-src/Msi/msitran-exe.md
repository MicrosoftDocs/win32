---
description: Msitran.exe uses MsiDatabaseGenerateTransform, MsiCreateTransformSummaryInfo, and MsiDatabaseApplyTransform to generate or apply a transform file.This tool is only available in the Windows SDK Components for Windows Installer Developers.
ms.assetid: cfc7b907-78d7-4a78-bab4-ede9012d5a36
title: Msitran.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msitran.exe

Msitran.exe uses [**MsiDatabaseGenerateTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasegeneratetransforma), [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa), and [**MsiDatabaseApplyTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseapplytransforma) to generate or apply a transform file.

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Syntax

Use the following syntax to generate a transform.

**msitran -g** *{base db}{ref db}{transform file name}\[{error conditions / validation conditions}\]*

Use the following syntax to apply a transform

**msitran -a** *{transform}{database}\[{error conditions}\]*

## Command Line Options

Msitran.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash.



| Option | Description            |
|--------|------------------------|
| -g     | Transform generation.  |
| -a     | Transform application. |



 

The following errors may be suppressed when applying a transform. To suppress an error, include the appropriate character in the {error conditions} argument. Conditions specified with -g are placed in the summary information of the transform, but are not used when applying a transform with -a. For information, see [**MsiDatabaseApplyTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseapplytransforma).



| Option | Suppressed error           |
|--------|----------------------------|
| a      | Add existing row.          |
| b      | Delete non-existing row.   |
| c      | Add existing table.        |
| d      | Delete non-existing table. |
| e      | Modify existing row.       |
| f      | Change codepage.           |



 

The following validation conditions may be used to indicate when a transform may be applied to a package. These conditions may be specified with -g, but not -a.



| Option | Validation condition                                  |
|--------|-------------------------------------------------------|
| g      | Check upgrade code.                                   |
| l      | Check language.                                       |
| p      | Check platform.                                       |
| r      | Check product.                                        |
| s      | Check major version only.                             |
| t      | Check major and minor versions only.                  |
| u      | Check major, minor, and upgrade versions.             |
| v      | Applied database version < Base database version.  |
| w      | Applied database version <= Base database version. |
| x      | Applied database version = Base database version.     |
| y      | Applied database version >= Base database version. |
| z      | Applied database version > Base database version.  |



 

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Database Transforms](database-transforms.md)
</dt> <dt>

[A Customization Transform Example](a-customization-transform-example.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



