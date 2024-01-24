---
description: Handling COM+ Administration Errors
ms.assetid: 03f00c19-ff81-478b-b545-048f3dbe5eda
title: Handling COM+ Administration Errors
ms.topic: article
ms.date: 05/31/2018
---

# Handling COM+ Administration Errors

Errors that are generated when using the COMAdmin objects are reported in two ways, as follows:

-   Using error codes specific to the COMAdmin library.
-   Using extended error information available in a special [**ErrorInfo**](errorinfo.md) collection.

## Error Codes

You handle administration error codes as you would any COM error message. In Microsoft Visual C++, these codes are returned as **HRESULT** values. In Microsoft Visual Basic, they are thrown as exceptions that you can catch. For C++ programmers, the COM+ administration error codes are defined in Winerror.h. For Visual Basic programmers, they are available through the Visual Basic IDE.

## ErrorInfo Collection

When an error occurs, signaled by some kind of failure code, more detailed information may be available, depending on the nature of the error. The COMAdmin objects provide extended information in circumstances where the precise cause of the failure is difficult to determine without a detailed report, such as with multiple read and write operations.

For example, when you use methods such as [**Populate**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-populate) and [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) on a [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object, you can be reading or writing data for every item in the collection. Complicated errors can occur, and they can be difficult to diagnose based on a single numeric error code. Therefore, the COMAdmin Library makes extended error information through a special collection.

When extended error information is available, it is placed in the [**ErrorInfo**](errorinfo.md) collection that is related to the original collection that had the error. To retrieve the error report, get the **ErrorInfo** collection that is related to the original collection and examine the items it contains. You can retrieve the **ErrorInfo** collection by using [**GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-getcollection) on [**COMAdminCatalogCollection**](comadmincatalogcollection.md), leaving the second parameter blank where you would normally specify a parent item's Key property.

When you get an error, you must immediately get and populate the [**ErrorInfo**](errorinfo.md) collection for the collection that failed, without performing any other operations on that collection. Otherwise, the **ErrorInfo** collection is reset and does not detail that failure.

The items in the [**ErrorInfo**](errorinfo.md) collection expose the special error-reporting properties MajorRef and MinorRef, which detail the particular cause of the error. For more information, see **ErrorInfo**.

## Related topics

<dl> <dt>

[COM+ Administration Operations Within Transactions](com--administration-operations-within-transactions.md)
</dt> <dt>

[Introductory Example Using the COM+ Administration Catalog](introductory-example-using-the-com--administration-catalog.md)
</dt> <dt>

[Overview of the COMAdmin Objects](overview-of-the-comadmin-objects.md)
</dt> <dt>

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> <dt>

[Setting Properties and Saving Changes to the COM+ Catalog](setting-properties-and-saving-changes-to-the-com--catalog.md)
</dt> </dl>

 

 



