---
title: Using the ADSI Extension for Remote Desktop Services User Configuration
description: Administration of Remote Desktop Services-specific user properties is possible by using the methods implemented by the Active Directory Service Interfaces (ADSI) extension, which is packaged with the dynamic-link library Tsuserex.dll.
ms.assetid: f6355730-9686-4446-b118-630562548fc9
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , using the ADSI extension
ms.topic: article
ms.date: 05/31/2018
---

# Using the ADSI Extension for Remote Desktop Services User Configuration

The Active Directory Service Interfaces (ADSI) extension for Remote Desktop Services user configuration is a library that is packaged with the dynamic-link library Tsuserex.dll. Administration of Remote Desktop Services-specific user properties is possible using the methods implemented by the extension. The methods allow configuration of the properties that are available in the extension interface for Remote Desktop Services users.

The ADSI extension for Remote Desktop Services user configuration supports the examination and manipulation of Remote Desktop Services user properties stored in the Directory Service database. The extension also supports configuration of user properties that are stored in the Active Directory, through the Lightweight Directory Access Protocol (LDAP) API.

The provider implements the following methods:

-   [**IADs::Get**](/windows/desktop/api/iads/nf-iads-iads-get). This method searches for a specific property or set of properties on an instance of the class.
-   [**IADs::Put**](/windows/desktop/api/iads/nf-iads-iads-put). This method configures a specific property or set of properties on an instance of the class.

See the [Reference for the ADSI Extension for Remote Desktop Services User Configuration](reference-for-the-adsi-extension-for-terminal-services-user-configuration.md) for a list of the specific Remote Desktop Services user properties you can configure.

For more information about accessing and modifying attributes with ADSI, see [Accessing and Manipulating Data with ADSI](/windows/desktop/ADSI/accessing-and-manipulating-data-with-adsi).

For more information about using ADSI naming conventions and AdsPath strings, see the information about individual [ADSI Service Providers](/windows/desktop/ADSI/adsi-system-providers) in the [Active Directory Service Interfaces](/windows/desktop/ADSI/active-directory-service-interfaces-adsi) Platform Software Development Kit (SDK) documentation.

 

 