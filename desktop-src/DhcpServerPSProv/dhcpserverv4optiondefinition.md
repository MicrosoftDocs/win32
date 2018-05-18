---
title: DhcpServerv4OptionDefinition class
description: Dhcp Server v4 Option Definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '22447846-dc98-4c74-9c40-ab2016801949'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4OptionDefinition class", "DhcpServerv4OptionDefinition class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4OptionDefinition
- DhcpServerv4OptionDefinition.OptionId
- DhcpServerv4OptionDefinition.Name
- DhcpServerv4OptionDefinition.Description
- DhcpServerv4OptionDefinition.VendorClass
- DhcpServerv4OptionDefinition.MultiValued
- DhcpServerv4OptionDefinition.Type
- DhcpServerv4OptionDefinition.DefaultValue
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4OptionDefinition class

Dhcp Server v4 Option Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4OptionDefinition
{
  Uint32  OptionId;
  string  Name;
  string  Description;
  string  VendorClass;
  boolean MultiValued;
  string  Type;
  string  DefaultValue[];
};
```

## Members

The **DhcpServerv4OptionDefinition** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4OptionDefinition** class has these properties.

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

<span id="String"></span><span id="string"></span><span id="STRING"></span>

**String** ("String")


</dt> <dd></dd> <dt>

<span id="BinaryData"></span><span id="binarydata"></span><span id="BINARYDATA"></span>

**BinaryData** ("BinaryData")


</dt> <dd></dd> <dt>

<span id="EncapsulatedData"></span><span id="encapsulateddata"></span><span id="ENCAPSULATEDDATA"></span>

**EncapsulatedData** ("EncapsulatedData")


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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





