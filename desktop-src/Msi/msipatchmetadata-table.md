---
description: The MsiPatchMetadata Table contains information about a Windows Installer patch that is required to remove the patch and that is used by Add/Remove Programs.
ms.assetid: b1c30e16-6c91-451a-8b75-7ddbcefcc092
title: MsiPatchMetadata Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPatchMetadata Table

The MsiPatchMetadata Table contains information about a Windows Installer patch that is required to remove the patch and that is used by **Add/Remove Programs**.

Patches installed without this table present in the patch database (.msp file) cannot be removed, and are missing some information from **Add/Remove Programs**. The table must be in the database of the patch file and not in a transform in the patch.

The MsiPatchMetadata Table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Company  | [Identifier](identifier.md) | Y   | Y        |
| Property | [Identifier](identifier.md) | Y   | N        |
| Value    | [Text](text.md)             | N   | N        |



 

## Columns

<dl> <dt>

<span id="Company"></span><span id="company"></span><span id="COMPANY"></span>Company
</dt> <dd>

The name of the company. An empty field (a Null value) indicates that the row contains one of the standard metadata properties of the Windows Installer. For more information, see the Remarks section of this topic.

By adding a row to the table and entering a company name in this field, you can add any company to extend the property set.

</dd> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

The name of a metadata property.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The value of the metadata property. This can never be Null or an empty string.

</dd> </dl>

## Remarks

Available in Windows Installer 3.0 and later.

Rows in the MsiPatchMetadata Table that contain a Null value in the CompanyName field refer to one of the following standard Windows Installer metadata properties.




| Property | Description | 
|----------|-------------|
| AllowRemoval | Indicates whether or not the patch is an <a href="uninstallable-patches.md">Uninstallable Patch</a>. If the value field contains 0 (zero), the patch cannot be removed. If the value field contains one (1), the patch is an Uninstallable Patch.This property is registered and its value can be obtain by using the <a href="/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa"><strong>MsiGetPatchInfoEx</strong></a> function. <br /> | 
| ManufacturerName | Name of the manufacturer of the application. | 
| MinorUpdateTargetRTM | Indicates that the patch targets the RTM version of the product or the most recent major upgrade patch. Author this optional property in minor upgrade patches that contain sequencing information to indicate that the patch removes of all patches up to the RTM version of the product, or up to the most recent major upgrade patch. This property is available in Windows Installer 3.1 and later. <br /> | 
| TargetProductName | Name of the application or target application suite. | 
| MoreInfoURL | A URL that provides information specific to this patch. This property is registered and its value can be obtained by using the <a href="/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa"><strong>MsiGetPatchInfoEx</strong></a> function. Beginning with Windows XP with Service Pack 2 (SP2), this value can be the support link for the patch displayed in <strong>Add/Remove Programs</strong>.<br /> | 
| CreationTimeUTC | Creation time of the .msp file in the form of mm-dd-yy HH:MM (month-day-year hour:minute). | 
| DisplayName | A title for the patch that is okay for public display. This property is registered, and its value can be obtained by using the <a href="/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa"><strong>MsiGetPatchInfoEx</strong></a> function. Beginning with Windows XP with SP2, this value is the name of the patch that is displayed in <strong>Add/Remove Programs</strong>.<br /> | 
| Description | Brief description of the patch. | 
| Classification | A string value that contains the arbitrary category of updates as defined by the author of the patch. For example, patch authors can specify that each patch be classified as a Hotfix, Security Rollup, Critical Update, Update, Service Pack, or Update Rollup. This property is required. | 
| OptimizeCA | Indicates whether the Windows Installer should skip custom actions when applying the patch. This can reduce the time required to apply the patch. The OptimizeCA property can have one of the following values:<br /><ul><li>0 - Do not skip any custom actions.</li><li>1 - Skip property and directory assignment custom actions. <a href="custom-action-type-35.md">Custom Action Type 35</a> and <a href="custom-action-type-51.md">Custom Action Type 51</a> can be property and directory assignment custom actions.</li><li>2 - Skip immediate custom actions that do not fall into the property or directory assignments. The immediate custom actions do not include msidbCustomActionTypeInScript option in the Type column of the <a href="customaction-table.md">CustomAction Table</a>.</li><li>4 - Skip custom actions that run within the script.</li></ul>The value of OptimizeCA must be the same for all patches that are being installed or no custom actions are skipped. For example, if two patches are being installed, and OptimizeCA is set to the values 1 and 2 respectively, no custom actions are skipped. <br /> The values of OptimizeCA can be combined when processing multiple new patches. If all patches have a 1 (one) included in the values, then all property and directory assignment custom actions are skipped. If one patch has the value 3 (three)for the property, and one patch has the value 1 (one) for the property, the property and directory assignment custom actions are skipped. However, the other immediate custom actions run, because not all of the patches requested are skipped. <br /> | 
| OptimizedInstallMode | If this property is set to 1 (one) in all the patches to be applied in a transaction, an application of the patch is optimized if possible. For more information, see <a href="patch-optimization.md">Patch Optimization</a>. Available beginning with Windows Installer 3.1. | 




 

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




