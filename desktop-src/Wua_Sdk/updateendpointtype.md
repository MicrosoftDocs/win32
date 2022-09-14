---
description: Defines the type of endpoints that can be used to connect to a service.
ms.assetid: 50397D25-7C71-4AA2-89BF-F90CBDCFFA91
title: UpdateEndpointType enumeration (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UpdateEndpointType
api_type: 
- HeaderDef
api_location: 
- UpdateEndpointAuth.h
---

# UpdateEndpointType enumeration

Defines the type of endpoints that can be used to connect to a service.

## Syntax


```C++
typedef enum tagEndpointType { 
  uetClientServer          = 0,
  uetReporting             = ( uetClientServer + 1 ),
  uetWuaSelfUpdate         = ( uetReporting + 1 ),
  uetRegulation            = ( uetWuaSelfUpdate + 1 ),
  uetSimpleTargeting       = ( uetRegulation + 1 ),
  uetSecuredClientServer   = ( uetSimpleTargeting + 1 ),
  uetSecondaryServiceAuth  = ( uetSecuredClientServer + 1 )
} UpdateEndpointType;
```



## Constants

<dl> <dt>

<span id="uetClientServer"></span><span id="uetclientserver"></span><span id="UETCLIENTSERVER"></span>**uetClientServer**
</dt> <dd>

A client-server endpoint that is used to connect to the update service, such as Windows Update, Microsoft Update, and WSUS server in a corporate environment, to find information on updates that may be applicable to the computer.

The update service returns information on updates that have been published, revised, or withdrawn since the last time that client performed a sync with the server.

</dd> <dt>

<span id="uetReporting"></span><span id="uetreporting"></span><span id="UETREPORTING"></span>**uetReporting**
</dt> <dd>

A reporting endpoint that is used when the client reports the results of scans, downloads, and installs back to the update service.

In the case of public services (Windows Update and Microsoft Update), this is done for quality monitoring purposes.

In the case of private services, such as a corporate WSUS server, thhis type of endpoint also allows the server to collect inventory and other information about the client computers under management.

</dd> <dt>

<span id="uetWuaSelfUpdate"></span><span id="uetwuaselfupdate"></span><span id="UETWUASELFUPDATE"></span>**uetWuaSelfUpdate**
</dt> <dd>

A self-update endpoint that is used when the client computer contacts an update service to see whether there is a new version of the Windows Update Agent client software.

The Self-update endpoint uses a different protocol then the Client-Server endpoint so that self-updates can be distributed even if there is an error condition that might be preventing the normal client-server sync from working on a particular client computer.

</dd> <dt>

<span id="uetRegulation"></span><span id="uetregulation"></span><span id="UETREGULATION"></span>**uetRegulation**
</dt> <dd>

A regulation endpoint that is used when the client computer contacts the regulation service to act on a particular update that is applicable to the target computer.

The regulation service can indicate whether the update is “regulated” (also known as “throttled”) – in other words, the regulation service can tell the client computer that it should not act on a particular update, even though that update appears to be applicable.

</dd> <dt>

<span id="uetSimpleTargeting"></span><span id="uetsimpletargeting"></span><span id="UETSIMPLETARGETING"></span>**uetSimpleTargeting**
</dt> <dd>

A simple-targeting endpoint that is used only with private services (WSUS servers in corporate environments). In a corporate environment, client computers can be assigned to particular target groups, and updates can be approved for installation on computers in some groups but not others.

For example, the WSUS administrator may create a “Testing” group for computers that are used to test new updates, and the administrator may approve newly-released updates for installation on computers in the Testing group without approving them for installation on other computers in the organization. The simple targeting exchange is used to allow a client computer to register itself with the WSUS server, and to allow the server to tell the client computer what group it is in.

</dd> <dt>

<span id="uetSecuredClientServer"></span><span id="uetsecuredclientserver"></span><span id="UETSECUREDCLIENTSERVER"></span>**uetSecuredClientServer**
</dt> <dd>

A secured-client-server endpoint that allows a client to obtain info on apps that need licensing so they can be used on a client computer. This licensing framework is currently only used by Windows 8 to deploy apps and updates that are obtained through the Windows Store. The secured-client-server endpoint is currently not used by Windows Update, Microsoft Update, or WSUS.

</dd> <dt>

<span id="uetSecondaryServiceAuth"></span><span id="uetsecondaryserviceauth"></span><span id="UETSECONDARYSERVICEAUTH"></span>**uetSecondaryServiceAuth**
</dt> <dd>

The secondary-service-authentication endpoint is used by a client to provide authentication before it obtains info on apps that need licensing so they can be used on a client computer. This licensing framework is currently only utilized by Windows 8 to deploy apps and updates that are obtained through the Windows Store. The secondary-service-authentication endpoint is currently not used by Windows Update, Microsoft Update, or WSUS.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                              |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |



 

 




