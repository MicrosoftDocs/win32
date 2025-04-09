---
title: MSFT\_NetEventSession\_Provider class
description: This class encapsulates an association between a session and a provider.
ms.assetid: 18364d7d-5753-4376-904a-e2a6ff777beb
keywords:
- MSFT_NetEventSession_Provider class
- MSFT_NetEventSession_Provider class, described
topic_type:
- apiref
api_name:
- MSFT_NetEventSession_Provider
- MSFT_NetEventSession_Provider.GroupComponent
- MSFT_NetEventSession_Provider.PartComponent
api_location:
- NetEventPacketCapture.dll
api_type:
- DllExport


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetEventSession\_Provider class

This class encapsulates an association between a session and a provider

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, UMLPackagePath("CIM::Core::CoreElements"), ClassVersion("1.0"), dynamic, provider("NetEventPacketCapture"), AMENDMENT]
class MSFT_NetEventSession_Provider : CIM_Component
{
  MSFT_NetEventSession  REF GroupComponent;
  MSFT_NetEventProvider REF PartComponent;
};
```

## Members

The **MSFT\_NetEventSession\_Provider** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetEventSession\_Provider** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetEventSession**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Aggregate**](/windows/win32/wmisdk/standard-qualifiers), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("GroupComponent")
</dt> </dl>

Identifies the session

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetEventProvider**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

Identifies the provider

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

 

