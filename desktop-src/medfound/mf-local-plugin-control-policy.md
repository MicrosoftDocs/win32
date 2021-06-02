---
description: Specifies a local plugin control policy.
ms.assetid: 2936F3C9-3BCB-452A-8C03-35D73A200CE2
title: MF_LOCAL_PLUGIN_CONTROL_POLICY attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_LOCAL\_PLUGIN\_CONTROL\_POLICY attribute

Specifies a local plugin control policy.

## Data type

**UINT32**

## Remarks

Set this attribute to one of the [**MF\_PLUGIN\_CONTROL\_POLICY**](/windows/desktop/api/mfobjects/ne-mfobjects-mf_plugin_control_policy) values.

This attributes allows the app to specify a more restrictive local policy than the process-wide policy configured by [**IMFPluginControl**](/windows/desktop/api/mfobjects/nn-mfobjects-imfplugincontrol).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




