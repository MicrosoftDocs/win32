---
title: MDM_HealthAttestation class
description: The MDM\_HealthAttestation class enables enterprise IT managers to assess the health of managed devices and take enterprise policy actions.
ms.assetid: 64f40ccc-98f6-48d6-bcd4-793375e3dbfb
keywords:
- MDM_HealthAttestation class
- MDM_HealthAttestation class, described
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# MDM\_HealthAttestation class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_HealthAttestation** class enables enterprise IT managers to assess the health of managed devices and take enterprise policy actions.

The following is a list of functions performed by the HealthAttestation CSP:

-   Collects data that is used in verifying a devices health states
-   Forwards the data to the Health Attestation Service (HAS)
-   Provisions the Health Attestation Certificate that it receives from HAS
-   Upon request, forwards the Health Attestation Certificate (received from HAS) and related runtime information to the MDM Server for verification

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_HealthAttestation
{
  string  InstanceID;
  string  ParentID;
  sint32  Status;
  boolean ForceRetrieve;
  string  Certificate;
  string  Nonce;
  string  CorrelationID;
  sint32  TpmReadyStatus;
  sint32  MaxSupportedProtocolVersion;
  sint32  PreferredMaxProtocolVersion;
  sint32  CurrentProtocolVersion;
  string  HASEndpoint;
};
```

## Members

The **MDM\_HealthAttestation** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_HealthAttestation** class has these methods.



| Method                                                                 | Description                                                                                  |
|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**VerifyHealthMethod**](mdm-healthattestation-verifyhealthmethod.md) | Method to notify the device to prepare a health certificate verification request.<br/> |



 

### Properties

The **MDM\_HealthAttestation** class has these properties.

<dl> <dt>

[Certificate](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#certificate)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

</dd> <dt>

[CorrelationID](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#correlationid)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**CurrentProtocolVersion**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

[ForceRetrieve](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#forceretrieve)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HASEndpoint](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "HealthAttestation".

</dd> <dt>

**MaxSupportedProtocolVersion**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

[Nonce](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#nonce)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/"

</dd> <dt>

**PreferredMaxProtocolVersion**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

[Status](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#status)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[TpmReadyStatus](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/healthattestation-csp#tpmreadystatus)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](https://msdn.microsoft.com/library/windows/hardware/mt614877)
</dt> </dl>

 

 





