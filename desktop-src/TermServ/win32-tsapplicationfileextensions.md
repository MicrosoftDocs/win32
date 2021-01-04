---
title: Win32_TSApplicationFileExtensions class
description: The file name extensions that are handled by an application on a Remote Desktop Session Host (RD Session Host) server.
ms.assetid: beefc266-5ad6-49ee-b761-98764e2905d6
ms.tgt_platform: multiple
keywords:
- Win32_TSApplicationFileExtensions class Remote Desktop Services
- Win32_TSApplicationFileExtensions class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSApplicationFileExtensions
- Win32_TSApplicationFileExtensions.Caption
- Win32_TSApplicationFileExtensions.Description
- Win32_TSApplicationFileExtensions.InstallDate
- Win32_TSApplicationFileExtensions.Name
- Win32_TSApplicationFileExtensions.Status
api_location:
- TsPubWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSApplicationFileExtensions class

Describes the file name extensions that are handled by an application on a Remote Desktop Session Host (RD Session Host) server.

## Syntax

``` syntax
class Win32_TSApplicationFileExtensions : CIM_LogicalElement
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
};
```

## Members

The **Win32\_TSApplicationFileExtensions** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSApplicationFileExtensions** class has these methods.



| Method                                                                         | Description                                                                                |
|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**FileAssociations**](fileassociations-win32-tsapplicationfileextensions.md) | Scans the registry to get the current file associations for an application.<br/>     |
| [**FileExtensions**](fileextensions-win32-tsapplicationfileextensions.md)     | Provides a list of the file name extensions that are handled by an application.<br/> |



 

### Properties

The **Win32\_TSApplicationFileExtensions** class has these properties.

<dl> <dt>

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

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

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

</dd> </dl>

## Remarks

To connect to the \\root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**, which can be set by using the [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) COM function. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of 6.

The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>Tsallow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



 

