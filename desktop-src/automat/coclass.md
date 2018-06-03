---
title: coclass macro
description: This statement describes the globally unique ID (GUID) and the supported interfaces for a Component Object Model (COM).
ms.assetid: 333d0904-ffa2-4d25-878d-7422bcd40582
keywords:
- coclass macro Automation
topic_type:
- apiref
api_name:
- coclass
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# coclass macro

This statement describes the globally unique ID (GUID) and the supported interfaces for a Component Object Model (COM).

## Syntax


```C++
 coclass(
    attributes,
    classname,
    attributes2,
    interfacename
);
```



## Parameters

<dl> <dt>

**attributes** 
</dt> <dd>

The uuid attribute is required on a coclass. This is the same uuid that is registered as a CLSID in the system registration database. The helpstring,helpcontext, version, licensed, version, control, hidden, and appobject attributes are accepted, but not required, before a coclass definition. The appobject attribute makes the functions and properties of the coclass globally available in the type library.

</dd> <dt>

**classname** 
</dt> <dd>

The name by which the common object is known in the type library.

</dd> <dt>

**attributes2** 
</dt> <dd>

Optional attributes for the interface or dispinterface. The source, default, and restricted attributes are accepted on an interface or dispinterface in a coclass.

</dd> <dt>

**interfacename** 
</dt> <dd>

Either an interface declared with the interface keyword, or a dispinterface declared with the dispinterface keyword.

</dd> </dl>

## Remarks

``` syntax
[attributes]
coclass classname {
   [attributes2] [interface | dispinterface] interfacename;
};
```

The Component Object Model defines a class as an implementation that allows **QueryInterface** between a set of interfaces.

### Example


```C++
[ uuid(BFB73347-822A-1068-8849-00DD011087E8), version(1.0), helpstring("A class"), helpcontext(2481), appobject]
coclass myapp {
   [source] interface IMydocFuncs;
   dispinterface DMydocFuncs;
};

[uuid 00000000-0000-0000-0000-123456789019] 
coclass test
{
   [restricted] interface ITest;
   interface ITest;
}
```



 

 




