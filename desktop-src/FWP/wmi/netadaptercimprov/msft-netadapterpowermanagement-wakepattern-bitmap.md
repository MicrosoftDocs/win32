---
description: MSFT\_NetAdapterPowerManagement\_WakePattern\_Bitmap defines settings for waking on a bitmap/mask wake pattern.
ms.assetid: 6768611a-face-446c-b36a-5607c019fbb5
title: MSFT\_NetAdapterPowerManagement\_WakePattern\_Bitmap class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_WakePattern_Bitmap
- MSFT_NetAdapterPowerManagement_WakePattern_Bitmap.Pattern
- MSFT_NetAdapterPowerManagement_WakePattern_Bitmap.Mask
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_WakePattern\_Bitmap class

MSFT\_NetAdapterPowerManagement\_WakePattern\_Bitmap defines settings for waking on a bitmap/mask wake pattern.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_WakePattern_Bitmap : MSFT_NetAdapterPowerManagement_Wake
{
  uint8 Pattern[];
  uint8 Mask[];
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_WakePattern\_Bitmap** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_WakePattern\_Bitmap** class has these properties.

<dl> <dt>

**Mask**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies a mask indicating which bits of the pattern to match against incoming packets.

</dd> <dt>

**Pattern**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the pattern to match against incoming packets.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




