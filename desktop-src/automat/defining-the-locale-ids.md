---
title: Defining the Locale IDs
description: Demonstrates how to use locale IDs.
ms.assetid: 3c0fc5fc-90d7-492f-ace4-0c1231bda125
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining the Locale IDs

Refer to the next section to obtain the language identifiers (LANGIDs) for the supported languages.


```C++
// Locale IDs for the languages that are supported.
#define LCID_ENGLISH MAKELCID(MAKELANGID(0x09, 0x01), SORT_DEFAULT)
#define LCID_GERMAN  MAKELCID(MAKELANGID(0x07, 0x01), SORT_DEFAULT)
```



Using the example code from the Hello sample, define member variables that can be used to contain U.S. English and German type information.


```C++
class CHello : public IHello
{
public:
   :

private:
   LPTYPEINFO m_ptinfoEnglish;  // English type information for application interface
   LPTYPEINFO m_ptinfoGerman;   // German type information for application interface
   :
};
 
```



 

 




