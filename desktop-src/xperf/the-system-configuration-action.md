---
title: The System Configuration Action
description: The System Configuration Action
ms.assetid: ee747210-6592-44de-bfb9-2b4253b058e6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The System Configuration Action

The system configuration action produces a text file that has detailed information about the system on which the trace was taken. The general usage is:


```
 -a sysconfig [-netidentity] 
              [-cpu] 
              [-memory] 
              [-etw] 
              [-power]  
              [-disk]
              [-idechannel] 
              [-video] 
              [-nic] 
              [-irq] 
              [-services] 
              [-pnp]  
```





| Option                  | Description                                        |
|-------------------------|----------------------------------------------------|
| netidentity <br/> | Display network identity information<br/>    |
| cpu <br/>         | Display CPU configuration<br/>               |
| memory <br/>      | Display memory configuration<br/>            |
| build <br/>       | Display build information<br/>               |
| etw <br/>         | Display ETW version information<br/>         |
| power <br/>       | Display power state support information<br/> |
| disk <br/>        | Display disk configuration<br/>              |
| idechannel <br/>  | Display IDE channel configuration<br/>       |
| video <br/>       | Display video configuration<br/>             |
| nic <br/>         | Display NIC configuration<br/>               |
| irq <br/>         | Display IRQ configuration <br/>              |
| services <br/>    | Display services information <br/>           |
| pnp <br/>         | Display PnP configuration<br/>               |



 

If no activity is selected, all activities are selected by default.

 

 





