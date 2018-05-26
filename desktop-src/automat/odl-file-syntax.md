---
title: ODL File Syntax
description: The general syntax for an .ODL file is as follows
ms.assetid: df7aa86f-1453-4409-939e-788d469d611e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ODL File Syntax

The general syntax for an .ODL file is as follows:


```C++
[attributes] library libname {definitions};
```



The attributes associate characteristics with the library, such as its Help file and universally unique identifier (UUID). Attributes must be enclosed in square brackets.

The definitions consist of the descriptions of the imported libraries, data types, modules, interfaces, dispinterfaces, and coclasses that are part of the type library. Braces ({}) must surround the definitions.

The following table summarizes the elements that can appear in definitions. Each element is described in more detail in the section [ODL Reference](odl-reference.md).



| Purpose                                                                  | Library element                                              | Description                                                                                                                                                                                   |
|--------------------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allows references to other type libraries.<br/>                    | [importlib](importlib.md) (lib1)<br/>                 | Specifies an external type library that contains definitions that are referenced in this type library.<br/>                                                                             |
| Declares data types used by the objects in this type library.<br/> | [typedef](typedef.md)\[attributes\]aliasname<br/>     | An alias declared using C syntax. Must have at least one attribute to be included in the type library.<br/>                                                                             |
|                                                                          | typedef \[attributes\] [enum](enum.md)<br/>           | An enumeration declared using the C keywordstypedef and enum.<br/>                                                                                                                      |
|                                                                          | typedef \[attributes\] [struct](struct.md)<br/>       | A structure declared using the C keywordstypedefand struct.<br/>                                                                                                                        |
|                                                                          | typedef \[attributes\] [union](union.md)<br/>         | A union declared using the C keywordstypedefand union.<br/>                                                                                                                             |
| Describes functions that enable querying the DLL.<br/>             | \[attributes\] [module](module.md)<br/>               | Constants and general data functions whose actions are not restricted to any specified class of objects.<br/>                                                                           |
| Describes interfaces.<br/>                                         | \[attributes\] [dispinterface](dispinterface.md)<br/> | An interface describing the methods and properties for an object that must be accessed through [**IDispatch::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master).<br/>                                      |
|                                                                          | \[attributes\] [interface](interface.md)<br/>         | An interface describing the methods and properties for an object that can be accessed through VTBL entries or possibly also through [**IDispatch::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master).<br/> |
| Describes OLE classes.<br/>                                        | \[attributes\] [coclass](coclass.md)<br/>             | Specifies a top-level object with all of its interfaces and dispinterfaces.<br/>                                                                                                        |



 

In the library description, modules, interfaces, dispinterfaces, and coclasses follow the same general syntax:


```C++
[attributes] elementname typename {
   memberdescriptions
};
```



The attributesset characteristics for the element. The elementname is a keyword that indicates the kind of item (module, interface, dispinterface, or coclass), and the typenamedefines the name of the item. The memberdescriptions define the members (constants, functions, properties, and methods) of each element.

Aliases, enumerations, unions, and structures have the following syntax:


```C++
typedef [typeattributes] typekind typename {
   memberdescriptions
};
```



## Remarks

For these types, the attributes follow the typedefkeyword, and the typekind indicates the data type (enum, union, or struct). For details, see [Attribute Descriptions](attribute-descriptions.md).

> [!Note]  
> The square brackets (\[ \]) and braces ({ }) in these descriptions are part of the syntax, and are not descriptive symbols. The semicolon after the closing brace (}) that terminates the library definition (and all other type definitions) is optional.

 

## Related topics

<dl> <dt>

[Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md)
</dt> </dl>

 

 





