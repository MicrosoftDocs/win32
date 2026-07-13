---
title: Consent for Win32 app isolation
description: Consent for Win32 app isolation can be granted or removed in several ways.
ms.topic: concept-article
ms.date: 08/26/2024
---

# Consent for Win32 app isolation

Consent for Win32 app isolation can be granted or removed in several ways. This document describes how consent is granted and how it can be revoked.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## How file access consent is granted

Consent is granted for Win32 app isolation in three ways.

1. **Implicit-Consent**: Apps are implicitly granted access to files and folders through the flows listed below.
   - File Dialog: Files and folders that are selected or created through Window's file dialog created from Win32 app isolation.
   - File Type Association: Apps that register FTA in the manifest will show up under the open-with context menu and can be set as the default app.
     - Apps that do this through a COM extension will need the `isolatedWin32-shellExtensionContextMenu` capability.
   - Drag and Drop: Apps that register drag and drop handlers will have access to any files and folders dragged onto them.
     - There is currently no support for dragging between different apps that use Win32 app isolation.
1. **Publisher Directory**: If the application has the `isolatedWin32-accessToPublisherDirectory` capability, then the app will have full access to:
   - Network shares whose share name ends with the publisher ID of the app.
   - Directories with names ending with the publisher ID of the app located in `\Device\BootDevice\ProgramData`.
1. **Prompting**: If the application has the `isolatedWin32-promptForAccess` capability, the first time the app attempts to access a file or directory, a prompt will be generated for the user to accept or decline. The choice will be saved until the consent is revoked

## How consent is revoked

Consent can currently be revoked in two ways:

1. **Settings**: Through the settings, navigate to "Reset file permissions on isolated Win32 applications". On this page you can fully reset the consent granted to specific apps that use Win32 app isolation. This will reset both prompted and implicit consent, but won't affect the publisher directory.
1. **Uninstall**: During uninstall, all consent will be revoked.

## Related topics

- [Win32 app isolation overview](app-isolation-overview.md)
