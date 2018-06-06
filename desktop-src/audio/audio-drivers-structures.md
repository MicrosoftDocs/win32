---
Description: Audio Drivers Structures
ms.assetid: 8257342f-474a-42b3-809d-96fdeede398b
title: Audio Drivers Structures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Audio Drivers Structures

## 

This section describes the structures that are used by WDM audio miniport drivers. The list of structures is as follows:

<dl>

[**APO\_REG\_PROPERTIES**](/windows/desktop/api/audioenginebaseapo/ns-audioenginebaseapo-apo_reg_properties)  
[**APOInitBaseStruct**](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-apoinitbasestruct)  
[**APOInitSystemEffects**](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects)  
[**APOInitSystemEffects2**](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects2)  
[**AudioFXExtensionParams**](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-__midl___midl_itf_audioenginebaseapo_0000_0007_0001)  
[**DMUS\_KERNEL\_EVENT**](/windows-hardware/drivers/ddi/content/dmusicks/ns-dmusicks-_dmus_kernel_event)  
[**DRMFORWARD**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-tagdrmforward)  
[**DRMRIGHTS**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-tagdrmrights)  
[**DS3DVECTOR**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ds3dvector)  
[**KSAC3\_ALTERNATE\_AUDIO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_alternate_audio)  
[**KSAC3\_BIT\_STREAM\_MODE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_bit_stream_mode)  
[**KSAC3\_DIALOGUE\_LEVEL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_dialogue_level)  
[**KSAC3\_DOWNMIX**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_downmix)  
[**KSAC3\_ERROR\_CONCEALMENT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_error_concealment)  
[**KSAC3\_LANGUAGE\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff537081)  
[**KSAC3\_ROOM\_TYPE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_room_type)  
[**KSAUDIO\_CHANNEL\_CONFIG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_channel_config)  
[**KSAUDIO\_COPY\_PROTECTION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_copy_protection)  
[**KSAUDIO\_DYNAMIC\_RANGE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_dynamic_range)  
[**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry)  
[**KSAUDIO\_MICROPHONE\_COORDINATES**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_microphone_coordinates)  
[**KSAUDIO\_MIX\_CAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mix_caps)  
[**KSAUDIO\_MIXCAP\_TABLE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mixcap_table)  
[**KSAUDIO\_MIXLEVEL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mixlevel)  
[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints)  
[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2)  
[**KSAUDIO\_PACKETSIZE\_PROCESSINGMODE\_CONSTRAINT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksaudio_packetsize_signalprocessingmode_constraint)  
[**KSAUDIO\_POSITION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_position)  
[**KSAUDIO\_POSITIONEX**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_positionex)  
[**KSAUDIO\_PREFERRED\_STATUS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_preferred_status)  
[**KSAUDIO\_PRESENTATION\_POSITION**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksaudio_presentation_position)  
[**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_tagksaudioengine_buffer_size_range)  
[**KSAUDIOENGINE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_tagksaudioengine_descriptor)  
[**KSAUDIOENGINE\_VOLUMELEVEL**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_tagksaudioengine_volumelevel)  
[**KSDATAFORMAT\_DSOUND**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdataformat_dsound)  
[**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdataformat_waveformatex)  
[**KSDATARANGE\_AUDIO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdatarange_audio)  
[**KSDATARANGE\_MUSIC**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdatarange_music)  
[**KSDRMAUDIOSTREAM\_CONTENTID**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-ksdrmaudiostream_contentid)  
[**KSDSOUND\_BUFFERDESC**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdsound_bufferdesc)  
[**KSDS3D\_BUFFER\_ALL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_buffer_all)  
[**KSDS3D\_BUFFER\_CONE\_ANGLES**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_buffer_cone_angles)  
[**KSDS3D\_HRTF\_FILTER\_FORMAT\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_hrtf_filter_format_msg)  
[**KSDS3D\_HRTF\_INIT\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_hrtf_init_msg)  
[**KSDS3D\_HRTF\_PARAMS\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_hrtf_params_msg)  
[**KSDS3D\_ITD\_PARAMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_itd_params)  
[**KSDS3D\_ITD\_PARAMS\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_itd_params_msg)  
[**KSDS3D\_LISTENER\_ALL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_listener_all)  
[**KSDS3D\_LISTENER\_ORIENTATION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_listener_orientation)  
[**KSJACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537136)  
[**KSJACK\_DESCRIPTION2**](https://msdn.microsoft.com/library/windows/hardware/ff537138)  
[**KSJACK\_SINK\_INFORMATION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagksjack_sink_information)  
[**KSMUSICFORMAT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksmusicformat)  
[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksnodeproperty)  
[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel)  
[**KSP\_DRMAUDIOSTREAM\_CONTENTID**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-ksp_drmaudiostream_contentid)  
[**KSP\_PINMODE**](/windows/desktop/api/Msapofxproxy/ns-msapofxproxy-tagksp_pinmode)  
[KSRTAUDIO Structures](https://www.bing.com/search?q=KSRTAUDIO+Structures)  
[**KSTELEPHONY\_CALLCONTROL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstelephony_callcontrol)  
[**KSTELEPHONY\_CALLINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstelephony_callinfo)  
[**KSTELEPHONY\_PROVIDERCHANGE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstelephony_providerchange)  
[**KSTOPOLOGY\_ENDPOINTID**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstopology_endpointid)  
[**KSTOPOLOGY\_ENDPOINTIDPAIR**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstopology_endpointidpair)  
[**LOOPEDSTREAMING\_POSITION\_EVENT\_DATA**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-loopedstreaming_position_event_data)  
[**MDEVICECAPSEX**](/windows/desktop/api/mmddk/ns-mmddk-mdevicecapsex)  
[**MIDIOPENDESC**](/windows/desktop/api/mmddk/ns-mmddk-midiopendesc_tag)  
[**RTAUDIO\_GETREADPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt169891)  
[**RTAUDIO\_SETWRITEPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt169892)  
[**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-keyworddetectoroemadapter-__midl___midl_itf_keyworddetectoroemadapter_0000_0000_0001)  
[**SYNTH\_BUFFER**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synth_buffer)  
[**SYNTH\_PORTPARAMS**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synth_portparams)  
[**SYNTH\_STATS**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synth_stats)  
[**SYNTHCAPS**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synthcaps)  
[**SYNTHDOWNLOAD**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synthdownload)  
[**SYNTHVOICEPRIORITY\_INSTANCE**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synthvoicepriority_instance)  
[**SYSAUDIO\_ATTACH\_VIRTUAL\_SOURCE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_attach_virtual_source)  
[**SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_create_virtual_source)  
[**SYSAUDIO\_INSTANCE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_instance_info)  
[**SYSAUDIO\_SELECT\_GRAPH**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_select_graph)  
[**UNCOMPRESSEDAUDIOFORMAT**](/windows/desktop/api/Audiomediatype/ns-audiomediatype-_uncompressedaudioformat)  
[**WAVEFORMATEX**](/windows/desktop/api/mmreg/ns-mmreg-twaveformatex)  
[**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-waveformatextensible)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audio%20Drivers%20Structures%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



