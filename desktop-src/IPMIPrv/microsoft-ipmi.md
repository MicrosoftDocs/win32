---
title: Microsoft\_IPMI class
description: Contains methods which issue commands to a device that has an implementation of IPMI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '525f8cc6-9d5b-4370-9a24-e49ec5424258'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WMI IPMI driver class", "IPMI driver WS-Management", "Microsoft_IPMI class", "Microsoft_IPMI class, described"]
topic_type:
- apiref
api_name:
- Microsoft_IPMI
- Root\wmi.Microsoft_IPMI.BMCAddress
- Root\wmi.Microsoft_IPMI.InstanceName
api_location:
- IpmiDrv.sys
api_type:
- DllExport
---

# Microsoft\_IPMI class

The **Microsoft\_IPMI** class contains methods which issue commands to a device that has an implementation of IPMI. The use of this Windows Driver Model (WDM) class is not required for client scripts to obtain Microsoft IPMI data. Use the [IPMI Provider](ipmi-provider.md) classes instead.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("WMIProv"), Dynamic]
class Microsoft_IPMI
{
  uint8  BMCAddress;
  string InstanceName;
};
```

## Members

The **Microsoft\_IPMI** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Microsoft\_IPMI** class has these methods.



| Method                                                        | Description                                                                                                                                                  |
|:--------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestResponse**](microsoft-ipmi-requestresponse.md)     | Sends a request for data from an IPMI provider to the IPMI driver.<br/>                                                                                |
| [**RequestResponseEx**](microsoft-ipmi-requestresponseex.md) | Extended version of [**RequestResponse**](microsoft-ipmi-requestresponse.md). Sends a request for data from an IPMI provider to the IPMI driver.<br/> |
| [**SMS\_Attention**](microsoft-ipmi-sms-attention.md)        | Obtains the value of the IPMI status register.<br/>                                                                                                    |



 

### Properties

The **Microsoft\_IPMI** class has these properties.

<dl> <dt>

**BMCAddress**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Hardware address of the BMC associated with the server.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

BMC name.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| DLL<br/>                      | <dl> <dt>IpmiDrv.sys</dt> </dl> |



## See also

<dl> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 





