---
title: DhcpServerv4OptionValue class
description: Dhcp Server v4 Option Value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12626f0d-ffaf-42f3-8db4-be7d7ce3541f
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4OptionValue class
- DhcpServerv4OptionValue class, described
topic_type:
- apiref
api_name:
- DhcpServerv4OptionValue
- DhcpServerv4OptionValue.OptionId
- DhcpServerv4OptionValue.Type
- DhcpServerv4OptionValue.UserClass
- DhcpServerv4OptionValue.VendorClass
- DhcpServerv4OptionValue.Value
- DhcpServerv4OptionValue.Name
- DhcpServerv4OptionValue.PolicyName
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4OptionValue class

Dhcp Server v4 Option Value.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4OptionValue
{
  Uint32 OptionId;
  string Type;
  string UserClass;
  string VendorClass;
  string Value[];
  string Name;
  string PolicyName;
};
```

## Members

The **DhcpServerv4OptionValue** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4OptionValue** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Option Name corresponding to given option.

</dd> <dt>

**OptionId**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Option identifier(unique) for the given option on Dhcp server

</dd> <dt>

**PolicyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the policy to which this value applies.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Data type for option value stored on Dhcp server

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

**UserClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Class of user to which the above option is applicable.

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Option data corresponding to given option.

</dd> <dt>

**VendorClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Class of vendors to which the above option is applicable.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





