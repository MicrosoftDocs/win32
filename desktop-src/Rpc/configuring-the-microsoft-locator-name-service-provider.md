---
title: Configuring the Microsoft Locator Name Service Provider
description: You can change the name service provider you specified by editing the Rpcreg.dat configuration file, which contains the NSP parameters and RPC protocol settings. Use a text editor to change NSP entries.
ms.assetid: b499e40e-d38f-4e51-bbce-41af3ff12a7e
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Microsoft Locator Name Service Provider

You can change the name service provider you specified by editing the Rpcreg.dat configuration file, which contains the NSP parameters and RPC protocol settings. Use a text editor to change NSP entries.

**To reconfigure the Microsoft Locator name service provider**

1.  Open the Rpcreg.dat file using a text editor.

    Rpcreg.dat is in the root directory unless you specified a different path during setup.

2.  Set the following values for the registry entries. 

    | Registry entry                                         | Value                                                                                                                                                 |
    |--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Software\\Microsoft\\RPC \\NameService\\Protocol       | The protocol sequence for the protocol you are using. The default is **ncacn\_np**.                                                                   |
    | Software\\Microsoft\\RPC\\ NameService\\NetworkAddress | The name of the computer running Locator that is used by clients during name service lookup operations. The default is the primary domain controller. |
    | Software\\Microsoft\\RPC\\ NameService\\Endpoint       | The name of the endpoint used by the name service. The default is \\pipe\\locator.                                                                    |

    

     

3.  Save and close the file.

 

 




