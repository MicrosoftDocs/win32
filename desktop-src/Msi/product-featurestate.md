---
description: The FeatureState property is the installation state of the feature for the instance of this product.This property calls MsiQueryFeatureStateEx, with the ProductCode, UserSid and Context of the object. The feature Id is provided as a parameter.
ms.assetid: 6821be80-4065-465e-b4c9-4cf17856bc5f
title: Product.FeatureState method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.FeatureState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.FeatureState method

The **FeatureState** property is the installation state of the feature for the instance of this product.

This property calls [**MsiQueryFeatureStateEx**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestateexa), with the *ProductCode*, *UserSid* and *Context* of the object. The feature Id is provided as a parameter.

## Syntax


```JScript
Product.FeatureState(
  FeatureId
)
```



## Parameters

<dl> <dt>

*FeatureId* 
</dt> <dd>

Feature Id appearing in the Feature column of the [Feature Table](feature-table.md).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the call succeeds, the property contains the value as a **DWORD**.



| State                    | Meaning                                      |
|--------------------------|----------------------------------------------|
| INSTALLSTATE\_ADVERTISED | This feature is advertised.                  |
| INSTALLSTATE\_LOCAL      | The feature is installed locally.            |
| INSTALLSTATE\_SOURCE     | The feature is installed to run from source. |



 

If the call fails, the property contains an error code from [**MsiQueryFeatureStateEx**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestateexa).



| Error                     | Meaning                                                                                                                                    |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR\_ACCESS\_DENIED     | The calling process must have administrative privileges to get information for a product installed for a user other than the current user. |
| ERROR\_BAD\_CONFIGURATION | The configuration data is corrupt.                                                                                                         |
| ERROR\_INVALID\_PARAMETER | An invalid parameter was passed to the function.                                                                                           |
| ERROR\_SUCCESS            | The function completed successfully.                                                                                                       |
| ERROR\_UNKNOWN\_FEATURE   | The feature ID does not identify a known feature.                                                                                          |
| ERROR\_UNKNOWN\_PRODUCT   | The product code does not identify a known product.                                                                                        |
| ERROR\_FUNCTION\_FAILED   | An unexpected internal failure.                                                                                                            |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IProduct is defined as 000C10A0-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                          |



## See also

<dl> <dt>

[**Product**](product-object.md)
</dt> <dt>

[**MsiQueryFeatureStateEx**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestateexa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




