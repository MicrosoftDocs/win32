---
description: This section describes which functions in the Windows Installer API can call the summary information stream properties. For more information on the summary information stream and how it works with databases, see About the Summary Information Stream.
ms.assetid: 2c22fe52-52a9-4e3f-9482-b5e41b91b3ae
title: Using the Summary Information Stream
ms.topic: article
ms.date: 05/31/2018
---

# Using the Summary Information Stream

This section describes which functions in the Windows Installer API can call the summary information stream properties. For more information on the summary information stream and how it works with databases, see [About the Summary Information Stream](about-the-summary-information-stream.md).

-   It is important to remember that the installer contains different types of databases, and some properties of the summary information stream have different meanings with different databases. For more information, see [Summary Property Descriptions](summary-property-descriptions.md).
-   When a database is opened as the output of another database, the summary information stream of the output database is actually a read-only mirror of the original database and thus cannot be changed. Additionally, it will not be persisted with the database. To create or modify the summary information for the output database it must be closed and re-opened.

The following steps describe how to use the summary information stream functions:

**To use the summary information stream properties**

1.  Obtain a handle to the database containing the summary information stream by calling the [**MsiGetSummaryInformation**](/windows/desktop/api/Msiquery/nf-msiquery-msigetsummaryinformationa) function.
2.  Call the [**MsiSummaryInfoGetPropertyCount**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfogetpropertycount) function to obtain the number of existing properties.
3.  Call the [**MsiSummaryInfoGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfogetpropertya) function to view a single summary information property.
4.  Call the [**MsiSummaryInfoSetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfosetpropertya) function to set a single property
5.  Call the [**MsiSummaryInfoPersist**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfopersist) function to save the summary information property.
6.  Call the [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa) function to create the summary information for an existing transform.

[Orca.exe](orca-exe.md) and [Msiinfo.exe](msiinfo-exe.md) are tools that can be used to edit or display the summary information stream of a database. These tools are only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

The summary information stream can also be accessed using the following methods and properties of the Windows Installer [Automation Interface](automation-interface.md).

-   [**SummaryInfo.Property**](summaryinfo-summaryinfo.md)
-   [**SummaryInfo.PropertyCount**](summaryinfo-propertycount.md)
-   [**SummaryInfo.Persist**](summaryinfo-persist.md)
-   [**Installer.SummaryInformation**](installer-summaryinformation.md)
-   [**Database.SummaryInformation**](database-summaryinformation.md)
-   [**Database.CreateTransformSummaryInfo**](database-createtransformsummaryinfo.md)

The VBScript file WiSumInf.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script can be used to manage the summary information stream of a Windows Installer package. For more information about WiSumInf.vbs, see [Manage Summary Information](manage-summary-information.md).

 

 



