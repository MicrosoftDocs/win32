---
description: Summary properties for installation packages, transforms, and patches are described in the following tables.
ms.assetid: b44b24b7-7fc4-4c3c-9d10-7e2f3c43cf36
title: Summary Property Descriptions
ms.topic: article
ms.date: 05/31/2018
---

# Summary Property Descriptions

Summary properties for installation packages, transforms, and patches are described in the following tables. Note that the meaning of a particular summary property can be different depending on whether the database belongs to an installation package, transform, or patch package. For more information about the property IDs, PIDs, and types, see [Summary Information Stream Property Set](summary-information-stream-property-set.md).

## Installation Packages



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Summary property</th>
<th>Meaning of this property in an Installation database</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="title-summary.md"><strong>Title</strong></a></td>
<td>A description of this file as an installation package. The description should include the phrase &quot;<a href="about-the-installer-database.md">Installation Database</a>.&quot;</td>
</tr>
<tr class="even">
<td><a href="subject-summary.md"><strong>Subject</strong></a></td>
<td>The name of the product installed by this package. This should be the same name as in the <a href="productname.md"><strong>ProductName</strong></a> property.</td>
</tr>
<tr class="odd">
<td><a href="author-summary.md"><strong>Author</strong></a></td>
<td>The name of the manufacturer of this product. This should be the same name as in the <a href="manufacturer.md"><strong>Manufacturer</strong></a> property.</td>
</tr>
<tr class="even">
<td><a href="keywords-summary.md"><strong>Keywords</strong></a></td>
<td>A list of keywords that may be used by file browsers to do keyword searches for a file. The keywords should include &quot;Installer&quot; as well as product-specific keywords.</td>
</tr>
<tr class="odd">
<td><a href="comments-summary.md"><strong>Comments</strong></a></td>
<td>Contains the phrase: &quot;This installer database contains the logic and data required to install <<em>product name</em>>.&quot;</td>
</tr>
<tr class="even">
<td><a href="template-summary.md"><strong>Template</strong></a> (REQUIRED)</td>
<td>The platform and languages compatible with this installation package. See <a href="template-summary.md"><strong>Template</strong></a> for syntax.</td>
</tr>
<tr class="odd">
<td><a href="last-saved-by-summary.md"><strong>Last Saved By</strong></a></td>
<td>Developers of database editing tools may use this property during the development process to track the last person to modify the installation database. This property should be set to Null in a final shipping database. The installer sets this property to the value of the <a href="logonuser.md"><strong>LogonUser</strong></a> property during an <a href="administrative-installation.md"><strong>administrative installation</strong></a>. The installer never uses this property and a user never needs to modify it.</td>
</tr>
<tr class="even">
<td><a href="revision-number-summary.md"><strong>Revision Number</strong></a> (REQUIRED)</td>
<td>Contains the <a href="package-codes.md">package code</a> for the installer package.</td>
</tr>
<tr class="odd">
<td><a href="last-printed-summary.md"><strong>Last Printed</strong></a></td>
<td>May be set to the date and time during an <a href="administrative-installation.md">administrative installation</a> to record when the administrative image was created.</td>
</tr>
<tr class="even">
<td><a href="create-time-date-summary.md"><strong>Create Time/Date</strong></a></td>
<td>The time and date when this installer database was created.</td>
</tr>
<tr class="odd">
<td><a href="last-saved-time-date-summary.md"><strong>Last Saved Time/Date</strong></a></td>
<td>The current system time and date at the time the installer database was last saved. Initially null.</td>
</tr>
<tr class="even">
<td><a href="page-count-summary.md"><strong>Page Count</strong></a> (REQUIRED)</td>
<td>Contains a value used to identify the minimum installer version required by this installation package. For example, if the package requires at minimum the 2.0 version of the installer, this property should be set to an integer of 200.
<blockquote>
[!Note]<br />
The value of this property must be 200 or greater with <a href="64-bit-windows-installer-packages.md">64-bit Windows Installer Packages</a>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="word-count-summary.md"><strong>Word Count</strong></a> (REQUIRED)</td>
<td>The type of the source file image. Stored in place of the standard Count property. This property is a bit field. See the <a href="word-count-summary.md"><strong>Word Count</strong></a> topic for the values.<br/> Starting with Windows Installer version 4.0 on Windows Vista, this property includes bits to specify whether elevated privileges are required.<br/></td>
</tr>
<tr class="even">
<td><a href="character-count-summary.md"><strong>Character Count</strong></a></td>
<td>Null</td>
</tr>
<tr class="odd">
<td><a href="creating-application-summary.md"><strong>Creating Application</strong></a></td>
<td>Contains the name of the software used to author this installation database.</td>
</tr>
<tr class="even">
<td><a href="security-summary.md"><strong>Security</strong></a></td>
<td>The value of this property should be 2 - Recommended read-only.</td>
</tr>
<tr class="odd">
<td><a href="codepage-summary.md"><strong>Codepage</strong></a></td>
<td>The numeric value of the ANSI code page used to display the Summary Information. This property must be set before any string properties are set in the summary information.</td>
</tr>
</tbody>
</table>



 

