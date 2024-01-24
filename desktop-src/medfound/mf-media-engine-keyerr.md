---
description: Defines media key error codes for the media engine.
ms.assetid: F6E13260-74A2-40D0-A704-4E1CDB16B8D8
title: MF_MEDIA_ENGINE_KEYERR enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MF_MEDIA_ENGINE_KEYERR
api_type: 
- HeaderDef
api_location: 
- mfmediaengine.h
---

# MF\_MEDIA\_ENGINE\_KEYERR enumeration

Defines media key error codes for the media engine.

## Syntax


```C++
typedef enum _MF_MEDIA_ENGINE_KEYERR { 
  MF_MEDIAENGINE_KEYERR_UNKNOWN          = 1,
  MF_MEDIAENGINE_KEYERR_CLIENT           = 2,
  MF_MEDIAENGINE_KEYERR_SERVICE          = 3,
  MF_MEDIAENGINE_KEYERR_OUTPUT           = 4,
  MF_MEDIAENGINE_KEYERR_HARDWARECHANGE   = 5,
  MF_MEDIAENGINE_KEYERR_DOMAIN           = 6
} MF_MEDIA_ENGINE_KEYERR;
```



## Constants

<dl> <dt>

<span id="MF_MEDIAENGINE_KEYERR_UNKNOWN"></span><span id="mf_mediaengine_keyerr_unknown"></span>**MF\_MEDIAENGINE\_KEYERR\_UNKNOWN**
</dt> <dd>

Unknown error occurred.

</dd> <dt>

<span id="MF_MEDIAENGINE_KEYERR_CLIENT"></span><span id="mf_mediaengine_keyerr_client"></span>**MF\_MEDIAENGINE\_KEYERR\_CLIENT**
</dt> <dd>

An error with the client occurred.

</dd> <dt>

<span id="MF_MEDIAENGINE_KEYERR_SERVICE"></span><span id="mf_mediaengine_keyerr_service"></span>**MF\_MEDIAENGINE\_KEYERR\_SERVICE**
</dt> <dd>

An error with the service occurred.

</dd> <dt>

<span id="MF_MEDIAENGINE_KEYERR_OUTPUT"></span><span id="mf_mediaengine_keyerr_output"></span>**MF\_MEDIAENGINE\_KEYERR\_OUTPUT**
</dt> <dd>

An error with the output occurred.

</dd> <dt>

<span id="MF_MEDIAENGINE_KEYERR_HARDWARECHANGE_"></span><span id="mf_mediaengine_keyerr_hardwarechange_"></span>**MF\_MEDIAENGINE\_KEYERR\_HARDWARECHANGE** 
</dt> <dd>

An error occurred related to a hardware change.

</dd> <dt>

<span id="MF_MEDIAENGINE_KEYERR_DOMAIN"></span><span id="mf_mediaengine_keyerr_domain"></span>**MF\_MEDIAENGINE\_KEYERR\_DOMAIN**
</dt> <dd>

An error with the domain occurred.

</dd> </dl>

## Remarks

**MF\_MEDIA\_ENGINE\_KEYERR** is used with the *code* parameter of [**IMFMediaKeySessionNotify::KeyError**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediakeysessionnotify-keyerror) and the *code* value returned from [**IMFMediaKeySession::GetError**](imfmediakeysession-geterror.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Enumerations](media-foundation-enumerations.md)
</dt> </dl>

 

 




