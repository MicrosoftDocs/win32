---
description: The FormatText method of the Record object formats fields according to the template in field 0.
ms.assetid: 89a98b88-bb74-458c-a2df-727a8084145b
title: Record.FormatText method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record.FormatText
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record.FormatText method

The **FormatText** method of the [**Record**](record-object.md) object formats fields according to the template in field 0.

## Syntax


```JScript
Record.FormatText()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **FormatText** method follows the functionality of the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function if **MsiFormatRecord** was passed a null installer handle as its first parameter. As a result, only the record field parameters are processed and properties are not available for substitution.

For example, a string such as "format this field: \[1\], format this property: \[property\]" is resolved to "format this field: value from field 1, format this property: \[property\]."

Parameters that are to be [formatted](formatted.md) are enclosed in square brackets \[...\]. The square brackets can be iterated because the substitutions are resolved from the inside out.

If a part of the string is enclosed in curly braces { } and contains no square brackets, it is left unchanged, including the curly braces.

Note in the case of [deferred execution custom actions](deferred-execution-custom-actions.md), **FormatText** only supports a limited set of properties: the CustomActionData and ProductCode properties. For more information, see [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



## See also

<dl> <dt>

[**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda)
</dt> <dt>

[Formatted](formatted.md)
</dt> <dt>

[Column Data Types](column-data-types.md)
</dt> </dl>

 

 




