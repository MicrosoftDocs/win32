---
title: MSFT\_NetEventCaptureTarget\_CaptureProvider class
description: This class encapsulates the association between the packet capture provider and a packet capture target.
ms.assetid: ad06fa95-977d-41bd-96c0-511651d1bb4e
keywords:
- MSFT_NetEventCaptureTarget_CaptureProvider class
- MSFT_NetEventCaptureTarget_CaptureProvider class, described
topic_type:
- apiref
api_name:
- MSFT_NetEventCaptureTarget_CaptureProvider
- MSFT_NetEventCaptureTarget_CaptureProvider.GroupComponent
- MSFT_NetEventCaptureTarget_CaptureProvider.PartComponent
api_location:
- NetEventPacketCapture.dll
api_type:
- DllExport


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetEventCaptureTarget\_CaptureProvider class

This class encapsulates the association between the packet capture provider and a packet capture target.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, UMLPackagePath("CIM::Core::CoreElements"), ClassVersion("1.0"), dynamic, provider("NetEventPacketCapture"), AMENDMENT]
class MSFT_NetEventCaptureTarget_CaptureProvider : CIM_Component
{
  MSFT_NetEventPacketCaptureProvider REF GroupComponent;
  MSFT_NetEventPacketCaptureTarget   REF PartComponent;
};
```

## Members

The **MSFT\_NetEventCaptureTarget\_CaptureProvider** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetEventCaptureTarget\_CaptureProvider** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetEventPacketCaptureProvider**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Aggregate**](/windows/win32/wmisdk/standard-qualifiers), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("GroupComponent")
</dt> </dl>

Identifies the packet capture provider.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetEventPacketCaptureTarget**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

Identifies the packet capture target.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                                       |
| MOF<br/>                      | <dl> <dt>NetEventPacketCapture.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetEventPacketCapture.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

