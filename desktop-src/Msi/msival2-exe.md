---
description: Msival2.exe is a command line utility that can run a suite of Internal Consistency Evaluators - ICEs.
ms.assetid: c48f4584-732a-468d-a651-2c09ce3c9ddd
title: Msival2.exe
ms.topic: reference
ms.date: 03/18/2026
---

# Msival2.exe

Msival2.exe is a command line utility that can run a suite of [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md).

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

For more information about ICEs and the CUB file, see [Using Internal Consistency Evaluators](using-internal-consistency-evaluators.md).

## Syntax

**Msival2** *{database} {CUB file} \[-f\] \[-l {logfile}\] \[-i {ICE Id}\[:{ICE Id}...\]\]*

## Arguments

*{database}*

The Windows Installer database (.msi file) to validate.

*{CUB file}*

A .cub file is a standard Windows Installer database that contains only ICEs and their required tables, used to store and provide access to ICE custom actions. For more information, see [Building an ICE Database](building-an-ice-database.md).

*{ICE Id}*

An Internal Consistency Evaluator (ICE) is a custom action that scans the database for entries that are valid individually but may cause incorrect behavior in the context of the whole database. For more information, see [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md). For a list of predefined ICEs, see [ICE Reference](ice-reference.md).

## Command Line Options

Msival2.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash.



| Option | Description                                                                                                                                                                                                                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -f     | Filter out all informational messages from the displayed results. All other types of messages are displayed.                                                                                                                                                                                              |
| -i     | Run only the ICEs listed on the command line in the order specified. Each ICE custom action should be listed as it appears in the [CustomAction table](customaction-table.md) of the CUB file. If this option is omitted, the tool runs the default set of ICEs specified by the author of the CUB file. |
| -l     | Write results to the specified file. The file must not already exist. If the file exists, it is not overwritten.                                                                                                                                                                                          |



## Example

The following example validates the database *mypackage.msi* using the ICE database *darice.cub*, running only ICE01, ICE02, and ICE03, and writing the results to *validation.log*:

```syntax
msival2.exe mypackage.msi darice.cub -i ICE01:ICE02:ICE03 -l validation.log
```

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



