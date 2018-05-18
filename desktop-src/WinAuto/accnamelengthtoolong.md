---
title: AccNameLengthTooLong
description: AccNameLengthTooLong
ms.assetid: '68997AE9-91FC-4DAD-8356-FEE6C6919939'
---

# AccNameLengthTooLong

## Text

Element's name should not return a string longer than {0} character

## Type

Error

## Description

The name of an element contains too many characters. For example, the [**get\_accName**](iaccessible-iaccessible--get-accname.md) method used to retrieve the MSAA name of an element returns a string greater than the limit of 32000 characters.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an element might have an unpronounceable, non-intuitive name.

## Possible causes

The element or its parent has an incorrectly assigned name or label.

## Related topics

<dl> <dt>

[**IAccessible::get\_accName**](iaccessible-iaccessible--get-accname.md)
</dt> <dt>

[Name Property](name-property.md)
</dt> </dl>

 

 




