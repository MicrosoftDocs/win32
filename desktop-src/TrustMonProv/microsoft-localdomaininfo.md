---
Description: Provides information about the domain on which this instance of the trust monitor is running.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 096cc27f-e150-4808-b225-32f45160eba1
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Microsoft\_LocalDomainInfo class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Microsoft\_LocalDomainInfo class

The **Microsoft\_LocalDomainInfo** Windows Management Instrumentation (WMI) class provides information about the domain on which this instance of the trust monitor is running.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[singleton, dynamic, provider("TrustPrv")]
class Microsoft_LocalDomainInfo
{
  string DNSname;
  string FlatName;
  string SID;
  string TreeName;
  string DCname;
};
```

## Members

The **Microsoft\_LocalDomainInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Microsoft\_LocalDomainInfo** class has these properties.

<dl> <dt>

**DCname**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the domain controller on which TrustMon is running.

</dd> <dt>

**DNSname**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DNS name of the local domain.

</dd> <dt>

**FlatName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SAM name of the local domain.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security identifier (SID) of the local domain.

</dd> <dt>

**TreeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the enterprise tree root.

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

[**Microsoft\_DomainTrustStatus**](microsoft-domaintruststatus.md)
</dt> <dt>

[**Microsoft\_TrustProvider**](microsoft-trustprovider.md)
</dt> <dt>

[Trustmon Provider](trustmon-provider.md)
</dt> <dt>

[Retrieving a Class](https://msdn.microsoft.com/library/aa393244)
</dt> </dl>

 

 




