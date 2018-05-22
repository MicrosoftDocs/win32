---
Description: 'Overview of partial trust issues and the StylusInput application programming interface (API).'
ms.assetid: '32c26632-03f4-4f21-8c67-ebf38b67d251'
title: Partial Trust Considerations for the StylusInput API
---

# Partial Trust Considerations for the StylusInput API

The [**RealTimeStylus**](realtimestylus-class.md) that takes the *handle* parameter requires the [UIPermissionWindow.AllWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag) permissions, in addition to the permissions required by the constructor that takes the *attachedControl* parameter.

For more information about security and trust issues, see [Security and Trust](security-and-trust.md).

 

 



