---
description: MSFT\_NetAdapter\_ProcessorNumber.
ms.assetid: 7b053e2a-8e26-4798-818d-b3868ed21fae
title: MSFT\_NetAdapter\_ProcessorNumber class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_ProcessorNumber
- MSFT_NetAdapter_ProcessorNumber.ProcessorGroup
- MSFT_NetAdapter_ProcessorNumber.ProcessorNumber
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_ProcessorNumber class

MSFT\_NetAdapter\_ProcessorNumber

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_ProcessorNumber
{
  uint16 ProcessorGroup;
  uint8  ProcessorNumber;
};
```

## Members

The **MSFT\_NetAdapter\_ProcessorNumber** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_ProcessorNumber** class has these properties.

<dl> <dt>

**ProcessorGroup**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The group number for a set of logical processors.

</dd> <dt>

**ProcessorNumber**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The processor number.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




