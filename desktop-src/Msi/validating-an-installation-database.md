---
description: Authors of installation packages should always run validation on their packages before attempting to install the package for the first time and rerun validation whenever making any changes to the package.
ms.assetid: 1f16a349-4919-46d2-9b78-2533b8679a73
title: Validating an Installation Database
ms.topic: article
ms.date: 05/31/2018
---

# Validating an Installation Database

Authors of installation packages should always run validation on their packages before attempting to install the package for the first time and rerun validation whenever making any changes to the package. Validation scans the database for errors that may appear valid individually but that cause incorrect behavior in the context of the whole database. Attempting to install a package that fails validation can damage the user's system. See the sections [Package Validation](package-validation.md) and [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md).

You can validate the sample package using [Orca.exe](orca-exe.md) or [Msival2.exe](msival2-exe.md). To view the help for Msival2.exe change directories and enter on the command line.

Msival2 -?

The .cub file darice.cub contains the ICE custom actions needed by Msival2.exe to perform validation. To validate the MNP2000.msi enter

msival2 MNP2000.msi Darice.cub

For a description of the error and warning messages returned by validation see the [ICE Reference](ice-reference.md). Correct all the errors in the package and rerun validation as necessary until the package passes validation without errors.

Once the package passes validation, you can install the sample package by clicking on the MNP2000.msi icon or from the command line using the [Command Line Options](command-line-options.md).

This completes the sample installation.

## Next example

[An Upgrade Example](an-upgrade-example.md)

 

 



