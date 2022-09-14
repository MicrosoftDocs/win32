---
description: The following summary information properties must be defined in every installation package, using a software tool to access the Istream interface of the Summary Information Stream.
ms.assetid: 9775959f-5ab2-43cd-8cc8-9d81945b4ec6
title: Adding Summary Information
ms.topic: article
ms.date: 05/31/2018
---

# Adding Summary Information

The following summary information properties must be defined in every installation package, using a software tool to access the **Istream** interface of the [Summary Information Stream](summary-information-stream.md). For example, you can use the tool Msiinfo.exe provided with the Windows Installer SDK to set these properties. If these properties are not set, the package will not pass [Package Validation](package-validation.md).



| Summary information property                                                   | Data                                   | Notes                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Template**](template-summary.md)(Platform and Language)<br/>         | ;1033                                  | Platform and language used by the database. If the platform specification is missing in the [**Template**](template-summary.md) Summary property value, the installer assumes the Intel architecture. The [**ProductLanguage**](productlanguage.md) property from the database is typically used for this summary property. The sample's Language ID indicates that the package uses U.S. English. |
| [**Revision Number**](revision-number-summary.md)(Package Code)<br/>    | {4966AEC4-3C59-4B07-9B98-1B6A7103C0D3} | This is the package code [GUID](guid.md) that uniquely identifies the sample package. If you reproduce this sample, use a utility such as GUIDGEN to generate a different GUID for your package. The results of GUIDGEN contain lowercase characters, note that you must change all lowercase characters to uppercase for a valid package code. See [Package Codes](package-codes.md).             |
| [**Page Count**](page-count-summary.md)(Minimum Installer Version)<br/> | 200                                    | For a minimum Windows Installer 2.0, this property should be set to the integer 200.                                                                                                                                                                                                                                                                                                                 |
| [**Word Count**](word-count-summary.md)(Type of Source)<br/>            | 0                                      | The global source type for the package is long file names and uncompressed. See [Compressed and Uncompressed Sources](compressed-and-uncompressed-sources.md) and the description of the Attributes column of the [File table](file-table.md) for more information.                                                                                                                                |



 

The remaining summary information stream properties are not required, but should be set for the MNP2000.msi sample.



| Summary information property                                 | Data                                                                             | Notes                                                                                                              |
|--------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**Title**](title-summary.md)                               | Installation Database                                                            | Informs users that this database is for an installation rather than a transform or a patch.                        |
| [**Subject**](subject-summary.md)                           | MNP2000                                                                          | File browsers can display this as the product to be installed with this database.                                  |
| [**Keywords**](keywords-summary.md)                         | Installer, MSI, Database                                                         | File browsers that are capable of keyword searching can search for these words.                                    |
| [**Author**](author-summary.md)                             | Microsoft Corporation                                                            | Name of the product's manufacturer.                                                                                |
| [**Comments**](comments-summary.md)                         | This installer database contains the logic and data required to install Notepad. | Informs users about the purpose of this database.                                                                  |
| [**Creating Application**](creating-application-summary.md) | Orca                                                                             | Application used to create the installation database. The sample specifies the Orca database editor as an example. |
| [**Security**](security-summary.md)                         | 0                                                                                | The sample database is unrestricted read-write.                                                                    |



 

You do not need the set the [**Last Saved By**](last-saved-by-summary.md), [**Last Saved Time/Date**](last-saved-time-date-summary.md), [**Create Time/Date**](create-time-date-summary.md), [**Last Printed**](last-printed-summary.md), [**Character Count**](character-count-summary.md), and [**Codepage**](codepage-summary.md) summary properties to complete this sample database. The sample relies upon the database editing tool to set and update these optional properties.

For example, to use MsiInfo to add the summary information to the sample, change to the directory containing the database and use the following command line. Do not reuse the example package ID shown below.

**Msiinfo.exe MNP2000.msi -T "Installation Database" -J Subject -A "Microsoft Corporation" -K "Installer, MSI, Database" -O "This installer database contains the logic and data required to install Notepad." -P ;1033 -V {4966AEC4-3C59-4B07-9B98-1B6A7103C0D3} -G 200 -W 0 -N Orca -U 0**

For more details about summary information, see [About the Summary Information Stream](about-the-summary-information-stream.md), [Using the Summary Information Stream](using-the-summary-information-stream.md), and [Summary Information Stream Reference](summary-information-stream-reference.md).

See the [Summary Information Stream Property Set](summary-information-stream-property-set.md) for a complete list of all the summary information properties and [Summary Property Descriptions](summary-property-descriptions.md) for their description.

[Continue](importing-the-user-interface.md)

 

 




