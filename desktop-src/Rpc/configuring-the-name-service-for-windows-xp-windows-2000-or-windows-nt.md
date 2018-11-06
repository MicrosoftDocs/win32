---
title: Configuring the Name Service
description: Starting with Windows 2000, when you install the Windows SDK, the setup program automatically selects Microsoft Locator as the name service provider. You can change the name service provider through Control Panel.
ms.assetid: bd72ca2f-bb93-4057-a877-be755a88719d
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Name Service

Starting with Windows 2000, when you install the Windows SDK, the setup program automatically selects Microsoft Locator as the name service provider. You can change the name service provider through Control Panel.

The host computer that runs the nsid acts as a gateway to the DCE Cell Directory Service, passing NSI function calls between computers that run Microsoft operating systems and DCE computers. A network address can be up to 80 characters—for example, 11.1.9.169 is a valid address.

> [!Note]  
> You must have the Digital Equipment Corporation DCE CDS product to configure the DCE CDS as your name service provider. See the documentation provided by Digital Equipment Corporation for information about DCE CDS.

 

**To reconfigure the name service provider**

1.  In Control Panel, click the **Network Connections** icon. The **Network Connections** window appears.
2.  Select the network connection to configure, right-click, and select **Properties** from the context menu. The **Connection Properties** dialog appears.
3.  In the **Connection Properties** dialog, select **Client for Microsoft Networks** and click the **Properties** button. The **Client for Microsoft Network Properties** dialog appears.
4.  In the **Client for Microsoft Network Properties** dialog, open the **Name service provider** drop-down and select a name provider from the list.
    1.  When you select Microsoft Locator, click OK. The configuration process is then complete.
    2.  When you select the DCE Cell Directory Service, in the **Network Address** box, type the name of the host computer that runs the NSI daemon (nsid), and then click OK.

**To reconfigure the name service provider for Windows 2000**

1.  In Control Panel, click the **Network** icon.

    The **Network** dialog box appears.

2.  In the **Network** dialog box, click **Configure**.
3.  In the **NetworkSoftware** list, select **RPC Configuration**.

    The **RPC Name Service Provider Configuration** dialog box appears.

4.  In the **RPC Name Service Provider Configuration** dialog box, select a name service provider from the list.
    1.  When you select Microsoft Locator, click OK. The configuration process is then complete.
    2.  When you select the DCE Cell Directory Service, in the **Network Address** box, type the name of the host computer that runs the NSI daemon (nsid), and then click OK.

 

 




