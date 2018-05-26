---
Description: Specifies a local plugin control policy.
ms.assetid: 2936F3C9-3BCB-452A-8C03-35D73A200CE2
title: MF\_LOCAL\_PLUGIN\_CONTROL\_POLICY attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_LOCAL\_PLUGIN\_CONTROL\_POLICY attribute

Specifies a local plugin control policy.

## Data type

**UINT32**

## Remarks

Set this attribute to one of the [**MF\_PLUGIN\_CONTROL\_POLICY**](/windows/win32/mfobjects/ne-mfobjects-mf_plugin_control_policy?branch=master) values.

This attributes allows the app to specify a more restrictive local policy than the process-wide policy configured by [**IMFPluginControl**](/windows/win32/mfobjects/nn-mfobjects-imfplugincontrol?branch=master).

## Requirements



|                                     |                                                                                    |
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

 

 




