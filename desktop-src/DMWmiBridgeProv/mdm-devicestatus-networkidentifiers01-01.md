---
title: MDM_DeviceStatus_NetworkIdentifiers01_01 class
description: The MDM\_DeviceStatus\_NetworkIdentifiers01\_01 class allows you to query a device for network properties.
ms.assetid: 2439010e-62fa-4482-b280-b9f98d1fbb7b
keywords:
- MDM_DeviceStatus_NetworkIdentifiers01_01 class
- MDM_DeviceStatus_NetworkIdentifiers01_01 class, described
topic_type:
- apiref
api_name:
- MDM_DeviceStatus_NetworkIdentifiers01_01
- MDM_DeviceStatus_NetworkIdentifiers01_01.InstanceID
- MDM_DeviceStatus_NetworkIdentifiers01_01.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_DeviceStatus\_NetworkIdentifiers01\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_DeviceStatus\_NetworkIdentifiers01\_01** class allows you to query a device for network properties.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_DeviceStatus_NetworkIdentifiers01_01
{
  string  InstanceID;
  string  ParentID;
  string  IPAddressV4;
  string  IPAddressV6;
  boolean IsConnected;
  sint32  Type;
};
```

## Members

The **MDM\_DeviceStatus\_NetworkIdentifiers01\_01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_DeviceStatus\_NetworkIdentifiers01\_01** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Node for queries on network and device properties.

</dd> <dt>

[IPAddressV4](/windows/client-management/mdm/devicestatus-csp#devicestatus-networkidentifiers-macaddress-ipaddressv4)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[IPAddressV6](/windows/client-management/mdm/devicestatus-csp#devicestatus-networkidentifiers-macaddress-ipaddressv6)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[IsConnected](/windows/client-management/mdm/devicestatus-csp#devicestatus-networkidentifiers-macaddress-isconnected)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/DeviceStatus"

</dd> <dt>

[Type](/windows/client-management/mdm/devicestatus-csp#devicestatus-networkidentifiers-macaddress-type)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