## Transforms



| Summary property                                              | Meaning of this property in a Transform                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Title**](title-summary.md)                                | A description of this file as a transform. The description should include the phrase: "[Transform](database-transforms.md)."                                                                                                                                                                     |
| [**Subject**](subject-summary.md)                            | The name of the product installed by the original installation package. This should be the same value as the [**Subject Summary**](subject-summary.md) property in the original installation package.                                                                                            |
| [**Author**](author-summary.md)                              | The name of the manufacturer of this transform.                                                                                                                                                                                                                                                   |
| [**Keywords**](keywords-summary.md)                          | A list of keywords that may be used by file browsers to do keyword searches for a file. The keywords should include "Installer" as well as product-specific keywords.                                                                                                                             |
| [**Comments**](comments-summary.md)                          | Contains the phrase: "This transform contains the logic and data required to install <*product name*>."                                                                                                                                                                                     |
| [**Template**](template-summary.md) (REQUIRED)               | The platform and language versions compatible with this transform. This value may be left blank if there are no restrictions. Only one language can be specified for a transform. For more information about the syntax, see [**Template**](template-summary.md).                                |
| [**Last Saved By**](last-saved-by-summary.md)                | The platform and language ID(s) that the database has after it has been transformed. The [**Template Summary**](template-summary.md) property in the new database should be set to the same values.                                                                                              |
| [**Revision Number**](revision-number-summary.md) (REQUIRED) | A list of the product code GUIDs and version of the new and original products and the upgrade code GUID. The list is separated by semicolons as follows. *Original-Product-Code Original-Product-Version*;*New-Product Code New-Product-Version*; *Upgrade-Code*<br/>                       |
| [**Last Printed**](last-printed-summary.md)                  | Null                                                                                                                                                                                                                                                                                              |
| [**Create Time/Date**](create-time-date-summary.md)          | The time and date when the transform was created.                                                                                                                                                                                                                                                 |
| [**Last Saved Time/Date**](last-saved-time-date-summary.md)  | The current system time and date at the time the transform was saved. Initially null.                                                                                                                                                                                                             |
| [**Page Count**](page-count-summary.md) (REQUIRED)           | A value used to indicate the minimum installer version required to process the transform. The value should be set to the greater of the two [**Page Count**](page-count-summary.md) property values that belong to the databases used to generate the transform.                                 |
| [**Word Count**](word-count-summary.md) (REQUIRED)           | Null                                                                                                                                                                                                                                                                                              |
| [**Character Count**](character-count-summary.md)            | This part of the summary information stream is divided into two 16-bit words. The upper word contains [*transform validation flags*](t-gly.md). Lower word contains [*transform error condition flags*](t-gly.md). |
| [**Creating Application**](creating-application-summary.md)  | Contains the name of the software used to create this transform.                                                                                                                                                                                                                                  |
| [**Security**](security-summary.md)                          | The value of this property should be 4 - Enforced read-only.                                                                                                                                                                                                                                      |
| [**Codepage**](codepage-summary.md)                          | The numeric value of the ANSI code page used to display the Summary Information. This property must be set before any string properties can be set in the summary information.                                                                                                                    |



 

