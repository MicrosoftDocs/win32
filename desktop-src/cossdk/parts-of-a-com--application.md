---
description: COM+ applications consist of one or more COM components.
ms.assetid: e7ed2844-276e-4726-952d-e4d3be2eb6e8
title: Parts of a COM+ Application
ms.topic: article
ms.date: 05/31/2018
---

# Parts of a COM+ Application

COM+ applications consist of one or more COM components.

The following terms are used throughout the COM+ documentation:

<dl> <dt>

<span id="COM_component"></span><span id="com_component"></span><span id="COM_COMPONENT"></span>*COM component*
</dt> <dd>

A binary unit of code that creates COM objects (includes packaging and registration code).

</dd> <dt>

<span id="COM_object"></span><span id="com_object"></span><span id="COM_OBJECT"></span>*COM object*
</dt> <dd>

An instance of a COM class.

</dd> <dt>

<span id="COM_class"></span><span id="com_class"></span><span id="COM_CLASS"></span>*COM class*
</dt> <dd>

A named, concrete implementation of one or more interfaces. A COM class is identified by a CLSID (sometimes by a ProgID also).

</dd> <dt>

<span id="COM_interface"></span><span id="com_interface"></span><span id="COM_INTERFACE"></span>*COM interface*
</dt> <dd>

A group of related method functions exposed by a COM class that specify a contract. This includes the name, interface signature, interface semantics, and marshaling buffer format. An interface is identified by an IID. The interface syntax is defined in IDL and/or type libraries. The interfaces of a COM class should be divided into manageable, cohesive sets of methods.

COM interfaces are immutable; the COM contract states that they cannot be modified. Any modification (such as adding methods) requires defining a new interface.

</dd> <dt>

<span id="COM_method"></span><span id="com_method"></span><span id="COM_METHOD"></span>*COM method*
</dt> <dd>

One of a set of related functions provided by a COM interface.

</dd> </dl>

## Configured and Unconfigured Components

To take advantage of the services that COM+ applications support, the COM+ environment imposes specific requirements on COM components built for COM+ applications. When added to a COM+ application, a COM component is known as a *configured component*.

COM components built for COM+ applications are in-process server components. The component must contain a type library (.tlb file) to describe all classes implemented in the component and declare the interfaces on all classes in the component. You can create and implement these components with Microsoft Visual Basic, Microsoft Visual C++, or any COM-compatible development tool.

An *unconfigured component* is a component that isn't installed in a COM+ application. You can transform most unconfigured components into configured components simply by integrating them into a COM+ application.

> [!Note]  
> Do not use the same AppID for both a COM+ application and in the registry for an unconfigured component. When the unconfigured component is activated , as activation may retrieve the COM+ application information from the registry that does not contain the information required for COM activation. Similar problems could arise if a call is made to [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) from DllHost that hosts COM+ Server application.

 

 

 
