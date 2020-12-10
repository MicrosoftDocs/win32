---
title: Win32_TSRemoteDesktop class
description: Describes a remote desktop connection that is available through Remote Desktop Web Access (RD Web Access).
ms.assetid: 40c7d8f1-cc45-4f0a-8c07-8215342ca02e
ms.tgt_platform: multiple
keywords:
- Win32_TSRemoteDesktop class Remote Desktop Services
- Win32_TSRemoteDesktop class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSRemoteDesktop
- Win32_TSRemoteDesktop.Caption
- Win32_TSRemoteDesktop.Description
- Win32_TSRemoteDesktop.InstallDate
- Win32_TSRemoteDesktop.Name
- Win32_TSRemoteDesktop.Status
- Win32_TSRemoteDesktop.Alias
- Win32_TSRemoteDesktop.SecurityDescriptor
- Win32_TSRemoteDesktop.IconPath
- Win32_TSRemoteDesktop.IconIndex
- Win32_TSRemoteDesktop.IconContents
- Win32_TSRemoteDesktop.ShowInPortal
- Win32_TSRemoteDesktop.RDPFileContents
- Win32_TSRemoteDesktop.IsVmFarm
- Win32_TSRemoteDesktop.VmFarmSettings
api_location:
- TsPubWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSRemoteDesktop class

Describes a remote desktop connection that is available through Remote Desktop Web Access (RD Web Access).

## Syntax

``` syntax
class Win32_TSRemoteDesktop : CIM_LogicalElement
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   Alias;
  string   SecurityDescriptor;
  string   IconPath;
  sint32   IconIndex;
  uint8    IconContents[];
  boolean  ShowInPortal;
  string   RDPFileContents;
  boolean  IsVmFarm;
  string   VmFarmSettings;
};
```

## Members

The **Win32\_TSRemoteDesktop** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TSRemoteDesktop** class has these properties.

<dl> <dt>

**Alias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The alias of the remote desktop connection.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**IconContents**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The byte contents of the icon that corresponds to the remote desktop connection.

</dd> <dt>

**IconIndex**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The index or ID of the icon for the remote desktop connection.

</dd> <dt>

**IconPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Path of the icon for the remote desktop connection.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**IsVmFarm**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if this remote desktop connection is part of a virtual machine farm.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**RDPFileContents**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Contents of the RDP file that correspond to the remote desktop connection.

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A security descriptor that controls access to the remote desktop connection, in SDDL format. An empty string implies allow all access. This security descriptor does not support DENY ACEs, or ACEs that refer to nondomain users or groups.

</dd> <dt>

**ShowInPortal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the remote desktop connection should be shown in RD Web Access.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> </dl>

</dd> <dt>

**VmFarmSettings**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Virtual machine farm settings for the remote desktop connection.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to set properties by using this class.

To connect to the \\root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**, which can be set by using the [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) COM function. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of 6. The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>Tsallow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



 

