---
title: Using Type Building Interfaces and Functions
description: The type building interfaces are used to build tools that automate the process of generating type descriptions and creating type libraries.
ms.assetid: 'aad137b1-b747-4d74-8d6c-5ec9b6e6983d'
---

# Using Type Building Interfaces and Functions

The type building interfaces are used to build tools that automate the process of generating type descriptions and creating type libraries. For example, the Microsoft Interface Definition Language (MIDL) compiler uses these interfaces to create type libraries.

The following interfaces and functions are used to create an Automation type library.



| Interface                                      | Description                                                                                                  |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ICreateTypeInfo**](icreatetypeinfo.md)     | Provides the tools for creating and administering the type information defined through the type description. |
| [**ICreateTypeInfo2**](icreatetypeinfo2.md)   | Adds methods for deleting items that have been added through [**ICreateTypeInfo**](icreatetypeinfo.md).     |
| [**ICreateTypeLib**](icreatetypelib.md)       | Provides the methods for creating and managing the component or file that contains type information.         |
| [CreateTypeLib API](createtypelib.md)         | Provides access to a new object instance that supports the **ICreateTypeLib** interface.                     |
| [**ICreateTypeLib2**](icreatetypelib2.md)     | Supports the creation and administration of type libraries and type descriptions.                            |
| [CreateTypeLib2 API](createtypelib2.md)       | Creates a type library in the current file format.                                                           |
| [**ITypeChangeEvents**](itypechangeevents.md) | Raises functions when change is requested on a type and after the change has been made.                      |



 

Generally, it is not necessary to write custom implementations of these interfaces. The compilers use the default implementations that are returned by the [**CreateTypeLib**](createtypelib.md) function. To create tools similar to MkTypLib, the default implementations can be called.

## Example

You create an Automation type library by using the [**ICreateTypeLib**](icreatetypelib.md) and [**ICreateTypeInfo**](icreatetypeinfo.md) interfaces.

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

 

 




