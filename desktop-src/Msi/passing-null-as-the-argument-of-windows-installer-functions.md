---
description: Windows Installer functions that return data in a user provided–memory location should not be called with null as the value for the pointer.
ms.assetid: f566c4a4-b90c-4d73-9d7f-f5b836630636
title: Passing null to Windows Installer Functions
ms.topic: article
ms.date: 05/31/2018
---

# Passing null as the Argument of Windows Installer Functions

Windows Installer functions that return data in a user provided–memory location should not be called with null as the value for the pointer. These functions return a string or return data as integer pointers, but return inconsistent values when passing null as the value for the output argument.

Do not pass Null as the value of the output argument for any of the following functions:

[**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya)

[**MsiRecordGetString**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordgetstringa)

[**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda)

[**MsiGetSourcePath**](/windows/desktop/api/Msiquery/nf-msiquery-msigetsourcepatha)

[**MsiGetTargetPath**](/windows/desktop/api/Msiquery/nf-msiquery-msigettargetpatha)

[**MsiGetFeatureState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturestatea)

[**MsiViewGetError**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewgeterrora)

[**MsiSummaryInfoGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfogetpropertya)

[**MsiEvaluateCondition**](/windows/desktop/api/Msiquery/nf-msiquery-msievaluateconditiona)

[**MsiGetFeatureCost**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturecosta)

[**MsiGetFeatureState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturestatea)

[**MsiGetComponentState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetcomponentstatea)

[**MsiGetFeatureCost**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturecosta)

[**MsiGetFeatureValidStates**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturevalidstatesa)

 

 



