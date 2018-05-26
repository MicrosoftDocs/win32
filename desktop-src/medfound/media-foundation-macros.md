---
Description: Media Foundation Macros
ms.assetid: c460b1cd-13d7-4b65-a755-23b2ea87864d
title: Media Foundation Macros
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Media Foundation Macros

## In this section



| Attribute                                                                                              | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DEFINE\_MEDIATYPE\_GUID**](/windows/win32/mfapi/nf-mfapi-define_mediatype_guid?branch=master)<br/>                              | Defines a media subtype GUID from a FOURCC code, **D3DFORMAT** value, or audio format type.<br/>                                                                       |
| [**MFP\_GET\_ACQUIRE\_USER\_CREDENTIAL\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_acquire_user_credential_event?branch=master)<br/> | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_ACQUIRE\_USER\_CREDENTIAL\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_acquire_user_credential_event?branch=master) pointer.<br/> |
| [**MFP\_GET\_ERROR\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_error_event?branch=master)<br/>                                       | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_ERROR\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_error_event?branch=master) pointer.<br/>                                       |
| [**MFP\_GET\_FRAME\_STEP\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_frame_step_event?branch=master)<br/>                            | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_FRAME\_STEP\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_frame_step_event?branch=master) pointer.<br/>                            |
| [**MFP\_GET\_MEDIAITEM\_CLEARED\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_mediaitem_cleared_event?branch=master)<br/>              | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MEDIAITEM\_CLEARED\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_mediaitem_cleared_event?branch=master) pointer.<br/>                   |
| [**MFP\_GET\_MEDIAITEM\_CREATED\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_mediaitem_created_event?branch=master)<br/>              | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_MEDIAITEM\_CREATED\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_mediaitem_created_event?branch=master) pointer.<br/>              |
| [**MFP\_GET\_MEDIAITEM\_SET\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_mediaitem_set_event?branch=master)<br/>                      | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_MEDIAITEM\_SET\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_mediaitem_set_event?branch=master) pointer.<br/>                      |
| [**MFP\_GET\_MF\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_mf_event?branch=master)<br/>                                             | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_MF\_EVENT**](mf.MFP_MF_EVENT) pointer.<br/>                                              |
| [**MFP\_GET\_PAUSE\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_pause_event?branch=master)<br/>                                       | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_PAUSE\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_pause_event?branch=master) pointer.<br/>                                       |
| [**MFP\_GET\_PLAY\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_play_event?branch=master)<br/>                                         | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_PLAY\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_play_event?branch=master) pointer.<br/>                                         |
| [**MFP\_GET\_PLAYBACK\_ENDED\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_playback_ended_event?branch=master)<br/>                    | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_PLAYBACK\_ENDED\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_playback_ended_event?branch=master) pointer.<br/>                    |
| [**MFP\_GET\_POSITION\_SET\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_position_set_event?branch=master)<br/>                        | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_POSITION\_SET\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_position_set_event?branch=master) pointer.<br/>                        |
| [**MFP\_GET\_RATE\_SET\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_rate_set_event?branch=master)<br/>                                | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_RATE\_SET\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_rate_set_event?branch=master) pointer.<br/>                                |
| [**MFP\_GET\_STOP\_EVENT**](/windows/win32/mfplay/nf-mfplay-mfp_get_stop_event?branch=master)<br/>                                         | Casts an [**MFP\_EVENT\_HEADER**](/windows/win32/mfplay/ns-mfplay-mfp_event_header?branch=master) pointer to an [**MFP\_STOP\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_stop_event?branch=master) pointer.<br/>                                         |



 

## Related topics

<dl> <dt>

[Media Foundation Programming Reference](media-foundation-programming-reference.md)
</dt> </dl>

 

 




