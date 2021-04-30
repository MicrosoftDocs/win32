---
description: The product database contains information about a product. For more information on obtaining product information with enumeration functions, see Initializing an Application.
ms.assetid: 528c915c-296c-4620-8105-0b5d543e56a5
title: Getting Application Information
ms.topic: article
ms.date: 05/31/2018
---

# Getting Application Information

The product database contains information about a product. For more information on obtaining product information with enumeration functions, see [Initializing an Application](initializing-an-application.md).

**To get product information**

1.  Verify that a product is installed by calling the [**MsiQueryProductState**](/windows/desktop/api/Msi/nf-msi-msiqueryproductstatea) function.
2.  Open the database and obtain a handle to it by calling the [**MsiOpenProduct**](/windows/desktop/api/Msi/nf-msi-msiopenproducta) function.

    If the database is contained in an installation package, call the [**MsiOpenPackage**](/windows/desktop/api/Msi/nf-msi-msiopenpackagea) function.

3.  Use the open handle to obtain product properties with the [**MsiGetProductProperty**](/windows/desktop/api/Msi/nf-msi-msigetproductpropertya) function, and to obtain descriptive feature information with the [**MsiGetFeatureInfo**](/windows/desktop/api/Msi/nf-msi-msigetfeatureinfoa) function.

    If you want to obtain product information using the product code, rather than using the open database handle, call the [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa) function instead of [**MsiGetProductProperty**](/windows/desktop/api/Msi/nf-msi-msigetproductpropertya).

4.  Close an open installation handle by calling the [**MsiCloseHandle**](/windows/desktop/api/Msi/nf-msi-msiclosehandle) function.

    The [**MsiCloseAllHandles**](/windows/desktop/api/Msi/nf-msi-msicloseallhandles) function is a diagnostic function and should not be used to close handles you know to be open. It is acceptable to call the **MsiCloseAllHandles** function when the application closes to ensure that all handles have been closed.

 

 



