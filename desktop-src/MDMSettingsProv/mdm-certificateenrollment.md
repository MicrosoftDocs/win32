---
title: MDM\_CertificateEnrollment class
description: Represents a Certificate Enrollment used in the Simple Certificate Enrollment Protocol (SCEP).
ms.assetid: 6eb73c81-5161-4332-8178-a42662cacf59
keywords:
- MDM_CertificateEnrollment class MDM Settings
- MDM_CertificateEnrollment class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_CertificateEnrollment
- MDM_CertificateEnrollment.RequestID
- MDM_CertificateEnrollment.StoreLocation
- MDM_CertificateEnrollment.EnhancedKeyUsages
- MDM_CertificateEnrollment.Issuers
- MDM_CertificateEnrollment.Status
- MDM_CertificateEnrollment.Error
- MDM_CertificateEnrollment.ExpirationThreshold
- MDM_CertificateEnrollment.SubjectName
- MDM_CertificateEnrollment.SubjectAlternativeNames
- MDM_CertificateEnrollment.Thumbprint
- MDM_CertificateEnrollment.SerialNumber
- MDM_CertificateEnrollment.ValidFrom
- MDM_CertificateEnrollment.ValidTo
- MDM_CertificateEnrollment.ConfigurationParameters
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_CertificateEnrollment class

Represents a Certificate Enrollment used in the Simple Certificate Enrollment Protocol (SCEP).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_CertificateEnrollment
{
  string   RequestID;
  uint8    StoreLocation;
  string   EnhancedKeyUsages;
  string   Issuers;
  uint32   Status;
  uint32   Error;
  uint32   ExpirationThreshold;
  string   SubjectName;
  string   SubjectAlternativeNames;
  string   Thumbprint;
  string   SerialNumber;
  datetime ValidFrom;
  datetime ValidTo;
  string   ConfigurationParameters;
};
```

## Members

The **MDM\_CertificateEnrollment** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_CertificateEnrollment** class has these properties.

<dl> <dt>

**ConfigurationParameters**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The XML blob containing static attributes like Issuer Name, SCEP URL, and Retries, that will be used by the client for the SCEP calls to Network Device Enrollment Service (NDES).

</dd> <dt>

**EnhancedKeyUsages**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The certificate selection criteria Enhanced Key Usages (EKU), delimited with commas. Matching on all specified EKUs.

</dd> <dt>

**Error**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detailed enrollment request error. Valid if the **Status** property is **EnrollError**.

</dd> <dt>

**ExpirationThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The certificate expiration threshold in days.

</dd> <dt>

**Issuers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The certificate selection criteria Issuer subject names, delimited with the "\|" (vertical bar) character. Names are case-sensitive and matched on individual issuers.

</dd> <dt>

**RequestID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the enrollment certificate request.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The serial number of the issued certificate.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a certificate matching the enrollment request criteria is issued.

</dd> <dt>

**StoreLocation**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The certificate store location.

Possible values are.

<dt>

<span id="1"></span>

**1** (ContextUser)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (ContextMachine)


</dt> <dd></dd> </dl>

</dd> <dt>

**SubjectAlternativeNames**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subject alternative names of the issued certificate with a separator bar as delimiter.

</dd> <dt>

**SubjectName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subject name of the issued certificate.

</dd> <dt>

**Thumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The thumbprint of the issued certificate.

</dd> <dt>

**ValidFrom**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Valid from date of the issued certificate.

</dd> <dt>

**ValidTo**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Valid to date of the issued certificate.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





