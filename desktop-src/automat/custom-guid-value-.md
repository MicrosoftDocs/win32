---
title: custom(guid, value)
description: Indicates a custom attribute (one not defined by Automation). This feature enables the independent definition and use of attributes.
ms.assetid: '3d4fadbd-ec22-40e5-96ac-cd0356432cf6'
---

# custom(guid, value)

Indicates a custom attribute (one not defined by Automation). This feature enables the independent definition and use of attributes.

## Parameters

<dl> <dt>

<span id="guid"></span><span id="GUID"></span>*guid*
</dt> <dd>

The standard GUID form.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

A value that can be put into a variant. See also the Const directive.

</dd> </dl>

## Allowed on

Library, typeinfo, typlib, variable, function, parameter.

## Not allowed on

A member of a coclass (IMPLTYPE).

## Representation

Can be retrieved using:

-   [**ITypeLib2::GetCustData**](itypelib2-getcustdata.md)
-   [**ITypeInfo2::GetCustData**](itypeinfo2-getcustdata.md)
-   [**ITypeInfo2::GetAllCustData**](itypeinfo2-getallcustdata.md)
-   [**ITypeInfo2::GetFuncCustData**](itypeinfo2-getfunccustdata.md)
-   [**ITypeInfo2::GetAllFuncCustData**](itypeinfo2-getallfunccustdata.md)
-   [**ITypeInfo2::GetVarCustData**](itypeinfo2-getvarcustdata.md)
-   [**ITypeInfo2::GetAllVarCustData**](itypeinfo2-getallvarcustdata.md)
-   [**ITypeInfo2::GetParamCustData**](itypeinfo2-getparamcustdata.md)
-   [**ITypeInfo2::GetAllParamCustData**](itypeinfo2-getallparamcustdata.md)
-   [**ITypeInfo2::GetImplTypeCustData**](itypeinfo2-getimpltypecustdata.md)
-   [**ITypeInfo2::GetAllImplTypeCustData**](itypeinfo2-getallimpltypecustdata.md)

## Flags

None.

## Example

The following example shows how to add a string-valued attribute that gives the ProgID for a class:


```C++
[
   custom(GUID_PROGID, "DAO.Dynaset")
]
coclass Dynaset
{
   [default] interface Dynaset;
   [default, source] interface IDynasetEvents;
}
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




