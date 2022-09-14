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
ms.date: 05/31/2018
---

# Mixer Architecture

The basic element of the mixer architecture is an *audio line*. An audio line consists of one or more channels of data originating from a single source or a system resource. For example, a stereo audio line has two data channels, but it is considered a single audio line because it originates from a single source.

The mixer architecture provides routing services to manage audio lines on a computer. You can use the routing services if you have adequate hardware devices and software drivers installed. The mixer architecture allows several audio source lines to map to a single destination audio line.

Each audio line can have mixer controls associated with it. A mixer control can perform any number of functions (such as control volume), depending on the characteristics of the associated audio line.

 

 




