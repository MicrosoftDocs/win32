---
title: Attaching to the SDO Computer
description: With the interface pointer returned by CoCreateInstance, call the ISdoMachine Attach method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b28691ef-4054-4cd1-92aa-72ad9902fba3'
ms.prod: 'windows-server-dev'
ms.technology: 'network-policy-and-access-services'
ms.tgt_platform: multiple
---

# Attaching to the SDO Computer

With the interface pointer returned by [**CoCreateInstance**](_com_cocreateinstance), call the [**ISdoMachine::Attach**](https://msdn.microsoft.com/library/bb960656) method. Pass **NULL** as the parameter to the **Attach** method. The value **NULL** specifies that **Attach** associate the machine object with the local computer. Attaching to a remote computer is not supported.

To determine if the local computer is already attached, call the [**ISdoMachine::GetAttachedComputer**](https://msdn.microsoft.com/library/bb960657) method.

See [Attaching to an SDO-Enabled Computer](https://msdn.microsoft.com/library/bb960609) for sample code that demonstrates how to attach to the local computer.

 

 




