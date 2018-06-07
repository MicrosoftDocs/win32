---
Description: Specifies whether whether the encoder should check for data consistency across passes when performing two-pass VBR encoding. Read-write.
ms.assetid: 68750820-e931-41c2-9d12-89ab83b4b97e
title: MFPKEY\_CHECKDATACONSISTENCY2P Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_CHECKDATACONSISTENCY2P Property

Specifies whether whether the encoder should check for data consistency across passes when performing two-pass VBR encoding. Read-write.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_TRUE**

## Remarks

If you leave this property at its default value of **VARIANT\_TRUE**, the encoder verifies that the input samples match between the two passes, and fails if it detects a discrepancy. The main scenario that leads to a discrepancy is when the input comes from a device.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




