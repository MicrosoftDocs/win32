---
Description: Contains information about a trusted domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 83d8e6dc-1170-4226-89b6-99314f3ce6a8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Microsoft\_DomainTrustStatus class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Microsoft\_DomainTrustStatus class

The **Microsoft\_DomainTrustStatus** [WMI class](https://msdn.microsoft.com/library/aa393244) contains information about a trusted domain.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("TrustPrv")]
class Microsoft_DomainTrustStatus
{
  string  TrustedDomain;
  string  FlatName;
  string  SID;
  uint32  TrustDirection;
  uint32  TrustType;
  uint32  TrustAttributes;
  string  TrustedDCName;
  uint32  TrustStatus;
  string  TrustStatusString;
  boolean TrustIsOK = FALSE;
};
```

## Members

The **Microsoft\_DomainTrustStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **Microsoft\_DomainTrustStatus** class has these properties.

<dl> <dt>

**FlatName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Domain name used with systems not connecting using Active Directory.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security identifier for the domain.

</dd> <dt>

**TrustAttributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Attributes can be a combination of the values listed in the following list.

<dt>

<span id="0x1"></span><span id="0X1"></span>

<span id="0x1"></span><span id="0X1"></span>**0x1**


</dt> <dd>

Nontransitive

</dd> <dt>

<span id="0x2"></span><span id="0X2"></span>

<span id="0x2"></span><span id="0X2"></span>**0x2**


</dt> <dd>

Uplevel clients only

</dd> <dt>

<span id="0x40000"></span><span id="0X40000"></span>

<span id="0x40000"></span><span id="0X40000"></span>**0x40000**


</dt> <dd>

Tree parent

</dd> <dt>

<span id="0x80000"></span><span id="0X80000"></span>

<span id="0x80000"></span><span id="0X80000"></span>**0x80000**


</dt> <dd>

Tree root

</dd> </dl>

</dd> <dt>

**TrustDirection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Direction of trust.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Inbound

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Outbound

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Bidirectional

</dd> </dl>

</dd> <dt>

**TrustedDCName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the trusted domain's domain controller.

</dd> <dt>

**TrustedDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Domain name.

</dd> <dt>

**TrustIsOK**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved.

</dd> <dt>

**TrustStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Error code of trust failure. A value of 0 (zero) indicates no failure.

</dd> <dt>

**TrustStatusString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of trust status.

</dd> <dt>

**TrustType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of trust.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Downlevel

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Uplevel

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Kerberos realm

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

DCE

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\microsoftactivedirectory<br/>                                               |
| MOF<br/>                      | <dl> <dt>Trustmon.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Trustmon.dll</dt> </dl> |



## See also

<dl> <dt>

[**Microsoft\_TrustProvider**](microsoft-trustprovider.md)
</dt> <dt>

[**Microsoft\_LocalDomainInfo**](microsoft-localdomaininfo.md)
</dt> <dt>

[Trustmon Provider](trustmon-provider.md)
</dt> </dl>

 

 




