---
Description: A value that indicates the type of sensor provided by a frame source, such as color, infrared, or depth.
ms.assetid: F327B9E9-C01C-4F5B-9A26-6404ECD7F27F
title: MF\_MT\_FRAMESOURCE\_TYPES attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_FRAMESOURCE\_TYPES attribute

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

A value that indicates the type of sensor provided by a frame source, such as color, infrared, or depth.

## Data type

**UINT32**

## Remarks

This value should be a member of the [**\_MFFrameSourceTypes**](mf._mfframesourcetypes) enumeration. For backward compatibility, when this attribute is not defined on a media type, it's assumed to be **\_MFFrameSourceTyes::Color**.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




