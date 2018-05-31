---
title: Stream Buffer Source Filter Enhancements in Windows 7
description: Stream Buffer Source Filter Enhancements in Windows 7
ms.assetid: af6262c5-391c-4248-9f96-26bd108b0fdf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffer Source Filter Enhancements in Windows 7

The Stream Buffer Engine (SBE) version 2 (SBE2) in Windows 7 offers several enhancements to the [Stream Buffer Source](stream-buffer-source-filter.md) filter that was shipped with previous versions of Windows. These enhancements allow the filter to handle features that are supported by the new TV Recording File Format (.WTV) that were not available in the .DVR-MS file format:

-   Dynamic addition and removal of audio, video, and data streams
-   Dynamic format changes to audio and video streams within a recording, including:
    -   Multiple video angles (for example, for a broadcast soccer game)
    -   Multiple languages
    -   Multiple streams with interactive TV data
-   Enhanced metadata that is required for content protection, interactive TV, and dynamic stream support
-   Enhanced recording for files, with more robust recovery

The [Stream Buffer Source](stream-buffer-source-filter.md) filter improvements in SBE2 give developers full access to these features through the following new interfaces, which are discussed in the following sections:



| Interface                                              | Functions                                                                                                                                                               |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISBE2Crossbar**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2crossbar)                 | Enumerates the streams in a WTV file; sets or changes profiles, stream mappings, and default modes for a [Stream Buffer Source](stream-buffer-source-filter.md) filter |
| [**ISBE2EnumStream**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2enumstream)             | Enumerates the streams discovered in a WTV file                                                                                                                         |
| [**ISBE2MediaTypeProfile**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2mediatypeprofile) | Manages the media streams in a profile                                                                                                                                  |
| [**ISBE2StreamMap**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2streammap)               | Manages stream mappings for a [Stream Buffer Source](stream-buffer-source-filter.md) filter                                                                            |



 

**Multiple Stream Support in the Stream Buffer Source Filter**

This section describes how to manage multiple streams within a WTV file using the new functionality of the [Stream Buffer Source](stream-buffer-source-filter.md) filter.

The [Stream Buffer Source](stream-buffer-source-filter.md) filter typically has one output pin per media type (for example, audio or video). Thus, if a file contains more than one steam of a certain media type, matching between a stream of a specific media type and a pin of the appropriate media type is needed. Such matching is referred to as *stream mapping*. The application can define a set of Stream Buffer Source filter output pins, referred to as an *output profile*, to override the default set. For example, this set can be used in order to limit output pins to audio and video only. This functionality is achieved through several new interfaces that are exposed by the Stream Buffer Source filter and its output pins.

### Setting Defaults, Output Profiles, and Stream Mappings

When the [Stream Buffer Source](stream-buffer-source-filter.md) filter is initialized with a WTV file, it can expose pins in one of two ways:

-   As described in the default output profile that present in the file. This profile is defined when the WTV file is first created.
-   As specified in an application-provided output profile.

When the [Stream Buffer Source](stream-buffer-source-filter.md) filter reads streams from a WTV file, it needs to know which pin to use for sending out each stream. Thus, the stream mapping is essential for the Source Buffer Source to be able to send sample data. The Stream Buffer Source filter can operate in one of two stream mapping modes:

-   *Default streams* mode, in which the filter maps streams to output pins automatically, following internal logic.
-   A mode where mapping is controlled by an application.

The [**ISBE2Crossbar**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2crossbar) interface, which is exposed by the [Stream Buffer Source](stream-buffer-source-filter.md) filter, is used to set these two important modes.

Applications can call the [**ISBE2Crossbar::EnableDefaultMode**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2crossbar-enabledefaultmode) method to set profile mode, stream mapping mode, or both. Use either or both of the following flags in the **EnableDefaultMode** call to explicitly set the default modes that you want to enable:



