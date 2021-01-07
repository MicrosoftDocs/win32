---
description: The Upgrade table contains information required during major upgrades.
ms.assetid: f5fda405-8a09-495e-aa8c-b808a2f02b0f
title: Upgrade Table
ms.topic: article
ms.date: 05/31/2018
---

# Upgrade Table

The Upgrade table contains information required during [major upgrades](major-upgrades.md). To fully enable the installer's upgrade capabilities, every package should have an [**UpgradeCode**](upgradecode.md) property and an Upgrade table. Each record in the Upgrade table gives a characteristic combination of upgrade code, product version, and language information used to identify a set of products affected by the upgrade. When the [FindRelatedProducts](findrelatedproducts-action.md) action detects an affected product installed on the system, it appends the product code to a property specified in the ActionProperty column. The [RemoveExistingProducts](removeexistingproducts-action.md) action and the [MigrateFeatureStates](migratefeaturestates-action.md) action only remove or migrate products listed in the ActionProperty column.

The Upgrade table contains the columns shown in the following table.



| Column         | Type                         | Key | Nullable |
|----------------|------------------------------|-----|----------|
| UpgradeCode    | [GUID](guid.md)             | Y   | N        |
| VersionMin     | [Text](text.md)             | Y   | Y        |
| VersionMax     | [Text](text.md)             | Y   | Y        |
| Language       | [Text](text.md)             | Y   | Y        |
| Attributes     | [Integer](integer.md)       | Y   | N        |
| Remove         | [Formatted](formatted.md)   | N   | Y        |
| ActionProperty | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="UpgradeCode"></span><span id="upgradecode"></span><span id="UPGRADECODE"></span>UpgradeCode
</dt> <dd>

The [UpgradeCode](upgradecode.md) property in this column specifies the upgrade code of all products that are to be detected by the [FindRelatedProducts](findrelatedproducts-action.md) action.

</dd> <dt>

<span id="VersionMin"></span><span id="versionmin"></span><span id="VERSIONMIN"></span>VersionMin
</dt> <dd>

Lower boundary of the range of product versions detected by [FindRelatedProducts](findrelatedproducts-action.md). Enter **msidbUpgradeAttributesVersionMinInclusive** in Attributes to include VersionMin in the range. If VersionMin equals an empty string ("") it is evaluated the same as 0. If VersionMin is null, FindRelatedProducts ignores **msidbUpgradeAttributesVersionMinInclusive** and detects all previous versions. VersionMin and VersionMax must not both be null.

VersionMin must be a valid product version as described for the [**ProductVersion**](productversion.md) property. Note that Windows Installer uses only the first three fields of the product version. If you include a fourth field in your product version, the installer ignores the fourth field.

</dd> <dt>

<span id="VersionMax"></span><span id="versionmax"></span><span id="VERSIONMAX"></span>VersionMax
</dt> <dd>

Upper boundary of the range of product versions detected by the [FindRelatedProducts](findrelatedproducts-action.md) action. Enter **msidbUpgradeAttributesVersionMaxInclusive** in Attributes to include VersionMax in the range. If VersionMax is an empty string (""), it is evaluated the same as 0. If VersionMax is null, FindRelatedProducts ignores **msidbUpgradeAttributesVersionMaxInclusive** and detects all product versions greater than (or greater than or equal to) the lower boundary specified by VersionMin and **msidbUpgradeAttributesVersionMinInclusive**. VersionMin and VersionMax must not both be null.

VersionMax must be a valid product version as described for the [**ProductVersion**](productversion.md) property. Note that Windows Installer uses only the first three fields of the product version. If you include a fourth field in your product version, the installer ignores the fourth field.

</dd> <dt>

<span id="Language"></span><span id="language"></span><span id="LANGUAGE"></span>Language
</dt> <dd>

The set of languages detected by [FindRelatedProducts](findrelatedproducts-action.md). Enter a list of numeric language identifiers (LANGID) separated by commas. Enter **msidbUpgradeAttributesLanguagesExclusive** in Attributes to detect all languages exclusive of those listed in Language. If Language is null or an empty string (""), FindRelatedProducts ignores **msidbUpgradeAttributesLanguagesExclusive** and detects all languages.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

This column contains bit flags specifying attributes of the Upgrade table.



| Bit flag name                                 | Decimal | Hexadecimal | Attribute                                                                                                            |
|-----------------------------------------------|---------|-------------|----------------------------------------------------------------------------------------------------------------------|
| **msidbUpgradeAttributesMigrateFeatures**     | 1       | 0x001       | Migrates feature states by enabling the logic in the [MigrateFeatureStates](migratefeaturestates-action.md) action. |
| **msidbUpgradeAttributesOnlyDetect**          | 2       | 0x002       | Detects products and applications but does not remove.                                                               |
| **msidbUpgradeAttributesIgnoreRemoveFailure** | 4       | 0x004       | Continues installation upon failure to remove a product or application.                                              |
| **msidbUpgradeAttributesVersionMinInclusive** | 256     | 0x100       | Detects the range of versions including the value in VersionMin.                                                     |
| **msidbUpgradeAttributesVersionMaxInclusive** | 512     | 0x200       | Detects the range of versions including the value in VersionMax.                                                     |
| **msidbUpgradeAttributesLanguagesExclusive**  | 1024    | 0x400       | Detects all languages, excluding the languages listed in the Language column.                                        |



 

</dd> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>Remove
</dt> <dd>

The installer sets the [**REMOVE**](remove.md) property to features specified in this column. The features to be removed can be determined at run time. The [Formatted](formatted.md) string entered in this field must evaluate to a comma-delimited list of feature names. For example: \[Feature1\],\[Feature2\],\[Feature3\]. No features are removed if the field contains formatted text that evaluates to an empty string (""). The installer sets REMOVE=ALL only if the Remove field is empty. Note the difference between an empty string and empty field. If the field is empty, it is null.

</dd> <dt>

<span id="ActionProperty"></span><span id="actionproperty"></span><span id="ACTIONPROPERTY"></span>ActionProperty
</dt> <dd>

When the [FindRelatedProducts](findrelatedproducts-action.md) action detects a related product installed on the system, it appends the product code to the property specified in this field. The property specified in this column must be a public property and the package author must add the property to the [**SecureCustomProperties**](securecustomproperties.md) property. Each row in the Upgrade table must have a unique ActionProperty value. After FindRelatedProducts, the value of this property is a list product codes, separated by semicolons (;), detected on the system.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
[ICE61](ice61.md)  
[ICE66](ice66.md)  
</dl>

 

 



