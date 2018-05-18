---
title: MSFT\_SMProvider class
description: Represents a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd1173048-091c-43b2-843b-f3d2ed17772c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMProvider class", "MSFT_SMProvider class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMProvider
- MSFT_SMProvider.ObjectId
- MSFT_SMProvider.Identifier
- MSFT_SMProvider.SystemName
- MSFT_SMProvider.ProviderSystemID
- MSFT_SMProvider.ElementName
- MSFT_SMProvider.VersionString
- MSFT_SMProvider.Manufacturer
- MSFT_SMProvider.URI
- MSFT_SMProvider.InteropNamespace
- MSFT_SMProvider.MultipleOperationsSupported
- MSFT_SMProvider.Namespaces
- MSFT_SMProvider.SMISProfileVersion
- MSFT_SMProvider.AutonomousProfiles
- MSFT_SMProvider.AutonomousProfileVersions
- MSFT_SMProvider.CommunicationMechanisms
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMProvider class

Represents a provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMProvider
{
  String  ObjectId;
  String  Identifier;
  String  SystemName;
  String  ProviderSystemID;
  String  ElementName;
  String  VersionString;
  String  Manufacturer;
  String  URI;
  String  InteropNamespace;
  Boolean MultipleOperationsSupported;
  String  Namespaces[];
  String  SMISProfileVersion;
  String  AutonomousProfiles[];
  String  AutonomousProfileVersions[];
  String  CommunicationMechanisms[];
};
```

## Members

The **MSFT\_SMProvider** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMProvider** class has these methods.



| Method                                   | Description                                     |
|:-----------------------------------------|:------------------------------------------------|
| [**Remove**](remove-msft-smprovider.md) | Removes the provider from the cache.<br/> |



 

### Properties

The **MSFT\_SMProvider** class has these properties.

<dl> <dt>

**AutonomousProfiles**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:  **

Autonomous profiles supported on the provider.

</dd> <dt>

**AutonomousProfileVersions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:  **

Versions of the autonomous profiles.

</dd> <dt>

**CommunicationMechanisms**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:  **

Communication mechanisms supported on the provider.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:** The name of the CIM server that is used for human interfaces.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the logical instance of the storage object.

</dd> <dt>

**InteropNamespace**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interop namespace on the provider.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manufacturer of this software.

</dd> <dt>

**MultipleOperationsSupported**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:  **

Whether multiple operations are supported on the provider.

</dd> <dt>

**Namespaces**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:  **

Vendor-specific namespaces.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

</dd> <dt>

**ProviderSystemID**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2012:** The name of the containing system as reported by the provider.

</dd> <dt>

**SMISProfileVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The high level SMI-S Registered profile version on the provider.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the containing system.

</dd> <dt>

**URI**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The provider URI.

</dd> <dt>

**VersionString**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representing the complete software version information - for example, '12.1(3)T'.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





