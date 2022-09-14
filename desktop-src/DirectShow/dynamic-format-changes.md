---
description: Dynamic Format Changes
ms.assetid: ff60de5a-3edc-405d-aa02-8704b96d5e87
title: Dynamic Format Changes
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Format Changes

When two filters connect, they agree on a media type, which describes the format of the data that the upstream filter will deliver. In most cases, the media type is fixed for the duration of the connection. However, DirectShow does offer limited support for filters to change the media type. When a filter switches media types, it is called a *dynamic format change*. If you are writing a DirectShow filter, you should be aware of the mechanisms for dynamic format changes. Even if your filter does not support such changes, it should respond correctly if another filter requests a new format.

DirectShow defines several distinct mechanisms for dynamic format changes, depending on the state of filter graph and the type of change that is required.

-   If the graph is stopped, the pins can reconnect and renegotiate the media type. For more information, see [Reconnecting Pins](reconnecting-pins.md).
-   Some filters can reconnect pins even while the graph is active (running or paused). For more information about this mechanism, see [Dynamic Reconnection](dynamic-reconnection.md).

Otherwise, if the graph is active, but the filters in question do not support dynamic pin reconnections, there are three possible mechanisms for changing the format:

-   [QueryAccept (Downstream)](queryaccept--downstream.md) is used when If an output pin proposes a format change to its downstream peer, but only if the new format does not require a larger buffer.
-   [QueryAccept (Upstream)](queryaccept--upstream.md) is used when an input pin proposes a format change to its upstream peer. The new format can be the same size, or it can be larger.
-   [ReceiveConnection](receiveconnection.md) is used when an output pin proposes a format change to its downstream peer, and the new format requires a larger buffer.

## Related topics

<dl> <dt>

[Handling Format Changes from the Video Renderer](handling-format-changes-from-the-video-renderer.md)
</dt> </dl>

 

 



