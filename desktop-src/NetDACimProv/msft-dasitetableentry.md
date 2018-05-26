---
Description: An entry in the DirectAccess site table.
ms.assetid: addf51a2-380f-4407-9fbe-0ce6df48b058
title: MSFT\_DASiteTableEntry class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_DASiteTableEntry class

An entry in the DirectAccess site table.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetDACim")]
class MSFT_DASiteTableEntry : MSFT_NetSettingData
{
  string PolicyStore;
  string EntryPointName;
  uint32 State;
  string ADSite;
  string EntryPointRange[];
  string TeredoServerIP;
  string EntryPointIPAddress;
  string IPHttpsProfile;
  string GslbIP;
};
```

## Members

The **MSFT\_DASiteTableEntry** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DASiteTableEntry** class has these methods.



| Method                                           | Description                                                                       |
|:-------------------------------------------------|:----------------------------------------------------------------------------------|
| [**Disable**](disable-msft-dasitetableentry.md) | Turns off manual site selection for DirectAccess.<br/>                      |
| [**Enable**](enable-msft-dasitetableentry.md)   | Turns on manual site selection for DirectAccess.<br/>                       |
| [**Rename**](rename-msft-dasitetableentry.md)   | Renames an entry in the DirectAccess site table.<br/>                       |
| [**Reset**](reset-msft-dasitetableentry.md)     | Resets the configuration of the entry in the Direct Access site table.<br/> |



 

### Properties

The **MSFT\_DASiteTableEntry** class has these properties.

<dl> <dt>

**ADSite**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the Active Directory site that the client uses.

</dd> <dt>

**EntryPointIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the DirectAccess server.

</dd> <dt>

**EntryPointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name of the site.

</dd> <dt>

**EntryPointRange**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPv6 address ranges attributed to a DirectAccess site

</dd> <dt>

**GslbIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address that the DirectAccess client uses to identify which site to use based on GSLB resolution.

</dd> <dt>

**IPHttpsProfile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of IP-HTTPs profile that you want to enable for this site.

</dd> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The policy store that stores this configuration object.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current activation state of the site.

<dl><span id="NotSelected"></span><span id="notselected"></span><span id="NOTSELECTED"></span><dt>

**NotSelected**
</dt><span id="AutomaticallySelected"></span><span id="automaticallyselected"></span><span id="AUTOMATICALLYSELECTED"></span><dt>

**AutomaticallySelected**
</dt><span id="ManuallySelected"></span><span id="manuallyselected"></span><span id="MANUALLYSELECTED"></span><dt>

**ManuallySelected**
</dt> </dl>

</dd> <dt>

**TeredoServerIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Teredo server that the client uses.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetDACim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetDACim.dll</dt> </dl> |



 

 




