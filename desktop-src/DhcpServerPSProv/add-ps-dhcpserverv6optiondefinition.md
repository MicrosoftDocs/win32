---
title: Add method of the PS\_DhcpServerv6OptionDefinition class
description: Adds a DHCPv6 option definition to a DHCP Server running on local or remote computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6a38b505-d16d-453f-a0dc-1149bcc30f0e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv6OptionDefinition class
- PS_DhcpServerv6OptionDefinition class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionDefinition.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerv6OptionDefinition class

Adds a DHCPv6 option definition to a DHCP Server running on local or remote computer.

## Syntax


```mof
uint32 Add(
  [in]  string                       ComputerName,
  [in]  uint32                       OptionId,
  [in]  string                       Type,
  [in]  string                       Name,
  [in]  boolean                      MultiValued,
  [in]  string                       Description,
  [in]  string                       VendorClass,
  [in]  string                       DefaultValue[],
  [in]  boolean                      PassThru,
  [out] DhcpServerv6OptionDefinition cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

Integer identifier for the option.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The data type of the option. The type can be Byte, Word, DWord, DWordDword, IPAddress, String, BinaryData, EncapsulatedData, IPv6Address.

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


</dt> <dd></dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the option definition.

</dd> <dt>

*MultiValued* \[in\]
</dt> <dd>

If specified, the option will allows multiple values to be specified.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the option definition.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, adds the option definition only for the specified vendor class.

</dd> <dt>

*DefaultValue* \[in\]
</dt> <dd>

Default value for the option. If the type of the option is Byte, Word, DWord, DWordDword, the default value must be specified as decimal or hexadecimal string(s). If the type of the option is IPAddress, IPv6Address, the default value must be specified as an IP address string. If the type of the option is String, the default value must be specified as an IP address string. If the type of the option is BinaryData, EncapsulatedData, the default value must be specified as an hexadecimal string.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6OptionDefinition**](dhcpserverv6optiondefinition.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv6OptionDefinition**](ps-dhcpserverv6optiondefinition.md)
</dt> </dl>

 

 





