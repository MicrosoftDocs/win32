---
description: The source code for a sample custom action named Launch, which meets the sample specifications, is provided by the Windows Installer SDK as the file Tutorial.cpp.
ms.assetid: 6f6d45b0-759d-4d28-a542-5cdbb589448f
title: Authoring the Launch Custom Action
ms.topic: article
ms.date: 05/31/2018
---

# Authoring the Launch Custom Action

The source code for a sample custom action named Launch, which meets the sample specifications, is provided by the Windows Installer SDK as the file Tutorial.cpp. This custom action makes use of [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) to format a string containing properties. The property \[\#FileKey\] resolves to the full path of the HTML file. Use the source file to create the file Tutorial.dll. The entry point to this DLL is LaunchTutorial.

The sample custom action Launch calls a DLL written in C++ and is generated from a temporary binary stream. Custom actions of this type include the base type constants msidbCustomActionTypeDll and msidbCustomActionTypeBinaryData, which give a base numeric type equal to 1. See [Custom Action Type 1](custom-action-type-1.md). Because the specifications require that the installation continue if the custom action fails, Launch also includes the optional constant **msidbCustomActionTypeContinue**, which is 64. See [Custom Action Return Processing Options](custom-action-return-processing-options.md). The total numeric type of Launch is 65.

Continue to [Adding Launch to the CustomAction and Binary Tables](adding-launch-to-the-customaction-and-binary-tables.md).

 

 



