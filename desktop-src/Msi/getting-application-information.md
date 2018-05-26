---
Description: The product database contains information about a product. For more information on obtaining product information with enumeration functions, see Initializing an Application.
ms.assetid: 528c915c-296c-4620-8105-0b5d543e56a5
title: Getting Application Information
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Application Information

The product database contains information about a product. For more information on obtaining product information with enumeration functions, see [Initializing an Application](initializing-an-application.md).

**To get product information**

1.  Verify that a product is installed by calling the [**MsiQueryProductState**](/windows/win32/Msi/nf-msi-msiqueryproductstatea?branch=master) function.
2.  Open the database and obtain a handle to it by calling the [**MsiOpenProduct**](/windows/win32/Msi/nf-msi-msiopenproducta?branch=master) function.

    If the database is contained in an installation package, call the [**MsiOpenPackage**](/windows/win32/Msi/nf-msi-msiopenpackagea?branch=master) function.

3.  Use the open handle to obtain product properties with the [**MsiGetProductProperty**](/windows/win32/Msi/nf-msi-msigetproductpropertya?branch=master) function, and to obtain descriptive feature information with the [**MsiGetFeatureInfo**](/windows/win32/Msi/nf-msi-msigetfeatureinfoa?branch=master) function.

    If you want to obtain product information using the product code, rather than using the open database handle, call the [**MsiGetProductInfo**](/windows/win32/Msi/nf-msi-msigetproductinfoa?branch=master) function instead of [**MsiGetProductProperty**](/windows/win32/Msi/nf-msi-msigetproductpropertya?branch=master).

4.  Close an open installation handle by calling the [**MsiCloseHandle**](/windows/win32/Msi/nf-msi-msiclosehandle?branch=master) function.

    The [**MsiCloseAllHandles**](/windows/win32/Msi/nf-msi-msicloseallhandles?branch=master) function is a diagnostic function and should not be used to close handles you know to be open. It is acceptable to call the **MsiCloseAllHandles** function when the application closes to ensure that all handles have been closed.

 

 



