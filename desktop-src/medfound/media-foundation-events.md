---
description: Media Foundation Events
ms.assetid: d925f63d-3359-4ba1-802f-0c2b11a3f973
title: Media Foundation Events
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Events



| Event                                                                                        | Description                                                                                                                                              |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MEAudioSessionDeviceRemoved](meaudiosessiondeviceremoved.md)                               | The audio device was removed.                                                                                                                            |
| [MEAudioSessionDisconnected](meaudiosessiondisconnected.md)                                 | The audio session was disconnected from a Windows Terminal Services session                                                                              |
| [MEAudioSessionExclusiveModeOverride](meaudiosessionexclusivemodeoverride.md)               | The audio session was preempted by an exclusive-mode connection.                                                                                         |
| [MEAudioSessionFormatChanged](meaudiosessionformatchanged.md)                               | The default audio format for the audio device changed.                                                                                                   |
| [MEAudioSessionGroupingParamChanged](meaudiosessiongroupingparamchanged.md)                 | The grouping parameters changed for the audio session.                                                                                                   |
| [MEAudioSessionIconChanged](meaudiosessioniconchanged.md)                                   | The audio session icon changed.                                                                                                                          |
| [MEAudioSessionNameChanged](meaudiosessionnamechanged.md)                                   | The audio session display name changed.                                                                                                                  |
| [MEAudioSessionServerShutdown](meaudiosessionservershutdown.md)                             | The Windows audio server system was shut down.                                                                                                           |
| [MEAudioSessionVolumeChanged](meaudiosessionvolumechanged.md)                               | The volume or mute state of the audio session changed                                                                                                    |
| [MEBufferingStarted](mebufferingstarted.md)                                                 | A media source started to buffer data.                                                                                                                   |
| [MEBufferingStopped](mebufferingstopped.md)                                                 | A media source stopped buffering data.                                                                                                                   |
| [MECaptureAudioSessionDeviceRemoved](mecaptureaudiosessiondeviceremoved.md)                 | The device was removed.                                                                                                                                  |
| [MECaptureAudioSessionDisconnected](mecaptureaudiosessiondisconnected.md)                   | The audio session is disconnected because the user logged off from a Windows Terminal Services (WTS) session.                                            |
| [MECaptureAudioSessionExclusiveModeOverride](mecaptureaudiosessionexclusivemodeoverride.md) | The user opened an audio stream in exclusive mode.                                                                                                       |
| [MECaptureAudioSessionFormatChanged](mecaptureaudiosessionformatchanged.md)                 | The audio format changed.                                                                                                                                |
| [MECaptureAudioSessionServerShutdown](mecaptureaudiosessionservershutdown.md)               | The audio session server shutdown.                                                                                                                       |
| [MECaptureAudioSessionVolumeChanged](mecaptureaudiosessionvolumechanged.md)                 | The volume changed.                                                                                                                                      |
| [MEConnectEnd](meconnectend.md)                                                             | The network source finished opening a URL.                                                                                                               |
| [MEConnectStart](meconnectstart.md)                                                         | The network source started opening a URL.                                                                                                                |
| [MEContentProtectionMessage](mecontentprotectionmessage.md)                                 | The configuration changed for an output protection scheme.                                                                                               |
| [MEEnablerCompleted](meenablercompleted.md)                                                 | A content enabler object's action is complete.                                                                                                           |
| [MEEnablerProgress](meenablerprogress.md)                                                   | Signals the progress of a content enabler object.                                                                                                        |
| [MEEndOfPresentation](meendofpresentation.md)                                               | Raised by a media source when a presentation ends.                                                                                                       |
| [MEEndOfPresentationSegment](meendofpresentationsegment.md)                                 | Raised by the sequencer source when a segment is completed and is followed by another segment.                                                           |
| [MEEndOfStream](meendofstream.md)                                                           | Raised by a media stream when the stream ends.                                                                                                           |
| [MEError](meerror.md)                                                                       | Signals a serious error.                                                                                                                                 |
| [MEExtendedType](meextendedtype.md)                                                         | Custom event type.                                                                                                                                       |
| [MEIndividualizationCompleted](meindividualizationcompleted.md)                             | Individualization is complete.                                                                                                                           |
| [MEIndividualizationStart](meindividualizationstart.md)                                     | Individualization is about to begin.                                                                                                                     |
| [MELicenseAcquisitionCompleted](melicenseacquisitioncompleted.md)                           | License acquisition is complete.                                                                                                                         |
| [MELicenseAcquisitionStart](melicenseacquisitionstart.md)                                   | License acquisition is about to begin.                                                                                                                   |
| [MEMediaSample](memediasample.md)                                                           | Raised when a media stream delivers a new sample.                                                                                                        |
| [MENewPresentation](menewpresentation.md)                                                   | Raised by a media source a new presentation is ready.                                                                                                    |
| [MENewStream](menewstream.md)                                                               | Raised by a media source when it starts a new stream.                                                                                                    |
| [MENonFatalError](menonfatalerror.md)                                                       | A non-fatal error occurred during streaming.                                                                                                             |
| [MEPolicyChanged](mepolicychanged.md)                                                       | The output policy for a stream changed.                                                                                                                  |
| [MEPolicyError](mepolicyerror.md)                                                           | Raised by a trusted output if an error occurs while enforcing the output policy.                                                                         |
| [MEPolicyReport](mepolicyreport.md)                                                         | Contains status information about the enforcement of an output policy.                                                                                   |
| [MEPolicySet](mepolicyset.md)                                                               | The [**IMFOutputTrustAuthority::SetPolicy**](/windows/desktop/api/mfidl/nf-mfidl-imfoutputtrustauthority-setpolicy) method completed.                                                    |
| [MEQualityNotify](mequalitynotify.md)                                                       | Provides feedback about playback quality to the quality manager.                                                                                         |
| [MEReconnectEnd](mereconnectend.md)                                                         | Raised by a media source at the end of a reconnection attempt.                                                                                           |
| [MEReconnectStart](mereconnectstart.md)                                                     | Raised by a media source at the start of a reconnection attempt.                                                                                         |
| [MERendererEvent](merendererevent.md)                                                       | Raised by the enhanced video renderer (EVR) when it receives a user event from the presenter.                                                            |
| [MESequencerSourceTopologyUpdated](mesequencersourcetopologyupdated.md)                     | Raised by the sequencer source when the [**IMFSequencerSource::UpdateTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-updatetopology) method completes asynchronously. |
| [MESessionCapabilitiesChanged](mesessioncapabilitieschanged.md)                             | Raised by the Media Session when the session capabilities change.                                                                                        |
| [MESessionClosed](mesessionclosed.md)                                                       | Raised when the [**IMFMediaSession::Close**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-close) method completes asynchronously.                                                 |
| [MESessionEnded](mesessionended.md)                                                         | Raised by the Media Session when it has finished playing the last presentation in the playback queue.                                                    |
| [MESessionNotifyPresentationTime](mesessionnotifypresentationtime.md)                       | Raised by the Media Session when a new presentation starts.                                                                                              |
| [MESessionPaused](mesessionpaused.md)                                                       | Raised when the [**IMFMediaSession::Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-pause) method completes asynchronously.                                                 |
| [MESessionRateChanged](mesessionratechanged.md)                                             | Raised by the Media Session when the playback rate changes.                                                                                              |
| [MESessionScrubSampleComplete](mesessionscrubsamplecomplete.md)                             | Raised by the Media Session when it completes a scrubbing request.                                                                                       |
| [MESessionStarted](mesessionstarted.md)                                                     | Raised when the [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) method completes asynchronously.                                                 |
| [MESessionStopped](mesessionstopped.md)                                                     | Raised when the [**IMFMediaSession::Stop**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-stop) method completes asynchronously.                                                   |
| [MESessionStreamSinkFormatChanged](mesessionstreamsinkformatchanged.md)                     | Raised by the Media Session when the format changes on a media sink.                                                                                     |
| [MESessionTopologiesCleared](mesessiontopologiescleared.md)                                 | Raised by the Media Session when the [**IMFMediaSession::ClearTopologies**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-cleartopologies) method completes asynchronously.        |
| [MESessionTopologySet](mesessiontopologyset.md)                                             | Raised after the [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) method completes asynchronously                                     |
| [MESessionTopologyStatus](mesessiontopologystatus.md)                                       | Raised by the Media Session when the status of a topology changes.                                                                                       |
| [MESinkInvalidated](mesinkinvalidated.md)                                                   | Raised when a media sink becomes invalid.                                                                                                                |
| [MESourceCharacteristicsChanged](mesourcecharacteristicschanged.md)                         | Raised by a media source when the source's characteristics change.                                                                                       |
| [MESourceMetadataChanged](mesourcemetadatachanged.md)                                       | Raised by a media source when it updates its metadata.                                                                                                   |
| [MESourcePaused](mesourcepaused.md)                                                         | Raised by a media source when the [**IMFMediaSource::Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause) method completes asynchronously.                                 |
| [MESourceRateChanged](mesourceratechanged.md)                                               | Raised by a media source when the playback rate changes.                                                                                                 |
| [MESourceRateChangeRequested](mesourceratechangerequested.md)                               | Raised by a media source to request a new playback rate.                                                                                                 |
| [MESourceSeeked](mesourceseeked.md)                                                         | Raised when a media source seeks to a new position.                                                                                                      |
| [MESourceStarted](mesourcestarted.md)                                                       | Raised when a media source starts without seeking.                                                                                                       |
| [MESourceStopped](mesourcestopped.md)                                                       | Raised by a media source when the [**IMFMediaSource::Stop**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-stop) method completes asynchronously.                                   |
| [MEStreamFormatChanged](mestreamformatchanged.md)                                           | Raised by a media stream when the media type of the stream changes.                                                                                      |
| [MEStreamPaused](mestreampaused.md)                                                         | Raised by a media stream when the [**IMFMediaSource::Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause) method completes asynchronously.                                 |
| [MEStreamSeeked](mestreamseeked.md)                                                         | Raised by a media stream after a call to [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) causes a seek in the stream.                              |
| [MEStreamSinkDeviceChanged](mestreamsinkdevicechanged.md)                                   | Raised by the stream sinks of the EVR if the video device changes.                                                                                       |
| [MEStreamSinkFormatChanged](mestreamsinkformatchanged.md)                                   | Raised by a stream sink when the sink's media type is no longer valid.                                                                                   |
| [MEStreamSinkMarker](mestreamsinkmarker.md)                                                 | Raised by a stream sink after the [**IMFStreamSink::PlaceMarker**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamsink-placemarker) method is called.                                      |
| [MEStreamSinkPaused](mestreamsinkpaused.md)                                                 | Raised by a stream sink when it completes the transition to the paused state.                                                                            |
| [MEStreamSinkPrerolled](mestreamsinkprerolled.md)                                           | Raised by a stream sink when the stream has received enough preroll data to begin rendering.                                                             |
| [MEStreamSinkRateChanged](mestreamsinkratechanged.md)                                       | Raised by a stream sink when the rate has changed.                                                                                                       |
| [MEStreamSinkRequestSample](mestreamsinkrequestsample.md)                                   | Raised by a stream sink to request a new media sample from the pipeline.                                                                                 |
| [MEStreamSinkScrubSampleComplete](mestreamsinkscrubsamplecomplete.md)                       | Raised by a stream sink when it completes a scrubbing request.                                                                                           |
| [MEStreamSinkStarted](mestreamsinkstarted.md)                                               | Raised by a stream sink when it completes the transition to the running state.                                                                           |
| [MEStreamSinkStopped](mestreamsinkstopped.md)                                               | Raised by a stream sink when it completes the transition to the stopped state.                                                                           |
| [MEStreamStarted](mestreamstarted.md)                                                       | Raised by a media stream when the source starts without seeking.                                                                                         |
| [MEStreamStopped](mestreamstopped.md)                                                       | Raised by a media stream when the [**IMFMediaSource::Stop**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-stop) method completes asynchronously.                                   |
| [MEStreamThinMode](mestreamthinmode.md)                                                     | Raised by a media stream when it starts or stops thinning the stream.                                                                                    |
| [MEStreamTick](mestreamtick.md)                                                             | Signals that a media stream does not have data available at a specified time.                                                                            |
| [METransformDrainComplete](metransformdraincomplete.md)                                     | Sent by an asynchronous Media Foundation transform (MFT) when a drain operation is complete.                                                             |
| [METransformHaveOutput](metransformhaveoutput.md)                                           | Sent by an asynchronous MFT when new output data is available from the MFT.                                                                              |
| [METransformMarker](metransformmarker.md)                                                   | Sent by an asynchronous MFT in response to an [**MFT\_MESSAGE\_COMMAND\_MARKER**](mft-message-command-marker.md) message.                               |
| [METransformNeedInput](metransformneedinput.md)                                             | Sent by an asynchronous MFT to request a new input sample.                                                                                               |
| [MEUnknown](meunknown.md)                                                                   | Unknown event type.                                                                                                                                      |
| [MEUpdatedStream](meupdatedstream.md)                                                       | Raised by a media source when it restarts or seeks a stream that is already active.                                                                      |
| [MEVideoCaptureDevicePreempted](mevideocapturedevicepreempted.md)                           | The device has been preempted.                                                                                                                           |
| [MEVideoCaptureDeviceRemoved](mevideocapturedeviceremoved.md)                               | The device has been removed.                                                                                                                             |



 

## Related topics

<dl> <dt>

[Media Foundation Programming Reference](media-foundation-programming-reference.md)
</dt> <dt>

[Media Event Generators](media-event-generators.md)
</dt> <dt>

[**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator)
</dt> </dl>

 

 



