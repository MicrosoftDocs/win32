---
title: Internet Connection Sharing and Internet Connection Firewall Interfaces
description: The ICS/ICF API exposes the following interfaces.
ms.assetid: dfef918e-9abf-4ac2-8365-28cd5b249add
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Internet Connection Sharing and Internet Connection Firewall Interfaces

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The ICS/ICF API exposes the following interfaces.



| Interface                                                                                | Purpose                                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [**IEnumNetSharingEveryConnection**](/windows/previous-versions/NetCon/nn-netcon-ienumnetsharingeveryconnection?branch=master)                 | Enumerates all connections in connections folder.           |
| [**IEnumNetSharingPortMapping**](/windows/previous-versions/NetCon/nn-netcon-ienumnetsharingportmapping?branch=master)                         | Enumerates port mappings.                                   |
| [**IEnumNetSharingPrivateConnection**](/windows/previous-versions/NetCon/nn-netcon-ienumnetsharingprivateconnection?branch=master)             | Enumerates privately-shared connections.                    |
| [**IEnumNetSharingPublicConnection**](/windows/previous-versions/NetCon/nn-netcon-ienumnetsharingpublicconnection?branch=master)               | Enumerates publicly-shared connections.                     |
| [**INetConnection**](/windows/previous-versions/NetCon/nn-netcon-inetconnection?branch=master)                                                 | Primary interface for network connection object.            |
| [**INetConnectionProps**](/windows/previous-versions/NetCon/nn-netcon-inetconnectionprops?branch=master)                                       | Retrieves the properties for a connection.                  |
| [**INetSharingConfiguration**](/windows/previous-versions/NetCon/nn-netcon-inetsharingconfiguration?branch=master)                             | Configures connection sharing, firewall, and port mappings. |
| [**INetSharingEveryConnectionCollection**](/windows/previous-versions/NetCon/nn-netcon-inetsharingeveryconnectioncollection?branch=master)     | Collection interface for all connections.                   |
| [**INetSharingManager**](/windows/previous-versions/NetCon/nn-netcon-inetsharingmanager?branch=master)                                         | Primary interface for the Manager object.                   |
| [**INetSharingPortMapping**](/windows/previous-versions/NetCon/nn-netcon-inetsharingportmapping?branch=master)                                 | Interface for port mapping.                                 |
| [**INetSharingPortMappingCollection**](/windows/previous-versions/NetCon/nn-netcon-inetsharingportmappingcollection?branch=master)             | Collection interface for port mappings.                     |
| [**INetSharingPortMappingProps**](/windows/previous-versions/NetCon/nn-netcon-inetsharingportmappingprops?branch=master)                       | Retrieve and set properties for a connection port mapping.  |
| [**INetSharingPrivateConnectionCollection**](/windows/previous-versions/NetCon/nn-netcon-inetsharingprivateconnectioncollection?branch=master) | Collection interface for privately-shared connections.      |
| [**INetSharingPublicConnectionCollection**](/windows/previous-versions/NetCon/nn-netcon-inetsharingpublicconnectioncollection?branch=master)   | Collection interface for publicly-shared connections.       |



 

## Related topics

<dl> <dt>

[Internet Connection Sharing Reference](internet-connection-sharing-and-internet-connection-firewall-reference.md)
</dt> </dl>

 

 




