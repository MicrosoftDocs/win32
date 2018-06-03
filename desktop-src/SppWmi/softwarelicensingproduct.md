---
title: SoftwareLicensingProduct class
description: This class exposes the product-specific properties and methods of the Software Licensing service.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d5f8b2e7-25cf-4a08-a4b0-c4256f85203f
keywords:
- SoftwareLicensingProduct class Windows Management Instrumentation
- SoftwareLicensingProduct class Windows Management Instrumentation , described
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct
- SoftwareLicensingProduct.ID
- SoftwareLicensingProduct.Name
- SoftwareLicensingProduct.Description
- SoftwareLicensingProduct.ApplicationID
- SoftwareLicensingProduct.ProcessorURL
- SoftwareLicensingProduct.MachineURL
- SoftwareLicensingProduct.ProductKeyURL
- SoftwareLicensingProduct.UseLicenseURL
- SoftwareLicensingProduct.LicenseStatus
- SoftwareLicensingProduct.LicenseStatusReason
- SoftwareLicensingProduct.GracePeriodRemaining
- SoftwareLicensingProduct.EvaluationEndDate
- SoftwareLicensingProduct.OfflineInstallationId
- SoftwareLicensingProduct.PartialProductKey
- SoftwareLicensingProduct.ProductKeyID
- SoftwareLicensingProduct.LicenseFamily
- SoftwareLicensingProduct.LicenseDependsOn
- SoftwareLicensingProduct.LicenseIsAddon
- SoftwareLicensingProduct.VLActivationInterval
- SoftwareLicensingProduct.VLRenewalInterval
- SoftwareLicensingProduct.KeyManagementServiceProductKeyID
- SoftwareLicensingProduct.KeyManagementServiceMachine
- SoftwareLicensingProduct.KeyManagementServicePort
- SoftwareLicensingProduct.DiscoveredKeyManagementServiceMachineName
- SoftwareLicensingProduct.DiscoveredKeyManagementServiceMachinePort
- SoftwareLicensingProduct.IsKeyManagementServiceMachine
- SoftwareLicensingProduct.KeyManagementServiceCurrentCount
- SoftwareLicensingProduct.RequiredClientCount
- SoftwareLicensingProduct.KeyManagementServiceUnlicensedRequests
- SoftwareLicensingProduct.KeyManagementServiceLicensedRequests
- SoftwareLicensingProduct.KeyManagementServiceOOBGraceRequests
- SoftwareLicensingProduct.KeyManagementServiceOOTGraceRequests
- SoftwareLicensingProduct.KeyManagementServiceNonGenuineGraceRequests
- SoftwareLicensingProduct.KeyManagementServiceTotalRequests
- SoftwareLicensingProduct.KeyManagementServiceFailedRequests
- SoftwareLicensingProduct.KeyManagementServiceNotificationRequests
- SoftwareLicensingProduct.GenuineStatus
- SoftwareLicensingProduct.ExtendedGrace
- SoftwareLicensingProduct.TokenActivationILID
- SoftwareLicensingProduct.TokenActivationILVID
- SoftwareLicensingProduct.TokenActivationGrantNumber
- SoftwareLicensingProduct.TokenActivationCertificateThumbprint
- SoftwareLicensingProduct.TokenActivationAdditionalInfo
- SoftwareLicensingProduct.TrustedTime
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

# SoftwareLicensingProduct class

