---
title: lcid
description: Indicates that the parameter is a locale ID (LCID).
ms.assetid: '4281058b-a617-4504-bc36-b18763b40897'
---

# lcid

Indicates that the parameter is a locale ID (LCID).

## Allowed on

Parameter in a member of an interface.

## Remarks

Only one parameter can have this attribute. The parameter must have the [in](in.md)attribute and not the [out](out.md) attribute, and its type must be long. The lcid attribute is not allowed on functions in dispinterfaces.

The lcidattribute allows members in the VTBL to receive an LCID at the time of invocation. By convention, the lcidparameter is the last parameter not to have the [retval](retval.md) attribute. If the member specifies [propertyput](propput.md) or [propertyputref](propputref.md), the lcid parameter must precede the parameter that represents the right side of the property assignment.

[**ITypeInfo::Invoke**](itypeinfo-invoke.md) passes the LCID of the type information into the lcidparameter. Parameters with this attribute are not displayed in user-oriented browsers.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




