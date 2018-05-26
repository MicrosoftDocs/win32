---
title: Glossary
description: Describes Automation terminology.
ms.assetid: f9000300-20f2-4926-9625-788ad367d526
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Glossary

## 

[A](#a) B [C](#c) [D](#d) [E](#e) F G [H](#h) [I](#i) J K [L](#l) [M](#m) [N](#n) [O](#) [P](#) Q [R](#r) [S](#s) [T](#) [U](#u) [V](#v) W X Y Z

### A

<dl> <dt>

<span id="accessor_function"></span><span id="ACCESSOR_FUNCTION"></span>*accessor function*
</dt> <dd>

A function that sets or retrieves the value of a property. Most properties have a pair of accessor functions. Properties that are read-only may have only one accessor function.

</dd> <dt>

<span id="ActiveX"></span><span id="activex"></span><span id="ACTIVEX"></span>*ActiveX*
</dt> <dd>

Microsofts brand name for the technologies that enable interoperability using the Component Object Model (COM). ActiveX technology includes, but is not limited to, OLE.

</dd> <dt>

<span id="ActiveX_control"></span><span id="activex_control"></span><span id="ACTIVEX_CONTROL"></span>*ActiveX control*
</dt> <dd>

A user interface element created using ActiveX technology.

</dd> <dt>

<span id="Application_object"></span><span id="application_object"></span><span id="APPLICATION_OBJECT"></span>*Application object*
</dt> <dd>

The top-level object in an applications object hierarchy. The Application object identifies the application to the system, and typically becomes active when the application starts. Specified by the **appobj** attribute in the type library.

</dd> <dt>

<span id="Automation"></span><span id="automation"></span><span id="AUTOMATION"></span>*Automation*
</dt> <dd>

COM-based technology that enables binding at run time, or late binding, to an object's methods and properties and also makes possible cross-application macro programming. Formerly referred to as OLE Automation.

</dd> <dt>

<span id="Automation_client"></span><span id="automation_client"></span><span id="AUTOMATION_CLIENT"></span>*Automation client*
</dt> <dd>

An application, programming tool, or scripting language that accesses services provided by Automation objects. Formerly referred to as Automation controller.

</dd> <dt>

<span id="Automation_object"></span><span id="automation_object"></span><span id="AUTOMATION_OBJECT"></span>*Automation object*
</dt> <dd>

An instance of a class defined within an application that is exposed for access by other applications or programming tools by Automation interfaces.

</dd> <dt>

<span id="Automation_server"></span><span id="automation_server"></span><span id="AUTOMATION_SERVER"></span>*Automation server*
</dt> <dd>

An application, type library, or other source that makes Automation objects available for programming by other applications, programming tools, or scripting languages.

</dd> </dl>

[return to top](#)

### C

<dl> <dt>

<span id="class_identifier__CLSID_"></span><span id="class_identifier__clsid_"></span><span id="CLASS_IDENTIFIER__CLSID_"></span>*class identifier (CLSID)*
</dt> <dd>

A universally unique identifier (UUID) for an application class that identifies an object. An object registers its class identifier (CLSID) in the system registration database so that it can be loaded and programmed by other applications.

</dd> <dt>

<span id="class_factory"></span><span id="CLASS_FACTORY"></span>*class factory*
</dt> <dd>

An object that implements the **IClassFactory** interface, which allows it to create other objects of a specific class.

</dd> <dt>

<span id="coclass__component_class_"></span><span id="COCLASS__COMPONENT_CLASS_"></span>*coclass (component class)*
</dt> <dd>

Component object class. A top-level object in the object hierarchy.

</dd> <dt>

<span id="code_page"></span><span id="CODE_PAGE"></span>*code page*
</dt> <dd>

The mapping between character glyphs (shapes) and the 1-byte or 2-byte numeric values that are used to represent them.

</dd> <dt>

<span id="collection_object"></span><span id="COLLECTION_OBJECT"></span>*collection object*
</dt> <dd>

A grouping of exposed objects. A collection object can address multiple occurrences of an object as a unit (for example, to draw a set of points).

</dd> <dt>

<span id="Component_Object_Model__COM_"></span><span id="component_object_model__com_"></span><span id="COMPONENT_OBJECT_MODEL__COM_"></span>*Component Object Model (COM)*
</dt> <dd>

The programming model and binary standard on which OLE is based. COM defines how objects and their clients interact within processes or across process boundaries.

</dd> <dt>

<span id="compound_document"></span><span id="COMPOUND_DOCUMENT"></span>*compound document*
</dt> <dd>

A document that contains data of different formats, such as sound clips, spreadsheets, text, and bitmaps, created by different applications. Compound documents are stored by container applications.

</dd> <dt>

<span id="container_application"></span><span id="CONTAINER_APPLICATION"></span>*container application*
</dt> <dd>

An OLE-based application that provides storage, a display site, and access to a compound document object.

</dd> <dt>

<span id="custom_interface"></span><span id="CUSTOM_INTERFACE"></span>*custom interface*
</dt> <dd>

A user-defined COM interface that is not defined as part of OLE.

</dd> </dl>

[return to top](#)

### D

<dl> <dt>

<span id="Dispatch_identifier__DISPID_"></span><span id="dispatch_identifier__dispid_"></span><span id="DISPATCH_IDENTIFIER__DISPID_"></span>*Dispatch identifier (DISPID)*
</dt> <dd>

The number by which a member function, parameter, or data member of an object is known internally to the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface.

</dd> <dt>

<span id="dispinterface__dispatch_interface_"></span><span id="DISPINTERFACE__DISPATCH_INTERFACE_"></span>*dispinterface (dispatch interface)*
</dt> <dd>

An **IDispatch** interface that responds only to a certain fixed set of names. The properties and methods of the dispinterface are not in the virtual function table (VTBL) for the object.

</dd> <dt>

<span id="dual_interface"></span><span id="DUAL_INTERFACE"></span>*dual interface*
</dt> <dd>

An interface that supports both **IDispatch** and **VTBLbinding**.

</dd> </dl>

[return to top](#)

### E

<dl> <dt>

<span id="event"></span><span id="EVENT"></span>*event*
</dt> <dd>

An action recognized by an object, such as clicking the mouse or pressing a key, and for which you can write code to respond. In Automation, an event is a method that is called, rather than implemented, by an Automation object.

</dd> <dt>

<span id="event_sink"></span><span id="EVENT_SINK"></span>*event sink*
</dt> <dd>

A function that handles events. The code associated with a Visual Basic form, which contains event handlers for one or more controls, is an event sink.

</dd> <dt>

<span id="event_source"></span><span id="EVENT_SOURCE"></span>*event source*
</dt> <dd>

A control that experiences events and calls an event handler to dispose of them.

</dd> <dt>

<span id="exposed_object"></span><span id="EXPOSED_OBJECT"></span>*exposed object*
</dt> <dd>

See Automation object.

</dd> </dl>

[return to top](#)

### H

<dl> <dt>

<span id="HRESULT"></span><span id="hresult"></span>*HRESULT*
</dt> <dd>

A value returned from a function call to an interface, consisting of a severity code, context information, a facility code, and a status code that describes the result. For 16-bit Windows systems, the HRESULT is an opaque result handle defined to be zero for a successful return from a function, and nonzero if error or status information is to be returned. To convert an HRESULT into a more detailed SCODE (or return value), applications call **GetSCode()**. See SCODE.

</dd> </dl>

[return to top](#)

### I

<dl> <dt>

<span id="ID_binding"></span><span id="id_binding"></span><span id="ID_BINDING"></span>*ID binding*
</dt> <dd>

The ability to bind member names to dispatch identifiers (DISPIDs) at compile time (for example, by obtaining the IDs from a type library). This approach eliminates the need for calls to [IDispatch::GetIDsOfNames](6F6CF233-3481-436E-8D6A-51F93BF91619), and results in improved performance over late-bound calls. See also late binding and VTBL binding.

</dd> <dt>

<span id="in-place_activation"></span><span id="IN-PLACE_ACTIVATION"></span>*in-place activation*
</dt> <dd>

The ability to activate an object from within an OLE control and to associate a verb with that activation (for example, edit, play, change). Sometimes referred to as in-place editing or visual editing.

</dd> <dt>

<span id="in-process_server"></span><span id="IN-PROCESS_SERVER"></span>*in-process server*
</dt> <dd>

An object application that runs in the same process space as the Automation controller.

</dd> <dt>

<span id="interfaces"></span><span id="INTERFACES"></span>*interfaces*
</dt> <dd>

One or more well-defined base classes providing member functions that, when implemented in an application, provide a specific service. Interfaces may include compiled support functions to simplify their implementation.

</dd> </dl>

[return to top](#)

### L

<dl> <dt>

<span id="late_binding"></span><span id="LATE_BINDING"></span>*late binding*
</dt> <dd>

The ability to bind member names to dispatch identifiers (IDs) at run time, rather than at compile time. See also ID binding and VTBL binding.

</dd> <dt>

<span id="LCID__locale_identifier_"></span><span id="lcid__locale_identifier_"></span><span id="LCID__LOCALE_IDENTIFIER_"></span>*LCID (locale identifier)*
</dt> <dd>

A 32-bit value that identifies the human language preferred by a user, region, or application.

</dd> <dt>

<span id="locale"></span><span id="LOCALE"></span>*locale*
</dt> <dd>

User-preference information, represented as a list of values describing the user's language and sublanguage.

</dd> </dl>

[return to top](#)

### M

<dl> <dt>

<span id="marshaling"></span><span id="MARSHALING"></span>*marshaling*
</dt> <dd>

The process of packaging and sending interface parameters across process boundaries.

</dd> <dt>

<span id="member_function"></span><span id="MEMBER_FUNCTION"></span>*member function*
</dt> <dd>

One of a group of related functions that make up an interface. See also method and property.

</dd> <dt>

<span id="method"></span><span id="METHOD"></span>*method*
</dt> <dd>

A member function of an exposed object that performs some action on the object, such as saving it to disk.

</dd> <dt>

<span id="MIDL_compiler"></span><span id="midl_compiler"></span><span id="MIDL_COMPILER"></span>*MIDL compiler*
</dt> <dd>

The Microsoft Interface Definition Library (MIDL) compiler can be used to generate a type library. For information about the MIDL compiler, see [Microsoft Interface Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa367091).

</dd> <dt>

<span id="multiple-document_interface__MDI__application"></span><span id="multiple-document_interface__mdi__application"></span><span id="MULTIPLE-DOCUMENT_INTERFACE__MDI__APPLICATION"></span>*multiple-document interface (MDI) application*
</dt> <dd>

An application that can support multiple documents from one application instance. MDI object applications can simultaneously service a user and one or more embedding containers. See also single-document interface (SDI) application.

</dd> </dl>

[return to top](#)

### N

<dl> <dt>

<span id="naming_guidelines"></span><span id="NAMING_GUIDELINES"></span>*naming guidelines*
</dt> <dd>

Recommendations meant to improve consistency and readability across applications.

</dd> </dl>

[return to top](#)

### O

<dl> <dt>

<span id="object"></span><span id="OBJECT"></span>*object*
</dt> <dd>

A unit of information that resides in a compound document and whose behavior is constant no matter where it is located or used.

</dd> <dt>

<span id="Object_Description_Language__ODL_"></span><span id="object_description_language__odl_"></span><span id="OBJECT_DESCRIPTION_LANGUAGE__ODL_"></span>*Object Description Language (ODL)*
</dt> <dd>

A scripting language used to describe exposed libraries, objects, types, and interfaces. ODL scripts are compiled into type libraries by the MIDL compiler.

</dd> <dt>

<span id="OLE"></span><span id="ole"></span>*OLE*
</dt> <dd>

Microsofts object-based technology for sharing information and services across process and machine boundaries (object linking and embedding).

</dd> <dt>

<span id="out-of_process_server"></span><span id="OUT-OF_PROCESS_SERVER"></span>*out-of process server*
</dt> <dd>

An object application implemented in an executable file that runs in a separate process space from the Automation controller.

</dd> </dl>

[return to top](#)

### P

<dl> <dt>

<span id="programmable_object"></span><span id="PROGRAMMABLE_OBJECT"></span>*programmable object*
</dt> <dd>

See Automation object.

</dd> <dt>

<span id="programmatic_identifier__ProgID_"></span><span id="programmatic_identifier__progid_"></span><span id="PROGRAMMATIC_IDENTIFIER__PROGID_"></span>*programmatic identifier (ProgID)*
</dt> <dd>

An applications unique name that is mapped to the system registry by the class identifier (CLSID). For example, registering Microsoft Excel associates a CLSID with the ProgID Excel.Application.

</dd> <dt>

<span id="property"></span><span id="PROPERTY"></span>*property*
</dt> <dd>

A data member of an exposed object. Properties are set or returned by means of get and put assessor functions.

</dd> <dt>

<span id="proxy"></span><span id="PROXY"></span>*proxy*
</dt> <dd>

An interface-specific object that packages parameters for that interface in preparation for a remote method call. A proxy runs in the address space of the sender and communicates with a corresponding stub in the receivers address space. See also stub, marshaling, and unmarshaling.

</dd> </dl>

[return to top](#)

### R

<dl> <dt>

<span id="running_object_table__ROT_"></span><span id="running_object_table__rot_"></span><span id="RUNNING_OBJECT_TABLE__ROT_"></span>*running object table (ROT)*
</dt> <dd>

A globally accessible table on each computer that keeps track of all COM objects in the running state that can be identified by a moniker. Moniker providers register an object in the table, which increments the object's reference count. Before the object can be destroyed, its moniker must be released from the table.

</dd> </dl>

[return to top](#)

### S

<dl> <dt>

<span id="safe_array"></span><span id="SAFE_ARRAY"></span>*safe array*
</dt> <dd>

An array that contains information about the number of dimensions and the bounds of its dimensions. Safe arrays are passed by [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) within VARIANTARGs. Their base type is VT\_tag \| VT\_ARRAY.

</dd> <dt>

<span id="SCODE"></span><span id="scode"></span>*SCODE*
</dt> <dd>

A DWORD value that is used in 16-bit systems to pass detailed information to the caller of an interface member or API function. The status codes for OLE interfaces and APIs are defined in FACILITY\_ITF. See HRESULT.

</dd> <dt>

<span id="single-document_interface__SDI__application"></span><span id="single-document_interface__sdi__application"></span><span id="SINGLE-DOCUMENT_INTERFACE__SDI__APPLICATION"></span>*single-document interface (SDI) application*
</dt> <dd>

An application that can support only one document at a time. Multiple instances of an SDI application must be started to service both an embedded object and a user. See also multiple-document interface (MDI) application.

</dd> <dt>

<span id="standard_objects"></span><span id="STANDARD_OBJECTS"></span>*standard objects*
</dt> <dd>

A set of objects defined by Automation, including the following: **Application**, **Document**, **Documents**, and **Font**.

</dd> <dt>

<span id="stub"></span><span id="STUB"></span>*stub*
</dt> <dd>

An interface-specific object that unpackages the parameters for that interface after they are marshaled across the process boundary, and makes the requested method call. The stub runs in the address space of the receiver and communicates with a corresponding proxy in the senders address space. See proxy, marshaling, and unmarshaling.

</dd> </dl>

[return to top](#)

### T

<dl> <dt>

<span id="type_description"></span><span id="TYPE_DESCRIPTION"></span>*type description*
</dt> <dd>

The information used to build the type information for one or more aspects of an applications interface. Type descriptions are written in Object Description Language (ODL), and include both programmable and nonprogrammable interfaces.

</dd> <dt>

<span id="type_information"></span><span id="TYPE_INFORMATION"></span>*type information*
</dt> <dd>

Information that describes the interfaces of an application. Type information is created from type descriptions using OLE Automation tools, such as the MIDL compiler or the [**CreateDispTypeInfo**](603E00E8-0370-4EBF-B9D2-85E6E58C2B3A) function. Type information can be accessed through the [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master) interface.

</dd> <dt>

<span id="type_information_element"></span><span id="TYPE_INFORMATION_ELEMENT"></span>*type information element*
</dt> <dd>

A unit of information identified by one of these statements in a type description: **typedef**, **enum**, **struct**, **module**, **interface**, **dispinterface**, or **coclass**.

</dd> <dt>

<span id="type_library"></span><span id="TYPE_LIBRARY"></span>*type library*
</dt> <dd>

A file or component within another file that contains type information about exposed objects. Type libraries are created using the MIDL compiler, and can be accessed through the [**ITypeLib**](/windows/previous-versions/oaidl/nn-oaidl-itypelib?branch=master) interface.

</dd> </dl>

[return to top](#)

### U

<dl> <dt>

<span id="unmarshaling"></span><span id="UNMARSHALING"></span>*unmarshaling*
</dt> <dd>

The process of unpackaging parameters that have been sent across process boundaries.

</dd> </dl>

[return to top](#)

### V

<dl> <dt>

<span id="Value_property"></span><span id="value_property"></span><span id="VALUE_PROPERTY"></span>*Value property*
</dt> <dd>

The property that defines the default behavior of an object when no other methods or properties are specified. Indicate the Value property by specifying the [default](50501057-73E9-40CF-BE7C-411F78E3B084) attribute in ODL.

</dd> <dt>

<span id="virtual_function_table__VTBL_"></span><span id="virtual_function_table__vtbl_"></span><span id="VIRTUAL_FUNCTION_TABLE__VTBL_"></span>*virtual function table (VTBL)*
</dt> <dd>

A table of function pointers, such as an implementation of a class in C++. The pointers in the VTBL point to the members of the interfaces that an object supports.

</dd> <dt>

<span id="VTBL_binding"></span><span id="vtbl_binding"></span><span id="VTBL_BINDING"></span>*VTBL binding*
</dt> <dd>

A process that allows an ActiveX client to call a method or property accessor function directly without using the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface. VTBL binding is faster than both *ID binding* and *latebinding* because the access is direct. See also late binding and ID binding.

</dd> </dl>

[return to top](#)

 

 