## Patch Packages



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Summary property</th>
<th>Meaning of this property in a Patch package</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="title-summary.md"><strong>Title</strong></a></td>
<td>A description of this file as a patch package. The description should include the phrase: &quot;<a href="patch-packages.md">Patch</a>.&quot;</td>
</tr>
<tr class="even">
<td><a href="subject-summary.md"><strong>Subject</strong></a></td>
<td>A description of the patch that includes the name of the product.</td>
</tr>
<tr class="odd">
<td><a href="author-summary.md"><strong>Author</strong></a></td>
<td>The name of the manufacturer of the patch package.</td>
</tr>
<tr class="even">
<td><a href="keywords-summary.md"><strong>Keywords</strong></a></td>
<td>A semicolon delimited list of sources of the patch.</td>
</tr>
<tr class="odd">
<td><a href="comments-summary.md"><strong>Comments</strong></a></td>
<td>Contains the phrase: &quot;This patch contains the logic and data required to install <<em>product name</em>>.&quot;</td>
</tr>
<tr class="even">
<td><a href="template-summary.md"><strong>Template</strong></a> (REQUIRED)</td>
<td>A semicolon delimited list of the product codes that can accept this patch.</td>
</tr>
<tr class="odd">
<td><a href="last-saved-by-summary.md"><strong>Last Saved By</strong></a></td>
<td>A semicolon delimited list of transform substorage names in the order they are applied by this patch.</td>
</tr>
<tr class="even">
<td><a href="revision-number-summary.md"><strong>Revision Number</strong></a> (REQUIRED)</td>
<td>Contains the GUID patch code for the patch. This may be followed by a list of patch code GUIDs for patches that are removed when this patch is applied. The patch codes are concatenated with no delimiters separating GUIDs in the list.
<blockquote>
[!Note]<br />
If the patch package contains a <a href="msipatchsequence-table.md"><strong>MsiPatchSequence</strong></a> table, the patch does not remove patches listed after the current patch's GUID.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="last-printed-summary.md"><strong>Last Printed</strong></a></td>
<td>Null</td>
</tr>
<tr class="even">
<td><a href="create-time-date-summary.md"><strong>Create Time/Date</strong></a></td>
<td>The time and date when patch file was created.</td>
</tr>
<tr class="odd">
<td><a href="last-saved-time-date-summary.md"><strong>Last Saved Time/Date</strong></a></td>
<td>The current system time and date at the time the patch package was saved. This value is initially null.</td>
</tr>
<tr class="even">
<td><a href="page-count-summary.md"><strong>Page Count</strong></a> (REQUIRED)</td>
<td>Null</td>
</tr>
<tr class="odd">
<td><a href="word-count-summary.md"><strong>Word Count</strong></a> (REQUIRED)</td>
<td>Contains a value that indicates the minimum Windows Installer version that is required to install the patch. A patch with a word count value of 4 requires Windows Installer version 3.0 or higher for the patch to be applied. A value of 3 indicates that Windows Installer version 2.0 or higher is required. A value of 2 indicates that Windows Installer version 1.2 or higher is required. The default value is 1.</td>
</tr>
<tr class="even">
<td><a href="character-count-summary.md"><strong>Character Count</strong></a></td>
<td>Null</td>
</tr>
<tr class="odd">
<td><a href="creating-application-summary.md"><strong>Creating Application</strong></a></td>
<td>The name of the software used to create the patch.</td>
</tr>
<tr class="even">
<td><a href="security-summary.md"><strong>Security</strong></a></td>
<td>The value of this property should be 4 - Enforced read-only.</td>
</tr>
<tr class="odd">
<td><a href="codepage-summary.md"><strong>Codepage</strong></a></td>
<td>The numeric value of the ANSI code page used to display the Summary Information. This property must be set before any string properties are set in the summary information.</td>
</tr>
</tbody>
</table>



 

 

 




