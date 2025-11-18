---
title: Agent Sessions
description: Agent sessions is a loopback Remote Desktop session intended for managing background tasks.
ms.tgt_platform: multiple
ms.topic: reference
ms.date: 10/24/2025
---

# Agent Sessions

Agent sessions, or Isolation Sessions, is a special session type that uses loopback Remote Desktop session. These sessions are similar to [Child sessions](child-sessions.md), and are used for performing background tasks.

This type of session is created using [IMsRdpExtendedSettings](imsrdpextendedsettings.md) and [put_Property](imsrdpextendedsettings-property.md), setting the string `"ConnectToAgentSession"`.
