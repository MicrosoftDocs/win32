---
title: Creating a Type Library
description: Demonstrates how to create a type library.
ms.assetid: 'e564328b-0ef1-4db0-9c44-48eb2d9382bf'
---

# Creating a Type Library

Most ActiveX components create *type libraries*. Type libraries contain type information, Help file names and contexts, and function-specific documentation strings. Access to this information is available at both compile time and run time.

*Type information* is the Automation standard for describing the objects, properties, and methods exposed by the ActiveX component. Browsers and compilers use the type information to display and access the exposed objects.

Type libraries are described in [ODL](glossary.md) and are compiled by the MIDL compiler.

**To create a type library**

1.  Write an object description script for the objects you expose. An object description script is essentially an annotated header file written in ODL.

2.  Using the MIDL compiler, build the type library (.tlb) file and class description header (.h) file from the object description script.

## Object Description Script Example


```C++
/* TDATA.ODL */
AppName library{
   dispinterface ObjeNamePro {
      interface ObjName
      }
}
```



Automation also supports the creation of alternative tools that compile and access type information. For information about creating these tools, refer to [Type Description Interfaces](387D44B7-407B-44A9-9239-A4CB20E88CAC).

A type library stores complete type information for all of an application's exposed objects. It may be included as a resource in a DLL or executable file, or remain as a stand-alone file (.tlb).

## MIDL Library Statement Example


```C++
[  
    uuid(F37C8060-4AD5-101B-B826-00DD01103DE1),    // LIBID_Hello 
    helpstring("Hello 2.0 Type Library"), 
    lcid(0x0409), 
    version(2.0) 
] 
library Hello 
{ 
    importlib("stdole.tlb"); 
    [ 
        uuid(F37C8062-4AD5-101B-B826-00DD01103DE1),    // IID_IHello 
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



 

 




