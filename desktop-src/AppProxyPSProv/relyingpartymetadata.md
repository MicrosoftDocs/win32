---
Description: Retrieves metadata for a relying party.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77058c18-5cc0-477e-b25f-cbdaadfebdc2
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RelyingPartyMetadata class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RelyingPartyMetadata class

Retrieves metadata for a relying party.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("AppProxyPSProvider"), AMENDMENT]
class RelyingPartyMetadata
{
  string  Name;
  string  ID;
  boolean Published;
  boolean IWA;
  boolean NonClaimsAware;
  boolean Enabled;
};
```

## Members

The **RelyingPartyMetadata** class has these types of members:

-   [Properties](#properties)

### Properties

The **RelyingPartyMetadata** class has these properties.

<dl> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the relying party is enabled. **True** if the relying party is enabled; otherwise, **False**.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ID of the relying party.

</dd> <dt>

**IWA**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported starting with Windows Server 2016.

**Windows Server 2012 R2:** Indicates whether the relying party uses Integrated Windows Authentication (IWA). **True** if the relying party uses IWA; otherwise, **False**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the relying party.

</dd> <dt>

**NonClaimsAware**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the relying party is non claims aware. **True** if the relying party is non claims aware; otherwise, **False**.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**Published**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the relying party is a published application. **True** if it is published; otherwise, **False**.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[Application Proxy WMI Provider Reference](application-proxy-wmi-provider-reference.md)
</dt> </dl>

 

 