This class exposes the product-specific properties and methods of the Software Licensing service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class SoftwareLicensingProduct
{
  string   ID;
  string   Name;
  string   Description;
  string   ApplicationID;
  string   ProcessorURL;
  string   MachineURL;
  string   ProductKeyURL;
  string   UseLicenseURL;
  uint32   LicenseStatus;
  uint32   LicenseStatusReason;
  uint32   GracePeriodRemaining;
  datetime EvaluationEndDate;
  string   OfflineInstallationId;
  string   PartialProductKey;
  string   ProductKeyID;
  string   LicenseFamily;
  string   LicenseDependsOn;
  boolean  LicenseIsAddon;
  uint32   VLActivationInterval;
  uint32   VLRenewalInterval;
  string   KeyManagementServiceProductKeyID;
  string   KeyManagementServiceMachine;
  uint32   KeyManagementServicePort;
  string   DiscoveredKeyManagementServiceMachineName;
  uint32   DiscoveredKeyManagementServiceMachinePort;
  uint32   IsKeyManagementServiceMachine;
  uint32   KeyManagementServiceCurrentCount;
  uint32   RequiredClientCount;
  uint32   KeyManagementServiceUnlicensedRequests;
  uint32   KeyManagementServiceLicensedRequests;
  uint32   KeyManagementServiceOOBGraceRequests;
  uint32   KeyManagementServiceOOTGraceRequests;
  uint32   KeyManagementServiceNonGenuineGraceRequests;
  uint32   KeyManagementServiceTotalRequests;
  uint32   KeyManagementServiceFailedRequests;
  uint32   KeyManagementServiceNotificationRequests;
  uint32   GenuineStatus;
  uint32   ExtendedGrace;
  string   TokenActivationILID;
  uint32   TokenActivationILVID;
  uint32   TokenActivationGrantNumber;
  string   TokenActivationCertificateThumbprint;
  string   TokenActivationAdditionalInfo;
  datetime TrustedTime;
};
```

## Members

The **SoftwareLicensingProduct** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SoftwareLicensingProduct** class has these methods.



| Method                                                                                                | Description                                                                                                                                |
|:------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Activate**](activate-softwarelicensingproduct.md)                                                 | Activates the product.<br/>                                                                                                          |
| [**ClearKeyManagementServiceMachine**](clearkeymanagementservicemachine-softwarelicensingproduct.md) | Clears any previously configured KMS host name.<br/>                                                                                 |
| [**ClearKeyManagementServicePort**](clearkeymanagementserviceport-softwarelicensingproduct.md)       | Clears any previously specified port number.<br/>                                                                                    |
| [**DepositOfflineConfirmationId**](depositofflineconfirmationid-softwarelicensingproduct.md)         | Activates the product by depositing an Offline Confirmation Identifier for this product when performing a telephone activation.<br/> |
| [**DepositTokenActivationResponse**](deposittokenactivationresponse-softwarelicensingproduct.md)     | Deposits a token-based activation response.<br/>                                                                                     |
| [**GenerateTokenActivationChallenge**](generatetokenactivationchallenge-softwarelicensingproduct.md) | Returns a token-based activation challenge.<br/>                                                                                     |
| [**GetPolicyInformationDWord**](getpolicyinformationdword-softwarelicensingproduct.md)               | Gets the license policy information of type DWORD.<br/>                                                                              |
| [**GetPolicyInformationString**](getpolicyinformationstring-softwarelicensingproduct.md)             | Gets the license policy information of type string.<br/>                                                                             |
| [**GetTokenActivationGrants**](gettokenactivationgrants-softwarelicensingproduct.md)                 | Returns token-based activation grants.<br/>                                                                                          |
| [**SetKeyManagementServiceMachine**](setkeymanagementservicemachine-softwarelicensingproduct.md)     | Sets the KMS host name for volume activation.<br/>                                                                                   |
| [**SetKeyManagementServicePort**](setkeymanagementserviceport-softwarelicensingproduct.md)           | Sets the TCP port used by a client to make requests of a KMS host. If not specified, port 1688 is used.<br/>                         |
| [**UninstallProductKey**](uninstallproductkey-softwarelicensingproduct.md)                           | Uninstalls the product key.<br/>                                                                                                     |



 

### Properties

The **SoftwareLicensingProduct** class has these properties.

<dl> <dt>

**ApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the ID of current product application.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product description.

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

**EvaluationEndDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the expiration date of this product application. After this date, the **LicenseStatus** property is set to Unlicensed and cannot be activated.

</dd> <dt>

**ExtendedGrace**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the extended grace time, in minutes, before the parent application goes into notification mode.

</dd> <dt>

**GenuineStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the genuine status for the product application.

</dd> <dt>

**GracePeriodRemaining**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the remaining time, in minutes, before the parent application goes into notification mode. For volume clients, this is the remaining time before reactivation is required.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Specifies the product identifier.

</dd> <dt>

**IsKeyManagementServiceMachine**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether KMS is enabled on the computer. The following values are possible.



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

Specifies the count of currently active KMS clients on the KMS host. A value of -1 indicates the host is not enabled as a KMS or that it has not received any client-licensing requests.

</dd> <dt>

**KeyManagementServiceFailedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of failed KMS requests.

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

Specifies the name of the KMS host. Returns **null** if [**SetKeyManagementServiceMachine**](setkeymanagementservicemachine-softwarelicensingproduct.md) has not been called.

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

**KeyManagementServicePort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the TCP port that is used by clients to send KMS-activation requests. Returns 0 if [**SetKeyManagementServicePort**](setkeymanagementserviceport-softwarelicensingproduct.md) has not been called.

</dd> <dt>

**KeyManagementServiceProductKeyID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the KMS product key ID. Returns **null** if it is not applicable.

</dd> <dt>

**KeyManagementServiceTotalRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of valid KMS requests.

</dd> <dt>

**KeyManagementServiceUnlicensedRequests**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the count of KMS requests from clients with **LicenseStatus** set to 0 (Unlicensed).

</dd> <dt>

**LicenseDependsOn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the dependency identifier for the set of SKUs used to determine license relationships for add-ons.

</dd> <dt>

**LicenseFamily**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the group identifier for the SKU used to determine license relationships for add-ons.

</dd> <dt>

**LicenseIsAddon**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates **TRUE** if the product is identified as an add-on license.

</dd> <dt>

**LicenseStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the license status of this product application. The following values are possible.



| Value                            | Description                |
|----------------------------------|----------------------------|
| <span id="0"></span>0<br/> | Unlicensed<br/>      |
| <span id="1"></span>1<br/> | Licensed<br/>        |
| <span id="2"></span>2<br/> | OOBGrace<br/>        |
| <span id="3"></span>3<br/> | OOTGrace<br/>        |
| <span id="4"></span>4<br/> | NonGenuineGrace<br/> |
| <span id="5"></span>5<br/> | Notification<br/>    |
| <span id="6"></span>6<br/> | ExtendedGrace<br/>   |



 

</dd> <dt>

**LicenseStatusReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the license status. Provides additional information about why a computer is in a specific licensing state.

</dd> <dt>

**MachineURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the binding certificate.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product name.

</dd> <dt>

**OfflineInstallationId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the offline installation identifier of this product application. Used for offline activation. Returns a **null** value if a product key is not installed.

</dd> <dt>

**PartialProductKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the last five characters of the product key. Returns a **null** value if a product key is not installed.

</dd> <dt>

**ProcessorURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the process certificate.

</dd> <dt>

**ProductKeyID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product key ID. Returns a **null** value if a product key is not installed.

</dd> <dt>

**ProductKeyURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the product certificate.

</dd> <dt>

**RequiredClientCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the minimum number of clients that are required to connect to a KMS host to enable volume licensing.

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

Specifies the thumbprint of the certificate that activated the product.

</dd> <dt>

**TokenActivationGrantNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the grant number in the token-based activation license that activated the product.

</dd> <dt>

**TokenActivationILID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the ID of the token-based activation license that activated the product.

</dd> <dt>

**TokenActivationILVID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the version of the token-based activation license that activated the product.

</dd> <dt>

**TrustedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the trusted time for the product.

</dd> <dt>

**UseLicenseURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the user license.

</dd> <dt>

**VLActivationInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the frequency, in minutes, of how often a client will contact the KMS host before the product is licensed.

</dd> <dt>

**VLRenewalInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the frequency, in minutes, of how often a client will contact the KMS host after the product is licensed.

</dd> </dl>

## Examples

For a longer discussion of accessing the **SoftwareLicensingProduct** class with PowerShell, see the [Scripting Guy blog entry](http://blogs.technet.com/b/heyscriptingguy/archive/2014/09/08/use-powershell-to-detect-activation-status.aspx).

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

 

 





