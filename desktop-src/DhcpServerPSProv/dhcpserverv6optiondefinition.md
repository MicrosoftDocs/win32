---
title: DhcpServerv6OptionDefinition class
description: Dhcp Server v6 Option Definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a13f9caf-9a9f-4fb6-950b-e800400201b6
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6OptionDefinition class
- DhcpServerv6OptionDefinition class, described
topic_type:
- apiref
api_name:
- DhcpServerv6OptionDefinition
- DhcpServerv6OptionDefinition.OptionId
- DhcpServerv6OptionDefinition.Name
- DhcpServerv6OptionDefinition.Description
- DhcpServerv6OptionDefinition.VendorClass
- DhcpServerv6OptionDefinition.MultiValued
- DhcpServerv6OptionDefinition.Type
- DhcpServerv6OptionDefinition.DefaultValue
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv6OptionDefinition class

Dhcp Server v6 Option Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6OptionDefinition
{
  Uint32  OptionId;
  string  Name;
  string  Description;
  string  VendorClass;
  boolean MultiValued;
  string  Type;
  string  DefaultValue[];
};
```

## Members

The **DhcpServerv6OptionDefinition** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6OptionDefinition** class has these properties.

<dl> <dt>

**DefaultValue**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Default option data corresponding to given option defn.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description for given option defn on Dhcp server

</dd> <dt>

**MultiValued**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if option defn is multivalued or single valued.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of given option defn on Dhcp server

</dd> <dt>

**OptionId**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Option identifier(unique) for the given option defn on Dhcp server

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Data type for option stored on Dhcp server

<dt>

<span id="Byte"></span><span id="byte"></span><span id="BYTE"></span>

**Byte** ("Byte")


</dt> <dd></dd> <dt>

<span id="Word"></span><span id="word"></span><span id="WORD"></span>

**Word** ("Word")


</dt> <dd></dd> <dt>

<span id="DWord"></span><span id="dword"></span><span id="DWORD"></span>

**DWord** ("DWord")


</dt> <dd></dd> <dt>

<span id="DWordDWord"></span><span id="dworddword"></span><span id="DWORDDWORD"></span>

**DWordDWord** ("DWordDWord")


</dt> <dd></dd> <dt>

<span id="IPv4Address"></span><span id="ipv4address"></span><span id="IPV4ADDRESS"></span>

**IPv4Address** ("IPv4Address")


</dt> <dd></dd> <dt>

<span id="StringData"></span><span id="stringdata"></span><span id="STRINGDATA"></span>

**StringData** ("StringData")


</dt> <dd></dd> <dt>

<span id="BinaryData"></span><span id="binarydata"></span><span id="BINARYDATA"></span>

**BinaryData** ("BinaryData")


</dt> <dd></dd> <dt>

<span id="EncapsulatedData"></span><span id="encapsulateddata"></span><span id="ENCAPSULATEDDATA"></span>

**EncapsulatedData** ("EncapsulatedData")


</dt> <dd></dd> <dt>

<span id="IPv6Address"></span><span id="ipv6address"></span><span id="IPV6ADDRESS"></span>

**IPv6Address** ("IPv6Address")


</dt> <dd></dd> </dl>

</dd> <dt>

**VendorClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Class of vendors to which the above option defn is applicable.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





