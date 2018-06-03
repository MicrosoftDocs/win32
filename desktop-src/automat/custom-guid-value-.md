---
title: custom(guid, value)
description: Indicates a custom attribute (one not defined by Automation). This feature enables the independent definition and use of attributes.
ms.assetid: 3d4fadbd-ec22-40e5-96ac-cd0356432cf6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

-   [**ITypeLib2::GetCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypelib2-getcustdata)
-   [**ITypeInfo2::GetCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getcustdata)
-   [**ITypeInfo2::GetAllCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getallcustdata)
-   [**ITypeInfo2::GetFuncCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getfunccustdata)
-   [**ITypeInfo2::GetAllFuncCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getallfunccustdata)
-   [**ITypeInfo2::GetVarCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getvarcustdata)
-   [**ITypeInfo2::GetAllVarCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getallvarcustdata)
-   [**ITypeInfo2::GetParamCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getparamcustdata)
-   [**ITypeInfo2::GetAllParamCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getallparamcustdata)
-   [**ITypeInfo2::GetImplTypeCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getimpltypecustdata)
-   [**ITypeInfo2::GetAllImplTypeCustData**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo2-getallimpltypecustdata)

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

 

 




