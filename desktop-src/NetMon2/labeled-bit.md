---
description: The LABELED\_BIT structure defines a label BIT pair.
ms.assetid: 500b5159-bf9f-49d4-8567-d8e462015eb0
title: LABELED_BIT structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LABELED_BIT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# LABELED\_BIT structure

The **LABELED\_BIT** structure defines a label BIT pair.

## Syntax


```C++
typedef struct _LABELED_BIT {
  BYTE  BitNumber;
  LPSTR LabelOff;
  LPSTR LabelOn;
} LABELED_BIT, *LPLABELED_BIT;
```



## Members

<dl> <dt>

**BitNumber**
</dt> <dd>

BIT number of the label BIT pair. Values range from 0 to 255. Set the **Bitnumber** member to the BIT used in the comparison of the property value.

</dd> <dt>

**LabelOff**
</dt> <dd>

String or label that is displayed when the BIT specified in **BitNumber** equals zero. For example, a possible label is "Bit OFF".

</dd> <dt>

**LabelOn**
</dt> <dd>

String or label that is displayed when the BIT specified in **BitNumber** equals 1. For example, a possible label is "Bit ON".

</dd> </dl>

## Remarks

An array of **LABELED\_BIT** structures is used to define a set of label BIT pairs. A pointer to the array is specified in the **lpLabeledBit** member of the [SET](set.md) structure. The pairs are used when you want to display a label based on the setting of each BIT. Typically, this type of set is used to indicate the ON or OFF value of BITs.

When a BIT set is specified, Network Monitor displays only the BITs included in the array of **SET** structures. BITs that are not in the **SET** structure are not displayed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[SET](set.md)
</dt> </dl>

 

 




