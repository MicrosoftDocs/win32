---
title: DACertificateContext class
description: Defines the DirectAccess certificate context object.
audience: developer
ms.assetid: 'c832c888-e512-43de-b900-9685357e775a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DACertificateContext class", "DACertificateContext class, described"]
topic_type:
- apiref
api_name:
- DACertificateContext
- DACertificateContext.EncodedCertificate
- DACertificateContext.PrivateKeyExists
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# DACertificateContext class

Defines the DirectAccess certificate context object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class DACertificateContext
{
  uint8   EncodedCertificate[];
  boolean PrivateKeyExists;
};
```

## Members

The **DACertificateContext** class has these types of members:

-   [Properties](#properties)

### Properties

The **DACertificateContext** class has these properties.

<dl> <dt>

**EncodedCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The encoded certificate byte blob.

</dd> <dt>

**PrivateKeyExists**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Private key for the certificate exists.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





