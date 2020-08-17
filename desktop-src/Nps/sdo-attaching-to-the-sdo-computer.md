---
title: Attaching to the SDO Computer
description: With the interface pointer returned by CoCreateInstance, call the ISdoMachine Attach method.
ms.assetid: b28691ef-4054-4cd1-92aa-72ad9902fba3
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Attaching to the SDO Computer

With the interface pointer returned by [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), call the [**ISdoMachine::Attach**](/windows/desktop/api/sdoias/nf-sdoias-isdomachine-attach) method. Pass **NULL** as the parameter to the **Attach** method. The value **NULL** specifies that **Attach** associate the machine object with the local computer. Attaching to a remote computer is not supported.

To determine if the local computer is already attached, call the [**ISdoMachine::GetAttachedComputer**](/windows/desktop/api/sdoias/nf-sdoias-isdomachine-getattachedcomputer) method.

See [Attaching to an SDO-Enabled Computer](/windows/desktop/Nps/sdo-attaching-to-an-sdo-enabled-computer) for sample code that demonstrates how to attach to the local computer.

 

 