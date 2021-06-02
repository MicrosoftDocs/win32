---
description: Tone monitoring monitors the media stream of a call for specified tones.
ms.assetid: c3218013-b71f-41cd-9397-ba717c0cf556
title: Tone Monitoring
ms.topic: article
ms.date: 05/31/2018
---

# Tone Monitoring

Tone monitoring monitors the media stream of a call for specified tones. A tone is described by its component frequencies and cadence. An implementation of the API may allow several different tones to be monitored simultaneously. An application can tag each tone to be able to distinguish the different tones for which it requests detection.

An application can enable or disable tone monitoring on a specified call with [**lineMonitorTones**](/windows/desktop/api/Tapi/nf-tapi-linemonitortones). With this function, the application indicates which tones to detect on a specified call. When tone monitoring is enabled, detected digits cause the application to be notified with the [**LINE\_MONITORTONE**](line-monitortone.md) message. This message provides the call handle on which the tone was detected as well as the application's tag for the tone.

The scope of tone monitoring is bound by the lifetime of the call. Tone monitoring on a call ends as soon the call *disconnects* or goes *idle*.

> [!Note]  
> The monitoring of tones, digits, or media types often requires the use of resources of which the service provider can only have a finite amount. A request for monitoring can be rejected if resources are not available. For the same reason, an application should disable any unnecessary monitoring.

 

 

 



