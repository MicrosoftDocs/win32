---
title: MSFT\_HgsClientConfiguration class
description: Describes the configuration of the Host Guardian Service Client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9d6c3852-8e59-42ae-b7e6-c4916eab9d3c
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_HgsClientConfiguration class
- MSFT_HgsClientConfiguration class, described
topic_type:
- apiref
api_name:
- MSFT_HgsClientConfiguration
- MSFT_HgsClientConfiguration.Mode
- MSFT_HgsClientConfiguration.IsHostGuarded
- MSFT_HgsClientConfiguration.KeyProtectionServerUrl
- MSFT_HgsClientConfiguration.AttestationServerUrl
- MSFT_HgsClientConfiguration.AttestationOperationMode
- MSFT_HgsClientConfiguration.AttestationStatus
- MSFT_HgsClientConfiguration.AttestationSubstatus
api_location:
- HgsClientWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_HgsClientConfiguration class

Describes the configuration of the Host Guardian Service Client.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("HgsClientWmi"), ClassVersion("1.0"), AMENDMENT]
class MSFT_HgsClientConfiguration
{
  uint16  Mode;
  boolean IsHostGuarded;
  string  KeyProtectionServerUrl;
  string  AttestationServerUrl;
  uint16  AttestationOperationMode;
  uint16  AttestationStatus;
  uint64  AttestationSubstatus;
};
```

## Members

The **MSFT\_HgsClientConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_HgsClientConfiguration** class has these methods.



| Method                                                                                             | Description                                                                |
|:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**Get**](get-msft-hgsclientconfiguration.md)                                                     | Retrieves the local Host Guardian Service configuration.<br/>        |
| [**SetByChangeToLocalMode**](msft-hgsclientconfiguration-setbychangetolocalmode.md)               | Modifies the configuration of the Host Guardian Service Client.<br/> |
| [**SetBySecureHostingServiceMode**](msft-hgsclientconfiguration-setbysecurehostingservicemode.md) | Modifies the configuration of the Host Guardian Service Client.<br/> |



 

### Properties

The **MSFT\_HgsClientConfiguration** class has these properties.

<dl> <dt>

**AttestationOperationMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the attestation mode.

The possible values are.

<dt>

0
</dt> <dd>

The attestation mode is unknown.

</dd> <dt>

1
</dt> <dd>

The attestation mode is TPM-based.

</dd> <dt>

2
</dt> <dd>

The attestation mode is AD-based.

</dd> </dl>

</dd> <dt>

**AttestationServerUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

URL for the attestation server.

</dd> <dt>

**AttestationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the attestation status.

<dt>

0
</dt> <dd>

Attestation is not configured.

</dd> <dt>

1
</dt> <dd>

No attestation has been attempted.

</dd> <dt>

100
</dt> <dd>

Last attestation attempt passed and the health cert is valid.

</dd> <dt>

200
</dt> <dd>

Last attestation attempt passed but the health cert has expired.

</dd> <dt>

300
</dt> <dd>

Last attestation attempt failed with a retriable error.

</dd> <dt>

301
</dt> <dd>

Last attestation attempt failed due to host not authorized on the fabric.

</dd> <dt>

302
</dt> <dd>

Last attestation attempt failed due to a TPM related error.

</dd> <dt>

303
</dt> <dd>

Last attestation attempt failed due to an insecure host configuration.

</dd> </dl>

</dd> <dt>

**AttestationSubstatus**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bitfield that indicates the attestation substatus.

<dt>

0
</dt> <dd>

No information is available.

</dd> <dt>

1
</dt> <dd>

One or more secure boot configurations are insecure.

</dd> <dt>

2
</dt> <dd>

One or more debug modes are enabled.

</dd> <dt>

4
</dt> <dd>

Code integrity policy is insecure.

</dd> </dl>

</dd> <dt>

**IsHostGuarded**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the VM host is guarded,

</dd> <dt>

**KeyProtectionServerUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

URL for the key protection server.

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the mode.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Local_Mode"></span><span id="local_mode"></span><span id="LOCAL_MODE"></span>

**Local Mode** (1)


</dt> <dd></dd> <dt>

<span id="Secure_Hosting_Service_Mode"></span><span id="secure_hosting_service_mode"></span><span id="SECURE_HOSTING_SERVICE_MODE"></span>

**Secure Hosting Service Mode** (2)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Host Guardian Service WMI Provider](hoster-guardian-service-wmi-provider-portal.md)
</dt> </dl>

 

 





