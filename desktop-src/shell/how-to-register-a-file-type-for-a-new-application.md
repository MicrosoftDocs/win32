---
description: If you plan to associate one or more file types with a new application, you must define a ProgID for each file type that you want to associate with the application.
ms.assetid: 997600C9-5264-44EC-BAEC-CB5CEEA0BD14
title: How to Register a File Type for a New Application
ms.topic: article
ms.date: 05/31/2018
---

# How to Register a File Type for a New Application

If you plan to associate one or more file types with a new application, you must define a ProgID for each file type that you want to associate with the application.

To create a ProgID for each unique file type that your application handles, use these steps.

## Instructions

### Step 1:

Note that some file types have multiple extensions that point to the same ProgID; for example:

-   **HKEY\_CLASSES\_ROOT**\\**App.jpeg** (your ProgID)
-   **HKEY\_CLASSES\_ROOT**\\**.jpg** = App.jpeg (the file type mappings)
-   **HKEY\_CLASSES\_ROOT**\\**.jpeg** = App.jpeg

### Step 2:

Remove the ProgID values when you install and uninstall your program.

### Step 3:

Leave the file type mappings unchanged at uninstall time. Doing so works because file type mappings are stored per user in HKEY\_CLASSES\_ROOT\\.ext, and the system identifies the case where the ProgID value is missing and ignores it. Leaving file type mappings unchanged avoids the need to have conditional code that only removes the file type mapping if the value still points to your ProgID. It is important to avoid doing so in cases where it might have been changed by another application and you thus cannot easily remove the value.

### Step 4:

Specify a unique value for the file type description of each file type ProgID by doing one of the following:

-   Leave the default value of the ProgID empty, in which case the system uses the .ext file.
-   Provide a localized value via FriendlyTypeName and, for compatibility with old applications that read the registry directly, be sure to provide the default value of the ProgID as the file type description (that is, use the same value that is referred to by the FriendlyTypeName in the English resource).

## Remarks

If you plan to associate the file with an existing application, locate an application ProgID in the registry. For more information, see [File Types](fa-file-types.md).

 

 



