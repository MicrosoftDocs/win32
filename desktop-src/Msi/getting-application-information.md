---
Description: 'The product database contains information about a product. For more information on obtaining product information with enumeration functions, see Initializing an Application.'
ms.assetid: '528c915c-296c-4620-8105-0b5d543e56a5'
title: Getting Application Information
---

# Getting Application Information

The product database contains information about a product. For more information on obtaining product information with enumeration functions, see [Initializing an Application](initializing-an-application.md).

**To get product information**

1.  Verify that a product is installed by calling the [**MsiQueryProductState**](msiqueryproductstate.md) function.
2.  Open the database and obtain a handle to it by calling the [**MsiOpenProduct**](msiopenproduct.md) function.

    If the database is contained in an installation package, call the [**MsiOpenPackage**](msiopenpackage.md) function.

3.  Use the open handle to obtain product properties with the [**MsiGetProductProperty**](msigetproductproperty.md) function, and to obtain descriptive feature information with the [**MsiGetFeatureInfo**](msigetfeatureinfo.md) function.

    If you want to obtain product information using the product code, rather than using the open database handle, call the [**MsiGetProductInfo**](msigetproductinfo.md) function instead of [**MsiGetProductProperty**](msigetproductproperty.md).

4.  Close an open installation handle by calling the [**MsiCloseHandle**](msiclosehandle.md) function.

    The [**MsiCloseAllHandles**](msicloseallhandles.md) function is a diagnostic function and should not be used to close handles you know to be open. It is acceptable to call the **MsiCloseAllHandles** function when the application closes to ensure that all handles have been closed.

 

 



