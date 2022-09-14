---
description: The package code of the upgrade package must be changed from that of the original product.
ms.assetid: 786e864a-93e0-4ea6-adab-e87afbdd6ac2
title: Updating Summary Information for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Summary Information for an Upgrade

The package code of the upgrade package must be changed from that of the original product. The package code is stored in the [**Revision Number Summary**](revision-number-summary.md) Property. For details, see [Package Codes](package-codes.md). Use Msiinfo.exe, or another editor, to change the summary information of MNP2001.msi as described in [Adding Summary Information](adding-summary-information.md).



| Summary information property                                                   | Data                                                                             | Notes                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Template**](template-summary.md)(Platform and Language)<br/>         | ;1033                                                                            | Platform and language used by the database. If the platform specification is missing in the [**Template**](template-summary.md) Summary property value, the installer assumes the Intel architecture. The [**ProductLanguage**](productlanguage.md) property from the database is typically used for this summary property. The sample's Language ID indicates that the package uses U.S. English. |
| [**Revision Number**](revision-number-summary.md)(Package Code)<br/>    | {A0EC5348-1D02-4FF6-93F5-61BD7AC1772E}                                           | This is the package code [GUID](guid.md) that uniquely identifies the sample package. If you reproduce this sample, use a utility such as GUIDGEN to generate a different GUID for your package. The results of GUIDGEN contain lowercase characters, note that you must change all lowercase characters to uppercase for a valid package code.                                                     |
| [**Page Count**](page-count-summary.md)(Minimum Installer Version)<br/> | 200                                                                              | For a minimum Windows Installer version 2.0, this property should be set to the integer 200.                                                                                                                                                                                                                                                                                                         |
| [**Word Count**](word-count-summary.md)(Type of Source)<br/>            | 0                                                                                | The global source type for the package is long file names and uncompressed. For more information, see [Compressed and Uncompressed Sources](compressed-and-uncompressed-sources.md) and the description of the Attributes column of the [File table](file-table.md).                                                                                                                               |
| [**Title**](title-summary.md)                                                 | Installation Database                                                            | Informs users that this database is for an installation rather than a transform or a patch.                                                                                                                                                                                                                                                                                                          |
| [**Subject**](subject-summary.md)                                             | MNP2001                                                                          | File browsers can display this as the product to be installed with this database.                                                                                                                                                                                                                                                                                                                    |
| [**Keywords**](keywords-summary.md)                                           | Installer, MSI, Database                                                         | File browsers that are capable of keyword searching can search for these words.                                                                                                                                                                                                                                                                                                                      |
| [**Author**](author-summary.md)                                               | Microsoft Corporation                                                            | Name of the product's manufacturer.                                                                                                                                                                                                                                                                                                                                                                  |
| [**Comments**](comments-summary.md)                                           | This installer database contains the logic and data required to install Notepad. | Informs users about the purpose of this database.                                                                                                                                                                                                                                                                                                                                                    |
| [**Creating Application**](creating-application-summary.md)                   | Orca                                                                             | Application used to create the installation database. The sample specifies the Orca database editor as an example.                                                                                                                                                                                                                                                                                   |
| [**Security**](security-summary.md)                                           | 0                                                                                | The sample database is unrestricted read-write.                                                                                                                                                                                                                                                                                                                                                      |



 

[Continue](validating-an-installation-upgrade.md)

 

 




