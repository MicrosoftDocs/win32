---
title: ComponentCategory enumeration
description: Specifies the type of content in an Advanced Television System Committee (ASTC) sub-stream (component).
ms.assetid: 20fe32fa-c8a5-4073-bcf3-7dde171d7ad4
keywords:
- ComponentCategory enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ComponentCategory
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ComponentCategory enumeration

Specifies the type of content in an Advanced Television System Committee (ASTC) sub-stream (component).

## Syntax


```C++
typedef enum ComponentCategory { 
  CategoryNotSet       = -1,
  CategoryOther        = 0,
  CategoryVideo,
  CategoryAudio,
  CategoryText,
  CategorySubtitles,
  CategoryCaptions,
  CategorySuperimpose,
  CategoryData,
  CATEGORY_COUNT
} ComponentCategory;
```



## Constants

<dl> <dt>

<span id="CategoryNotSet"></span><span id="categorynotset"></span><span id="CATEGORYNOTSET"></span>**CategoryNotSet**
</dt> <dd>

The category for the stream is not set.

</dd> <dt>

<span id="CategoryOther"></span><span id="categoryother"></span><span id="CATEGORYOTHER"></span>**CategoryOther**
</dt> <dd>

The stream contains none of the defined types.

</dd> <dt>

<span id="CategoryVideo"></span><span id="categoryvideo"></span><span id="CATEGORYVIDEO"></span>**CategoryVideo**
</dt> <dd>

Video stream.

</dd> <dt>

<span id="CategoryAudio"></span><span id="categoryaudio"></span><span id="CATEGORYAUDIO"></span>**CategoryAudio**
</dt> <dd>

Audio stream.

</dd> <dt>

<span id="CategoryText"></span><span id="categorytext"></span><span id="CATEGORYTEXT"></span>**CategoryText**
</dt> <dd>

Text stream.

</dd> <dt>

<span id="CategorySubtitles"></span><span id="categorysubtitles"></span><span id="CATEGORYSUBTITLES"></span>**CategorySubtitles**
</dt> <dd>

Subtitle stream.

</dd> <dt>

<span id="CategoryCaptions"></span><span id="categorycaptions"></span><span id="CATEGORYCAPTIONS"></span>**CategoryCaptions**
</dt> <dd>

Caption stream.

</dd> <dt>

<span id="CategorySuperimpose"></span><span id="categorysuperimpose"></span><span id="CATEGORYSUPERIMPOSE"></span>**CategorySuperimpose**
</dt> <dd>

Superimposed character stream.

</dd> <dt>

<span id="CategoryData"></span><span id="categorydata"></span><span id="CATEGORYDATA"></span>**CategoryData**
</dt> <dd>

Data stream.

</dd> <dt>

<span id="CATEGORY_COUNT"></span><span id="category_count"></span>**CATEGORY\_COUNT**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This enumeration type was changed in Windows 7. The new definition is not compatible with previous versions.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IComponentType::get\_Category**](/previous-versions/windows/desktop/api/tuner/nf-tuner-icomponenttype-get_category)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





