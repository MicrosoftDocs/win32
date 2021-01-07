---
description: The PatchMetadata Table contains information about a Windows Installer patch that is required to remove a patch and that is used by Add/Remove Programs.
ms.assetid: 09a06de4-0713-4e92-ab29-f34f6c94b677
title: PatchMetadata Table (PATCHWIZ.DLL)
ms.topic: article
ms.date: 05/31/2018
---

# PatchMetadata Table (PATCHWIZ.DLL)

The PatchMetadata Table contains information about a Windows Installer patch that is required to remove a patch and that is used by Add/Remove Programs. All the properties in the PatchMetadata Table are added to the [MsiPatchMetadata Table](msipatchmetadata-table.md) of the .msp file for a patch.

The PatchMetadata Table is required in patch creation properties files (.pcp files) that have a MinimumRequiredMsiVersion equal to 300 in the [Properties Table](properties-table-patchwiz-dll-.md). The table is optional if MinimumRequiredMsiVersion is not equal to 300.

The PatchMetadata Table has the following columns.



| Column   | Type | Key | Nullable |
|----------|------|-----|----------|
| Company  | text | Y   | Y        |
| Property | text | Y   | N        |
| Value    | text |     | Y        |



 

### Columns

<dl> <dt>

<span id="Company"></span><span id="company"></span><span id="COMPANY"></span>Company
</dt> <dd>

The name of the company. An empty field (a Null value) indicates that this row contains one of the standard metadata properties. A company can extend the property set by adding a row to the table, and entering a company name in this field.

</dd> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

The name of a metadata property. The AllowRemoval, ManufacturerName, TargetProductName, MoreInfoURL, DisplayName, Description, and Classification properties are required in the PatchMetadata Table . This field must contain one of the following standard metadata properties if the Company field is empty (a Null value).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AllowRemoval</td>
<td>An integer value that indicates whether or not the patch is an <a href="uninstallable-patches.md">Uninstallable Patch</a>. If the Value field contains a 0 (zero), the patch cannot be removed. If the Value field contains 1 (one), the patch is an Uninstallable Patch. This property is required.This property is registered and its value can be obtain by using the <a href="/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa"><strong>MsiGetPatchInfoEx</strong></a> function.<br/></td>
</tr>
<tr class="even">
<td>ManufacturerName</td>
<td>A string value that contains the name of the manufacturer of the application. This property is required.</td>
</tr>
<tr class="odd">
<td>MinorUpdateTargetRTM</td>
<td>Indicates that the patch targets the RTM version of the product or the most recent major upgrade patch. Author this optional property in minor upgrade patches that contain sequencing information to indicate that the patch removes of all patches up to the RTM version of the product, or up to the most recent major upgrade patch. This property is available beginning with Windows Installer 3.1.
<blockquote>
[!Note]<br />
To require that Windows Installer 3.1 be installed to apply the patch, set the MinimumRequiredMsiVersion property to 310 in the <a href="properties-table-patchwiz-dll-.md">Properties Table</a> of the .pcp file.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>TargetProductName</td>
<td>A string value that contains the name of the application or target application suite. This property is required.</td>
</tr>
<tr class="odd">
<td>MoreInfoURL</td>
<td>A string value that contains a URL pointing to information for this patch. This required property is registered and its value can be obtained by using the <a href="/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa"><strong>MsiGetPatchInfoEx</strong></a> function. Beginning with Windows XP with Service Pack 2 (SP2), this value can be the support link for the patch displayed in Add/Remove Programs.<br/></td>
</tr>
<tr class="even">
<td>CreationTimeUTC</td>
<td>A string value that contains the creation time of the .msp file in the form mm-dd-yy HH:MM (month-day-year hour:minute). This property is optional.</td>
</tr>
<tr class="odd">
<td>DisplayName</td>
<td>A string value that contains the title for the patch that is suitable for public display. This property is required. This property is registered and its value can be obtain by using the <a href="/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa"><strong>MsiGetPatchInfoEx</strong></a> function. Beginning with Windows XP with SP2, this value is the name of the patch displayed in Add/Remove Programs beginning with Windows XP with SP2.<br/></td>
</tr>
<tr class="even">
<td>Description</td>
<td>A string value that contains a brief description of the patch. This property is required.</td>
</tr>
<tr class="odd">
<td>Classification</td>
<td>A string value that contains the arbitrary category of updates as defined by the author of the patch. For example, patch authors can specify that each patch be classified as a Hotfix, Security Rollup, Critical Update, Update, Service Pack, or Update Rollup. This property is required.</td>
</tr>
<tr class="even">
<td>OptimizedInstallMode</td>
<td>If this property is set to 1 (one) in all the patches to be applied in a transaction, the application of the patch is optimized if possible. For information, see <a href="patch-optimization.md">Patch Optimization</a>. Available beginning with Windows Installer 3.1.</td>
</tr>
</tbody>
</table>



 

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

Value of the metadata property. This can never be Null or an empty string. This value can be localized.

</dd> </dl>

### Remarks

Available beginning in Windows Installer 3.0.

All properties authored into the PatchMetadata Table are added to the MsiPatchMetadata table of the msp file. AllowRemoval, MoreInfoURL and DisplayName properties are registered and are accessible through the [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa).

 

 




