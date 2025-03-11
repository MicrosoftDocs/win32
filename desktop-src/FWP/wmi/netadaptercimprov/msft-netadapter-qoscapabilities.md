---
description: This class is used to report QoS capabilities on a network adapter.
ms.assetid: 72ea6ea3-443d-492c-9d95-60da3ffbf57c
title: MSFT\_NetAdapter\_QosCapabilities class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_QosCapabilities
- MSFT_NetAdapter_QosCapabilities.MacSecBypassSupported
- MSFT_NetAdapter_QosCapabilities.CeeDcbxSupported
- MSFT_NetAdapter_QosCapabilities.IeeeDcbxSupported
- MSFT_NetAdapter_QosCapabilities.NumberOfTrafficClasses
- MSFT_NetAdapter_QosCapabilities.NumberOfEtsCapableTrafficClasses
- MSFT_NetAdapter_QosCapabilities.NumberOfPfcEnabledTrafficClasses
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_QosCapabilities class

This class is used to report QoS capabilities on a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_QosCapabilities
{
  boolean MacSecBypassSupported;
  boolean CeeDcbxSupported;
  boolean IeeeDcbxSupported;
  uint8   NumberOfTrafficClasses;
  uint8   NumberOfEtsCapableTrafficClasses;
  uint8   NumberOfPfcEnabledTrafficClasses;
};
```

## Members

The **MSFT\_NetAdapter\_QosCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_QosCapabilities** class has these properties.

<dl> <dt>

**CeeDcbxSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CEE DCBX is supported.

</dd> <dt>

**IeeeDcbxSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IEEE DCBX is supported.

</dd> <dt>

**MacSecBypassSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MACsec bypass for IEEE 802.1Qbb Priority-based Flow Control is supported.

</dd> <dt>

**NumberOfEtsCapableTrafficClasses**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** (8)
</dt> </dl>

Number of supported traffic classes that can be enabled for IEEE 802.1Qaz Enhanced Transmission Selection.

</dd> <dt>

**NumberOfPfcEnabledTrafficClasses**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** (8)
</dt> </dl>

Number of supported traffic classes that can be enabled for IEEE 802.1Qbb Priority-based Flow Control.

</dd> <dt>

**NumberOfTrafficClasses**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** (8)
</dt> </dl>

Number of traffic classes supported.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




