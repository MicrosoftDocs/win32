---
title: Command Help
description: Commands in NetShell helpers should provide a common method of providing help. If the command show adapters is a valid operation, then show adapters should provide useful help that describes how to complete the command.
ms.assetid: d4ecccd9-9987-4e5d-8f9d-290348b39dae
keywords:
- helper NetSh , command syntax, command help
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Command Help

Commands in NetShell helpers should provide a common method of providing help. If the command **show adapters** is a valid operation, then **show adapters ?** should provide useful help that describes how to complete the command.

The following example illustrates the preferred format for help provided on a command.

``` syntax
Usage: add dns [name=]<string> [address=]<IP address> [[index=]<integer>]

Parameters:
                        Tag           Value
      name        - The name of the interface where DNS servers are added.
      address     - The IP address for the DNS server you are adding.
      index       - Specifies the index (preference) for the specialized
                    DNS server address.

Remarks: Adds a new DNS server IP address to the statically-configured 
         list. By default, the DNS server is added to the end of the list.
         If an index is specified, the DNS server will be placed in that 
         position in the list, with other servers being moved down to
         make room.  If DNS servers were previously obtained through
         DHCP, the new address will replace the old list.

Examples: 
          add dns "Local Area Connection" 10.0.0.1
          add dns "Local Area Connection" 10.0.0.3 index=2
```

 

 




