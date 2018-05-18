---
title: MSFT\_ServerInventory class
description: Represents the inventory information of the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '81ed0a53-f85c-4a9b-8f4c-fea1589269e5'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_ServerInventory class", "MSFT_ServerInventory class, described"]
topic_type:
- apiref
api_name:
- MSFT_ServerInventory
- MSFT_ServerInventory.Name
- MSFT_ServerInventory.Description
- MSFT_ServerInventory.Fqdn
- MSFT_ServerInventory.Domain
- MSFT_ServerInventory.IsDomainJoined
- MSFT_ServerInventory.Type
- MSFT_ServerInventory.ProductId
- MSFT_ServerInventory.CeipSetting
- MSFT_ServerInventory.WerSetting
- MSFT_ServerInventory.IsWerSettingEnforcedByGP
- MSFT_ServerInventory.ActivationStatus
- MSFT_ServerInventory.CbsTimestamp
- MSFT_ServerInventory.TotalPhysicalMemory
- MSFT_ServerInventory.Manufacturer
- MSFT_ServerInventory.ProcessorNames
api_location:
- MgmtProvider.dll
api_type:
- DllExport
---

# MSFT\_ServerInventory class

Represents the inventory information of the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerInventory
{
  string   Name;
  string   Description;
  string   Fqdn;
  string   Domain;
  boolean  IsDomainJoined;
  uint8    Type;
  string   ProductId;
  uint8    CeipSetting;
  uint8    WerSetting;
  boolean  IsWerSettingEnforcedByGP;
  uint8    ActivationStatus;
  datetime CbsTimestamp;
  uint64   TotalPhysicalMemory;
  string   Manufacturer;
  string   ProcessorNames[];
};
```

## Members

The **MSFT\_ServerInventory** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerInventory** class has these properties.

<dl> <dt>

**ActivationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The activation status of the server.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Activated"></span><span id="activated"></span><span id="ACTIVATED"></span>

**Activated** (1)


</dt> <dd></dd> <dt>

<span id="Not_Activated"></span><span id="not_activated"></span><span id="NOT_ACTIVATED"></span>

**Not Activated** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**CbsTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp of the last update by Component Based Servicing.

</dd> <dt>

**CeipSetting**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Customer Experience Improvement Program setting on the server.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (1)


</dt> <dd></dd> <dt>

<span id="Disabled_by_Group_Policy"></span><span id="disabled_by_group_policy"></span><span id="DISABLED_BY_GROUP_POLICY"></span>

**Disabled by Group Policy** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Enabled_by_GroupPolicy"></span><span id="enabled_by_grouppolicy"></span><span id="ENABLED_BY_GROUPPOLICY"></span>

**Enabled by GroupPolicy** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the server.

</dd> <dt>

**Domain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The domain name of the server.

</dd> <dt>

**Fqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified domain of the server.

</dd> <dt>

**IsDomainJoined**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Is the server joined to a domain.

</dd> <dt>

**IsWerSettingEnforcedByGP**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Is Windows Error Reporting setting enforced by Group Policy.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The manufacturer of the server.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the server.

</dd> <dt>

**ProcessorNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The names of the processors installed on the server.

</dd> <dt>

**ProductId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The product ID of the server.

</dd> <dt>

**TotalPhysicalMemory**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total physical memory installed on the server.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the server.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Physical"></span><span id="physical"></span><span id="PHYSICAL"></span>

**Physical** (1)


</dt> <dd></dd> <dt>

<span id="Virtual"></span><span id="virtual"></span><span id="VIRTUAL"></span>

**Virtual** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**WerSetting**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Windows Error Reporting setting on the server.

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

 

 