| Flags                                            | Effects                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[none\]                                         | Disables both profile and streams default mode. The application must set an output profile (using the [**ISBE2Crossbar::SetOutputProfile**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2crossbar-setoutputprofile) method) and stream mappings (using the [**ISBE2StreamMap::MapStream**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2streammap-mapstream) method). |
| **DEF\_MODE\_PROFILE**                           | Enables profile default mode, disables streams default mode. The application cannot change output profiles but can specify new stream mappings while the graph is running.                                                                                                                    |
| **DEF\_MODE\_STREAMS**                           | Enables streams default mode, disables profile default mode. The application cannot change stream mappings but must specify a new output profiles.                                                                                                                                            |
| **DEF\_MODE\_PROFILE** \| **DEF\_MODE\_STREAMS** | Enables both profile and streams default mode. The application cannot change output profiles or specify new stream mappings.                                                                                                                                                                  |



 

If the application does not call [**EnableDefaultMode**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2crossbar-enabledefaultmode), both default streams and default profile modes are enabled.

### Stream Mapping Modes: Default

In default streams mode, the [Stream Buffer Source](stream-buffer-source-filter.md) filter uses the following logic to map streams to output pins:

1.  For all streams with media type (major) other than **MEDIATYPE\_Audio**, the Stream Buffer Source filter maps the default stream for each media type to an output pin with a matching media type. The default stream is a stream that has the Default member set to **TRUE** in its [**DVR\_STREAM\_DESC**](/previous-versions/windows/desktop/api/sbe/ns-sbe-__midl___midl_itf_sbe_0000_0015_0002) structure.
2.  For audio streams (**MEDIATYPE\_Audio**), language-based mapping logic is applied. The languages are defined for audio streams by an in-band spanning event with an ID of **EVENTID\_LanguageSpanningEvent**. First, the user-preferred language used for mapping is determined using the following steps:
    1.  If a preferred language is set in Windows Media Center, that language is used.
    2.  If no preferred language is set in Windows Media Center, the default language for Windows is used. The [**GetUserDefaultLangID**](https://msdn.microsoft.com/library/windows/desktop/dd318134) function returns the default language for Windows.

    Once the preferred language has been determined, the following logic determines the audio stream mapping:
    1.  An attempt is made to map an audio stream that matches the preferred language.
    2.  If no matching audio stream is found, the default audio stream is mapped.

If streams are deleted and/or created during the playback of a WTV file, the [Stream Buffer Source](stream-buffer-source-filter.md) filter maps or remaps streams as appropriate. In some cases, media types can change dynamically as a result of stream mappings. An example of such a case is a TV recording that has a commercial with MPEG-1 audio and has a new Dolby AC-3 audio stream created dynamically while the original MPEG-1 audio stream is deleted.

### **Default Stream Mapping Modes: Application-Defined**

In application-defined stream mapping mode, the application performs stream mapping according to application-specific logic. It is important to remember that in this mode the [Stream Buffer Source](stream-buffer-source-filter.md) filter does not perform any automatic stream mappings, so the application must map all streams that it wants the Stream Buffer Source filter to send through its output pins. Unmapped streams are discarded while a WTV file is being read so that they do not interfere with mapped stream output. Similarly, Stream Buffer Source filter output pins that are not mapped to streams do not interfere with output from other output pins.

In order for an application to map a specific stream to a specific pin, the application should use the [**ISBE2StreamMap**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2streammap) interface that is exposed by that pin. The application calls the [**ISBE2StreamMap::MapStream**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2streammap-mapstream) method with the stream ID of the desired stream to map that stream to a pin. The stream ID argument uniquely identifies the stream within the [Stream Buffer Source](stream-buffer-source-filter.md) filter. It can be obtained from the [**DVR\_STREAM\_DESC**](/previous-versions/windows/desktop/api/sbe/ns-sbe-__midl___midl_itf_sbe_0000_0015_0002) structure, which is received from the Stream Buffer Source filter and signaled by and event with an ID of **SBE2\_STREAM\_DESC\_EVENT**.

**Stream Mapping Modes: Examples**

The following pseudocode illustrates how an application can map audio streams based on a preferred language. The examples use helper functions, whose functionality is described within the pseudocode.

The following method configures the [Stream Buffer Source](stream-buffer-source-filter.md) filter to disable default stream mapping.


```C++
ApplicationClass::InitializeSBESourceFilter(IBaseFilter* pSBESourceFilter)
{
    CComQIPtr <ISBE2Crossbar> spSBECrossBar = pSBESourceFilter;
    
    // Disable default stream mapping in SBE, only leave default profile.
    spSBECrossBar->EnableDefaultMode(DEF_MODE_PROFILE);
}
```



The following method receives spanning and broadcast events, and performs stream mapping.


```C++
ApplicationClass::FireEx (GUID EventID, ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4)
{
    if (IsEqualGUID( EventID, SBE2_STREAM_DESC_EVENT ) || 
        IsEqualGUID( EventID, EVENTID_LanguageSpanningEvent)
    )
    {
            CComQIPtr<ISBE2GlobalEvent> spSBE2GlobalEvent = m_pSBESourceFilter;

        BYTE* pEventPayload = NULL;
        DWORD dwEventSize = 0;
        BOOL fSpanning = FALSE;

        spSBE2GlobalEvent->GetEvent(
                EventID, Param1, Param2, Param3, Param4, &amp;fSpanning, 
                &amp;dwEventSize, NULL);
        
        if (dwEventSize != 0) 
        {
            pEventPayload = new BYTE[dwEventSize];
            spSBE2GlobalEvent->GetEvent(EventID,  Param1, Param2, 
                    Param3, Param4, &amp;fSpanning, &amp;dwEventSize, 
                reinterpret_cast<BYTE *> (pEventPayload));
        }
        else
        {
            // Spanning event with zero payload - spanning event cancellation.
        }

        if (IsEqualGUID( EventID, SBE2_STREAM_DESC_EVENT ))
        {   
            OnStreamEvent( reinterpret_cast<DVR_STREAM_DESC*>(pEventPayload) );
        }
        else if (IsEqualGUID( EventID, EVENTID_LanguageSpanningEvent ))
        {
            OnLanguageEvent((SBE2_STREAM_ID)Param3, 
               reinterpret_cast<const LanguageInfo*>(pEventPayload));
        }
    }
}

```



The following method handles stream events:


```C++
ApplicationClass::OnStreamEvent(const DVR_STREAM_DESC* pDesc)
{
    if (pDesc->Creation)
    {
        // Stream is created. 

    // Helper method, that adds stream information to application 
// internal state variables.
        AddStream (pDesc->StreamId, pDesc);

        // Map all streams except audio here. For audio we wait till we get a language event.
        if (pDesc->MediaType.majortype != MEDIATYPE_Audio)
        {
            // Attempts to map default stream of this media type to matching pin.
            MapDefaultStream(pDesc->MediaType.majortype);
        }
    }
    else 
    {
        // Stream is deleted. 
        // If this stream was mapped, Stream Buffer Source filter automatically 
        // unmapped this stream and we need to map another stream.
        
        // IsStreamMapped is a helper method that queries internal state variables
        // and returns 'true' if this stream is mapped.
        
        if (IsStreamMapped(pDesc->StreamId))
        {
            UnMapStream(pDesc->MediaType.majortype);

            if (pDesc->MediaType.majortype != MEDIATYPE_Audio)
            {
                // Attempt to map default stream of this media type to matching pin.
                MapDefaultStream(pDesc->MediaType.majortype);
            }
            else 
            {
                // Follow special logic for audio streams
                MapAudioStream();
            }
        }
    
// Helper method, that removes stream information from application 
// internal state variables.
        RemoveStream(pDesc->StreamId);
    }
}

```



The following method handles a language stream event:


```C++
ApplicationClass::OnLanguageEvent(SBE2_STREAM_ID StreamId, const LanguageInfo* pLanguageInfo)
{
    // Helper method, that updates stream information with received language info 
    // within internal state variables.
    UpdateStream(StreamId, pLanguageInfo);
  
    // Attempt to map audio based on updated language information
    MapAudioStream();
}
```



The following method performs the logic needed to map a default stream for a major type:


```C++
ApplicationClass::MapDefaultStream(GUID MajorType)
{
    // GetMappedStream is a helper method that, based on internal state variables,
    // returns either the stream ID of a mapped stream with matching major type or
    // zero if no stream is mapped with matching major type.
    
    // GetDefaultStream is a helper method, that based on internal state variables,
    // returns stream ID of a default stream for a matching major type or
    // zero if no default stream is yet discovered with matching major type.

    // GetStream is a helper method that, based on internal state variables,
    // returns the stream ID of the first discovered stream for a matching major type.
    // This stream is used as a fallback if no default stream is found.

    SBE2_STREAM_ID MappedStreamId = GetMappedStream(MajorType);
    SBE2_STREAM_ID DefaultStreamId = GetDefaultStream(MajorType);
    SBE2_STREAM_ID FallbackStreamId = GetStream(MajorType);

    if (DefaultStreamId != 0)
    {
        // Found a default stream - 
        // should we unmap previously mapped non-default stream?
        if (MappedStreamId != 0)
        {
            if (MappedStreamId != DefaultStreamId)
            {
                UnMapStream(MajorType);

                MapStream(DefaultStreamId, MajorType);
            }
            else
            {
                // done - already mapped stream is default.
            }
        }
        else
        {
            // No previously mapped streams - map this default stream.
            MapStream(DefaultStreamId, MajorType);
        }
    }
    else if (MappedStreamId == 0)
    {
        // no default stream, and no stream mapped for this major type - map fallback stream.
        MapStream(FallbackStreamId, MajorType);
    }

    // Application may choose to map only default streams to simplify the preceding logic.
}
```



The following method performs the logic needed to map an audio stream, based on internal application logic for language selection.


```C++
 ApplicationClass::MapAudioStream()
{
    // FindAudioStreamByLanguage is a helper method that, based on internal state variables
    // and internal logic, returns the stream ID of an audio stream with matching language,
    // as signaled by an EVENTID_LanguageSpanningEvent event.

    SBE2_STREAM_ID PreferredLangStreamID = FindAudioStreamByLanguage(m_PreferredLanguageId);
    SBE2_STREAM_ID MappedAudioStream = GetMappedStream(MEDIATYPE_Audio);

    if (PreferredLangStreamID != 0)
    {
        if (MappedAudioStream == PreferredLangStreamID)
        {
            // no op, mapped stream already has the language we need.
        }
        else 
        {
            if (MappedAudioStream != 0)
            {
                // Mapped stream is not what we want.
                UnMapStream(MEDIATYPE_Audio);
            }

            MapStream(PreferredLangStreamID, MEDIATYPE_Audio);
        }
    }
    else 
    {
        // Could not find stream with preferred language, fallback to default audio stream
        MapDefaultStream(MEDIATYPE_Audio);
    }
}
```



The following two methods perform low-level stream mapping and unmapping on [Stream Buffer Source](stream-buffer-source-filter.md) filter output pins.


```C++
ApplicationClass::MapStream(SBE2_STREAM_ID StreamId, GUID MajorType)
{
    // FindSBEPinByMajorType is a helper method that 
    // returns an output SBE Source Filter pin (return type is IPin*) by matching major type.

    CComQIPtr<ISBE2StreamMap> spPinMap = FindSBEPinByMajorType(MajorType);

    spPinMap->MapStream(StreamId);
    
    // UpdateStreamMapping is a helper method that updates internal state variables
    // with the stream mapping state. Second parameter of 0 means stream is unmapped.
    
    UpdateStreamMapping(MajorType, StreamId);
}

ApplicationClass::UnMapStream (GUID MajorType)
{
    CComQIPtr<ISBE2StreamMap> spPinMap = FindSBEPinByMajorType(MajorType);

    SBE2_STREAM_ID MappedStreamId = GetMappedStream(MajorType);

    spPinMap->UnmapStream(MappedStreamId);
    
    UpdateStreamMapping(MajorType, 0);
}
```



## Related topics

<dl> <dt>

[**ISBE2Crossbar**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2crossbar)
</dt> <dt>

[**ISBE2Crossbar::SetOutputProfile**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2crossbar-setoutputprofile)
</dt> <dt>

[**ISBE2StreamMap::MapStream**](/previous-versions/windows/desktop/api/sbe/nf-sbe-isbe2streammap-mapstream)
</dt> <dt>

[Stream Buffer Source Filter](stream-buffer-source-filter.md)
</dt> </dl>

 

 




