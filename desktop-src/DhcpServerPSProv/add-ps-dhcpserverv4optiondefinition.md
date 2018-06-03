---
title: Add method of the PS\_DhcpServerv4OptionDefinition class
description: Adds a new DHCPv4 option definition on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ac036dc8-4e83-4f48-b7cb-c5ecc3f1ae2b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv4OptionDefinition class
- PS_DhcpServerv4OptionDefinition class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionDefinition.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DhcpServerv4OptionDefinition class

Adds a new DHCPv4 option definition on the server.

## Syntax


```mof
uint32 Add(
  [in]  string                       ComputerName,
  [in]  string                       Name,
  [in]  string                       Description,
  [in]  uint32                       OptionId,
  [in]  string                       Type,
  [in]  boolean                      MultiValued,
  [in]  string                       VendorClass,
  [in]  string                       DefaultValue[],
  [in]  boolean                      PassThru,
  [out] DhcpServerv4OptionDefinition cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the DHCPv4 option

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description of the option definition being added

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

The numerical identifier of the option \[1-255\]

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The data type of the values for this option. Valid values are {Byte \| Word \| DWord \| DWordDword \| IPAddress \| String \| BinaryData \| EncapsulatedData \| IPv6Address}

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


</dt> <dd></dd> </dl> </dd> <dt>

*MultiValued* \[in\]
</dt> <dd>

This true if the option definition allows for multiple values.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, adds the Option Definition for the specified vendor Class

</dd> <dt>

*DefaultValue* \[in\]
</dt> <dd>

The default value for the option for which a definition is created. The syntax to specify the default value for the option are as follows: 1) Byte, Word, DWord, DWordDword (these can be specified as decimal or hexadecimal string); 2) IPAddress, IPv6Address (these can be specified as IP address string); 3) String (this can be specified as string); 4) BinaryData, EncapsulatedData (these can be specified as hexadecimal string)

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4OptionDefinition**](dhcpserverv4optiondefinition.md) class.

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

[**PS\_DhcpServerv4OptionDefinition**](ps-dhcpserverv4optiondefinition.md)
</dt> </dl>

 

 





