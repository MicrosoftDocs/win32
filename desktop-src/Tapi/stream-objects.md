---
description: Stream objects are an abstraction of the media stream or streams associated with a call session.
ms.assetid: 4bd7a305-69ff-4892-bf03-df9c6479adab
title: Stream Objects
ms.topic: article
ms.date: 05/31/2018
---

# Stream Objects

Stream objects are an abstraction of the media stream or streams associated with a call session. The interfaces and methods exposed on stream and substream objects allow an application to exercise very detailed controls such as pausing a stream, adding new media types to a communications session, or adjusting the audio volume of a particular conference participant.

The two main types of stream are the stream and the substream. The interfaces and methods of a standard implementation are similar for both, but substreaming allowing a lower level of control. All media service providers (MSPs) must implement the basic stream control interfaces, but support for substreams is optional.

In addition, some service providers implement [provider-specific interfaces](provider-specific-interfaces.md) for streams. For example, the IPConf MSP provides participant level controls. See [IPConf MSP Interfaces](ipconf-msp-interfaces.md) for a summary. For other interfaces that might be implemented, see the service provider's documentation.

The MSP and TAPI create stream objects for a call during initial setup of an outgoing or incoming session. The application is responsible for identifying appropriate terminals for these streams, and selecting the terminals onto the streams.

Note that in some cases an MSP may require that the application stop or pause streams prior to certain call session operations.

The stream interfaces are documented in the [Media Service Provider Interface (MSPI) Reference](media-service-provider-interface-mspi-reference.md).

The [Select a Terminal](select-a-terminal.md) code example shows an example of enumerating streams and selecting terminals onto them.

 

 



