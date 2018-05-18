---
title: MSFT\_ServerNetworkAdapter class
description: Represent an installed network adapter on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4c95c84-2d44-43a6-ad9a-15ccc42bed32'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_ServerNetworkAdapter class", "MSFT_ServerNetworkAdapter class, described"]
topic_type:
- apiref
api_name:
- MSFT_ServerNetworkAdapter
- MSFT_ServerNetworkAdapter.Name
- MSFT_ServerNetworkAdapter.ConnectionStatus
- MSFT_ServerNetworkAdapter.DHCPEnabled
- MSFT_ServerNetworkAdapter.Addresses
api_location:
- MgmtProvider.dll
api_type:
- DllExport
---

# MSFT\_ServerNetworkAdapter class

Represent an installed network adapter on the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerNetworkAdapter
{
  string  Name;
  uint16  ConnectionStatus;
  boolean DHCPEnabled;
  string  Addresses[];
};
```

## Members

The **MSFT\_ServerNetworkAdapter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerNetworkAdapter** class has these properties.

<dl> <dt>

**Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP addresses mapped to the network adapter.

</dd> <dt>

**ConnectionStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The connection status of the network adapter.

<dt>

<span id="Disconnected"></span><span id="disconnected"></span><span id="DISCONNECTED"></span>

**Disconnected** (0)


</dt> <dd></dd> <dt>

<span id="Connecting"></span><span id="connecting"></span><span id="CONNECTING"></span>

**Connecting** (1)


</dt> <dd></dd> <dt>

<span id="Connected"></span><span id="connected"></span><span id="CONNECTED"></span>

**Connected** (2)


</dt> <dd></dd> <dt>

<span id="Disconnecting"></span><span id="disconnecting"></span><span id="DISCONNECTING"></span>

**Disconnecting** (3)


</dt> <dd></dd> <dt>

<span id="Hardware_not_present"></span><span id="hardware_not_present"></span><span id="HARDWARE_NOT_PRESENT"></span>

**Hardware not present** (4)


</dt> <dd></dd> <dt>

<span id="Hardware_disabled"></span><span id="hardware_disabled"></span><span id="HARDWARE_DISABLED"></span>

**Hardware disabled** (5)


</dt> <dd></dd> <dt>

<span id="Hardware_malfunction"></span><span id="hardware_malfunction"></span><span id="HARDWARE_MALFUNCTION"></span>

**Hardware malfunction** (6)


</dt> <dd></dd> <dt>

<span id="Media_disconnected"></span><span id="media_disconnected"></span><span id="MEDIA_DISCONNECTED"></span>

**Media disconnected** (7)


</dt> <dd></dd> <dt>

<span id="Authenticating"></span><span id="authenticating"></span><span id="AUTHENTICATING"></span>

**Authenticating** (8)


</dt> <dd></dd> <dt>

<span id="Authentication_succeeded"></span><span id="authentication_succeeded"></span><span id="AUTHENTICATION_SUCCEEDED"></span>

**Authentication succeeded** (9)


</dt> <dd></dd> <dt>

<span id="Authentication_failed"></span><span id="authentication_failed"></span><span id="AUTHENTICATION_FAILED"></span>

**Authentication failed** (10)


</dt> <dd></dd> <dt>

<span id="Invalid_address"></span><span id="invalid_address"></span><span id="INVALID_ADDRESS"></span>

**Invalid address** (11)


</dt> <dd></dd> <dt>

<span id="Credentials_required"></span><span id="credentials_required"></span><span id="CREDENTIALS_REQUIRED"></span>

**Credentials required** (12)


</dt> <dd></dd> </dl>

</dd> <dt>

**DHCPEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Is IP address assigned by Dynamic Host Configuration Protocol (DHCP).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the network adapter.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetServerInventory method of MSFT\_ServerManagerTasks**](getserverinventory-msft-servermanagertasks.md)
</dt> </dl>

 

 





