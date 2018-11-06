---
title: Modify Device Redirection Default
description: Because Remote Desktop Gateway servers attempt to enforce secure device redirection policies before passing the client connection through to a Remote Desktop Session Host server, you may need to disable this default in some cases.
ms.assetid: 03F2617C-D478-4A51-9EEC-E9643CA831B7
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Modify Device Redirection Default

Because Remote Desktop Gateway servers attempt to enforce secure device redirection policies before passing the client connection through to a Remote Desktop Session Host server, you may need to disable this default in some cases.

On Windows Server 2008 R2 and later, Remote Desktop Gateway servers will by default attempt to enforce secure device redirection policies before passing the client connection through to a Remote Desktop Session Host server. However, this feature is not supported by some servers. For example, this is not supported for connections to Hyper-V console sessions, and it may be necessary to disable the default to support federated authentication. In these cases, this feature can be disabled by creating the following registry key to allow connections to go through.

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Terminal Server Gateway\\preRDPDisableRegKey**

When this key exists, the Remote Desktop Gateway will not enforce device redirection.

 

 




