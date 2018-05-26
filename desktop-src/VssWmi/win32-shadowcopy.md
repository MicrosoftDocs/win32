---
title: Win32\_ShadowCopy class
description: The Win32\_ShadowCopy class is a storage extent that represents a duplicate copy of the original volume at a previous time.
ms.assetid: 62ba9405-108b-4025-9355-e637d52107ab
keywords:
- Win32_ShadowCopy class
- Win32_ShadowCopy class, described
topic_type:
- apiref
api_name:
- Win32_ShadowCopy
- Win32_ShadowCopy.Caption
- Win32_ShadowCopy.Description
- Win32_ShadowCopy.ID
- Win32_ShadowCopy.InstallDate
- Win32_ShadowCopy.Name
- Win32_ShadowCopy.SetID
- Win32_ShadowCopy.ProviderID
- Win32_ShadowCopy.Status
- Win32_ShadowCopy.Count
- Win32_ShadowCopy.DeviceObject
- Win32_ShadowCopy.VolumeName
- Win32_ShadowCopy.OriginatingMachine
- Win32_ShadowCopy.ServiceMachine
- Win32_ShadowCopy.ExposedName
- Win32_ShadowCopy.State
- Win32_ShadowCopy.Persistent
- Win32_ShadowCopy.ClientAccessible
- Win32_ShadowCopy.NoAutoRelease
- Win32_ShadowCopy.NoWriters
- Win32_ShadowCopy.Transportable
- Win32_ShadowCopy.NotSurfaced
- Win32_ShadowCopy.HardwareAssisted
- Win32_ShadowCopy.Differential
- Win32_ShadowCopy.Plex
- Win32_ShadowCopy.Imported
- Win32_ShadowCopy.ExposedRemotely
- Win32_ShadowCopy.ExposedLocally
api_location:
- Vsswmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ShadowCopy class

