---
description: Network Monitor loads a capture from the capture file, and then starts calling the Register function for all the protocols that it can identify. Each parser DLL must implement a Register function for each protocol that the parser DLL supports.
ms.assetid: a53c64cb-569f-454b-ae85-7b850228c954
title: Implementing Register
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Register

Network Monitor loads a capture from the capture file, and then starts calling the [**Register**](register-parser.md) function for all the protocols that it can identify. Each parser DLL must implement a **Register** function for each protocol that the parser DLL supports.

Each implementation of the [**Register**](register-parser.md) function must call the [**CreatePropertyDatabase**](createpropertydatabase.md) and [**AddProperty**](/previous-versions/bb251873(v=msdn.10)) functions to create and fill-in the [*property database*](p.md) for the protocol, and then the [**CreateHandoffTable**](createhandofftable.md) to create the [*handoff table*](h.md) for the protocol — if needed.

> [!Note]  
> Protocol properties are defined for Network Monitor. Properties are not mapped to a location in a capture data until the [**AttachProperties**](attachproperties.md) export function is called.

 

The following procedure identifies the steps necessary to implement the [**Register**](register-parser.md) function.

**To implement Register for one protocol**

1.  Define an array of [**PROPERTYINFO**](propertyinfo.md) structures to describe each property that the protocol supports.
2.  Call [**CreatePropertyDatabase**](createpropertydatabase.md) to provide a protocol handle, and the number of properties that the protocol supports.
3.  Call [**AddProperty**](/previous-versions/bb251873(v=msdn.10)) in a loop to add each property defined in the [**PROPERTYINFO**](propertyinfo.md) structure array.
4.  If the protocol uses a handoff table, call [**CreateHandoffTable**](createhandofftable.md)— after all the properties of the protocol are added to the property database.

The following is a basic implementation of [**Register**](register-parser.md). Note that a property database is created for a protocol that supports only two properties. This code example is taken from the generic parser that Network Monitor provides.

``` syntax
#include <windows.h>

PROPERTYINFO MyProtocolPropertyTable[]
{
  // Summary property (0)
  {
     0,                               // Handle to property.
     0,                               // Reserved.
     "Summary",                       // Property label.
     "Summary of protocol packet",    // Property comment.
     PROP_TYPE_SUMMARY,               // Data type of property.
     PROP_QUAL_NONE,                  // Data type qualifier.
     NULL,                            // Reserved.
     80,                              // 
     FormatPropertyInstance           // 
  }

  // WORD property (1)
  {
     0,                               // Handle to property.
     0,                               // Reserved.
     "WORD property",                 // Property label.
     "16-bit WORD property",         // Property comment.
     PROP_TYPE_WORD,                  // Data type of property.
     PROP_QUAL_NONE,                  // Data type qualifier.
     NULL,                            // Reserved.
     80,                              // 
     FormatPropertyInstance           // 
  }

}

void BHAPI MyProtocolRegister( HPPROTOCOL hProtocol) 
{
  // Create property database.
  DWORD dwNumberOfProperties = 2;
  CreatePropertyDatabase (hProtocol,
                          dwNumberOfProperties
                          );
  
  // Add properties to database.
  WORD i;
  for( i=0; i< dwNumberOfProperties; i++)
  {
     AddProperty(hProtocol, &MyProtocolPropertyTable[i]);
  }

  // Create handoff table.
  CreateHandoffTable("myProtocolHandoffTable",
                          "myProtocol.ini",
                           hTable,
                           MaxEntries,
                           10       // Handoff set values are base 10.
                          )
}
```

 

 
