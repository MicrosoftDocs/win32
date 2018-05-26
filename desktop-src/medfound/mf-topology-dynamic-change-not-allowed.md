---
Description: Specifies whether the Media Session attempts to modify the topology when the format of a stream changes.
ms.assetid: 8272ded7-9d27-4652-877b-40fc76426ffc
title: MF\_TOPOLOGY\_DYNAMIC\_CHANGE\_NOT\_ALLOWED attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPOLOGY\_DYNAMIC\_CHANGE\_NOT\_ALLOWED attribute

Specifies whether the Media Session attempts to modify the topology when the format of a stream changes.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master)

## Remarks

This attribute controls how the Media Session responds if the format of a stream changes during streaming.

If the format changes and the MF\_TOPOLOGY\_DYNAMIC\_CHANGE\_NOT\_ALLOWED attribute is **FALSE**, the Media Session might insert new nodes into the topology to match the new format. For example, if the video size changes, the Media Session might add a Media Foundation transform (MFT) that resizes the video. Otherwise, if the attribute is **TRUE**, the Media Session will not modify the topology.

The default value of this attribute is **FALSE**. The recommended value is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




