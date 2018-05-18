---
title: MSFT\_StorageProvider class
description: Represents a storage management provider (SMP) package that manages a storage subsystem.
ms.assetid: 'afafd4d5-c0c1-4461-814d-bf00de403b3f'
keywords: ["MSFT_StorageProvider class Windows Storage Management API", "MSFT_StorageProvider class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageProvider
- MSFT_StorageProvider.Type
- MSFT_StorageProvider.Name
- MSFT_StorageProvider.Manufacturer
- MSFT_StorageProvider.Version
- MSFT_StorageProvider.CimServerName
- MSFT_StorageProvider.URI
- MSFT_StorageProvider.URI_IP
- MSFT_StorageProvider.RemoteSubsystemCacheMode
- MSFT_StorageProvider.SupportsSubsystemRegistration
- MSFT_StorageProvider.SupportedRemoteSubsystemCacheModes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageProvider class

Represents a storage management provider (SMP) package that manages a storage subsystem.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageProvider : MSFT_StorageObject
{
  UInt16  Type;
  String  Name;
  String  Manufacturer;
  String  Version;
  String  CimServerName;
  String  URI;
  String  URI_IP;
  UInt16  RemoteSubsystemCacheMode;
  Boolean SupportsSubsystemRegistration;
  UInt16  SupportedRemoteSubsystemCacheModes;
};
```

## Members

The **MSFT\_StorageProvider** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageProvider** class has these methods.



| Method                                                                      | Description                                                                                                |
|:----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**Discover**](discover-msft-storageprovider.md)                           | Discovers the objects that are owned by the storage provider.<br/>                                   |
| [**GetSecurityDescriptor**](msft-storageprovider-getsecuritydescriptor.md) | Retrieves the security descriptor that controls access to the storage provider object instance.<br/> |
| [**RegisterSubsystem**](msft-storageprovider-registersubsystem.md)         | Registers a subsystem to be managed by this provider.<br/>                                           |
| [**SetAttributes**](msft-storageprovider-setattributes.md)                 | Sets the attributes of the provider.<br/>                                                            |
| [**SetSecurityDescriptor**](setsecuritydescriptor-msft-storageprovider.md) | Sets the security descriptor that controls access to the storage provider object instance.<br/>      |
| [**UnregisterSubsystem**](msft-storageprovider-unregistersubsystem.md)     | Unregisters a subsystem.<br/>                                                                        |



 

### Properties

The **MSFT\_StorageProvider** class has these properties.

<dl> <dt>

**CimServerName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **Type** property is **SMI-S**, this property contains the name of the CIM Server to be displayed in the user interface. For example, "ACME CIM Server". This property is required to support the SLP discovery mechanism.

If the **Type** property is not **SMI-S**, this property is **NULL**.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The name of the manufacturer of the SMP software.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the storage provider.

</dd> <dt>

**RemoteSubsystemCacheMode**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The caching mode of this provider.



| Value                                                                                                | Meaning                     |
|------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unknown<br/>          |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Disabled<br/>         |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Manual-Discovery<br/> |



 

</dd> <dt>

**SupportedRemoteSubsystemCacheModes**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The caching modes that this provider supports.



| Value                                                                                                | Meaning                     |
|------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unknown<br/>          |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Disabled<br/>         |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Manual-Discovery<br/> |



 

</dd> <dt>

**SupportsSubsystemRegistration**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if this provider supports remote registration and management; **FALSE** if it does not.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Indicates whether the provider is implemented using SMI-S standard interfaces or SMP WMI interfaces.



| Value                                                                                                                                                                                        | Meaning                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <span id="SMP"></span><span id="smp"></span><dl> <dt>**SMP**</dt> <dt>1</dt> </dl>        | The provider is a native SMP-based provider.<br/>                                                                 |
| <span id="SMI-S"></span><span id="smi-s"></span><dl> <dt>**SMI-S**</dt> <dt>2 </dt> </dl> | The provider is an SMI-S-based provider that is visible through the SMI-S proxy storage management provider.<br/> |



 

</dd> <dt>

**URI**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **Type** property is **SMI-S**, this property contains the protocol, host name, and port that connect to an SMI-S server.

If the **Type** property is not **SMI-S**, this property is **NULL**.

</dd> <dt>

**URI\_IP**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **Type** property is **SMI-S**, this property contains the protocol, IP address, and port that connect to an SMI-S server. This pro

If the **Type** property is not **SMI-S**, this property is **NULL**.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A free-form version string used by the SMP manufacturer to differentiate between software versions.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





