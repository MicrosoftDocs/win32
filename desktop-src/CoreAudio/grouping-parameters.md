---
description: Grouping Parameters
ms.assetid: 088156f7-fb75-4fcf-b928-87e97b13bdab
title: Grouping Parameters
ms.topic: article
ms.date: 05/31/2018
---

# Grouping Parameters

A grouping parameter identifies a collection of [audio sessions](audio-sessions.md) that are all controlled by a single volume control in the system volume-control program, Sndvol. The grouping parameter is a GUID that uniquely identifies the collection within the scope of the computer.

The purpose of a grouping parameter is similar to that of the session GUID for a cross-process session. That is, the grouping parameter enables the user to control a collection of streams from any number of processes as a single unit. However, the grouping parameter serves this purpose in circumstances in which cross-process sessions cannot provide a solution.

If several clients assign their respective streams to separate sessions but assign the same grouping parameter to all of the sessions, Sndvol displays a single volume control for these sessions. To provide support for grouping parameters, Sndvol or any similar volume-control application must do the following:

-   Before displaying the volume controls, check the grouping parameters of all the active sessions. Group together under a single volume control all sessions that have the same grouping parameter.
-   When the user changes the setting on a volume control for a particular grouping parameter, update the volume levels of all of the sessions that share that grouping parameter.

Grouping parameters help to reduce the number of volume controls that are displayed by Sndvol. Users might become confused if Sndvol clutters its display with too many controls. Without support for grouping parameters, Sndvol would always display a separate volume control for each session, which might not be appropriate in all circumstances. In addition, grouping parameters provide a convenient way to ensure that sessions that contain similar types of audio content can easily be set to the same volume level.

As explained previously, higher-level audio APIs typically assign their streams to the default, process-specific session (identified by the session GUID value GUID\_NULL). This default enables Sndvol to display a separate volume control for each client application process, which is frequently the desired behavior. Furthermore, if several instances of the same client run in separate processes but require a single, shared volume control, the clients can simply assign their streams to the same cross-process session. Neither of these cases requires the use of grouping parameters. However, one important case, as exemplified by Microsoft Internet Explorer, does require the use of grouping parameters to achieve the desired behavior.

Internet Explorer allows users to open multiple browser windows, and these windows might not all run in the same process. Users might become confused if Sndvol displayed a separate volume control for each application instance, all of which had the same label, "Internet Explorer." A cross-process session is not a feasible solution in this case—if several instances of Internet Explorer run in different processes, they might be unable to assign all of their audio streams to a single cross-process session. The reason is that the Internet Explorer windows might be running instances of Windows Media Player or some other multimedia plug-in that uses a higher-level audio API to play its audio streams. These APIs typically assign the streams in a process to a default, process-specific session. Internet Explorer has no control over the assignment of these streams to sessions.

WASAPI solves this problem by enabling each instance of Internet Explorer to access the session controls for its default, process-specific session and to assign a grouping parameter to that session. If all instances of Internet Explorer assign the same grouping parameter to all of their audio sessions, then Sndvol will display a single volume control for these sessions.

By default, a session does not belong to any grouping. If a client does not explicitly assign a session to a grouping, then Sndvol displays a dedicated volume control for that session. The grouping parameter value GUID\_NULL indicates that a session does not belong to any grouping. If no client has explicitly assigned a grouping parameter to a session, then the grouping parameter value for that session is GUID\_NULL by default.

A client can dynamically change the grouping to which a session is assigned.

A grouping can include any combination of cross-process sessions and process-specific sessions on an [audio endpoint device](audio-endpoint-devices.md).

The Sndvol user interface allows the user to display the volume controls for only one audio endpoint device at a time. When the user adjusts the volume controls for a particular device, the volume levels of sessions that connect to other devices are not affected. In particular, a volume control for a particular grouping parameter affects only sessions that share the grouping parameter and are connected to the currently selected device. A session that happens to have an identical grouping parameter but is connected to another device is not affected.

As described previously, Sndvol labels each volume control that it displays with a display name and icon. In the case of a volume control for a grouping, Sndvol arbitrarily selects one of the sessions in the grouping as the source for the display name and icon that it displays with the volume control. Thus, to ensure that Sndvol always displays the same display name and icon for a grouping, all application instances that assign sessions to that grouping should ensure that their respective sessions have the same display name and icon. For more information about display names and icons, see [Audio Sessions](audio-sessions.md).

An application such as Sndvol can register itself to receive notifications when the grouping parameter for a session changes. Such notifications might be useful if the application caches information about the assignment of sessions to grouping parameters. A notification informs the application that the cached information might no longer be valid.

To assign a grouping parameter to a session, call the [**IAudioSessionControl::SetGroupingParam**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessioncontrol-setgroupingparam) method. To obtain the grouping parameter that is assigned to a session, call the [**IAudioSessionControl::GetGroupingParam**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessioncontrol-getgroupingparam) method.

## Related topics

<dl> <dt>

[Audio Sessions](audio-sessions.md)
</dt> </dl>

 

 



