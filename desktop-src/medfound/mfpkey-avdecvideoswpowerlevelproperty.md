---
Description: Specifies the power level for the decoder.
ms.assetid: c4ede790-e7ef-4ed0-bdbe-a635350d92f3
title: MFPKEY\_AVDecVideoSWPowerLevel Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_AVDecVideoSWPowerLevel Property

Specifies the power level for the decoder.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx).

## Data Type

**VT\_UI4**

## Default Value

**100**

## Remarks

This property must be set to one of the following values.



| Value | Meaning                                                             |
|-------|---------------------------------------------------------------------|
| 0     | The decoder uses a power level that is optimized for battery life.  |
| 50    | The decoder uses a balanced power level.                            |
| 100   | The decoder uses a power level that is optimized for video quality. |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




