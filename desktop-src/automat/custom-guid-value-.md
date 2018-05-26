---
title: custom(guid, value)
description: Indicates a custom attribute (one not defined by Automation). This feature enables the independent definition and use of attributes.
ms.assetid: 3d4fadbd-ec22-40e5-96ac-cd0356432cf6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

-   [**ITypeLib2::GetCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypelib2-getcustdata?branch=master)
-   [**ITypeInfo2::GetCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getcustdata?branch=master)
-   [**ITypeInfo2::GetAllCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getallcustdata?branch=master)
-   [**ITypeInfo2::GetFuncCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getfunccustdata?branch=master)
-   [**ITypeInfo2::GetAllFuncCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getallfunccustdata?branch=master)
-   [**ITypeInfo2::GetVarCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getvarcustdata?branch=master)
-   [**ITypeInfo2::GetAllVarCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getallvarcustdata?branch=master)
-   [**ITypeInfo2::GetParamCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getparamcustdata?branch=master)
-   [**ITypeInfo2::GetAllParamCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getallparamcustdata?branch=master)
-   [**ITypeInfo2::GetImplTypeCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getimpltypecustdata?branch=master)
-   [**ITypeInfo2::GetAllImplTypeCustData**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo2-getallimpltypecustdata?branch=master)

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

 

 




