---
title: library
description: This statement describes a type library. This description contains all of the information in a MIDL input file (ODL).
ms.assetid: 089eb146-9f24-4b15-a768-1706614667a9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# library

This statement describes a type library. This description contains all of the information in a MIDL input file (ODL).

## Syntax

``` syntax
[attributes] library libname {
   definitions
};
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The helpstring, helpcontext, lcid, restricted, hidden, control, uuid and version attributes are accepted before a library statement. The uuid attribute is required.

</dd> <dt>

<span id="libname"></span><span id="LIBNAME"></span>*libname*
</dt> <dd>

The name by which the type library is known.

</dd> <dt>

<span id="definitions"></span><span id="DEFINITIONS"></span>*definitions*
</dt> <dd>

Descriptions of any imported libraries, data types, modules, interfaces, dispinterfaces, and coclasses relevant to the object being exposed.

</dd> </dl>

## Remarks

The library statement must precede any other type definitions.

## Example


```C++
[
   uuid(F37C8060-4AD5-101B-B826-00DD01103DE1), // LIBID_Hello.
   helpstring("Hello 2.0 Type Library"),
   lcid(0x0409),
   version(2.0)
]
library Hello
{
   importlib("stdole.tlb"); 
   [
      uuid(F37C8062-4AD5-101B-B826-00DD01103DE1),   // IID_Ihello.
      helpstring("Application object for the Hello application."),
      oleautomation,
      dual
   ]
   interface IHello : IDispatch
   {
      [propget, helpstring("Returns the application of the object.")]
      HRESULT Application([in, lcid] long localeID, 
         [out, retval] IHello** retval)
   }
}
```



 

 




