---
Description: Windows Installer functions that return data in a user provided–memory location should not be called with null as the value for the pointer.
ms.assetid: f566c4a4-b90c-4d73-9d7f-f5b836630636
title: Passing null as the Argument of Windows Installer Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Passing null as the Argument of Windows Installer Functions

Windows Installer functions that return data in a user provided–memory location should not be called with null as the value for the pointer. These functions return a string or return data as integer pointers, but return inconsistent values when passing null as the value for the output argument.

Do not pass Null as the value of the output argument for any of the following functions:

[**MsiGetProperty**](/windows/win32/Msiquery/nf-msiquery-msigetpropertya?branch=master)

[**MsiRecordGetString**](/windows/win32/Msiquery/nf-msiquery-msirecordgetstringa?branch=master)

[**MsiFormatRecord**](/windows/win32/Msiquery/nf-msiquery-msiformatrecorda?branch=master)

[**MsiGetSourcePath**](/windows/win32/Msiquery/nf-msiquery-msigetsourcepatha?branch=master)

[**MsiGetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msigettargetpatha?branch=master)

[**MsiGetFeatureState**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturestatea?branch=master)

[**MsiViewGetError**](/windows/win32/Msiquery/nf-msiquery-msiviewgeterrora?branch=master)

[**MsiSummaryInfoGetProperty**](/windows/win32/Msiquery/nf-msiquery-msisummaryinfogetpropertya?branch=master)

[**MsiEvaluateCondition**](/windows/win32/Msiquery/nf-msiquery-msievaluateconditiona?branch=master)

[**MsiGetFeatureCost**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturecosta?branch=master)

[**MsiGetFeatureState**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturestatea?branch=master)

[**MsiGetComponentState**](/windows/win32/Msiquery/nf-msiquery-msigetcomponentstatea?branch=master)

[**MsiGetFeatureCost**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturecosta?branch=master)

[**MsiGetFeatureValidStates**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturevalidstatesa?branch=master)

 

 



