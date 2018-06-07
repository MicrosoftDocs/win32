---
Description: The Win32\_ClusterShare class represents a shared resource on a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c8b40e3-431f-4728-a389-affbc04b8415
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_ClusterShare class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ClusterShare class

\[The **Win32\_ClusterShare** class is deprecated. Please use the [**MSFT\_FileShare**](https://msdn.microsoft.com/library/windows/desktop/dn887254) and [**MSFT\_SMFileShare**](https://msdn.microsoft.com/library/mt127097) classes instead.\]

The Win32\_ClusterShare class represents a shared resource on a cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4D6-5FBB-11D2-AAC1-006008C78BC7}"), SupportsCreate, CreateBy("Create"), SupportsDelete, DeleteBy("DeleteInstance"), AMENDMENT]
class Win32_ClusterShare : Win32_Share
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  uint32   AccessMask;
  boolean  AllowMaximum;
  uint32   MaximumAllowed;
  string   Name;
  string   Path;
  uint32   Type;
  string   ServerName;
};
```

## Members

The **Win32\_ClusterShare** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ClusterShare** class has these methods.



| Method                                                    | Description                                                      |
|:----------------------------------------------------------|:-----------------------------------------------------------------|
| [**Create**](create-win32-clustershare.md)               | Creates a new **Win32\_ClusterShare** instance.<br/>       |
| [**Delete**](delete-win32-clustershare.md)               | Deletes a **Win32\_ClusterShare** instance.<br/>           |
| [**GetAccessMask**](getaccessmask-win32-clustershare.md) | Returns a bitmap with the access rights to the share.<br/> |
| [**SetShareInfo**](setshareinfo-win32-clustershare.md)   | Sets the parameters of the shared resource.<br/>           |



 

### Properties

The **Win32\_ClusterShare** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is obsolete and is no longer used. Use the [**Win32\_Share.GetAccessMask**](getaccessmask-method-in-class-win32-share.md) method instead. The value of the **AccessMask** property is set to **null** by WMI. For more information about setting access when a share is created, see the [**Create**](create-method-in-class-win32-share.md) method.

This property is inherited from [**Win32\_Share**](win32-share.md).

</dd> <dt>

**AllowMaximum**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Network Management Structures\|[**SHARE\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525410)\|shi502\_max\_uses")
</dt> </dl>

Number of concurrent users for this resource has been limited. If **True**, the value in the **MaximumAllowed** property is ignored.

This property is inherited from [**Win32\_Share**](win32-share.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Caption")
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Description")
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Install Date")
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**MaximumAllowed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Network Management Structures\|[**SHARE\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525410)\|shi502\_max\_uses")
</dt> </dl>

Limit on the maximum number of users allowed to use this resource concurrently. The value is only valid if the **AllowMaximum** property is set to **FALSE**.

This property is inherited from [**Win32\_Share**](win32-share.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Network Management Structures\|[**SHARE\_INFO\_1**](https://msdn.microsoft.com/library/windows/desktop/bb525407)\|shi1\_netname")
</dt> </dl>

Alias given to a path set up as a share on a computer system running Windows.

Windows 2008 example: "\\SERVER01\\public" - Windows Server 2008 requires that you place the UNC in the name.

This property is inherited from [**Win32\_Share**](win32-share.md).

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Network Management Structures\|[**SHARE\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525410)\|shi502\_path")
</dt> </dl>

Local path of the Windows share.

Example: "C:\\Program Files"

This property is inherited from [**Win32\_Share**](win32-share.md).

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ServerName"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Network Management Structures\|[**SHARE\_INFO\_503**](https://msdn.microsoft.com/library/windows/desktop/cc462916)\|shi503\_servername")
</dt> </dl>

The cluster server on which the share is hosted.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Status")
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

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

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Network Management Structures\|[**SHARE\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525410)\|shi502\_type")
</dt> </dl>

Type of resource being shared. Types include: disk drives, print queues, interprocess communications (IPC), and general devices.

This property is inherited from [**Win32\_Share**](win32-share.md).

<dt>

<span id="Disk_Drive"></span><span id="disk_drive"></span><span id="DISK_DRIVE"></span>

**Disk Drive** (0)


</dt> <dd></dd> <dt>

<span id="Print_Queue"></span><span id="print_queue"></span><span id="PRINT_QUEUE"></span>

**Print Queue** (1)


</dt> <dd></dd> <dt>

<span id="Device"></span><span id="device"></span><span id="DEVICE"></span>

**Device** (2)


</dt> <dd></dd> <dt>

<span id="IPC"></span><span id="ipc"></span>

**IPC** (3)


</dt> <dd></dd> <dt>

<span id="Disk_Drive_Admin"></span><span id="disk_drive_admin"></span><span id="DISK_DRIVE_ADMIN"></span>

**Disk Drive Admin** (2147483648)


</dt> <dd></dd> <dt>

<span id="Print_Queue_Admin"></span><span id="print_queue_admin"></span><span id="PRINT_QUEUE_ADMIN"></span>

**Print Queue Admin** (2147483649)


</dt> <dd></dd> <dt>

<span id="Device_Admin"></span><span id="device_admin"></span><span id="DEVICE_ADMIN"></span>

**Device Admin** (2147483650)


</dt> <dd></dd> <dt>

<span id="IPC_Admin"></span><span id="ipc_admin"></span><span id="IPC_ADMIN"></span>

**IPC Admin** (2147483651)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Cimwin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Share**](win32-share.md)
</dt> </dl>

 

 




