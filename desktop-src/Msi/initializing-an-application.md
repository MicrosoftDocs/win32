---
Description: To enable installer functionality, an application must call a number of functions when it is initializing.
ms.assetid: cfeaf9b9-f772-49f9-8b6f-e7fd0c93cc9f
title: Initializing an Application
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Initializing an Application

To enable installer functionality, an application must call a number of functions when it is initializing. For more information, see [Installation Mechanism](installation-mechanism.md). The following steps describe how to use the installer to initialize an application:

**To initialize an application**

1.  Call the [**MsiGetProductCode**](/windows/win32/Msi/nf-msi-msigetproductcodea?branch=master) function so the application can identify itself to the installer.

    The product code is a required parameter for many installer functions.

2.  Call the [**MsiGetUserInfo**](/windows/win32/Msi/nf-msi-msigetuserinfoa?branch=master) function to collect user information the first time the application starts.

    If the call to [**MsiGetUserInfo**](/windows/win32/Msi/nf-msi-msigetuserinfoa?branch=master) fails, call the [**MsiCollectUserInfo**](/windows/win32/Msi/nf-msi-msicollectuserinfoa?branch=master) function to collect user information.

3.  Display a default user interface, if necessary, by calling the [**MsiSetInternalUI**](/windows/win32/Msi/nf-msi-msisetinternalui?branch=master) function.

    To author your own user interface, register it with the installer by calling the [**MsiSetExternalUI**](/windows/win32/Msi/nf-msi-msisetexternaluia?branch=master) function.

4.  Call the [**MsiEnableLog**](/windows/win32/Msi/nf-msi-msienableloga?branch=master) function to set the logging level.
5.  Present the user with available features by enumerating the features of your application. You can enumerate features in the following ways:
    -   Query the installer feature-by-feature. For example, before the application draws a button or a menu item, the application calls the [**MsiQueryFeatureState**](/windows/win32/Msi/nf-msi-msiqueryfeaturestatea?branch=master) function so the installer can check that the feature is available.
    -   Enumerate all of the available features at once by calling the [**MsiEnumFeatures**](/windows/win32/Msi/nf-msi-msienumfeaturesa?branch=master) function. To use this function, the application must call **MsiEnumFeatures** repeatedly while incrementing an index.
6.  Get detailed information about the current installation by calling the following enumeration functions repeatedly, incrementing an index variable for each call:

    -   Call the [**MsiEnumProducts**](/windows/win32/Msi/nf-msi-msienumproductsa?branch=master) function to enumerate products registered with the installer.
    -   Call the [**MsiEnumComponents**](/windows/win32/Msi/nf-msi-msienumcomponentsa?branch=master) function to enumerate components.
    -   Call the [**MsiEnumComponentQualifiers**](/windows/win32/Msi/nf-msi-msienumcomponentqualifiersa?branch=master) function to enumerate component qualifiers.
    -   Call the [**MsiEnumClients**](/windows/win32/Msi/nf-msi-msienumclientsa?branch=master) function to enumerate the products for a particular component.

    If the return value on an enumeration function is ERROR\_SUCCESS, there are still more items to be enumerated and the function should be called again with an incremented index variable. If the return value is ERROR\_NO\_MORE\_ITEMS, then all of the items have been enumerated, and the function should not be called again.

 

 



