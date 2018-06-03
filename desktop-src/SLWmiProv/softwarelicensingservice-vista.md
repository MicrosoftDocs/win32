---
Description: Not supported. Use the SoftwareLicensingService class.
ms.assetid: 953c2f88-00cd-47d1-8bf1-277bcb64f622
title: SoftwareLicensingService class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SoftwareLicensingService class

Not supported. Use the [**SoftwareLicensingService**](https://msdn.microsoft.com/library/cc534597) class.

**Windows Vista and Windows Server 2008:** This class exposes the product-independent properties and methods of the Software Licensing service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class SoftwareLicensingService
{
  string Version;
  string KeyManagementServiceMachine;
  uint32 IsKeyManagementServiceMachine;
  uint32 VLActivationInterval;
  uint32 VLRenewalInterval;
  uint32 KeyManagementServiceCurrentCount;
  uint32 RequiredClientCount;
  string KeyManagementServiceProductKeyID;
  uint32 PolicyCacheRefreshRequired;
  string ClientMachineID;
  uint32 KeyManagementServiceUnlicensedRequests;
  uint32 KeyManagementServiceLicensedRequests;
  uint32 KeyManagementServiceOOBGraceRequests;
  uint32 KeyManagementServiceOOTGraceRequests;
  uint32 KeyManagementServiceNonGenuineGraceRequests;
  uint32 KeyManagementServiceTotalRequests;
  uint32 KeyManagementServiceFailedRequests;
  uint32 KeyManagementServiceNotificationRequests;
};
```

## Members

The **SoftwareLicensingService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SoftwareLicensingService** class has these methods.



| Method                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                              |
|:------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireGenuineTicket**](acquiregenuineticket-softwarelicensingservice-vista.md)                         | Acquires a genuine ticket online.<br/>                                                                                                                                                                                                                                                                                                             |
| [**ClearKeyManagementServiceMachine**](clearkeymanagementservicemachine-softwarelicensingservice-vista.md) | Clears the key management service machine name.<br/>                                                                                                                                                                                                                                                                                               |
| [**ClearProductKeyFromRegistry**](clearproductkeyfromregistry-softwarelicensingservice-vista.md)           | Clears a product key from the registry.<br/>                                                                                                                                                                                                                                                                                                       |
| [**InstallLicense**](installlicense-softwarelicensingservice-vista.md)                                     | Installs a license for the current product.<br/>                                                                                                                                                                                                                                                                                                   |
| [**InstallLicensePackage**](installlicensepackage-softwarelicensingservice-vista.md)                       | Installs a license package for the current product.<br/>                                                                                                                                                                                                                                                                                           |
| [**InstallProductKey**](installproductkey-softwarelicensingservice-vista.md)                               | Installs a product key.<br/>                                                                                                                                                                                                                                                                                                                       |
| [**ReArmWindows**](rearmwindows-softwarelicensingservice-vista.md)                                         | Resets the licensing status of the machine.<br/>                                                                                                                                                                                                                                                                                                   |
| [**RefreshLicenseStatus**](refreshlicensestatus-softwarelicensingservice-vista.md)                         | Updates the licensing status of the machine so that applications have access to current licensing information.<br/>                                                                                                                                                                                                                                |
| [**SetKeyManagementServiceMachine**](setkeymanagementservicemachine-softwarelicensingservice-vista.md)     | Sets the name of the key management service (KMS) machine to use for volume activation.<br/>                                                                                                                                                                                                                                                       |
| [**SetVLActivationInterval**](setvlactivationinterval-softwarelicensingservice-vista.md)                   | Sets the activation frequency, in minutes, of how often the current machine should contact the key management service machine before the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.<br/> |
| [**SetVLRenewalInterval**](setvlrenewalinterval-softwarelicensingservice-vista.md)                         | Sets the renewal frequency, in minutes, of how often the current machine should contact the key management service machine after the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.<br/>     |



 

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

**KeyManagementServiceCurrentCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of currently active volume clients. A value of -1 indicates that the machine is not enabled as a KMS or that it has not received any client licensing-requests.

</dd> <dt>

**KeyManagementServiceFailedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the total count of failed KMS requests.

</dd> <dt>

**KeyManagementServiceLicensedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 1 (Licensed).

</dd> <dt>

**KeyManagementServiceMachine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the registered key management service machine name. Returns null if [**SetKeyManagementServiceMachine**](setkeymanagementservicemachine-softwarelicensingservice-vista.md) has not been called.

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

**RequiredClientCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the minimum number of clients required to connect to a KMS machine to enable volume licensing.

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



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| End of client support<br/>    | Windows Vista<br/>                                                             |
| End of server support<br/>    | Windows Server 2008<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>SLWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SLWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](https://msdn.microsoft.com/library/cc534597)
</dt> </dl>

 

 




