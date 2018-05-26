---
title: WinRM Plug-in API Structures
description: WinRM Plug-in API Structures
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 745619bc-c7b3-48fa-8212-cb1b5b9ed4db
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WinRM Plug-in API Structures

The following table provides an overview of the structures in the Windows Remote Management (WinRM) plug-in application programming interface (API).



| Structure                                                        | Description                                                                              |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**WSMAN\_AUTHZ\_QUOTA**](/windows/win32/Wsman/ns-wsman-_wsman_authz_quota?branch=master)                 | Defines quota information on a per-user basis.                                           |
| [**WSMAN\_CERTIFICATE\_DETAILS**](/windows/win32/Wsman/ns-wsman-_wsman_certificate_details?branch=master) | Represents the fields within the client certificate.                                     |
| [**WSMAN\_COMMAND\_ARG\_SET**](/windows/win32/Wsman/ns-wsman-_wsman_command_arg_set?branch=master)        | Represents the set of arguments that are passed in to the command line.                  |
| [**WSMAN\_FILTER**](/windows/win32/Wsman/ns-wsman-_wsman_filter?branch=master)                            | Defines the filtering used for an operation.                                             |
| [**WSMAN\_FRAGMENT**](/windows/win32/Wsman/ns-wsman-_wsman_fragment?branch=master)                        | Defines the fragment information for an operation.                                       |
| [**WSMAN\_OPERATION\_INFO**](/windows/win32/Wsman/ns-wsman-_wsman_operation_info?branch=master)           | Represents a specific resource end-point for which the plug-in must perform the request. |
| [**WSMAN\_PLUGIN\_REQUEST**](/windows/win32/Wsman/ns-wsman-_wsman_plugin_request?branch=master)           | Contains information about the request and is passed into every plug-in operation.       |
| [**WSMAN\_SENDER\_DETAILS**](/windows/win32/Wsman/ns-wsman-_wsman_sender_details?branch=master)           | Specifies client details for every inbound request.                                      |



 

 

 




