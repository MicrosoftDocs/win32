---
description: Session Volume Controls
ms.assetid: e6d112f9-08c9-4d95-b37b-267beebd0d7f
title: Session Volume Controls
ms.topic: article
ms.date: 05/31/2018
---

# Session Volume Controls

As explained previously, WASAPI clients can individually control the volume level of each [audio session](audio-sessions.md). WASAPI applies the volume setting for a session uniformly to all of the streams in the session. Each volume level is a value in the range 0.0 to 1.0, where 0.0 indicates silence and 1.0 indicates full volume (no attenuation).

A client implicitly creates a session by assigning the first stream to that session. The default volume level of the new session is 1.0. As discussed previously, the user can adjust the volume level of the session through the user interface of a control program (for example, Sndvol) that is a WASAPI client. The control settings are persistent.

In addition to the client-controlled volume settings, the system applies its own volume settings to sessions. These settings are based on audio policy and change dynamically in response to changes in the streams that make up the global audio mix. For more information about audio policy, see [User-Mode Audio Components](user-mode-audio-components.md).

The system software that implements the volume control for each stream multiplies the PCM samples in the stream by the effective volume level. The effective volume level is the result of multiplying the client and system volume settings. Thus, the resulting change in signal amplitude is a linear combination of the client and system volume levels. For example, if the client volume level is 0.8 and the system volume level is 0.5, the effective volume level is (0.8)<sup>.</sup>(0.5) = 0.4.

Note that perceived loudness is not linear with respect to signal amplitude. Instead, loudness varies approximately as the logarithm of the volume level v:

loudness in decibels = 20<sup>.</sup>log₁₀(v)

Thus, setting v = 0.5 attenuates the loudness of the original signal (the signal before the volume level is applied) by 6 decibels, setting v = 0.25 attenuates the signal by 12 decibels, and so on. A volume level v = 1.0, corresponding to 0 decibels, does not alter the original signal level.

Audio applications with user interfaces for controlling the volume level typically display sliders that generate changes in perceived loudness that are linearly proportional to changes in slider position. To produce a linear relationship between perceived loudness and slider position, the application must define a nonlinear relationship between the volume level v and the slider position. For more information, see [Audio-Tapered Volume Controls](audio-tapered-volume-controls.md).

As explained previously, the system volume-control program, Sndvol, displays volume sliders for the audio sessions that are playing on each audio rendering device. These sliders appear in the group box labeled **Applications** in the SndVol window. Typically, each session contains all of the playback streams from a particular application window. Through the sliders in the Sndvol window, users control the volume levels of individual audio applications.

As a general rule, an application should assign all of its playback streams to the same audio session. WASAPI does not prevent an application from distributing its playback streams among multiple sessions. However, the resulting proliferation of volume sliders in Sndvol might confuse users.

As an option, an application window can display a volume slider. The application slider should reflect the state of the corresponding Sndvol slider at all times. Thus, if the user changes the volume level by moving the slider in the application window, then the corresponding slider in the Sndvol window should move in unison with the application slider. Similarly, if the user moves the Sndvol slider, then the application slider should move in unison with the Sndvol slider.

To support this behavior, WASAPI implements the [**ISimpleAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-isimpleaudiovolume) interface. When the user moves the application slider, the application calls the [**ISimpleAudioVolume::SetMasterVolume**](/windows/desktop/api/Audioclient/nf-audioclient-isimpleaudiovolume-setmastervolume) method to adjust the session volume level accordingly. Sndvol monitors volume changes made through this method and reflects the changes in the volume sliders that it displays. In addition, an application can receive notifications of session volume changes that the user makes through Sndvol. For this purpose, the application implements an [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface and registers the interface with WASAPI. Thereafter, each time the user changes the session volume level through Sndvol, the application receives a notification call through the [**IAudioSessionEvents::OnSimpleVolumeChanged**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessionevents-onsimplevolumechanged) method. For a code example that implements an **IAudioSessionEvents** interface, see [Audio Session Events](audio-session-events.md). For a code example that registers an **IAudioSessionEvents** interface, see [Audio Events for Legacy Audio Applications](audio-events-for-legacy-audio-applications.md).

The **ISimpleAudioVolume** interface applies the same volume level uniformly to all of the channels in an audio session. Although this interface should satisfy the volume-control requirements of most applications, a few applications might require more specialized volume-control capabilities. The [**IAudioStreamVolume**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiostreamvolume) interface controls the volume of an individual stream in a session relative to the other streams in the session. **IAudioStreamVolume** also enables a client to individually control the volume levels of all the channels in the stream. For example, an application might use this capability to achieve audio effects such as simulating spatial movement of an audio source by panning from left to right. Another specialized interface, [**IChannelAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-ichannelaudiovolume), controls the volume levels of the individual channels in a session. For example, an application might use **IChannelAudioVolume** to implement balance controls for a stereophonic sound system.

The volume sliders in the **Applications** box in Sndvol reflect only volume changes that are made through the **ISimpleAudioVolume** interface. They do not reflect volume changes that are made through the **IAudioStreamVolume** and **IChannelAudioVolume** interfaces. Although some applications might enable users to directly or indirectly control volume settings through **IAudioStreamVolume** and **IChannelAudioVolume**, developers should avoid presenting application sliders for these volume settings that users are likely to confuse with the volume sliders in Sndvol. Otherwise, a user might move an application slider expecting to see the change reflected in a Sndvol slider and become confused when no such change occurs. Developers can avoid this problem through careful user interface design.

The effective volume level of any channel in the session submix, as heard at the speakers, is the product of the following four volume-level factors:

-   The per-channel volume levels of the streams in the session, which clients can control through the methods in the **IAudioStreamVolume** interface.
-   The per-channel volume level of the session, which clients can control through the methods in the **IChannelAudioVolume** interface.
-   The master volume level of the session, which clients can control through the methods in the **ISimpleAudioVolume** interface.
-   The policy-based volume level of the session, which the system dynamically modifies as the global mix changes.

Each of the four volume-level factors in the preceding list is a value in the range 0.0 to 1.0, where 0.0 indicates silence and 1.0 indicates full volume (no attenuation). The effective volume level is also a value in the range 0.0 to 1.0.

The audio engine applies the effective volume level for each channel to the channels in a stream before mixing the stream with the other streams in the audio session. If any sample values in a channel exceed 0 decibels after the audio engine has multiplied them by the effective volume level, the engine clips the samples before adding them to the session submix.

## Related topics

<dl> <dt>

[Volume Controls](volume-controls.md)
</dt> </dl>

 

 



