---
title: Mixer Architecture
description: Mixer Architecture
ms.assetid: 11d650bf-c258-4818-88b7-9fdc71a8d859
keywords:
- multimedia audio,mixer architecture
- audio,mixer architecture
- audio mixers,architecture
- audio mixers,audio lines
- audio lines
- audio mixers,controls
- multimedia audio,mixer controls
- audio,mixer controls
- mixers,audio lines
- mixers,architecture
- mixers,controls
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mixer Architecture

\[The feature associated with this page, [Audio Mixers](/windows/win32/multimedia/audio-mixers), is a legacy feature. It has been superseded by [Volume Controls](/windows/win32/coreaudio/volume-controls). **Volume Controls** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Volume Controls** instead of **Audio Mixers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The basic element of the mixer architecture is an *audio line*. An audio line consists of one or more channels of data originating from a single source or a system resource. For example, a stereo audio line has two data channels, but it is considered a single audio line because it originates from a single source.

The mixer architecture provides routing services to manage audio lines on a computer. You can use the routing services if you have adequate hardware devices and software drivers installed. The mixer architecture allows several audio source lines to map to a single destination audio line.

Each audio line can have mixer controls associated with it. A mixer control can perform any number of functions (such as control volume), depending on the characteristics of the associated audio line.

 

 




