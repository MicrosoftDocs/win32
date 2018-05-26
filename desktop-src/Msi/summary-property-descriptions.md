---
Description: Summary properties for installation packages, transforms, and patches are described in the following tables.
ms.assetid: b44b24b7-7fc4-4c3c-9d10-7e2f3c43cf36
title: Summary Property Descriptions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>Title</strong>](title-summary.md)</td>
<td>A description of this file as an installation package. The description should include the phrase &quot;[Installation Database](about-the-installer-database.md).&quot;</td>
</tr>
<tr class="even">
<td>[<strong>Subject</strong>](subject-summary.md)</td>
<td>The name of the product installed by this package. This should be the same name as in the [<strong>ProductName</strong>](productname.md) property.</td>
</tr>
<tr class="odd">
<td>[<strong>Author</strong>](author-summary.md)</td>
<td>The name of the manufacturer of this product. This should be the same name as in the [<strong>Manufacturer</strong>](manufacturer.md) property.</td>
</tr>
<tr class="even">
<td>[<strong>Keywords</strong>](keywords-summary.md)</td>
<td>A list of keywords that may be used by file browsers to do keyword searches for a file. The keywords should include &quot;Installer&quot; as well as product-specific keywords.</td>
</tr>
<tr class="odd">
<td>[<strong>Comments</strong>](comments-summary.md)</td>
<td>Contains the phrase: &quot;This installer database contains the logic and data required to install &lt;<em>product name</em>&gt;.&quot;</td>
</tr>
<tr class="even">
<td>[<strong>Template</strong>](template-summary.md) (REQUIRED)</td>
<td>The platform and languages compatible with this installation package. See [<strong>Template</strong>](template-summary.md) for syntax.</td>
</tr>
<tr class="odd">
<td>[<strong>Last Saved By</strong>](last-saved-by-summary.md)</td>
<td>Developers of database editing tools may use this property during the development process to track the last person to modify the installation database. This property should be set to Null in a final shipping database. The installer sets this property to the value of the [<strong>LogonUser</strong>](logonuser.md) property during an [<strong>administrative installation</strong>](administrative-installation.md). The installer never uses this property and a user never needs to modify it.</td>
</tr>
<tr class="even">
<td>[<strong>Revision Number</strong>](revision-number-summary.md) (REQUIRED)</td>
<td>Contains the [package code](package-codes.md) for the installer package.</td>
</tr>
<tr class="odd">
<td>[<strong>Last Printed</strong>](last-printed-summary.md)</td>
<td>May be set to the date and time during an [administrative installation](administrative-installation.md) to record when the administrative image was created.</td>
</tr>
<tr class="even">
<td>[<strong>Create Time/Date</strong>](create-time-date-summary.md)</td>
<td>The time and date when this installer database was created.</td>
</tr>
<tr class="odd">
<td>[<strong>Last Saved Time/Date</strong>](last-saved-time-date-summary.md)</td>
<td>The current system time and date at the time the installer database was last saved. Initially null.</td>
</tr>
<tr class="even">
<td>[<strong>Page Count</strong>](page-count-summary.md) (REQUIRED)</td>
<td>Contains a value used to identify the minimum installer version required by this installation package. For example, if the package requires at minimum the 2.0 version of the installer, this property should be set to an integer of 200.
<blockquote>
[!Note]<br />
The value of this property must be 200 or greater with [64-bit Windows Installer Packages](64-bit-windows-installer-packages.md).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Word Count</strong>](word-count-summary.md) (REQUIRED)</td>
<td>The type of the source file image. Stored in place of the standard Count property. This property is a bit field. See the [<strong>Word Count</strong>](word-count-summary.md) topic for the values.<br/> Starting with Windows Installer version 4.0 on Windows Vista, this property includes bits to specify whether elevated privileges are required.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Character Count</strong>](character-count-summary.md)</td>
<td>Null</td>
</tr>
<tr class="odd">
<td>[<strong>Creating Application</strong>](creating-application-summary.md)</td>
<td>Contains the name of the software used to author this installation database.</td>
</tr>
<tr class="even">
<td>[<strong>Security</strong>](security-summary.md)</td>
<td>The value of this property should be 2 - Recommended read-only.</td>
</tr>
<tr class="odd">
<td>[<strong>Codepage</strong>](codepage-summary.md)</td>
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
| [**Comments**](comments-summary.md)                          | Contains the phrase: "This transform contains the logic and data required to install &lt;*product name*&gt;."                                                                                                                                                                                     |
| [**Template**](template-summary.md) (REQUIRED)               | The platform and language versions compatible with this transform. This value may be left blank if there are no restrictions. Only one language can be specified for a transform. For more information about the syntax, see [**Template**](template-summary.md).                                |
| [**Last Saved By**](last-saved-by-summary.md)                | The platform and language ID(s) that the database has after it has been transformed. The [**Template Summary**](template-summary.md) property in the new database should be set to the same values.                                                                                              |
| [**Revision Number**](revision-number-summary.md) (REQUIRED) | A list of the product code GUIDs and version of the new and original products and the upgrade code GUID. The list is separated by semicolons as follows. *Original-Product-Code Original-Product-Version*;*New-Product Code New-Product-Version*; *Upgrade-Code*<br/>                       |
| [**Last Printed**](last-printed-summary.md)                  | Null                                                                                                                                                                                                                                                                                              |
| [**Create Time/Date**](create-time-date-summary.md)          | The time and date when the transform was created.                                                                                                                                                                                                                                                 |
| [**Last Saved Time/Date**](last-saved-time-date-summary.md)  | The current system time and date at the time the transform was saved. Initially null.                                                                                                                                                                                                             |
| [**Page Count**](page-count-summary.md) (REQUIRED)           | A value used to indicate the minimum installer version required to process the transform. The value should be set to the greater of the two [**Page Count**](page-count-summary.md) property values that belong to the databases used to generate the transform.                                 |
| [**Word Count**](word-count-summary.md) (REQUIRED)           | Null                                                                                                                                                                                                                                                                                              |
| [**Character Count**](character-count-summary.md)            | This part of the summary information stream is divided into two 16-bit words. The upper word contains [*transform validation flags*](t-gly.md#-msi-transform-validation-flags-gly). Lower word contains [*transform error condition flags*](t-gly.md#-msi-transform-error-condition-flags-gly). |
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
<td>[<strong>Title</strong>](title-summary.md)</td>
<td>A description of this file as a patch package. The description should include the phrase: &quot;[Patch](patch-packages.md).&quot;</td>
</tr>
<tr class="even">
<td>[<strong>Subject</strong>](subject-summary.md)</td>
<td>A description of the patch that includes the name of the product.</td>
</tr>
<tr class="odd">
<td>[<strong>Author</strong>](author-summary.md)</td>
<td>The name of the manufacturer of the patch package.</td>
</tr>
<tr class="even">
<td>[<strong>Keywords</strong>](keywords-summary.md)</td>
<td>A semicolon delimited list of sources of the patch.</td>
</tr>
<tr class="odd">
<td>[<strong>Comments</strong>](comments-summary.md)</td>
<td>Contains the phrase: &quot;This patch contains the logic and data required to install &lt;<em>product name</em>&gt;.&quot;</td>
</tr>
<tr class="even">
<td>[<strong>Template</strong>](template-summary.md) (REQUIRED)</td>
<td>A semicolon delimited list of the product codes that can accept this patch.</td>
</tr>
<tr class="odd">
<td>[<strong>Last Saved By</strong>](last-saved-by-summary.md)</td>
<td>A semicolon delimited list of transform substorage names in the order they are applied by this patch.</td>
</tr>
<tr class="even">
<td>[<strong>Revision Number</strong>](revision-number-summary.md) (REQUIRED)</td>
<td>Contains the GUID patch code for the patch. This may be followed by a list of patch code GUIDs for patches that are removed when this patch is applied. The patch codes are concatenated with no delimiters separating GUIDs in the list.
<blockquote>
[!Note]<br />
If the patch package contains a [<strong>MsiPatchSequence</strong>](msipatchsequence-table.md) table, the patch does not remove patches listed after the current patch's GUID.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Last Printed</strong>](last-printed-summary.md)</td>
<td>Null</td>
</tr>
<tr class="even">
<td>[<strong>Create Time/Date</strong>](create-time-date-summary.md)</td>
<td>The time and date when patch file was created.</td>
</tr>
<tr class="odd">
<td>[<strong>Last Saved Time/Date</strong>](last-saved-time-date-summary.md)</td>
<td>The current system time and date at the time the patch package was saved. This value is initially null.</td>
</tr>
<tr class="even">
<td>[<strong>Page Count</strong>](page-count-summary.md) (REQUIRED)</td>
<td>Null</td>
</tr>
<tr class="odd">
<td>[<strong>Word Count</strong>](word-count-summary.md) (REQUIRED)</td>
<td>Contains a value that indicates the minimum Windows Installer version that is required to install the patch. A patch with a word count value of 4 requires Windows Installer version 3.0 or higher for the patch to be applied. A value of 3 indicates that Windows Installer version 2.0 or higher is required. A value of 2 indicates that Windows Installer version 1.2 or higher is required. The default value is 1.</td>
</tr>
<tr class="even">
<td>[<strong>Character Count</strong>](character-count-summary.md)</td>
<td>Null</td>
</tr>
<tr class="odd">
<td>[<strong>Creating Application</strong>](creating-application-summary.md)</td>
<td>The name of the software used to create the patch.</td>
</tr>
<tr class="even">
<td>[<strong>Security</strong>](security-summary.md)</td>
<td>The value of this property should be 4 - Enforced read-only.</td>
</tr>
<tr class="odd">
<td>[<strong>Codepage</strong>](codepage-summary.md)</td>
<td>The numeric value of the ANSI code page used to display the Summary Information. This property must be set before any string properties are set in the summary information.</td>
</tr>
</tbody>
</table>



 

 

 




