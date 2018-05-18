---
title: AccNameContainsInvalidString
description: AccNameContainsInvalidString
ms.assetid: '392E4D10-4A8E-4118-B0E7-F74571812043'
---

# AccNameContainsInvalidString

## Text

accName should not contain the string {0}

## Type

Error

## Description

The name of an element contains invalid characters (these characters are replaced by AccChecker). For example, the [**get\_accName**](iaccessible-iaccessible--get-accname.md) method used to retrieve the MSAA name of an element returns a string that contains tab, newline, or ampersand characters.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an element might have an unpronounceable, non-intuitive name.

## Possible causes

The element or its parent has an incorrectly assigned name or label.

## Related topics

<dl> <dt>

[**IAccessible::get\_accName**](iaccessible-iaccessible--get-accname.md)
</dt> <dt>

[Name Property](name-property.md)
</dt> </dl>

 

 




