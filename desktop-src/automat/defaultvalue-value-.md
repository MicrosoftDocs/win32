---
title: defaultvalue(value)
description: Enables specification of a default value for a typed optional parameter.
ms.assetid: 445a0572-9f08-43d8-b392-e2d5ad6eb785
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# defaultvalue(value)

Enables specification of a default value for a typed optional parameter.

## Parameters

<dl> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

The default value.

</dd> </dl>

## Allowed on

Parameter.

## Remarks

The expression *value* resolves to a constant that can be described in a variant. The ODL already allows some expression forms, as when a constant is declared in a module. The same expressions are supported without modification.

The following example shows some legal parameter descriptions:


```C++
interface IFoo
{
   void Ex1([defaultvalue(44)] LONG    i);
   void Ex2([defaultvalue(44)] SHORT    i);
   void Ex3([defaultvalue("Hello")] BSTR    i);
}
```



The following rules apply:

1.  It is invalid to specify a default value for a parameter whose type is a safe array. It is invalid to specify a default value for any type that cannot go in a variant, including structures and arrays.

2.  Parameters can be mixed. Optional parameters and default value parameters must follow mandatory parameters.

3.  The default value can be any constant that is represented by a VARIANT data type.

## Example


```C++
interface QueryDef
{

// Type is now known to be a LONG type (good for browser in VBA and
// for a C/C++ programmer) and also has a default value of
// dbOpenTable (constant).

HRESULT   OpenRecordset(   [in, defaultvalue(dbOpenTable)]
                           LONG Type,
                           [out,retval] 
                           Recordset **pprst);}
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




