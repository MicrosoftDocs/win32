---
Description: Audio Drivers Structures
ms.assetid: 8257342f-474a-42b3-809d-96fdeede398b
title: Audio Drivers Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Drivers Structures

## 

This section describes the structures that are used by WDM audio miniport drivers. The list of structures is as follows:

<dl>

[**APO\_REG\_PROPERTIES**](/windows/win32/audioenginebaseapo/ns-audioenginebaseapo-apo_reg_properties?branch=master)  
[**APOInitBaseStruct**](/windows/win32/Audioenginebaseapo/ns-audioenginebaseapo-apoinitbasestruct?branch=master)  
[**APOInitSystemEffects**](/windows/win32/Audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects?branch=master)  
[**APOInitSystemEffects2**](/windows/win32/Audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects2?branch=master)  
[**AudioFXExtensionParams**](/windows/win32/Audioenginebaseapo/ns-audioenginebaseapo-__midl___midl_itf_audioenginebaseapo_0000_0007_0001?branch=master)  
[**DMUS\_KERNEL\_EVENT**](/windows-hardware/drivers/ddi/content/dmusicks/ns-dmusicks-_dmus_kernel_event?branch=master)  
[**DRMFORWARD**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-tagdrmforward?branch=master)  
[**DRMRIGHTS**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-tagdrmrights?branch=master)  
[**DS3DVECTOR**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ds3dvector?branch=master)  
[**KSAC3\_ALTERNATE\_AUDIO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_alternate_audio?branch=master)  
[**KSAC3\_BIT\_STREAM\_MODE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_bit_stream_mode?branch=master)  
[**KSAC3\_DIALOGUE\_LEVEL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_dialogue_level?branch=master)  
[**KSAC3\_DOWNMIX**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_downmix?branch=master)  
[**KSAC3\_ERROR\_CONCEALMENT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_error_concealment?branch=master)  
[**KSAC3\_LANGUAGE\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff537081)  
[**KSAC3\_ROOM\_TYPE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksac3_room_type?branch=master)  
[**KSAUDIO\_CHANNEL\_CONFIG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_channel_config?branch=master)  
[**KSAUDIO\_COPY\_PROTECTION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_copy_protection?branch=master)  
[**KSAUDIO\_DYNAMIC\_RANGE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_dynamic_range?branch=master)  
[**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry?branch=master)  
[**KSAUDIO\_MICROPHONE\_COORDINATES**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_microphone_coordinates?branch=master)  
[**KSAUDIO\_MIX\_CAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mix_caps?branch=master)  
[**KSAUDIO\_MIXCAP\_TABLE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mixcap_table?branch=master)  
[**KSAUDIO\_MIXLEVEL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_mixlevel?branch=master)  
[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints?branch=master)  
[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2?branch=master)  
[**KSAUDIO\_PACKETSIZE\_PROCESSINGMODE\_CONSTRAINT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksaudio_packetsize_signalprocessingmode_constraint?branch=master)  
[**KSAUDIO\_POSITION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_position?branch=master)  
[**KSAUDIO\_POSITIONEX**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_positionex?branch=master)  
[**KSAUDIO\_PREFERRED\_STATUS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksaudio_preferred_status?branch=master)  
[**KSAUDIO\_PRESENTATION\_POSITION**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksaudio_presentation_position?branch=master)  
[**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_tagksaudioengine_buffer_size_range?branch=master)  
[**KSAUDIOENGINE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_tagksaudioengine_descriptor?branch=master)  
[**KSAUDIOENGINE\_VOLUMELEVEL**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_tagksaudioengine_volumelevel?branch=master)  
[**KSDATAFORMAT\_DSOUND**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdataformat_dsound?branch=master)  
[**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdataformat_waveformatex?branch=master)  
[**KSDATARANGE\_AUDIO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdatarange_audio?branch=master)  
[**KSDATARANGE\_MUSIC**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdatarange_music?branch=master)  
[**KSDRMAUDIOSTREAM\_CONTENTID**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-ksdrmaudiostream_contentid?branch=master)  
[**KSDSOUND\_BUFFERDESC**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksdsound_bufferdesc?branch=master)  
[**KSDS3D\_BUFFER\_ALL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_buffer_all?branch=master)  
[**KSDS3D\_BUFFER\_CONE\_ANGLES**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_buffer_cone_angles?branch=master)  
[**KSDS3D\_HRTF\_FILTER\_FORMAT\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_hrtf_filter_format_msg?branch=master)  
[**KSDS3D\_HRTF\_INIT\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_hrtf_init_msg?branch=master)  
[**KSDS3D\_HRTF\_PARAMS\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_hrtf_params_msg?branch=master)  
[**KSDS3D\_ITD\_PARAMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_itd_params?branch=master)  
[**KSDS3D\_ITD\_PARAMS\_MSG**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_itd_params_msg?branch=master)  
[**KSDS3D\_LISTENER\_ALL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_listener_all?branch=master)  
[**KSDS3D\_LISTENER\_ORIENTATION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksds3d_listener_orientation?branch=master)  
[**KSJACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537136)  
[**KSJACK\_DESCRIPTION2**](https://msdn.microsoft.com/library/windows/hardware/ff537138)  
[**KSJACK\_SINK\_INFORMATION**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagksjack_sink_information?branch=master)  
[**KSMUSICFORMAT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksmusicformat?branch=master)  
[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksnodeproperty?branch=master)  
[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel?branch=master)  
[**KSP\_DRMAUDIOSTREAM\_CONTENTID**](/windows-hardware/drivers/ddi/content/drmk/ns-drmk-ksp_drmaudiostream_contentid?branch=master)  
[**KSP\_PINMODE**](/windows/win32/Msapofxproxy/ns-msapofxproxy-tagksp_pinmode?branch=master)  
[KSRTAUDIO Structures](ksrtaudio-structures.md)  
[**KSTELEPHONY\_CALLCONTROL**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstelephony_callcontrol?branch=master)  
[**KSTELEPHONY\_CALLINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstelephony_callinfo?branch=master)  
[**KSTELEPHONY\_PROVIDERCHANGE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstelephony_providerchange?branch=master)  
[**KSTOPOLOGY\_ENDPOINTID**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstopology_endpointid?branch=master)  
[**KSTOPOLOGY\_ENDPOINTIDPAIR**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_tagkstopology_endpointidpair?branch=master)  
[**LOOPEDSTREAMING\_POSITION\_EVENT\_DATA**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-loopedstreaming_position_event_data?branch=master)  
[**MDEVICECAPSEX**](/windows/win32/mmddk/ns-mmddk-mdevicecapsex?branch=master)  
[**MIDIOPENDESC**](/windows/win32/mmddk/ns-mmddk-midiopendesc_tag?branch=master)  
[**RTAUDIO\_GETREADPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt169891)  
[**RTAUDIO\_SETWRITEPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt169892)  
[**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-keyworddetectoroemadapter-__midl___midl_itf_keyworddetectoroemadapter_0000_0000_0001?branch=master)  
[**SYNTH\_BUFFER**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synth_buffer?branch=master)  
[**SYNTH\_PORTPARAMS**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synth_portparams?branch=master)  
[**SYNTH\_STATS**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synth_stats?branch=master)  
[**SYNTHCAPS**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synthcaps?branch=master)  
[**SYNTHDOWNLOAD**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synthdownload?branch=master)  
[**SYNTHVOICEPRIORITY\_INSTANCE**](/windows-hardware/drivers/ddi/content/dmusprop/ns-dmusprop-_synthvoicepriority_instance?branch=master)  
[**SYSAUDIO\_ATTACH\_VIRTUAL\_SOURCE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_attach_virtual_source?branch=master)  
[**SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_create_virtual_source?branch=master)  
[**SYSAUDIO\_INSTANCE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_instance_info?branch=master)  
[**SYSAUDIO\_SELECT\_GRAPH**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-sysaudio_select_graph?branch=master)  
[**UNCOMPRESSEDAUDIOFORMAT**](/windows/win32/Audiomediatype/ns-audiomediatype-_uncompressedaudioformat?branch=master)  
[**WAVEFORMATEX**](/windows/win32/mmreg/ns-mmreg-twaveformatex?branch=master)  
[**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-waveformatextensible?branch=master)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audio%20Drivers%20Structures%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



