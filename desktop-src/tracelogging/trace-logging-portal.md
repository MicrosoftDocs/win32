---
title: TraceLogging
description: TraceLogging
ms.assetid: c516424a-9eba-4b56-80de-8c713fd3461a
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging

## Purpose

TraceLogging is a system for logging events that can be decoded without a
manifest. On Windows, TraceLogging is used in user-mode and kernel-mode to
generate [Event Tracing for Windows (ETW)](../etw/about-event-tracing.md)
events. TraceLogging builds on Event Tracing for Windows (ETW) and provides a
simplified way to instrument code.

## In this section

- [**About TraceLogging**](./trace-logging-about.md)

  This topic gives an overview of TraceLogging. It provides guidance about when
  to use TraceLogging and provides links to the various TraceLogging APIs
  available for different development scenarios.

- [**Using TraceLogging**](./tracelogging-using-tracelogging.md)

  These topics provide a TraceLogging quick start for C/C++ and .NET code, with
  examples.

- [**TraceLogging Reference**](./trace-logging-reference.md)

  These topics provide information about the C/C++ TraceLogging API.

## Developer audience

TraceLogging is designed for use by user-mode application developers and
kernel-mode driver developers who want to add tracing to their code.
