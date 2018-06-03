---
title: DhcpServerv4Policy class
description: Dhcp Server v4Policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ae73ff0-3fc5-43eb-88d8-3148abcf4d7f
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4Policy class
- DhcpServerv4Policy class, described
topic_type:
- apiref
api_name:
- DhcpServerv4Policy
- DhcpServerv4Policy.Name
- DhcpServerv4Policy.Description
- DhcpServerv4Policy.ScopeId
- DhcpServerv4Policy.Enabled
- DhcpServerv4Policy.Condition
- DhcpServerv4Policy.ProcessingOrder
- DhcpServerv4Policy.VendorClass
- DhcpServerv4Policy.UserClass
- DhcpServerv4Policy.MacAddress
- DhcpServerv4Policy.ClientId
- DhcpServerv4Policy.RelayAgent
- DhcpServerv4Policy.CircuitId
- DhcpServerv4Policy.RemoteId
- DhcpServerv4Policy.SubscriberId
- DhcpServerv4Policy.LeaseDuration
- DhcpServerv4Policy.Fqdn
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4Policy class

Dhcp Server v4Policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Policy
{
  string   Name;
  string   Description;
  string   ScopeId;
  boolean  Enabled;
  string   Condition;
  uint16   ProcessingOrder;
  string   VendorClass[];
  string   UserClass[];
  string   MacAddress[];
  string   ClientId[];
  string   RelayAgent[];
  string   CircuitId[];
  string   RemoteId[];
  string   SubscriberId[];
  Datetime LeaseDuration;
  string   Fqdn[];
};
```

## Members

The **DhcpServerv4Policy** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Policy** class has these properties.

<dl> <dt>

**CircuitId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare CircuitId with

</dd> <dt>

**ClientId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare ClientId with

</dd> <dt>

**Condition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether Policy rules are logically combined with an 'And' or an 'Or'

<dt>

<span id="And"></span><span id="and"></span><span id="AND"></span>

**And** ("And")


</dt> <dd></dd> <dt>

<span id="Or"></span><span id="or"></span><span id="OR"></span>

**Or** ("Or")


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the Dhcp Policy

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the policy is enabled or not

</dd> <dt>

**Fqdn**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare with Fqdn.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**LeaseDuration**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lease duration to be set for clients matching the policy.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**MacAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare MacAddress with

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Unique name of the Dhcp Policy

</dd> <dt>

**ProcessingOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Processing order of the Dhcp Policy

</dd> <dt>

**RelayAgent**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare RelayAgent with

</dd> <dt>

**RemoteId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare RemoteId with

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If specified, indicates the Scope for which the Policy exists. If not specified, indicates a Policy at the Server level.

</dd> <dt>

**SubscriberId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare SubscriberId with

</dd> <dt>

**UserClass**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare UserClass with

</dd> <dt>

**VendorClass**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The comparator to use, and values to compare VendorClass with

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





