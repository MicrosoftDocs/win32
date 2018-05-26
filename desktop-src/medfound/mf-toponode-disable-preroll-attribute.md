---
Description: Specifies whether the Media Session uses preroll on the media sink represented by this topology node.
ms.assetid: 1781f3a0-6baa-4e06-b2eb-9a8f572aa040
title: MF\_TOPONODE\_DISABLE\_PREROLL attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_DISABLE\_PREROLL attribute

Specifies whether the Media Session uses preroll on the media sink represented by this topology node.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to output nodes (**MF\_TOPOLOGY\_OUTPUT\_NODE**).

If the value of this attribute is **TRUE**, the Media Session does not preroll any data to the media sink, even if the media sink exposes the [**IMFMediaSinkPreroll**](/windows/win32/mfidl/nn-mfidl-imfmediasinkpreroll?branch=master) interface. If the value is **FALSE**, the Media Session prerolls data if the media sink implements **IMFMediaSinkPreroll**. The default value is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




