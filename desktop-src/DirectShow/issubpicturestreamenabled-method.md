---
description: The IsSubpictureStreamEnabled method retrieves a value indicating whether the specified subpicture stream is enabled in the current title.
ms.assetid: c6436f77-ca94-464f-9336-f485f5d5d199
title: IsSubpictureStreamEnabled Method
ms.topic: reference
ms.date: 05/31/2018
---

# IsSubpictureStreamEnabled Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `IsSubpictureStreamEnabled` method retrieves a value indicating whether the specified subpicture stream is enabled in the current title.

``` syntax
[ bEnabled = ] MSWebDVD.IsSubpictureStreamEnabled(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the subpicture stream as an Integer.



| Value   | Description              |
|---------|--------------------------|
| 0 to 31 | subpicture stream        |
| 63      | muted low-bitrate stream |



 

</dd> </dl>

## Return Value

Returns a Boolean value indicating whether the specified audio stream is available in the current title. True means it is available.

## Remarks

Although a disc can contain up to 32 subpicture streams, each stream is not necessarily available for each title. Always verify that a stream is available for a title before setting the [**CurrentSubpictureStream**](currentsubpicturestream-property.md) property.

 

 



