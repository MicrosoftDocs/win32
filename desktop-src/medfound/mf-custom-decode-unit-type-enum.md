---
Description: Specifies the type of unit contained in an IMFSample in a MFSampleExtension\_ForwardedDecodeUnits collection.
ms.assetid: B74890ED-9586-475B-8C77-457ECB893980
title: MF\_CUSTOM\_DECODE\_UNIT\_TYPE enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_CUSTOM\_DECODE\_UNIT\_TYPE enumeration

Specifies the type of unit contained in an [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master) in a [MFSampleExtension\_ForwardedDecodeUnits](mfsampleextension-forwardeddecodeunits.md) collection.

## Members



| Member                    | Description                                                             | Value |
|---------------------------|-------------------------------------------------------------------------|-------|
| **MF\_DECODE\_UNIT\_NAL** | The unit type is network abstraction layer unit (NALU). <br/>     | 0     |
| **MF\_DECODE\_UNIT\_SEI** | The unit type is Supplemental Enhancement Information (SEI).<br/> | 1     |



## Remarks

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




