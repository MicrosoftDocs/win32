---
Description: The Win32\_PortResource WMI class represents an I/O port on a computer system running Windows.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 820f4f49-571c-4044-aefc-69bac5d59e6f
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_PortResource class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PortResource class

The **Win32\_PortResource** [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) represents an I/O port on a computer system running Windows.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4D0-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_PortResource : Win32_SystemMemoryResource
{
  boolean  Alias;
  string   Caption;
  string   CreationClassName;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  uint64   EndingAddress;
  datetime InstallDate;
  string   Name;
  uint64   StartingAddress;
  string   Status;
};
```

## Members

The **Win32\_PortResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PortResource** class has these properties.

<dl> <dt>

**Alias**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|Configuration Manager Structures\|IO\_INFO")
</dt> </dl>

If **TRUE**, this instance represents one of the ranges with an alias. If **FALSE**, the instance represents a base port address. A base port address is a predetermined port address dedicated to a specific service or device. A port alias address is one that a device responds to as if it were the actual address of an I/O port.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (64), [**DisplayName**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Caption")
</dt> </dl>

Short description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256), [**CIM\_Key**](https://msdn.microsoft.com/63bdbafc-51f3-4714-8b7e-9d5a61cef45e)
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, the property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_MemoryMappedIO**](cim-memorymappedio.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**CreationClassName**"), [**CIM\_Key**](https://msdn.microsoft.com/63bdbafc-51f3-4714-8b7e-9d5a61cef45e), [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256)
</dt> </dl>

Creation class name of the scoping computer system.

This property is inherited from [**CIM\_MemoryMappedIO**](cim-memorymappedio.md).

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256), [**CIM\_Key**](https://msdn.microsoft.com/63bdbafc-51f3-4714-8b7e-9d5a61cef45e)
</dt> </dl>

Name of the scoping computer system.

This property is inherited from [**CIM\_MemoryMappedIO**](cim-memorymappedio.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Description")
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("MIF.DMTF\|Memory Mapped I/O\|001.2")
</dt> </dl>

Ending address of memory mapped I/O.

This property is inherited from [**CIM\_MemoryMappedIO**](cim-memorymappedio.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, the property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("StartingAddress"), [**Key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("MIF.DMTF\|Memory Mapped I/O\|001.1")
</dt> </dl>

Starting address of memory mapped I/O. The hardware resource identifier property should be set to this value to construct the mapped I/O resource key.

This property is inherited from [**CIM\_MemoryMappedIO**](cim-memorymappedio.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (10), [**DisplayName**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_PortResource** class is derived from [**Win32\_SystemMemoryResource**](win32-systemmemoryresource.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SystemMemoryResource**](win32-systemmemoryresource.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




