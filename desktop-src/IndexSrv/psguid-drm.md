---
Description: PSGUID\_DRM
ms.assetid: a1c54e90-ff8a-4ba6-9e9e-c2d1c3032a74
title: PSGUID\_DRM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSGUID\_DRM

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The PSGUID\_DRM property set defines properties for digital rights management.

``` syntax
#define PSGUID_DRM {0xaeac19e4, 0x89ae, 0x4508, 0xb9, 0xb7, 0xbb, \
    0x86, 0x7a, 0xbe, 0xe2, 0xed}
```

### Remarks

The PSGUID\_DRM property set contains the following property constants:

<dl> <dt>

<span id="PIDDRSI_PROTECTED"></span><span id="piddrsi_protected"></span>PIDDRSI\_PROTECTED
</dt> <dd>

Property ID 2. Displays the license for digital rights management.

</dd> <dt>

<span id="PIDDRSI_DESCRIPTION"></span><span id="piddrsi_description"></span>PIDDRSI\_DESCRIPTION
</dt> <dd>

Property ID 3. Displays the description for digital rights management.

</dd> <dt>

<span id="PIDDRSI_PLAYCOUNT"></span><span id="piddrsi_playcount"></span>PIDDRSI\_PLAYCOUNT
</dt> <dd>

Property ID 4. Indicates the play count for digital rights management.

</dd> <dt>

<span id="PIDDRSI_PLAYSTARTS"></span><span id="piddrsi_playstarts"></span>PIDDRSI\_PLAYSTARTS
</dt> <dd>

Property ID 5. Indicates when play starts for digital rights management.

</dd> <dt>

<span id="PIDDRSI_PLAYEXPIRES"></span><span id="piddrsi_playexpires"></span>PIDDRSI\_PLAYEXPIRES
</dt> <dd>

Property ID 6. Indicates when play expires for digital rights management.

</dd> </dl>

## Related topics

<dl> <dt>

[PSGUID\_AUDIO](psguid-audio.md)
</dt> <dt>

[PSGUID\_IMAGESUMMARYINFORMATION](psguid-imagesummaryinformation.md)
</dt> <dt>

[PSGUID\_MUSIC](psguid-music.md)
</dt> <dt>

[PSGUID\_VIDEO](psguid-video.md)
</dt> </dl>

 

 



