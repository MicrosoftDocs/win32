---
description: Using Parental Controls APIs
ms.assetid: 3d0bb750-0882-4b95-a595-38611f161ca9
title: Using Parental Controls APIs
ms.topic: article
ms.date: 05/31/2018
---

# Using Parental Controls APIs

## API Selection

As noted in the overview section, development involves use of up to three APIs:

-   Basic settings access: the Parental Controls minimum compliance COM API (Compliance API) defined in Wpcapi.h for simple access to a key subset of Parental Controls state.
-   Full settings write/read access: use of a small subset of the WMI COM API for full access is only required if the ISV needs to modify settings. Addition of a UI extensibility link, replacement of the Web Content Filter, or additions to the computer-wide HTTP application or URL filtering exemption lists are the primarily reasons to use the API. As the WMI Parental Controls namespace usage provides raw access to the underlying settings store, ISVs should proceed with caution in interpreting state from individual settings that may in fact have gating dependencies on other settings. It is therefore recommended to use the Compliance API for reading state for all values exposed by that API.
-   Logging: the Windows Vista Event Tracing and Reporting system API (also referred to as ETW) for publishing activity events into the Parental Controls logs, in conjunction with event descriptors and array enumerations defined in WpcEvent.h.

All of the APIs are callable as a standard user. For logging, any user may source log events. Calling to retrieve or change settings for another user will fail if the caller does not have administrator privileges. In other words, a standard user can access his or her own settings only, and only for reading.

Settings and logging API usage are discussed further in these sections:

-   [Using Parental Controls Settings APIs](using-parental-controls-settings-apis.md)
-   [Using Logging APIs for Parental Controls](using-logging-apis-for-parental-controls.md)

## Development Environment

Developing for Parental Controls requires access to three header files: Wpc.h, WpcApi.h, and WpcEvent.h. Wpc.h is a collector that includes the settings public compliance API and event headers, so it is sufficient to include Wpc.h in application code.

Read/write permissions to the WMI API is specified by the Wpcsprov.mof file. This file is installed to the WBEM subdirectory under the Windows System32 directory.

The Microsoft Windows Software Development Kit (SDK) contains sample code to reinforce example code shown here and provide simple command-line driven tools for API exploration or integration testing.

 

 



