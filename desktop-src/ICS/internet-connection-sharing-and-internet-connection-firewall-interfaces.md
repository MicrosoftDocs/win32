---
title: Internet Connection Sharing and Internet Connection Firewall Interfaces
description: The ICS/ICF API exposes the following interfaces.
ms.assetid: dfef918e-9abf-4ac2-8365-28cd5b249add
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Internet Connection Sharing and Internet Connection Firewall Interfaces

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The ICS/ICF API exposes the following interfaces.



| Interface                                                                                | Purpose                                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [**IEnumNetSharingEveryConnection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-ienumnetsharingeveryconnection)                 | Enumerates all connections in connections folder.           |
| [**IEnumNetSharingPortMapping**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-ienumnetsharingportmapping)                         | Enumerates port mappings.                                   |
| [**IEnumNetSharingPrivateConnection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-ienumnetsharingprivateconnection)             | Enumerates privately-shared connections.                    |
| [**IEnumNetSharingPublicConnection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-ienumnetsharingpublicconnection)               | Enumerates publicly-shared connections.                     |
| [**INetConnection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetconnection)                                                 | Primary interface for network connection object.            |
| [**INetConnectionProps**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetconnectionprops)                                       | Retrieves the properties for a connection.                  |
| [**INetSharingConfiguration**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingconfiguration)                             | Configures connection sharing, firewall, and port mappings. |
| [**INetSharingEveryConnectionCollection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingeveryconnectioncollection)     | Collection interface for all connections.                   |
| [**INetSharingManager**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingmanager)                                         | Primary interface for the Manager object.                   |
| [**INetSharingPortMapping**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingportmapping)                                 | Interface for port mapping.                                 |
| [**INetSharingPortMappingCollection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingportmappingcollection)             | Collection interface for port mappings.                     |
| [**INetSharingPortMappingProps**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingportmappingprops)                       | Retrieve and set properties for a connection port mapping.  |
| [**INetSharingPrivateConnectionCollection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingprivateconnectioncollection) | Collection interface for privately-shared connections.      |
| [**INetSharingPublicConnectionCollection**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingpublicconnectioncollection)   | Collection interface for publicly-shared connections.       |



 

## Related topics

<dl> <dt>

[Internet Connection Sharing Reference](internet-connection-sharing-and-internet-connection-firewall-reference.md)
</dt> </dl>

 

 




