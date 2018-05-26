---
title: Win32\_ServiceControl class
description: The Win32\_ServiceControl WMI class represents instructions for controlling installed and uninstalled services.
ms.assetid: 345bfbf7-48f6-4ea4-a78b-27b0397a8c5f
keywords:
- Win32_ServiceControl class
- Win32_ServiceControl class, described
topic_type:
- apiref
api_name:
- Win32_ServiceControl
- Win32_ServiceControl.Arguments
- Win32_ServiceControl.Caption
- Win32_ServiceControl.Description
- Win32_ServiceControl.Event
- Win32_ServiceControl.ID
- Win32_ServiceControl.Name
- Win32_ServiceControl.ProductCode
- Win32_ServiceControl.SettingID
- Win32_ServiceControl.Wait
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ServiceControl class

The **Win32\_ServiceControl** [WMI class](https://msdn.microsoft.com/library/aa393244) represents instructions for controlling installed and uninstalled services.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ServiceControl : Win32_MSIResource
{
  string Arguments;
  string Caption;
  string Description;
  string Event;
  string ID;
  string Name;
  string ProductCode;
  string SettingID;
  unit16 Wait;
};
```

## Members

The **Win32\_ServiceControl** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ServiceControl** class has these properties.

<dl> <dt>

**Arguments**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of arguments for starting services. The arguments are separated by null characters \[~\]. For example, the list of arguments One, Two, and Three are listed as the following: "One\[~\]Two\[~\]Three".

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object a one-line string.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**Event**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bitmap that represents the operations for which this object applies. Decimal value is noted in parentheses.



| Value used to set the bit                                                          | Meaning                                                          |
|------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>1 (0x1)</dt> </dl> | Starts the service during the StartServices action.<br/>   |
| <dl> <dt>2 (0x2)</dt> </dl> | Stops the service during the StopServices action.<br/>     |
| <dl> <dt>4 (0x4)</dt> </dl> | &lt;reserved&gt;<br/>                                      |
| <dl> <dt>8 (0x8)</dt> </dl> | Deletes the service during the DeleteServices action.<br/> |



 

The following values are only used during an uninstall.



| Value                                                                                 | Meaning                                                          |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>16 (0x10)</dt> </dl>  | Starts the service during the StartServices action.<br/>   |
| <dl> <dt>32 (0x20)</dt> </dl>  | Stops the service during the StopServices action.<br/>     |
| <dl> <dt>64 (0x40)</dt> </dl>  | &lt;reserved&gt;<br/>                                      |
| <dl> <dt>128 (0x80)</dt> </dl> | Deletes the service during the DeleteServices action.<br/> |



 

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Unique key that identifies a service control item within its product.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name used to identify a software element.

</dd> <dt>

**ProductCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product code for the product of which this service control is a part.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**Wait**
</dt> <dd> <dl> <dt>

Data type: **unit16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Waiting time before action is taken. A value of 1 (one) in this column means to wait until the service actually completes before proceeding. This implies that the event is critical to the install, and that if the event fails the error cannot be ignored. A value of 0 (zero) in this column means to wait only until the service control manager (SCM) reports that this service is in a pending state.

</dd> </dl>

## Remarks

The **Win32\_ServiceControl** class is derived from [**Win32\_MSIResource**](win32-msiresource.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





