---
title: How to develop an OEM app that uses a custom file
description: Learn how to develop an app that uses a custom file to pass info from the OEM to the app.
ms.assetid: BCDB4B13-3644-44E4-9A70-04D8E90500EE
ms.topic: article
ms.date: 05/31/2018
---

# How to develop an OEM app that uses a custom file

For more information on creating and using custom data files, see [DISM App Package (.appx or .appxbundle) Servicing Command-Line Options](/windows-hardware/manufacture/desktop/dism-app-package--appx-or-appxbundle--servicing-command-line-options).

Learn how to develop an app that uses a custom file to pass info from the OEM to the app.

For apps that you create for OEM deployment, you can use a custom file to pass info from the OEM to the apps. To pass OEM info to an app, you create a Custom.data file in the microsoft.system.package.metadata folder. This file name is special to the operating system and is automatically carried forward during operating system updates. OEMs can use this file to pass in custom identifiers, so that apps know when OEMs have deployed them. You can have only one Custom.data file per app. Apps must be able to look for and read this file correctly. Developers treat the file as untrusted data.

## What you need to know

### Technologies

-   [Quickstart: Query app package manifest info](how-to-query-package-identity-information.md)

### Prerequisites

-   You need the [Deployment Image Servicing and Management (DISM)](/windows/desktop/Win7AppQual/dism-replaces-pkgmgr-peimg-and-intlconfg-tools) tool to add the app package with the custom data file.

## Instructions

### Step 1: Create custom file and add it to the package metadata folder

You can design your app to use any format you choose for the custom data. For example, you can use XML, a text file, or another file type to organize your data. We recommend that you consider how you can test and validate the file. For example, you can create an XML schema to validate an XML file.

You can specify any type of file with any file name for the custom data. When you add the app package with the custom data file by using the [DISM](/windows/desktop/Win7AppQual/dism-replaces-pkgmgr-peimg-and-intlconfg-tools) tool, DISM renames the custom file to Custom.data and saves the file to the microsoft.system.package.metadata folder.

> [!Note]  
> The custom data file can't be modified by the app. It's a read-only resource.

 

### Step 2: Access the custom data file for an app

You can access the Custom.data file for an app from your code by using Windows APIs to get information for the current package. For example:

``` syntax
Windows.ApplicationModel.Package.current.installedLocation.getFileAsync(
"microsoft.system.package.metadata\\custom.data")
```

For more info about developing with the [**Package.Current**](/uwp/api/windows.applicationmodel.package.current) property, see [Quickstart: Query app package manifest info](how-to-query-package-identity-information.md).

For more info about accessing the custom.data file via [**IStorageFolder.GetFileAsync**](/uwp/api/windows.storage.istoragefolder.getfileasync) and by using [**StorageFile**](/uwp/api/Windows.Storage.StorageFile) objects, see [Accessing data and files](/previous-versions/windows/apps/hh464959(v=win.10)).

## Related topics

<dl> <dt>

[Quickstart: Query app package manifest info](how-to-query-package-identity-information.md)
</dt> </dl>

 

 