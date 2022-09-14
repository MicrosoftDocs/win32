---
title: Creating a Remote Desktop Protocol Provider
description: Information about creating a Remote Desktop Protocol Provider. The protocol manager is implemented as a COM server and registered in a location searched when the Remote Desktop Services service starts.
ms.assetid: 9a3e6d5c-464f-4227-a06f-16eb8ed1079e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Remote Desktop Protocol Provider

The following sections contain information about creating a Remote Desktop Protocol Provider. The protocol manager is implemented as a COM server and registered in a location searched when the Remote Desktop Services service starts.

## In this section

<dl> <dt>

[Registering the Protocol Manager](registering-the-custom-protocol.md)
</dt> <dd>

You must create at least one registry value entry for your protocol manager so that the Remote Desktop Services service can instantiate it.

</dd> <dt>

[Method Call Sequence](method-call-sequence.md)
</dt> <dd>

The Remote Desktop Services service and your protocol provider call each other in clearly defined sequences.

</dd> </dl>

-   [Registering the Protocol Manager](registering-the-custom-protocol.md)
-   [Method Call Sequence](method-call-sequence.md)

## Related topics

<dl> <dt>

[Remote Desktop Protocol Provider API](custom-remote-desktop-protocols.md)
</dt> <dt>

[Using Remote Desktop Services](using-terminal-services.md)
</dt> </dl>

 

 




