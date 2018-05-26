---
Description: Specifies the size of the destination window for video playback.
ms.assetid: 46af4c11-042c-4580-ba9d-3aee6172de56
title: MF\_TOPOLOGY\_PLAYBACK\_MAX\_DIMS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPOLOGY\_PLAYBACK\_MAX\_DIMS attribute

Specifies the size of the destination window for video playback.

## Data type

**UINT64**

## Get/set

To get this attribute, call [**MFGetAttributeSize**](/windows/win32/mfapi/nf-mfapi-mfgetattributesize?branch=master).

To set this attribute, call [**MFSetAttributeSize**](/windows/win32/mfapi/nf-mfapi-mfsetattributesize?branch=master).

## Applies to

[**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master)

## Remarks

The topology loader uses this attribute to optimize the pipeline before playback starts. If you set this attribute, also set the [MF\_TOPOLOGY\_STATIC\_PLAYBACK\_OPTIMIZATIONS](mf-topology-static-playback-optimizations.md) attribute to **TRUE**.

The upper 32 bits of the attribute value contain the width and the lower 32 bits contain the height, both in pixels.

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
</dt> <dt>

[Video Quality Management](video-quality-management.md)
</dt> </dl>

 

 




