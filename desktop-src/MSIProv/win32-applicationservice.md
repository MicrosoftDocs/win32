---
title: Win32\_ApplicationService class
description: The Win32\_ApplicationService WMI class represents any installed or advertised component or application available on the system.
ms.assetid: dea14f4f-faa4-45c5-9bd2-786cfda4438b
keywords:
- Win32_ApplicationService class
- Win32_ApplicationService class, described
topic_type:
- apiref
api_name:
- Win32_ApplicationService
- Win32_ApplicationService.Caption
- Win32_ApplicationService.CreationClassName
- Win32_ApplicationService.Description
- Win32_ApplicationService.InstallDate
- Win32_ApplicationService.Name
- Win32_ApplicationService.Started
- Win32_ApplicationService.StartMode
- Win32_ApplicationService.Status
- Win32_ApplicationService.SystemCreationClassName
- Win32_ApplicationService.SystemName
api_location:
- MsiProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ApplicationService class

The **Win32\_ApplicationService** [WMI class](https://msdn.microsoft.com/library/aa393244) represents any installed or advertised component or application available on the system. Instances of this class include all properly installed and instrumented executable files.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ApplicationService : CIM_Service
{
  string   Caption;
  string   CreationClassName;
  string   Description;
  datetime InstallDate;
  string   Name;
  boolean  Started;
  string   StartMode;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
};
```

## Members

The **Win32\_ApplicationService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ApplicationService** class has these methods.



| Method                                                                        | Description                                         |
|:------------------------------------------------------------------------------|:----------------------------------------------------|
| [**StartService**](startservice-method-in-class-win32-applicationservice.md) | Places the service in the started state.<br/> |
| [**StopService**](stopservice-method-in-class-win32-applicationservice.md)   | Places the service in the stopped state.<br/> |



 

### Properties

The **Win32\_ApplicationService** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description (one-line) of the object.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

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

Date and time object was installed. This property does not need a value to indicate that the object is installed.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier of the service which provides an indication of the functionality that is managed. This functionality is described in more detail in the object's **Description** property.

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, service has been started.

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Service can be started automatically started by a operating system, or only started upon request. Values are:

"Automatic"

"Manual"

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

Values are:

"OK"

"Error"

"Degraded"

"Unknown"

"Pred Fail"

"Starting"

"Stopping"

"Service"

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type name of the system that hosts the service.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the system that hosts the service.

</dd> </dl>

## Remarks

The **Win32\_ApplicationService** class is derived from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





