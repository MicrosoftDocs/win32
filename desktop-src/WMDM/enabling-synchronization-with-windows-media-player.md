---
title: Enabling Synchronization with Windows Media Player
description: Enabling Synchronization with Windows Media Player
ms.assetid: a312dfef-ac48-4c58-a59a-b277f5386419
keywords:
- Windows Media Device Manager,synchronization with Windows Media Player
- Device Manager,synchronization with Windows Media Player
- programming guide,synchronization with Windows Media Player
- service providers,synchronization with Windows Media Player
- creating service providers,synchronization with Windows Media Player
- synchronization with Windows Media Player
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Synchronization with Windows Media Player

You can enable a device to participate in automatic synchronization with Windows Media Player. Automatic synchronization means that when a user-designated synchronized device connects to the computer, Windows Media Player will automatically download, update, or delete files from the device without requiring any additional user input.

By default the following devices are synchronized with Windows Media Player:

-   MTP devices
-   Mass-storage devices
-   Windows CE devices (Windows Media Player 10 Mobile and later)

For any other device to synchronize with Windows Media Player, the following requirements must met:

-   The device must advertise a PAP device interface that is {F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}
-   The device objects returned by service provider must support the **IMDSPDevice3** interface.
-   The device parameter UseExtendedWmdm must be set to a **DWORD** value of 1. See [Device Parameters](device-parameters.md) for more information.
-   The service provider should implement the following interfaces:

    [**IMDSPDevice3**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspdevice3)

    [**IMDSPObject2**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspobject2)

    [**IMDSPStorage4**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspstorage4)

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> <dt>

[**Device Parameters**](device-parameters.md)
</dt> </dl>

 

 