The **Win32\_ShadowCopy** class is a storage extent that represents a duplicate copy of the original volume at a previous time.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowCopy : CIM_LogicalElement
{
  string   Caption;
  string   Description;
  string   ID;
  datetime InstallDate;
  string   Name;
  string   SetID;
  string   ProviderID;
  string   Status;
  uint32   Count;
  string   DeviceObject;
  string   VolumeName;
  string   OriginatingMachine;
  string   ServiceMachine;
  string   ExposedName;
  uint32   State;
  boolean  Persistent;
  boolean  ClientAccessible;
  boolean  NoAutoRelease;
  boolean  NoWriters;
  boolean  Transportable;
  boolean  NotSurfaced;
  boolean  HardwareAssisted;
  boolean  Differential;
  boolean  Plex;
  boolean  Imported;
  boolean  ExposedRemotely;
  boolean  ExposedLocally;
};
```

## Members

The **Win32\_ShadowCopy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ShadowCopy** class has these methods.



| Method                                                    | Description                                                      |
|:----------------------------------------------------------|:-----------------------------------------------------------------|
| [**Create**](create-method-in-class-win32-shadowcopy.md) | Creates a shadow copy by using the specified context.<br/> |



 

### Properties

The **Win32\_ShadowCopy** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object. This property is inherited from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892).

</dd> <dt>

**ClientAccessible**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by the Windows Previous Versions component.

</dd> <dt>

**Count**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of shadow copies in a shadow copy set to which a shadow copy belongs.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object. This property is inherited from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892).

</dd> <dt>

**DeviceObject**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Windows object manager name for an underlying storage device that supports the original volume.

</dd> <dt>

**Differential**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by a differential shadow copy provider. The provider can be implemented in hardware or software.

</dd> <dt>

**ExposedLocally**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is exposed on the local computer with a drive letter or mount point. If **ExposedLocally** and **ExposedRemotely** are not set, the shadow copy is hidden.

</dd> <dt>

**ExposedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File system name of a shadow copy when it is exposed. The **ExposedName** property might contain a drive letter or mount point. The **ExposedName** property is **NULL** when a shadow copy is hidden or otherwise not exposed.

</dd> <dt>

**ExposedRemotely**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is exposed on a remote computer with a network share. If **ExposedRemotely** and **ExposedLocally** are not set, the shadow copy is hidden.

</dd> <dt>

**HardwareAssisted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by a hardware shadow copy provider.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier for a shadow copy on the system.

</dd> <dt>

**Imported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is imported to a computer by using the **Import** method and is not created by using the [**Create**](create-method-in-class-win32-shadowcopy.md) method.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892).

</dd> <dt>

**NoAutoRelease**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is retained after the requestor process ends. If **false**, the shadow copy is automatically deleted when the requestor process ends.

</dd> <dt>

**NotSurfaced**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is not currently in the device namespace of a local computer.

</dd> <dt>

**NoWriters**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created with the involvement of the shadow copy writer components.

</dd> <dt>

**OriginatingMachine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer that hosts the original volume.

</dd> <dt>

**Persistent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is persistent across reboots.

</dd> <dt>

**Plex**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by a split mirror shadow copy provider. The provider can be implemented in hardware or software.

</dd> <dt>

**ProviderID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier for a shadow provider that creates a shadow.

</dd> <dt>

**ServiceMachine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer that services the shadow copy.

</dd> <dt>

**SetID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier for a shadow copy set to which the shadow belongs.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current state of a shadow copy.



| Value                                                                         | Meaning                         |
|-------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>0</dt> </dl>  | Unknown<br/>              |
| <dl> <dt>1</dt> </dl>  | Preparing<br/>            |
| <dl> <dt>2</dt> </dl>  | ProcessingPrepare<br/>    |
| <dl> <dt>3</dt> </dl>  | Prepared<br/>             |
| <dl> <dt>4</dt> </dl>  | ProcessingPrecommit<br/>  |
| <dl> <dt>5</dt> </dl>  | Precommitted<br/>         |
| <dl> <dt>6</dt> </dl>  | ProcessingCommit<br/>     |
| <dl> <dt>7</dt> </dl>  | Committed<br/>            |
| <dl> <dt>8</dt> </dl>  | ProcessingPostcommit<br/> |
| <dl> <dt>9</dt> </dl>  | Created<br/>              |
| <dl> <dt>10</dt> </dl> | Aborted<br/>              |
| <dl> <dt>11</dt> </dl> | Deleted<br/>              |
| <dl> <dt>12</dt> </dl> | Count<br/>                |



 

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892).

Values include the following:

<dl><span id="OK"></span><span id="ok"></span><dt>

**"OK"**
</dt><span id="Error"></span><span id="error"></span><span id="ERROR"></span><dt>

**"Error"**
</dt><span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dt>

**"Degraded"**
</dt><span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dt>

**"Unknown"**
</dt><span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span><dt>

**"Pred Fail"**
</dt><span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dt>

**"Starting"**
</dt><span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dt>

**"Stopping"**
</dt><span id="Service"></span><span id="service"></span><span id="SERVICE"></span><dt>

**"Service"**
</dt><span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dt>

**"Stressed"**
</dt><span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span><dt>

**"NonRecover"**
</dt><span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dt>

**"No Contact"**
</dt><span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span><dt>

**"Lost Comm"**
</dt> </dl>

</dd> <dt>

**Transportable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy can be surfaced on another computer. If **false**, and the volumes are surfaced locally, it may not be possible to surface them later on a different computer.

</dd> <dt>

**VolumeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the original volume for which a shadow copy is made.

</dd> </dl>

## Remarks

> [!Note]  
> This class is unavailable for 32-bit applications on Windows Server 2008 x64. To access the class with Visual Studio, go to **Project Properties**, then **General**, and un-check the **Prefer 32-bit** box.

 

## Examples

The [Get Remote Shadow Volume Information With Powershell](http://gallery.technet.microsoft.com/Get-Remote-Shadow-Volume-e5a72619) PowerShell sample on TechNet gallery uses **Win32\_ShadowCopy** to retrieve shadow volume information.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vss.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vsswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[**Win32\_ShadowProvider**](win32-shadowprovider.md)
</dt> <dt>

[**Win32\_ShadowContext**](win32-shadowcontext.md)
</dt> <dt>

[**Win32\_ShadowStorage**](win32-shadowstorage.md)
</dt> <dt>

[**Win32\_ShadowBy**](win32-shadowby.md)
</dt> <dt>

[**Win32\_ShadowFor**](win32-shadowfor.md)
</dt> <dt>

[**Win32\_ShadowOn**](win32-shadowon.md)
</dt> <dt>

[**Win32\_ShadowVolumeSupport**](win32-shadowvolumesupport.md)
</dt> <dt>

[**Win32\_ShadowDiffVolumeSupport**](win32-shadowdiffvolumesupport.md)
</dt> </dl>

 

 





