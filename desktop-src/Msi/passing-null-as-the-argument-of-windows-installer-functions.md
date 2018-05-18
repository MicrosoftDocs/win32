---
Description: 'Windows Installer functions that return data in a user provided–memory location should not be called with null as the value for the pointer.'
ms.assetid: 'f566c4a4-b90c-4d73-9d7f-f5b836630636'
title: Passing null as the Argument of Windows Installer Functions
---

# Passing null as the Argument of Windows Installer Functions

Windows Installer functions that return data in a user provided–memory location should not be called with null as the value for the pointer. These functions return a string or return data as integer pointers, but return inconsistent values when passing null as the value for the output argument.

Do not pass Null as the value of the output argument for any of the following functions:

[**MsiGetProperty**](msigetproperty.md)

[**MsiRecordGetString**](msirecordgetstring.md)

[**MsiFormatRecord**](msiformatrecord.md)

[**MsiGetSourcePath**](msigetsourcepath.md)

[**MsiGetTargetPath**](msigettargetpath.md)

[**MsiGetFeatureState**](msigetfeaturestate.md)

[**MsiViewGetError**](msiviewgeterror.md)

[**MsiSummaryInfoGetProperty**](msisummaryinfogetproperty.md)

[**MsiEvaluateCondition**](msievaluatecondition.md)

[**MsiGetFeatureCost**](msigetfeaturecost.md)

[**MsiGetFeatureState**](msigetfeaturestate.md)

[**MsiGetComponentState**](msigetcomponentstate.md)

[**MsiGetFeatureCost**](msigetfeaturecost.md)

[**MsiGetFeatureValidStates**](msigetfeaturevalidstates.md)

 

 



