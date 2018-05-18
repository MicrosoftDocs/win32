---
title: Win32\_CommandLineAccess class
description: The Win32\_CommandLineAccess WMI class represents the command line interface to a service or application.
ms.assetid: '788788a9-78d5-468e-8c89-80d6df63b096'
keywords: ["Win32_CommandLineAccess class", "Win32_CommandLineAccess class, described"]
topic_type:
- apiref
api_name:
- Win32_CommandLineAccess
- Win32_CommandLineAccess.Caption
- Win32_CommandLineAccess.CommandLine
- Win32_CommandLineAccess.CreationClassName
- Win32_CommandLineAccess.Description
- Win32_CommandLineAccess.InstallDate
- Win32_CommandLineAccess.Name
- Win32_CommandLineAccess.Status
- Win32_CommandLineAccess.SystemCreationClassName
- Win32_CommandLineAccess.SystemName
- Win32_CommandLineAccess.Type
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_CommandLineAccess class

The **Win32\_CommandLineAccess** [WMI class](https://msdn.microsoft.com/library/aa393244) represents the command line interface to a service or application. The name of the access point is always the full command line text.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_CommandLineAccess : CIM_ServiceAccessPoint
{
  string   Caption;
  string   CommandLine;
  string   CreationClassName;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   Type;
};
```

## Members

The **Win32\_CommandLineAccess** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_CommandLineAccess** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object—a one-line string.

</dd> <dt>

**CommandLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String used to start the service.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier of the service access point and an indication of the functionality that is managed. This functionality is described in more detail in the object's **Description** property.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

Values are the following:

<dl><span id="_OK_"></span><span id="_ok_"></span><dt>

**"OK"**
</dt><span id="_Error_"></span><span id="_error_"></span><span id="_ERROR_"></span><dt>

**"Error"**
</dt><span id="_Degraded_"></span><span id="_degraded_"></span><span id="_DEGRADED_"></span><dt>

**"Degraded"**
</dt><span id="_Unknown_"></span><span id="_unknown_"></span><span id="_UNKNOWN_"></span><dt>

**"Unknown"**
</dt><span id="_Pred_Fail_"></span><span id="_pred_fail_"></span><span id="_PRED_FAIL_"></span><dt>

**"Pred Fail"**
</dt><span id="_Starting_"></span><span id="_starting_"></span><span id="_STARTING_"></span><dt>

**"Starting"**
</dt><span id="_Stopping_"></span><span id="_stopping_"></span><span id="_STOPPING_"></span><dt>

**"Stopping"**
</dt><span id="_Service_"></span><span id="_service_"></span><span id="_SERVICE_"></span><dt>

**"Service"**
</dt> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scoping system's creation class name.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scoping system's name.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows Server 2003 and Windows XP:** Type of service access point (SAP).

Values are the following:



| Value                                                                                                  | Meaning                  |
|--------------------------------------------------------------------------------------------------------|--------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Write<br/>         |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Read<br/>          |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | Redirected<br/>    |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | Net\_Attached<br/> |
| <span id="16"></span><dl> <dt>**16**</dt> </dl> | Unknown<br/>       |



 

</dd> </dl>

## Remarks

The **Win32\_CommandLineAccess** class is derived from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





