---
description: Represents the parameters for copying a file from the host into the guest.
ms.assetid: 255F4132-C212-4A3B-A9B8-3F531E7D1CF9
title: Msvm_CopyFileToGuestSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CopyFileToGuestSettingData
- Msvm_CopyFileToGuestSettingData.Description
- Msvm_CopyFileToGuestSettingData.Caption
- Msvm_CopyFileToGuestSettingData.InstanceID
- Msvm_CopyFileToGuestSettingData.ElementName
- Msvm_CopyFileToGuestSettingData.OverwriteExisting
- Msvm_CopyFileToGuestSettingData.CreateFullPath
- Msvm_CopyFileToGuestSettingData.SourcePath
- Msvm_CopyFileToGuestSettingData.DestinationPath
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CopyFileToGuestSettingData class

Represents the parameters for copying a file from the host into the guest. This class derives from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_CopyFileToGuestSettingData : CIM_SettingData
{
  string  Description;
  string  Caption;
  string  InstanceID;
  string  ElementName;
  boolean OverwriteExisting;
  boolean CreateFullPath;
  string  SourcePath;
  string  DestinationPath;
};
```

## Members

The **Msvm\_CopyFileToGuestSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CopyFileToGuestSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

A short textual description of the object.

</dd> <dt>

**CreateFullPath**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether missing directories in the destination file's path must be created before copying the file.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

</dd> <dt>

**DestinationPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The complete path of the destination file to be copied. This destination file must be accessible to the guest and can contain environment variables, which are expanded by the guest. If the path specified is an existing directory in the guest, the destination file is created in this directory. In this case, the file name from **SourcePath** is used as the destination file name.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The display name for this instance of SettingData. In addition, the display name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above preferred algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

</dd> <dt>

**OverwriteExisting**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether an existing destination file must be overwritten.

</dd> <dt>

**SourcePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The complete path of the source file to be copied. This source file must be accessible to the Hyper-V host and can contain environment variables, which are expanded by the Hyper-V host.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85))
</dt> </dl>

 

