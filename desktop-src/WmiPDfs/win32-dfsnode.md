---
title: Win32\_DFSNode class
description: The Win32\_DFSNode WMI class represents a root or junction node of a domain-based or stand-alone Distributed file system (DFS).
audience: developer
author: REDMOND\\martinek
manager: REDMOND\\martinek
ms.assetid: 7c91e416-f4d6-4ec2-8177-69a93ecbfa1c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_DFSNode class
- Win32_DFSNode class, described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_DFSNode class

The **Win32\_DFSNode** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a root or junction node of a domain-based or stand-alone Distributed file system (DFS). The DFS root is also represented by this class because the root is also a node. Each link has one or more targets or actual share paths for the storage defined by the [**Win32\_DFSTarget**](win32-dfstarget.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("DFSProvider"), SupportsCreate, CreateBy("Create"), SupportsDelete, DeleteBy("DeleteInstance"), SupportsUpdate, AMENDMENT]
class Win32_DFSNode : CIM_LogicalElement
{
  string       Caption;
  datetime REF InstallDate;
  string       Status;
  string       Name;
  boolean      Root;
  uint32       State;
  string       Description;
  uint32       Timeout;
};
```

## Members

The **Win32\_DFSNode** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_DFSNode** class has these methods.



| Method                                                 | Description                                                        |
|:-------------------------------------------------------|:-------------------------------------------------------------------|
| [**Create**](create-method-in-class-win32-dfsnode.md) | Creates a new instance of the **Win32\_DFSNode** class.<br/> |



 

### Properties

The **Win32\_DFSNode** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("The Description indicates a comment describing the node.")
</dt> </dl>

TBD

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name"), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifier for the DFS node. It is the same as the entry path of a node, based on the Universal Naming Convention (UNC). It can take one of the following two forms:

\\\\\\\\*DfsServerName*\\\\*ShareName*\\\\*PathToLink*

\\\\\\\\*DomainName*\\\\*FtDfsName*\\\\*PathToLink*

where

*DfsServerName* is the name of a server that hosts the DFS root volume.

*ShareName* is the name of the share published on the host server.

*PathToLink* is the path to the physical share.

*DomainName* is the name of the domain that hosts the DFS root volume.

*FtDfsName* is the name of the fault-tolerant DFS root published.

*PathToLink* is the path to the physical share.

This property overrides the **Name** property in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Root**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the node is a DFS root or a link. A value of **TRUE** indicates that the node is a root.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the node.

<dt>

<span id="Ok"></span><span id="ok"></span><span id="OK"></span>

**Ok** (0)


</dt> <dd></dd> <dt>

<span id="Inconsistent"></span><span id="inconsistent"></span><span id="INCONSISTENT"></span>

**Inconsistent** (1)


</dt> <dd></dd> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

**Online** (2)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("seconds")
</dt> </dl>

Time, in seconds, that the client caches the referral of this link.

</dd> </dl>

## Remarks

The **Win32\_DFSNode** class is derived from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892), which derives from the [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) class.

## Examples

While Impersonation works with a DFS root server, Delegation is required for all other DC's in a domain-based DFS. The following PowerShell describes how to set delegation.


```PowerShell
Get-WmiObject Win32_DFSNode -computer <dns-domain-name> -impersonation delegate
```



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Wmipdfs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipdfs.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 





