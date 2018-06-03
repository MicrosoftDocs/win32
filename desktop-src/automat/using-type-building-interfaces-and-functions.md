---
title: Using Type Building Interfaces and Functions
description: The type building interfaces are used to build tools that automate the process of generating type descriptions and creating type libraries.
ms.assetid: aad137b1-b747-4d74-8d6c-5ec9b6e6983d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Type Building Interfaces and Functions

The type building interfaces are used to build tools that automate the process of generating type descriptions and creating type libraries. For example, the Microsoft Interface Definition Language (MIDL) compiler uses these interfaces to create type libraries.

The following interfaces and functions are used to create an Automation type library.



| Interface                                      | Description                                                                                                  |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ICreateTypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypeinfo)     | Provides the tools for creating and administering the type information defined through the type description. |
| [**ICreateTypeInfo2**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypeinfo2)   | Adds methods for deleting items that have been added through [**ICreateTypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypeinfo).     |
| [**ICreateTypeLib**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypelib)       | Provides the methods for creating and managing the component or file that contains type information.         |
| [CreateTypeLib API](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createtypelib)         | Provides access to a new object instance that supports the **ICreateTypeLib** interface.                     |
| [**ICreateTypeLib2**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypelib2)     | Supports the creation and administration of type libraries and type descriptions.                            |
| [CreateTypeLib2 API](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createtypelib2)       | Creates a type library in the current file format.                                                           |
| [**ITypeChangeEvents**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypechangeevents) | Raises functions when change is requested on a type and after the change has been made.                      |



 

Generally, it is not necessary to write custom implementations of these interfaces. The compilers use the default implementations that are returned by the [**CreateTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createtypelib) function. To create tools similar to MkTypLib, the default implementations can be called.

## Example

You create an Automation type library by using the [**ICreateTypeLib**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypelib) and [**ICreateTypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreatetypeinfo) interfaces.

In the following example, a type library is created (Hello.tlb) by the MIDL compiler, using the following .odl file.


```C++
 [
uuid(2F6CA420-C641-101A-B826-00DD01103DE1),            // LIBID_Hello
helpstring("Hello 1.0 Type Library"),
lcid(0x0409),
version(1.0)
] 
library Hello
{
#ifdef WIN32
importlib("stdole32.tlb");
#else
importlib("stdole.tlb");
#endif

[
uuid(2F6CA422-C641-101A-B826-00DD01103DE1),        // IID_IHello
helpstring("Hello Interface")
]
interface IHello : IUnknown
{
[propput] void HelloMessage([in] BSTR Message);
[propget] BSTR HelloMessage(void);
void SayHello(void);
}
[
uuid(2F6CA423-C641-101A-B826-00DD01103DE1),        // IID_DHello
helpstring("Hello Dispinterface")
] 
dispinterface DHello
{
interface IHello;
}

[
uuid(2F6CA421-C641-101A-B826-00DD01103DE1),       // CLSID_Hello.
helpstring("Hello Class")
]
coclass Hello
{
dispinterface DHello;
interface IHello;
}
}
```



## Related topics

<dl> <dt>

[Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md)
</dt> </dl>

 

 




