---
title: The SpeechInput Object
description: The SpeechInput Object
ms.assetid: 'e968edb8-747f-421a-800b-29f13857410c'
---

# The SpeechInput Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [**SpeechInput**](lwef-speechinput_object) object provides access to the speech input properties maintained by the Agent server. The properties are read-only for client applications, but the user can change them in the Microsoft Agent property sheet. The server returns values only if a compatible speech engine has been installed and is enabled.

The [**Engine**](lwef-engine_property), [**Installed**](lwef-installed_property), and [**Language**](lwef-language_property) properties are no longer supported, but (for backward compatibility) return null values if queried. To query or set a speech recognition's mode, use the [**SRModeID**](srmodeid-property.md) property.

-   [SpeechInput Properties](speechinput-properties.md)

 

 




