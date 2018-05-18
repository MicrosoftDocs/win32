---
Description: 'A wrapper method used to change the network configuration of the BMC.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'A030FF83-E618-484A-B36F-E2AE6D2D6754'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ChangeNetworkConfiguration method of the MSFT\_PCSVDevice class'
---

# ChangeNetworkConfiguration method of the MSFT\_PCSVDevice class

A wrapper method used to change the network configuration of the BMC.

## Syntax


```mof
uint32 ChangeNetworkConfiguration(
  [in]      uint16              IPv4AddressOrigin,
  [in]      string              IPv4Address,
  [in]      string              IPv4SubnetMask,
  [in]      string              IPv4DefaultGateway,
  [in, out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*IPv4AddressOrigin* \[in\]
</dt> <dd>

Identifies the method by which the IPv4 address, subnet mask, and gateway were assigned to the NIC.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (2)


</dt> <dd></dd> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>

**Static** (3)


</dt> <dd></dd> <dt>

<span id="DHCP"></span><span id="dhcp"></span>

**DHCP** (4)


</dt> <dd></dd> <dt>

<span id="BOOTP"></span><span id="bootp"></span>

**BOOTP** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*IPv4Address* \[in\]
</dt> <dd>

The IPv4 address of the target PCSV device.

</dd> <dt>

*IPv4SubnetMask* \[in\]
</dt> <dd>

The IPv4 subnet mask of the target PCSV device.

</dd> <dt>

*IPv4DefaultGateway* \[in\]
</dt> <dd>

The IPv4 default gateway of the target PCSV device.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

Reference to a [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) object that contains the job spawned if the operation continues after the method returns. May be **NULL** if the task is completed.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Reserved** (3–4095)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097–32767)
</dt> <dt>

**Vendor Reserved** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>PCSVDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVDevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVdevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




