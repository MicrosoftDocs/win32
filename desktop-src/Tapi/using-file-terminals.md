---
description: The file terminals can be used in two ways.
ms.assetid: 5a7d6aa7-0eb8-4652-af0b-74fbdb5a2c2f
title: Using File Terminals
ms.topic: article
ms.date: 05/31/2018
---

# Using File Terminals

The file terminals can be used in two ways. The simplest method is to use [**ITBasicCallControl2::SelectTerminalOnCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-selectterminaloncall) to select a file terminal (playback or record) onto a TAPI call object. In this case TAPI takes care of connecting the audio streams to the track terminals.

The second method allows an application to have finer control over the mapping of audio streams to tracks. In this scenario, the application enumerates the streams available on the call, picks the ones it wants to record (or use for playback), creates (or finds for playback) the corresponding tracks on the file terminal, and selects the tracks on call streams.

For more information, see the following topics:

-   [Simple Playback](simple-playback.md)
-   [Track-Controlled Playback](track-controlled-playback.md)
-   [Simple Record](simple-record.md)
-   [Track-Controlled Record](track-controlled-record.md)

 

 



