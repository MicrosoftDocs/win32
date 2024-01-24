---
description: The value of the Revision Number Summary Property in the summary information stream must be changed to a new, unique value when localizing a database, because the installation database is being changed. See Package Codes.
ms.assetid: fce292c5-6702-4948-a13a-2a9ccacbd5c9
title: Updating a Summary Information Stream
ms.topic: article
ms.date: 05/31/2018
---

# Updating a Summary Information Stream

The value of the [**Revision Number Summary**](revision-number-summary.md) Property in the [summary information stream](summary-information-stream.md) must be changed to a new, unique value when localizing a database, because the installation database is being changed. See [Package Codes](package-codes.md).

The value of the [**Template Summary**](template-summary.md) Property in the summary information stream must be changed to the numeric language identifier (LANGID) of the new language.

If the descriptive text strings in the summary information stream are localized to the new language, the [**Codepage Summary**](codepage-summary.md) Property must be set to the correct code page for the new language.

You may modify the summary information stream of the localized package by the same procedure as in [Adding Summary Information](adding-summary-information.md). An example demonstrating the use of the database summary information methods is also provided in the Windows Installer SDK as the utility WiSumInf.vbs. For more information about WiSumInf.vbs, see [Manage Summary Information](manage-summary-information.md).

[Continue](adding-localized-resources.md)

 

 



