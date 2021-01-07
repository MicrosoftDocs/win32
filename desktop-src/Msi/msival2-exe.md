---
description: Msival2.exe is a command line utility that can run a suite of Internal Consistency Evaluators - ICEs.
ms.assetid: c48f4584-732a-468d-a651-2c09ce3c9ddd
title: Msival2.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msival2.exe

Msival2.exe is a command line utility that can run a suite of [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md).

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

For more information about ICEs and the CUB file, see [Using Internal Consistency Evaluators](using-internal-consistency-evaluators.md).

## Syntax

**Msival2** *{database}{CUB file}\[-f\]\[-l {logfile}\]\[-i {ICE Id}\[:{ICE Id}...\]\]*

## Command Line Options

Msival2.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash.



| Option | Description                                                                                                                                                                                                                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -f     | Filter out all informational messages from the displayed results. All other types of messages are displayed.                                                                                                                                                                                              |
| -i     | Run only the ICEs listed on the command line in the order specified. Each ICE custom action should be listed as it appears in the [CustomAction table](customaction-table.md) of the CUB file. If this option is omitted, the tool runs the default set of ICEs specified by the author of the CUB file. |
| -l     | Write results to the specified file. The file must not already exist. If the file exists, it is not overwritten.                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



