---
description: This class represents QoS settings on a network adapter.
ms.assetid: c56672e0-6921-4d00-85c4-62c630da55e7
title: MSFT\_NetAdapter\_QosSettings class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_QosSettings
- MSFT_NetAdapter_QosSettings.TransmissionSelectionEnabled
- MSFT_NetAdapter_QosSettings.PriorityAssignmentTable
- MSFT_NetAdapter_QosSettings.TsaAssignmentTable
- MSFT_NetAdapter_QosSettings.BandwidthAssignmentTable
- MSFT_NetAdapter_QosSettings.FlowControlEnabled
- MSFT_NetAdapter_QosSettings.PriorityFlowControlEnableArray
- MSFT_NetAdapter_QosSettings.ClassificationEnabled
- MSFT_NetAdapter_QosSettings.NumberOfClassificationElements
- MSFT_NetAdapter_QosSettings.ClassificationTable
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_QosSettings class

This class represents QoS settings on a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_QosSettings
{
  boolean TransmissionSelectionEnabled;
  uint8   PriorityAssignmentTable[];
  uint8   TsaAssignmentTable[];
  uint8   BandwidthAssignmentTable[];
  boolean FlowControlEnabled;
  boolean PriorityFlowControlEnableArray[];
  boolean ClassificationEnabled;
  uint32  NumberOfClassificationElements;
  string  ClassificationTable[];
};
```

## Members

The **MSFT\_NetAdapter\_QosSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_QosSettings** class has these properties.

<dl> <dt>

**BandwidthAssignmentTable**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bandwidth assignments per Traffic Class.

</dd> <dt>

**ClassificationEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Classification settings are enabled.

</dd> <dt>

**ClassificationTable**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Classification entries.

</dd> <dt>

**FlowControlEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flow Control settings are enabled.

</dd> <dt>

**NumberOfClassificationElements**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of classification entries.

</dd> <dt>

**PriorityAssignmentTable**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Priority to Traffic Class assignments.

</dd> <dt>

**PriorityFlowControlEnableArray**
</dt> <dd> <dl> <dt>

Data type: **boolean** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

IEEE 802.1Qbb Priority Flow Control enabled per Priority.

</dd> <dt>

**TransmissionSelectionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Transmission Selection settings are enabled.

</dd> <dt>

**TsaAssignmentTable**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Transmission Selection Algorithm assignments per Traffic Class.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




