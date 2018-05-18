---
Description: 'Represents a virtualization policy record, which maps virtual addressees to physical address in the WNV module to implement Hyper-V network virtualization.'
ms.assetid: '0f8b983c-000c-4d17-8da3-24a00654ae6a'
title: 'MSFT\_NetVirtualizationLookupRecordSettingData class'
---

# MSFT\_NetVirtualizationLookupRecordSettingData class

Represents a virtualization policy record, which maps virtual addressees to physical address in the WNV module to implement Hyper-V network virtualization.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetVirtualizationLookupRecordSettingData : MSFT_NetSettingData
{
  string  CustomerAddress;
  string  ProviderAddress;
  string  MACAddress;
  uint32  VirtualSubnetID;
  string  CustomerID;
  string  Context;
  uint8   Rule;
  string  VMName;
  boolean UseVmMACAddress;
  uint8   Type;
  boolean Unusable;
  boolean Unsynchronized;
};
```

## Members

The **MSFT\_NetVirtualizationLookupRecordSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetVirtualizationLookupRecordSettingData** class has these properties.

<dl> <dt>

**Context**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The custom context or comment set by the administrators.

</dd> <dt>

**CustomerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address assigned to the customer virtual machine.

</dd> <dt>

**CustomerID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The GUID set by the administrators to identify a customer entity that owns the corresponding lookup records and customer route records.

</dd> <dt>

**MACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MAC address corresponding to the CustomerAddress.

</dd> <dt>

**ProviderAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP address corresponding to the CustomerAddress in the physical network.

</dd> <dt>

**Rule**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The virtualization mechanism used by the WNV module to transform packets between CustomerAddress and ProviderAddress defined in this policy record.

<dl> <dt>

<span id="TranslationMethodNat"></span><span id="translationmethodnat"></span><span id="TRANSLATIONMETHODNAT"></span>**TranslationMethodNat** (35)
</dt> <dt>

<span id="TranslationMethodEncap"></span><span id="translationmethodencap"></span><span id="TRANSLATIONMETHODENCAP"></span>**TranslationMethodEncap** (36)
</dt> <dt>

<span id="_TranslationMethodNone"></span><span id="_translationmethodnone"></span><span id="_TRANSLATIONMETHODNONE"></span> **TranslationMethodNone** ( 37)
</dt> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the address mapping.

<dl> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>**Static** (35)
</dt> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>**Dynamic** (36)
</dt> <dt>

<span id="GatewayWildcard"></span><span id="gatewaywildcard"></span><span id="GATEWAYWILDCARD"></span>**GatewayWildcard** (37)
</dt> <dt>

<span id="L2Only"></span><span id="l2only"></span><span id="L2ONLY"></span>**L2Only** (41)
</dt> </dl>

</dd> <dt>

**Unsynchronized**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this record is not synchronized with the central policy controller.

</dd> <dt>

**Unusable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether this record is not usable for data communication.

</dd> <dt>

**UseVmMACAddress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Use the virtual machine MAC address defined in this policy record on the packets instead of the MAC address of the physical NIC.

</dd> <dt>

**VirtualSubnetID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** ( 16777215 )
</dt> </dl>

The unique identifier number of the virtual subnet the CustomerAddress belongs to.

</dd> <dt>

**VMName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The virtual machine name set by the administrators to identify the VM corresponding to the CustomerAddress.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



## See also

<dl> <dt>

[NetWNV Provider Classes](net-virtualization-classes.md)
</dt> </dl>

 

 




