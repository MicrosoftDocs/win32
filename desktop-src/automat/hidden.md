---
title: hidden
description: Indicates that the item exists, but should not be displayed in a user-oriented browser.
ms.assetid: '23141a6d-8e38-4f90-940c-93f74fde0e61'
---

# hidden

Indicates that the item exists, but should not be displayed in a user-oriented browser.

## Allowed on

Property, method, coclass, dispinterface, interface, library.

## Flags

<dl> VARFLAG\_FHIDDEN  
FUNCFLAG\_FHIDDEN  
TYPEFLAG\_FHIDDEN  
</dl>

## Remarks

This attribute allows members to be removed from an interface by shielding them from further use, while maintaining compatibility with existing code.

When specified for a library, the attribute prevents the entire library from being displayed. It is intended for use by controls. Hosts need to create a new type library that wraps the control with extended properties.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




