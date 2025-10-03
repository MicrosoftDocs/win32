---
title: Agent Sessions
description: Agent sessions is a loopback Remote Desktop session intended for managing background tasks.
ms.assetid: b9d06cbd-e0b3-45fe-ab0c-a2f3760b2fdf
ms.tgt_platform: multiple
ms.topic: reference
ms.date: 09/30/2025
---

# Agent Sessions

Agent sessions, or Isolation Sessions, is a special session type that uses
loopback Remote Desktop session. These sessions are similar to
[Child sessions](child-sessions.md), and are intended to be used for performing
background tasks.

This type of session is created using
[IMsRdpExtendedSettings](imsrdpextendedsettings.md)/
[put_Property](imsrdpextendedsettings-property.md), setting the string
`"ConnectToAgentSession"`.
