---
title: Host Names and IP Addresses
description: TCP/IP networks require host names to be resolved to IP addresses before the address information can be used to create a connection.
ms.assetid: f077e7d0-2e2c-4a2b-b5cd-1c7f43f7743b
keywords:
- Host Names and IP Addresses SNMP
- Host Names, resolving SNMP
ms.topic: article
ms.date: 05/31/2018
---

# Host Names and IP Addresses

TCP/IP networks require host names to be resolved to IP addresses before the address information can be used to create a connection. Computers running on the Windows operating system use a host file that, for this purpose, maps host names to IP addresses.

The host file is a text file that lists explicit host names and IP addresses. The host file is automatically loaded into memory on startup and consulted when a host name requires resolution. If the host file does not contain the mapping information that is required to resolve a specific host name to its IP address, a resolution query is made to a DNS server.

SNMP uses the Windows Internet Naming Service (WINS) for host name resolution. WINS makes it possible to map NetBIOS names, or machine names, to IP addresses on TCP/IP networks. If the computer cannot access a WINS server, the SNMP service uses the host file to resolve host names to IP addresses.

The SNMP service supports the use of both host names and IP addresses. However, when you have a choice between using host names or IP addresses to identify network locations, your SNMP management applications should use host names. If you use host names, add all host name and IP address mappings of the participating systems to the host file.

 

 




