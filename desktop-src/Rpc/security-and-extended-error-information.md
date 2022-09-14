---
title: Security and Extended Error Information
description: Extended error information offers very useful data when troubleshooting an RPC problem, but such data many be considered confidential by security-conscious organizations.
ms.assetid: ca6ef213-e59d-4b4e-ae7e-f5b20d11fd01
ms.topic: article
ms.date: 05/31/2018
---

# Security and Extended Error Information

Extended error information offers very useful data when troubleshooting an RPC problem, but such data many be considered confidential by security-conscious organizations. In consideration of such security issues, extended error information is turned off by default.

Extended error information is still generated when extended error information is disabled, but the information is never transmitted across process or computer boundaries. This approach enables error information to be used by tools that have access to the process address space, such as debuggers. When turned on, extended error information is generated and can be sent across process and computer boundaries. Currently, extended error information is used for connection oriented protocol sequences and local RPC (LRPC). It is partially implemented for datagrams.

 

 




