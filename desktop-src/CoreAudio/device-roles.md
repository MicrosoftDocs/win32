---
description: Device Roles
ms.assetid: aa787004-0d3e-448b-80dd-92055f841aee
title: Device Roles
ms.topic: article
ms.date: 05/31/2018
---

# Device Roles

If a system contains two or more audio-rendering endpoint devices, then one device might be best for playing one type of audio content, and another device might be best for playing another type of content. For example, if a system has two rendering devices, the user might choose to play music on one device and to play system notification sounds on the other.

Similarly, if a system contains two or more audio-capture endpoint devices, then one device might be best for capturing one type of audio content, and another device might be best for capturing another type of content. For example, if a system has two capture devices, the user might choose to record live music on one device and to use the other device for voice commands.

Devices can have three roles: Console, Communications, and Multimedia.The following table describes the device roles identified by the three constants—eConsole, eCommunications, and eMultimedia—in the [**ERole**](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-erole) enumeration.



| ERole constant  | Device role                              | Rendering examples             | Capture examples                   |
|-----------------|------------------------------------------|--------------------------------|------------------------------------|
| eConsole        | Interaction with the computer            | Games and system notifications | Voice commands                     |
| eCommunications | Voice communications with another person | Chat and VoIP                  | Chat and VoIP                      |
| eMultimedia     | Playing or recording audio content       | Music and movies               | Narration and live music recording |



 

A particular rendering or capture device might be assigned none, one, some, or all of the roles in the preceding table. At any time, each role in the table is assigned to one (and only one) rendering device and to one (and only one) capture device. That is, the assignment of roles to rendering devices is independent of the assignment of roles to capture devices.

An application might choose to play all of its output streams through a single rendering endpoint device, and to record all of its input streams from a single capture endpoint device. Alternatively, an application might choose to play some of its output streams through one rendering device and to play other output streams through another rendering device. Similarly, it might choose to record some of its input streams through one capture device and to record other input streams through another capture device. In all cases, the application can assign each stream to the device whose role is most appropriate for that stream.

For example, a VoIP application might assign the output stream that contains the ring-in notification to the rendering endpoint device with the eConsole role.

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> <dt>

[Working with Device Roles](device-roles-in-windows-vista.md)
</dt> <dt>

[Interoperability with Legacy Audio APIs](interoperability-with-legacy-audio-apis.md)
</dt> </dl>

 

 



