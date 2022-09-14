---
description: The system registry contains resource-related data.
ms.assetid: e66f1db8-a5f3-41d3-9835-34b81b9da5ed
ms.tgt_platform: multiple
title: Describing a Resource for the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Describing a Resource for the Registry

The system registry contains resource-related data. This data is located under the following registry key and is kept in a special registry data type named **REG\_RESOURCE\_LIST**. Applications can obtain the resource-related data through the System Registry provider. You can add and modify system resources in the registry.

```
HKEY_LOCAL_MACHINE
   Hardware
      ResourceMap
```

The following procedure describes how to store resource-related information in the system registry.

**To store resource-related information in the system registry**

1.  Create a string that contains the following fields.

    

    <table>
    <thead>
    <tr class="header">
    <th>Field</th>
    <th>Contains</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>Interface type</td>
    <td>One of the following values:<br/> <dl> Internal<br />
    Isa<br />
    Eisa<br />
    MicroChannel<br />
    TurboChannel<br />
    PCIBus<br />
    VMEBus<br />
    NuBus<br />
    PCMCIABus<br />
    CBus<br />
    MPIBus<br />
    MPSABus<br />
    </dl></td>
    </tr>
    <tr class="even">
    <td>Bus number</td>
    <td>Integer specifying the bus number.</td>
    </tr>
    <tr class="odd">
    <td>Partial descriptor number</td>
    <td>Integer specifying the descriptor number.</td>
    </tr>
    <tr class="even">
    <td>Offset or union type</td>
    <td>One of the following values:<br/> <dl> Port.Start<br />
    Port.PhysicalAddress<br />
    Port.Length<br />
    Interrupt.Level<br />
    Interrupt.Vector<br />
    Interrupt.Affinity<br />
    Memory.Start<br />
    Memory.PhysicalAddress<br />
    Memory.Length<br />
    Dma.Channel<br />
    Dma.Port<br />
    Dma.Reserved1<br />
    DeviceSpecificData.DataSize<br />
    DeviceSpecificData.Reserved1<br />
    DeviceSpecificData.Reserved2<br />
    </dl></td>
    </tr>
    </tbody>
    </table>

    

     

2.  Place the string in the appropriate key under the registry key.

    ```
    HKEY_LOCAL_MACHINE
       Hardware
          ResourceMap
    ```

The following code example describes a valid resource descriptor.

``` syntax
local|hkey_local_machine\hardware\resourcemap\
  hardware abstraction layer\
  pc compatible eisa/isa HAL|.raw("eisa",0,0,"interrupt.affinity")
```

The following code example shows valid MOF syntax for retrieving a resource descriptor.

``` syntax
[DYNPROPS] 
class MyRegProp
{    
   [KEY]  
   STRING MyKey; 
   STRING MyReservedTranslated;
};

[DYNPROPS] 
instance of MyRegProp
{
   MyKey = "1";
   [PropertyContext("local|hkey_local_Machine\\hardware\\ResourceMap\\
                   System Resources\\Reserved|.Translated
                   (\"Internal\")(0)(1)(\"Memory.PhysicalAddress\")"),
   Dynamic, Provider("RegPropProv")] 
   MyReservedTranslated;
};
```

 

 




