---
description: Represents the settings for the virtual computer terminal services on a host.
ms.assetid: 1f8d0718-09da-4231-95eb-cc63b6f324dd
title: Msvm_TerminalServiceSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_TerminalServiceSettingData
- Msvm_TerminalServiceSettingData.InstanceID
- Msvm_TerminalServiceSettingData.Caption
- Msvm_TerminalServiceSettingData.Description
- Msvm_TerminalServiceSettingData.ElementName
- Msvm_TerminalServiceSettingData.ListenerPort
- Msvm_TerminalServiceSettingData.DisableSelfSignedCertificateGeneration
- Msvm_TerminalServiceSettingData.AuthCertificateHash
- Msvm_TerminalServiceSettingData.TrustedIssuerCertificateHashes
- Msvm_TerminalServiceSettingData.AllowedHashAlgorithms
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_TerminalServiceSettingData class

Represents the settings for the virtual computer terminal services on a host. The properties for this class cannot be modified directly. The client must call the [**Msvm\_TerminalService.ModifyServiceSettings**](modifyservicesettings-msvm-terminalservice.md) method to modify any of these properties.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_TerminalServiceSettingData : CIM_SettingData
{
  string  InstanceID;
  string  Caption = "Hyper-V Terminal Service Settings";
  string  Description = "Settings for the Hyper-V Terminal Service";
  string  ElementName = "Hyper-V Terminal Service Settings";
  uint32  ListenerPort;
  boolean DisableSelfSignedCertificateGeneration;
  uint8   AuthCertificateHash[];
  string  TrustedIssuerCertificateHashes[];
  string  AllowedHashAlgorithms[];
};
```

## Members

The **Msvm\_TerminalServiceSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_TerminalServiceSettingData** class has these properties.

<dl> <dt>

**AllowedHashAlgorithms**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of hash algorithms accepted for verifying the signature of federated authentication tokens.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**AuthCertificateHash**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The hash of the certificate to use for remote authentication.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**DisableSelfSignedCertificateGeneration**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Disables self-signed certificate generation.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ListenerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network port on which the initial remote session connection will be made.

</dd> <dt>

**TrustedIssuerCertificateHashes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of trusted issuer certificate hashes for verifying the signature of federated authentication tokens.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

