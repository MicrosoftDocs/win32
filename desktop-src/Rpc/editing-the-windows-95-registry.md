---
title: Editing the Windows 95 Registry
description: You can use REGEDIT to edit the Windows 95 registry to designate an NSP.
ms.assetid: 109daf4a-722f-4a25-a778-72360ee07ad9
ms.topic: article
ms.date: 05/31/2018
---

# Editing the Windows 95 Registry

You can use REGEDIT to edit the Windows 95 registry to designate an NSP.

**To designate a Microsoft Locator name service provider for Windows 95**

1.  Select

    **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Rpc**

2.  Create a new key called

    **NameService**

3.  With the **NameService** key selected, create the new **StringValue** names and modify them to contain data as shown in the following table.

    

    | Name                     | Data                                                                        |
    |--------------------------|-----------------------------------------------------------------------------|
    | **DefaultSyntax**        | 3<br/>                                                                |
    | **Protocol**             | ncacn\_np<br/>                                                        |
    | **Endpoint**             | \\pipe\\locator<br/>                                                  |
    | **NetworkAddress**       | myserver (where myserver is the name of the Windows NT computer)<br/> |
    | **ServerNetworkAddress** | myserver<br/>                                                         |

    

     

You can use REGEDIT to edit the Windows 95 registry to designate a DCE CDS NSP.

**To designate a DCE CDS name service provider for Windows 95**

1.  Select

    **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Rpc**

2.  Create a new key called

    **NameService**

3.  With the **NameService** key selected, create the new **StringValue** names and modify them to contain data as shown in the following table.

    

    | Name                     | Data                                                             |
    |--------------------------|------------------------------------------------------------------|
    | **DefaultSyntax**        | 3<br/>                                                     |
    | **Protocol**             | ncacn\_ip\_tcp<br/>                                        |
    | **Endpoint**             | "" (an empty string)<br/>                                  |
    | **NetworkAddress**       | myserver (the name of the host computer running nsid)<br/> |
    | **ServerNetworkAddress** | myserver (the name of the host computer running nsid)<br/> |

    

     

    > [!Note]  
    > You must have the Digital Equipment Corporation DCE Cell Directory Service product to configure the DCE CDS as your name service provider. See the documentation provided by Digital Equipment Corporation for information about DCE CDS.

     

 

 





