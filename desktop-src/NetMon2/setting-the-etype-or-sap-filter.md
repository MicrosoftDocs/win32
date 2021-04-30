---
description: Setting the Etype or SAP portion of the capture filter is the first step in the capture filter creation process.
ms.assetid: 0a22f74b-5bb1-43df-a70a-9f30195177ea
title: Setting the Etype or SAP Filter
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Etype or SAP Filter

Setting the Etype or SAP portion of the capture filter is the first step in the capture filter creation process.

In the following example, the capture filter is set to only retrieve IPX traffic:


```C++
BYTE Sap[]   = { 0x10, 0xE0 };
WORD Etype[] = { 0x8137 }; 

rc = SetNPPEtypeSapFilter(m_hBlob, 
     2,      //  nSaps,
     1,      //  nEtypes,
     &Sap,   //  LPBYTE lpSapTable,
     &Etype, //  LPWORD lpEtypeTable,
     0,      //  DWORD  FilterFlags,
     NULL
);
```



SAP and Etype values are usually available in RFCs. Both SAP and Etype values can be in an array.

 

 



