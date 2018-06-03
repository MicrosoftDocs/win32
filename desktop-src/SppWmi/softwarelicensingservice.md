---
title: SoftwareLicensingService class
description: This class exposes the product-independent properties and methods of the Software Licensing service.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 36b1cbfb-374c-4937-a225-d9c61cfab9d0
keywords:
- SoftwareLicensingService class Windows Management Instrumentation
- SoftwareLicensingService class Windows Management Instrumentation , described
topic_type:
- apiref
api_name:
- SoftwareLicensingService
- SoftwareLicensingService.Version
- SoftwareLicensingService.KeyManagementServiceMachine
- SoftwareLicensingService.IsKeyManagementServiceMachine
- SoftwareLicensingService.VLActivationInterval
- SoftwareLicensingService.VLRenewalInterval
- SoftwareLicensingService.KeyManagementServiceCurrentCount
- SoftwareLicensingService.RequiredClientCount
- SoftwareLicensingService.KeyManagementServiceProductKeyID
- SoftwareLicensingService.DiscoveredKeyManagementServiceMachineName
- SoftwareLicensingService.DiscoveredKeyManagementServiceMachinePort
- SoftwareLicensingService.PolicyCacheRefreshRequired
- SoftwareLicensingService.ClientMachineID
- SoftwareLicensingService.RemainingWindowsReArmCount
- SoftwareLicensingService.KeyManagementServiceListeningPort
- SoftwareLicensingService.KeyManagementServiceDnsPublishing
- SoftwareLicensingService.KeyManagementServiceLowPriority
- SoftwareLicensingService.KeyManagementServiceHostCaching
- SoftwareLicensingService.KeyManagementServiceUnlicensedRequests
- SoftwareLicensingService.KeyManagementServiceLicensedRequests
- SoftwareLicensingService.KeyManagementServiceOOBGraceRequests
- SoftwareLicensingService.KeyManagementServiceOOTGraceRequests
- SoftwareLicensingService.KeyManagementServiceNonGenuineGraceRequests
- SoftwareLicensingService.KeyManagementServiceTotalRequests
- SoftwareLicensingService.KeyManagementServiceFailedRequests
- SoftwareLicensingService.KeyManagementServiceNotificationRequests
- SoftwareLicensingService.TokenActivationILID
- SoftwareLicensingService.TokenActivationILVID
- SoftwareLicensingService.TokenActivationGrantNumber
- SoftwareLicensingService.TokenActivationCertificateThumbprint
- SoftwareLicensingService.TokenActivationAdditionalInfo
- SoftwareLicensingService.KeyManagementServiceActivationDisabled
api_location:
- SppWmi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SoftwareLicensingService class

