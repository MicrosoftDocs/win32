---
description: Audio Sessions
ms.assetid: b8a1b656-a582-4112-99e9-bd575719ebb3
title: Audio Sessions
ms.topic: article
ms.date: 05/31/2018
---

# Audio Sessions

An *audio session* is a group of related audio streams that a WASAPI client can manage collectively. Clients can control the volume level and muting state of each individual session. The system applies client-specified volume and mute settings uniformly to all of the streams in the session.

When a client initializes an audio stream, it assigns the audio stream to an audio session. For more information, see [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize).

An audio session contains either rendering streams or capture streams, but not both. By default, the volume and mute settings for a rendering session are persistent across system restarts. The volume and mute settings for a capture session are not persistent. (A session that contains streams that operate in loopback mode is treated the same as a capture session. That is, the session settings are not persistent. For more information about loopback mode, see [Loopback Recording](loopback-recording.md).)

Every audio stream belongs to exactly one session. A client assigns an audio stream to a particular session at the time that it initializes the stream object. The stream retains its membership in the session for the lifetime of the stream. After a stream object is created, the object exists until a client releases the last counted reference to the object, and then the object is deleted.

Although a client cannot change the session to which an existing stream is assigned, it can achieve a similar effect by deleting the stream (by releasing all references to it), creating a new stream to replace the deleted stream, and assigning the new stream to another session.

Each rendering session represents a subset of the streams that form the global mix that plays through a particular [audio endpoint device](audio-endpoint-devices.md). The global mix combines all of the sessions from all of the applications that share the device.

Frequently, an application with several streams assigns all of its streams to the same session. However, the application can, as an option, assign different streams to different sessions. Any stream that the application does not explicitly assign to a session belongs to the default session.

Typical audio applications should avoid modifying the volume and mute settings for sessions. Instead, users control these settings through the user interfaces of control programs. For example, in Windows Vista, the system-supplied program, Sndvol.exe, displays a volume control and mute control for each active or recently active rendering session in the system. Through these controls, users can adjust the volume and mute settings for all of the sessions in the system.

The Sndvol program currently displays volume controls for audio-rendering endpoint devices only. It does not display volume controls for audio-capture devices.

A session is active if it contains one or more active streams. An active stream is in the *running state*. An inactive stream is in the *stopped state*. A session becomes active when its first stream becomes active. A session becomes inactive when its last active stream becomes inactive. After a session has been inactive for a period of time, the system changes the state of the session from inactive to expired.

Sndvol displays volume and mute controls for all active and inactive rendering sessions. Sndvol removes the volume and mute controls for a session when the state of the session changes from inactive to expired, or when the session terminates. (A session terminates when the last of its streams is deleted; that is, when a client releases the final reference count on the last remaining stream object in the session.) The one exception to this rule is for system-notification sounds. Sndvol always displays the volume and mute controls for system-notification sounds regardless of the state of the session for these sounds.

Typically, a stream belongs to a session that spans only the process that contains the application that created the stream. However, applications have the option of defining cross-process sessions that combine streams from two or more processes.

WASAPI supports cross-process sessions primarily so that:

-   The Sndvol program can present the user with a single volume control to manage system-notification sounds across all applications.
-   A media player that runs in one process can stream protected content to a decryption program that runs in another process.

Similar to the control settings for process-specific rendering sessions, the control settings for cross-process rendering sessions are, by default, persistent across system restarts. WASAPI provides this behavior primarily for the benefit of system-notification sounds, which must retain the user's volume and mute settings as the application mix varies over time.

The Sndvol program labels the volume control for each session with a display name and an icon. A client has the option of explicitly assigning a display name and icon to a session. If the client does not provide these items, then Sndvol displays a default name and default icon instead. The default name incorporates information such as the title of the application window. The default icon is the icon for the application window. Only in the case of process-specific sessions do these defaults provide meaningful information to users. Note that a cross-process session can be associated with more than one application. In this case, only a client-provided display name and icon are meaningful.

Although the volume and mute settings for a rendering session are, by default, persistent across system restarts, the client-provided display name and icon are not. To ensure that Sndvol displays the client-provided name and icon, the client must explicitly assign the name and icon to the session at the time that the client assigns the first stream to the session. The system retains the display name and icon for a session only until the session terminates.

Each session is identified by a session GUID. At the time that a client opens a stream, the client assigns that stream to a particular session. The client supplies the following two pieces of information to identify that session:

-   A session GUID.
-   Whether the session is a cross-process or process-specific session—a process-specific session contains only streams from the client's process.

This information is sufficient to distinguish a particular session from all other sessions in the same computer. The session GUID for a process-specific session uniquely identifies the session only within the scope of the process that owns the session. In contrast, the session GUID for a cross-process session is unique within the scope of all of the processes that are running on the computer.

In the case of a process-specific session, the system uses a combination of session GUID and process ID to uniquely identify the session within the scope of the computer. Thus, if clients in two different processes assign their respective streams to two process-specific sessions with identical session GUIDs, the system treats the sessions as separate because their process IDs are different. In addition, if a cross-process session uses the same session GUID as one or more process-specific sessions, the system treats the cross-process session as distinct from the process-specific sessions, even though they share the same session GUID.

For example, in Windows Vista, higher-level APIs such as the Windows multimedia **waveOutXxx** functions and DirectSound typically assign the audio streams that they create to default, process-specific sessions that are identified by the session GUID value GUID\_NULL. For clients of these APIs, the default session for each client process is separate from the default sessions for other client processes, even though the sessions have identical session GUIDs. In addition, if one or more applications assign streams to the cross-process session that is identified by the session GUID value GUID\_NULL, then the system treats this cross-process session as separate from the default, process-specific sessions that share the same session GUID. Accordingly, the Sndvol program displays a separate volume control for each client's default, process-specific session, and it displays an additional volume control for the cross-process session that is identified by the session GUID value GUID\_NULL, if that session exists.

Each session is associated with only one audio endpoint device. If two sessions have identical session GUIDs and process IDs but are associated with different devices, then the system treats the two sessions as separate. A session can never contain both capture and rendering streams because a capture stream can be associated only with a capture device and a rendering stream can be associated only with a rendering device.

As mentioned previously, the volume and mute settings for a session are persistent across system restarts. Two or more instances of an application can create process-specific sessions with identical session GUIDs. Through the Sndvol program, the user can select different volume and mute settings for each of these sessions. After these sessions terminate, the system retains the control settings of only one of these sessions—the last session to terminate. Later, if a new instance of the application creates a process-specific session with the same session GUID as before, that session inherits the previously saved volume and mute settings.

An application should not attempt to add a stream to or control the volume level of a session that is owned by another, unrelated application. In addition, an application should not attempt to control the volume level of the system-managed session for notification sounds. However, an application can play a sound through the system session for notification sounds by calling the **PlaySound** function. For more information, see [Notification Sounds for Legacy Audio Applications](notification-sounds-for-legacy-audio-applications.md).

An application can register to receive notifications when the state of a session changes. For more information, see [Audio Session Events](audio-session-events.md).

In rare cases, an application that creates a process-specific session might need to consolidate the control of the process-specific sessions for two or more application instances under a single volume control in Sndvol. For more information, see [Grouping Parameters](grouping-parameters.md).

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> </dl>

 

 



