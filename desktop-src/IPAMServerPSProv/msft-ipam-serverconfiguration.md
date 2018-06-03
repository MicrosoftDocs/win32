---
Description: Represents an IPAM server configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd96ec97-1b5e-44af-921f-6f4079db33e2
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_ServerConfiguration class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_IPAM\_ServerConfiguration class

Represents an IPAM server configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::Settings"), ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_ServerConfiguration : CIM_Setting
{
  string Caption;
  string Description;
  string ElementName;
  string SettingID;
  string InstanceID;
  string Version;
  uint16 Port;
  uint16 ProvisioningMethod;
  string GpoPrefix;
  string HMACKey;
};
```

## Members

The **MSFT\_IPAM\_ServerConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_IPAM\_ServerConfiguration** class has these methods.



| Method                                                                                                                             | Description                                                                                                                                                                    |
|:-----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplyIncrementalChangeToCollection**](msft-ipam-serverconfiguration-applyincrementalchangetocollection.md)                     | Applies the subset of the properties in the setting to a collection of managed system elements.<br/>                                                                     |
| [**ApplyIncrementalChangeToMSE**](msft-ipam-serverconfiguration-applyincrementalchangetomse.md)                                   | Applies the subset of the properties in the setting to a managed system element.<br/>                                                                                    |
| [**ApplyToCollection**](msft-ipam-serverconfiguration-applytocollection.md)                                                       | Applies the setting to a collection of managed system elements.<br/>                                                                                                     |
| [**ApplyToMSE**](msft-ipam-serverconfiguration-applytomse.md)                                                                     | Applies the setting to a managed system element.<br/>                                                                                                                    |
| [**SetIpamConfiguration**](setipamconfiguration-msft-ipam-serverconfiguration.md)                                                 | Updates the configuration for an IPAM server.<br/>                                                                                                                       |
| [**VerifyOKToApplyIncrementalChangeToCollection**](msft-ipam-serverconfiguration-verifyoktoapplyincrementalchangetocollection.md) | Indicates whether a subset of the properties in the setting can be applied to the collection of managed systems element during the specified time or time interval.<br/> |
| [**VerifyOKToApplyIncrementalChangeToMSE**](msft-ipam-serverconfiguration-verifyoktoapplyincrementalchangetomse.md)               | Indicates whether a subset of the properties in the setting can be applied to the managed system element during the specified time or time interval.<br/>                |
| [**VerifyOKToApplyToCollection**](msft-ipam-serverconfiguration-verifyoktoapplytocollection.md)                                   | Indicates whether the setting can be applied to the specified collection of managed system elements during the specified time or time interval..<br/>                    |
| [**VerifyOKToApplyToMSE**](msft-ipam-serverconfiguration-verifyoktoapplytomse.md)                                                 | Indicates whether the setting can be applied to the specified managed system element during the specified time or time interval.<br/>                                    |



 

### Properties

The **MSFT\_IPAM\_ServerConfiguration** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**GpoPrefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GPO prefix to use for Group Policy based provisioning.

</dd> <dt>

**HMACKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The secret key used to encrypt the IPAM data store.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (InstanceID), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

</dd> <dt>

**Port**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The incoming port that is configured on the server.

</dd> <dt>

**ProvisioningMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The provisioning method that is configured on the server.

<dt>

<span id="GpoBased"></span><span id="gpobased"></span><span id="GPOBASED"></span>

**GpoBased** (0)


</dt> <dd></dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

**Manual** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The ID of the setting.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The product version of the IPAM server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




