---
description: Defines the encapsulation types the Adapter can support for LSO.
ms.assetid: 3a7dcfc7-c16b-4975-bb07-a7c7779a3f33
title: MSFT\_NetAdapterLsoEncapsulationTypes class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterLsoEncapsulationTypes
- MSFT_NetAdapterLsoEncapsulationTypes.NdisEncapsulationNotSupported
- MSFT_NetAdapterLsoEncapsulationTypes.NdisEncapsulationNotNull
- MSFT_NetAdapterLsoEncapsulationTypes.NdisEncapsulationIeee802_3
- MSFT_NetAdapterLsoEncapsulationTypes.NdisEncapsulationIeee802_3pAndq
- MSFT_NetAdapterLsoEncapsulationTypes.NdisEncapsulationIeee802_3PAndQInOob
- MSFT_NetAdapterLsoEncapsulationTypes.NdisEncapsulationIeeLlcSnapRouted
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterLsoEncapsulationTypes class

Defines the encapsulation types the Adapter can support for LSO.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterLsoEncapsulationTypes
{
  boolean NdisEncapsulationNotSupported;
  boolean NdisEncapsulationNotNull;
  boolean NdisEncapsulationIeee802_3;
  boolean NdisEncapsulationIeee802_3pAndq;
  boolean NdisEncapsulationIeee802_3PAndQInOob;
  boolean NdisEncapsulationIeeLlcSnapRouted;
};
```

## Members

The **MSFT\_NetAdapterLsoEncapsulationTypes** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterLsoEncapsulationTypes** class has these properties.

<dl> <dt>

**NdisEncapsulationIeee802\_3**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies IEEE 802.3 encapsulation.

</dd> <dt>

**NdisEncapsulationIeee802\_3pAndq**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies IEEE 802.3p and IEEE 802.3q encapsulation.

</dd> <dt>

**NdisEncapsulationIeee802\_3PAndQInOob**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies that IEEE 802.3p and IEEE 802.3q encapsulation settings are specified in the NetBufferList as OOB info.

</dd> <dt>

**NdisEncapsulationIeeLlcSnapRouted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies logical link control (LLC) encapsulation for routed protocols. Also used to indicate Ethernet LLC/SNAP encapsulation.

</dd> <dt>

**NdisEncapsulationNotNull**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies NULL encapsulation.

</dd> <dt>

**NdisEncapsulationNotSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies that no encapsulation offload is supported.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




