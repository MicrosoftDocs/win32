---
description: Windows Management Instrumentation (WMI) defines a set of system properties that are associated with all classes and instances of classes.
ms.assetid: e812c0cb-3e08-4cac-8d05-2cd7abc922d1
ms.tgt_platform: multiple
title: WMI System Properties
ms.topic: article
ms.date: 05/31/2018
---

# WMI System Properties

Windows Management Instrumentation (WMI) defines a set of system properties that are associated with all classes and instances of classes. As with system classes, system property names begin with a double underscore, distinguishing them from properties created by applications or providers that must not start with a single or double underscore. Another way to identify a system property is to use the [**IWbemClassObject::Get**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-get) method.

System properties are available at any time, but values might be **NULL**. **NULL** indicates a property does not apply to a specific object. However, system properties might not be available all the time for all classes or instances.

## System Properties

The following list describes the WMI system properties. The examples given are taken from the system properties of the [**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature) class, which is described at the bottom of this topic.

<dl> <dt>

<span id="__Class"></span><span id="__class"></span><span id="__CLASS"></span>**\_\_Class**
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only for instances; read/write for classes

The name of the class.

Example: Win32\_OptionalFeature

</dd> <dt>

<span id="__Derivation"></span><span id="__derivation"></span><span id="__DERIVATION"></span>**\_\_Derivation**
</dt> <dd>

Data type: **CIM\_STRING** array

Access type: Read-only for both instances and classes

Class hierarchy of the current class or instance. The first element is the immediate parent class, the next is its parent, and so on; the last element is the base class.

Example: {CIM\_LogicalElement, CIM\_ManagedSystemElement}

</dd> <dt>

<span id="__Dynasty"></span><span id="__dynasty"></span><span id="__DYNASTY"></span>**\_\_Dynasty**
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only

Name of the top-level class from which the class or instance is derived. When this class or instance is the top-level class, the values of **\_\_Dynasty** and **\_\_Class** are the same.

Example: CIM\_ManagedSystemElement

</dd> <dt>

<span id="__Genus"></span><span id="__genus"></span><span id="__GENUS"></span>**\_\_Genus**
</dt> <dd>

Data type: **CIM\_SINT32**

Access type: Read-only

Value that is used to distinguish between classes and instances. This value is **WBEM\_GENUS\_CLASS** (1) for classes, and **WBEM\_GENUS\_INSTANCE** (2) for instances and events.

Example: 2

</dd> <dt>

<span id="__Namespace"></span><span id="__namespace"></span><span id="__NAMESPACE"></span>[**\_\_Namespace**](--namespace.md)
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only

Name of the [*namespace*](gloss-n.md) of the class or instance.

Example: root\\cimv2

</dd> <dt>

<span id="__Path"></span><span id="__path"></span><span id="__PATH"></span>**\_\_Path**
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only

Full path to the class or instance—including server and namespace.

Example: \\\\MyServer\\root\\cimv2:Win32\_OptionalFeature.Name="TelnetClient"

</dd> <dt>

<span id="__Property_Count"></span><span id="__property_count"></span><span id="__PROPERTY_COUNT"></span>**\_\_Property\_Count**
</dt> <dd>

Data type: **CIM\_SINT32**

Access type: Read-only

Number of nonsystem properties defined for the class or instance.

Example: 6

</dd> <dt>

<span id="__Relpath"></span><span id="__relpath"></span><span id="__RELPATH"></span>**\_\_Relpath**
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only

Relative path to the class or instance.

Example: Win32\_OptionalFeature.Name="TelnetClient"

</dd> <dt>

<span id="__Server"></span><span id="__server"></span><span id="__SERVER"></span>**\_\_Server**
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only

Name of the server supplying the class or instance.

Example: MyServer

</dd> <dt>

<span id="__Superclass"></span><span id="__superclass"></span><span id="__SUPERCLASS"></span>**\_\_Superclass**
</dt> <dd>

Data type: **CIM\_STRING**

Access type: Read-only

Name of the immediate parent class of the class or instance.

Example: CIM\_LogicalElement

</dd> </dl>

The following PowerShell code retrieves the properties of the [**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature) class, which includes the system properties.


```PowerShell
Get-WmiObject win32_OptionalFeature | Where-Object {$_.name -eq "TelnetClient"}
```



The previous code sample returns the following:


```PowerShell
__GENUS          : 2
__CLASS          : Win32_OptionalFeature
__SUPERCLASS     : CIM_LogicalElement
__DYNASTY        : CIM_ManagedSystemElement
__RELPATH        : Win32_OptionalFeature.Name="TelnetClient"
__PROPERTY_COUNT : 6
__DERIVATION     : {CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER         : myServer
__NAMESPACE      : root\cimv2
__PATH           : \\myServer\root\cimv2:Win32_OptionalFeature.Name="TelnetClient"
Caption          : Telnet Client
Description      : 
InstallDate      : 
InstallState     : 2
Name             : TelnetClient
Status           : 
PSComputerName   : myServer
```



 

 