This class exposes the product-independent properties and methods of the Software Licensing service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class SoftwareLicensingService
{
  string  Version;
  string  KeyManagementServiceMachine;
  uint32  IsKeyManagementServiceMachine;
  uint32  VLActivationInterval;
  uint32  VLRenewalInterval;
  uint32  KeyManagementServiceCurrentCount;
  uint32  RequiredClientCount;
  string  KeyManagementServiceProductKeyID;
  string  DiscoveredKeyManagementServiceMachineName;
  uint32  DiscoveredKeyManagementServiceMachinePort;
  uint32  PolicyCacheRefreshRequired;
  string  ClientMachineID;
  uint32  RemainingWindowsReArmCount;
  uint32  KeyManagementServiceListeningPort;
  boolean KeyManagementServiceDnsPublishing;
  boolean KeyManagementServiceLowPriority;
  boolean KeyManagementServiceHostCaching;
  uint32  KeyManagementServiceUnlicensedRequests;
  uint32  KeyManagementServiceLicensedRequests;
  uint32  KeyManagementServiceOOBGraceRequests;
  uint32  KeyManagementServiceOOTGraceRequests;
  uint32  KeyManagementServiceNonGenuineGraceRequests;
  uint32  KeyManagementServiceTotalRequests;
  uint32  KeyManagementServiceFailedRequests;
  uint32  KeyManagementServiceNotificationRequests;
  string  TokenActivationILID;
  uint32  TokenActivationILVID;
  uint32  TokenActivationGrantNumber;
  string  TokenActivationCertificateThumbprint;
  string  TokenActivationAdditionalInfo;
  boolean KeyManagementServiceActivationDisabled;
};
```

## Members

The **SoftwareLicensingService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SoftwareLicensingService** class has these methods.



| Method                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireGenuineTicket**](acquiregenuineticket-softwarelicensingservice.md)                                         | Acquires a genuine ticket online.<br/>                                                                                                                                                                                                                                                                                                             |
| [**ClearKeyManagementServiceListeningPort**](clearkeymanagementservicelisteningport-softwarelicensingservice.md)     | Clears any previously specified listening port. Applies to KMS hosts only.<br/>                                                                                                                                                                                                                                                                    |
| [**ClearKeyManagementServiceMachine**](clearkeymanagementservicemachine-softwarelicensingservice.md)                 | Clears the key management service machine name.<br/>                                                                                                                                                                                                                                                                                               |
| [**ClearKeyManagementServicePort**](clearkeymanagementserviceport-softwarelicensingservice.md)                       | Clears any previously specified port number.<br/>                                                                                                                                                                                                                                                                                                  |
| [**ClearProductKeyFromRegistry**](clearproductkeyfromregistry-softwarelicensingservice.md)                           | Clears a product key from the registry.<br/>                                                                                                                                                                                                                                                                                                       |
| [**DisableKeyManagementServiceActivation**](disablekeymanagementserviceactivation-softwarelicensingservice.md)       | Disables volume activation through a KMS machine.<br/>                                                                                                                                                                                                                                                                                             |
| [**DisableKeyManagementServiceDnsPublishing**](disablekeymanagementservicednspublishing-softwarelicensingservice.md) | Disables the DNS publishing on a KMS host computer. <br/>                                                                                                                                                                                                                                                                                          |
| [**DisableKeyManagementServiceHostCaching**](disablekeymanagementservicehostcaching-softwarelicensingservice.md)     | Disables the caching of the KMS hostname and port on a volume activation client. <br/>                                                                                                                                                                                                                                                             |
| [**EnableKeyManagementServiceLowPriority**](enablekeymanagementservicelowpriority-softwarelicensingservice.md)       | Enables the KMS service to run with low priority. <br/>                                                                                                                                                                                                                                                                                            |
| [**InstallLicense**](installlicense-softwarelicensingservice.md)                                                     | Installs a license for the current product.<br/>                                                                                                                                                                                                                                                                                                   |
| [**InstallLicensePackage**](installlicensepackage-softwarelicensingservice.md)                                       | Installs a license package for the current product.<br/>                                                                                                                                                                                                                                                                                           |
| [**InstallProductKey**](installproductkey-softwarelicensingservice.md)                                               | Installs a product key.<br/>                                                                                                                                                                                                                                                                                                                       |
| [**ReArmWindows**](rearmwindows-softwarelicensingservice.md)                                                         | Resets the licensing status of the machine.<br/>                                                                                                                                                                                                                                                                                                   |
| [**RefreshLicenseStatus**](refreshlicensestatus-softwarelicensingservice.md)                                         | Updates the licensing status of the machine so that applications have access to current licensing information.<br/>                                                                                                                                                                                                                                |
| [**SetKeyManagementServiceListeningPort**](setkeymanagementservicelisteningport-softwarelicensingservice.md)         | Sets the TCP port on which a KMS host listens for activation requests. Applies to KMS hosts only. If a port is not specified, port 1688 is used.<br/>                                                                                                                                                                                              |
| [**SetKeyManagementServiceMachine**](setkeymanagementservicemachine-softwarelicensingservice.md)                     | Sets the name of the key management service (KMS) machine to use for volume activation.<br/>                                                                                                                                                                                                                                                       |
| [**SetKeyManagementServicePort**](setkeymanagementserviceport-softwarelicensingservice.md)                           | Sets the TCP port that is used by a client to make requests of a KMS host. If a port is not specified, port 1688 is used.<br/>                                                                                                                                                                                                                     |
| [**SetVLActivationInterval**](setvlactivationinterval-softwarelicensingservice.md)                                   | Sets the activation frequency, in minutes, of how often the current machine should contact the key management service machine before the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.<br/> |
| [**SetVLRenewalInterval**](setvlrenewalinterval-softwarelicensingservice.md)                                         | Sets the renewal frequency, in minutes, of how often the current machine should contact the key management service machine after the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.<br/>     |



 

### Properties

The **SoftwareLicensingService** class has these properties.

<dl> <dt>

**ClientMachineID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier for this volume client machine. The client includes this CMID in requests it sends to the KMS.

</dd> <dt>

**DiscoveredKeyManagementServiceMachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the last discovered KMS host name through DNS.

</dd> <dt>

**DiscoveredKeyManagementServiceMachinePort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the last discovered KMS host port through DNS.

</dd> <dt>

**IsKeyManagementServiceMachine**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the machine has a key management service (KMS) enabled. The following values are possible.



| Value                            | Description      |
|----------------------------------|------------------|
| <span id="0"></span>0<br/> | False<br/> |
| <span id="1"></span>1<br/> | True<br/>  |



 

</dd> <dt>

**KeyManagementServiceActivationDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the volume activation through key management service is disabled.

</dd> <dt>

**KeyManagementServiceCurrentCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of currently active volume clients. A value of -1 indicates that the machine is not enabled as a KMS or that it has not received any client licensing-requests.

</dd> <dt>

**KeyManagementServiceDnsPublishing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the DNS publishing status of a KMS host. The following values are possible.



| Value                            | Description                               |
|----------------------------------|-------------------------------------------|
| <span id="0"></span>0<br/> | Disabled<br/>                       |
| <span id="1"></span>1<br/> | Auto-publish enabled (default)<br/> |



 

</dd> <dt>

**KeyManagementServiceFailedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the total count of failed KMS requests.

</dd> <dt>

**KeyManagementServiceHostCaching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the caching status of the KMS host name and port. The following values are possible.



| Value                            | Description                          |
|----------------------------------|--------------------------------------|
| <span id="0"></span>0<br/> | Caching disabled<br/>          |
| <span id="1"></span>1<br/> | Caching enabled (default)<br/> |



 

</dd> <dt>

**KeyManagementServiceLicensedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 1 (Licensed).

</dd> <dt>

**KeyManagementServiceListeningPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the TCP port on which the KMS host listens for activation requests.

</dd> <dt>

**KeyManagementServiceLowPriority**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the thread priority status of the KMS. The following values are possible.



| Value                            | Description                          |
|----------------------------------|--------------------------------------|
| <span id="0"></span>0<br/> | Normal priority (default)<br/> |
| <span id="1"></span>1<br/> | Low priority<br/>              |



 

</dd> <dt>

**KeyManagementServiceMachine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the registered key management service machine name. Returns null if [**SetKeyManagementServiceMachine**](setkeymanagementservicemachine-softwarelicensingservice.md) has not been called.

</dd> <dt>

**KeyManagementServiceNonGenuineGraceRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 4 (NonGenuineGrace).

</dd> <dt>

**KeyManagementServiceNotificationRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 5 (Notification).

</dd> <dt>

**KeyManagementServiceOOBGraceRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 2 (OOBGrace).

</dd> <dt>

**KeyManagementServiceOOTGraceRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 3 (OOTGrace).

</dd> <dt>

**KeyManagementServiceProductKeyID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the KMS product key ID. Returns null if not applicable.

</dd> <dt>

**KeyManagementServiceTotalRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the total count of valid KMS requests.

</dd> <dt>

**KeyManagementServiceUnlicensedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 0 (Unlicensed).

</dd> <dt>

**PolicyCacheRefreshRequired**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the licensing policy cache needs to be updated. The following values are possible.



| Value                            | Description                      |
|----------------------------------|----------------------------------|
| <span id="0"></span>0<br/> | Refresh not required.<br/> |
| <span id="1"></span>1<br/> | Refresh required.<br/>     |



 

</dd> <dt>

**RemainingWindowsReArmCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the remaining number of times that the client can be successfully rearmed.

</dd> <dt>

**RequiredClientCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the minimum number of clients required to connect to a KMS machine to enable volume licensing.

</dd> <dt>

**TokenActivationAdditionalInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies additional information for token-based activation.

</dd> <dt>

**TokenActivationCertificateThumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the thumbprint of the certificate that activated the computer.

</dd> <dt>

**TokenActivationGrantNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the grant number in the token-based activation license that activated the computer.

</dd> <dt>

**TokenActivationILID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the ID of the token-based activation license that activated the computer.

</dd> <dt>

**TokenActivationILVID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the version of the token-based activation license that activated the computer.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Specifies the version of the Software Licensing service.

</dd> <dt>

**VLActivationInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the frequency, in minutes, of how often a client should contact the KMS machine before the client is licensed.

</dd> <dt>

**VLRenewalInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the frequency, in minutes, of how often the current machine should contact the KMS machine after the client is licensed.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Software Licensing Classes for Windows Vista](https://msdn.microsoft.com/library/ee957720)
</dt> </dl>

 

 





