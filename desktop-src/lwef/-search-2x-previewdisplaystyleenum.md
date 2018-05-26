---
title: PreviewDisplayStyle enumeration
description: Used by IResultsViewer PreviewStyle to set or determine the display style currently being used.
ms.assetid: ccbbfe38-0719-41e0-9331-cc0c1be651eb
keywords:
- PreviewDisplayStyle enumeration Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- PreviewDisplayStyle
api_location:
- WdsView.idl
api_type:
- IDLDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PreviewDisplayStyle enumeration

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

Used by [**IResultsViewer::PreviewStyle**](-search-2x-iresultsviewer-previewstyle.md) to set or determine the display style currently being used.

## Syntax


```C++
typedef enum PreviewDisplayStyleEnum { 
  AutoPreview    = 0,
  RightPreview   = 1,
  BottomPreview  = 2,
  NoPreview      = 3
} PreviewDisplayStyle;
```



## Constants

<dl> <dt>

<span id="AutoPreview"></span><span id="autopreview"></span><span id="AUTOPREVIEW"></span>**AutoPreview**
</dt> <dd>

Indicates AutoPreview.

</dd> <dt>

<span id="RightPreview"></span><span id="rightpreview"></span><span id="RIGHTPREVIEW"></span>**RightPreview**
</dt> <dd>

Indicates RightPreview.

</dd> <dt>

<span id="BottomPreview"></span><span id="bottompreview"></span><span id="BOTTOMPREVIEW"></span>**BottomPreview**
</dt> <dd>

Indicates BottomPreview.

</dd> <dt>

<span id="NoPreview"></span><span id="nopreview"></span><span id="NOPREVIEW"></span>**NoPreview**
</dt> <dd>

Indicates NoPreview.

</dd> </dl>

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>WdsView.idl</dt> </dl> |



 

 





