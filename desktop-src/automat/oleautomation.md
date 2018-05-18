---
title: oleautomation
description: Indicates that an interface is compatible with Automation.
ms.assetid: '335e8f55-c313-423e-a301-8ef6a38c5b05'
---

# oleautomation

Indicates that an interface is compatible with Automation.

## Allowed on

Interface.

## Flags

<dl> TYPEFLAG\_FOLEAUTOMATION  
</dl>

## Remarks

Not allowed on dispinterfaces.

The parameters and return types specified for its members must be compatible with Automation, as listed in the following table:



| Type                                        | Description                                                                                                                                                      |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **boolean**                                 | Data item that can have the value VARIANT\_TRUE or VARIANT\_FALSE. The size corresponds to VARIANT\_BOOL.                                                        |
| **unsigned char**                           | 8-bit unsigned data item.                                                                                                                                        |
| **double**                                  | 64-bit IEEE floating-point number.                                                                                                                               |
| **float**                                   | 32-bit IEEE floating-point number.                                                                                                                               |
| **int**                                     | Signed integer, whose size is system dependent.                                                                                                                  |
| **long**                                    | 32-bit signed integer.                                                                                                                                           |
| **short**                                   | 16-bit signed integer.                                                                                                                                           |
| **BSTR**                                    | Length-prefixed string, as described in [Dispatch Interface and API Functions](75BFF268-BD85-49C4-B761-B557F4B1C588).                                            |
| **CURRENCY**                                | 8-byte, fixed-point number.                                                                                                                                      |
| **DATE**                                    | 64-bit, floating-point fractional number of days since December 30, 1899.                                                                                        |
| **SCODE**                                   | For 16-bit systems - Built-in error type that corresponds to VT\_ERROR.                                                                                          |
| **typedef enum***myenum*                    | Signed integer, whose size is system dependent.                                                                                                                  |
| **IDispatch \***                            | Pointer to the[**IDispatch**](idispatch.md) interface (VT\_DISPATCH).                                                                                           |
| **IUnknown \***                             | Pointer to an interface that does not derive from [**IDispatch**](idispatch.md) (VT\_UNKNOWN). (Any OLE interface can be represented by its IUnknowninterface.) |
| **dispinterface** Typename \*               | Pointer to an interface derived from[**IDispatch**](idispatch.md)(VT\_DISPATCH).                                                                                |
| **coclass** Typename \*                     | Pointer to a coclass name (VT\_UNKNOWN).                                                                                                                         |
| **\[oleautomation\] interface** Typename \* | Pointer to an interface that derives from IUnknown.                                                                                                              |
| **SAFEARRAY**(TypeName)                     | TypeName is any of the above types. Array of these types.                                                                                                        |
| TypeName\*                                  | TypeName is any of the above types. Pointer to a type.                                                                                                           |
| **Decimal**                                 | 96-bit unsigned binary integer scaled by a variable power of 10. A decimal data type that provides a size and scale for a number (as in coordinates).            |



 

A parameter is compatible with Automation if its type is compatible with an Automation type, a pointer to an Automation type, or a SAFEARRAY of an Automation type.

A return type is compatible with Automation if its type is an HRESULT or is void. Methods in Automation must return either HRESULT or void.

A member is compatible with Automation if its return type and all of its parameters are compatible with Automation.

An interface is compatible with Automation if it derives from [**IDispatch**](idispatch.md) or IUnknown, if it has the oleautomation attribute, and if all of its VTBL entries are compatible with Automation. For 32-bit systems, the calling convention for all methods in the interface must be STDCALL. For 16-bit systems, all methods must have the CDECL calling convention. Every dispinterface is compatible with Automation.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




