---
description: Specifies the maximum time, in milliseconds, between key frames in the codec output.
ms.assetid: 2a52e6a5-10a0-46dd-aa31-cb55094903b5
title: MFPKEY_KEYDIST Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_KEYDIST Property

Specifies the maximum time, in milliseconds, between key frames in the codec output.

## Constant for IPropertyBag

g\_wszWMVCKeyframeDistance

## Data Type

VT\_I4

## Default Value

The default value depends on which version of Windows is running, as shown in the following table.



| Operating system | Default value |
|------------------|---------------|
| Windows XP       | 8000          |
| Windows Vista    | 8000          |
| Windows 7        | 2000          |



 

## Remarks

The internal logic of the codec determines the actual location of each key frame. The distance between any two key frames may be less than the value of this property, however, it will never be greater.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




