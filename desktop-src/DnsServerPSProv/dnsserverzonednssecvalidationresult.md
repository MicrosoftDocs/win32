---
title: DnsServerZoneDnsSecValidationResult class
description: Represents a set of results returned by a Domain Name System Security Extensions (DNSSEC) validation operation.
audience: developer
ms.assetid: feffde55-5f38-4441-bea1-8d1166d877d7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerZoneDnsSecValidationResult class
- DnsServerZoneDnsSecValidationResult class, described
topic_type:
- apiref
api_name:
- DnsServerZoneDnsSecValidationResult
- DnsServerZoneDnsSecValidationResult.ZoneName
- DnsServerZoneDnsSecValidationResult.ValidationErrorCode
- DnsServerZoneDnsSecValidationResult.ValidationErrorCodeDescription
- DnsServerZoneDnsSecValidationResult.ExtendedErrorCode
- DnsServerZoneDnsSecValidationResult.ExtendedErrorCodeDescription
- DnsServerZoneDnsSecValidationResult.KeyId
- DnsServerZoneDnsSecValidationResult.SigningKeyPointerString
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerZoneDnsSecValidationResult class

Represents a set of results returned by a Domain Name System Security Extensions (DNSSEC) validation operation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneDnsSecValidationResult
{
  String ZoneName;
  UInt32 ValidationErrorCode;
  String ValidationErrorCodeDescription;
  UInt32 ExtendedErrorCode;
  String ExtendedErrorCodeDescription;
  String KeyId;
  String SigningKeyPointerString;
};
```

## Members

The **DnsServerZoneDnsSecValidationResult** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneDnsSecValidationResult** class has these properties.

<dl> <dt>

**ExtendedErrorCode**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The extended error code for the validation operation.

</dd> <dt>

**ExtendedErrorCodeDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The extended error description for the validation operation.

</dd> <dt>

**KeyId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the key for a validation error.

</dd> <dt>

**SigningKeyPointerString**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The key pointer string for a validation error.

</dd> <dt>

**ValidationErrorCode**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error code from the validation operation.

</dd> <dt>

**ValidationErrorCodeDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error description for the validation operation.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





