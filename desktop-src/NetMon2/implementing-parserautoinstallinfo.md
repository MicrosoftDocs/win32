---
description: Network Monitor uses the ParserAutoInstallInfo export function to install a parser. When ParserAutoInstallInfo is called, the parser returns a PF\_PARSERDLLINFO structure containing all the information that Network Monitor needs to install a parser DLL.
ms.assetid: 1add9988-9cb2-43f9-8ae2-32acfe21b6f3
title: Implementing ParserAutoInstallInfo
ms.topic: article
ms.date: 05/31/2018
---

# Implementing ParserAutoInstallInfo

Network Monitor uses the [**ParserAutoInstallInfo**](parserautoinstallinfo.md) export function to install a parser. When **ParserAutoInstallInfo** is called, the parser returns a [**PF\_PARSERDLLINFO**](pf-parserdllinfo.md) structure containing all the information that Network Monitor needs to install a parser DLL.

> [!Note]  
> Network Monitor keeps a list of existing parsers in the [*Parser.ini*](p.md) file, and creates a separate INI file for each installed parser.

 

During the installation process, the parser DLL must identify the following:

-   The number of parsers in the DLL—including a name and comment description for each parser.
-   The protocols that precede the parser protocol.
-   The protocols that follow the parser protocol.

> [!Note]  
> Network Monitor uses the preceding and following parser protocol information to update the [*handoff sets*](h.md) and [*follow sets*](f.md) of parsers that your parser DLL identifies.

 

The following procedure identifies the steps necessary to implement [**ParserAutoInstallInfo**](parserautoinstallinfo.md).

**To implement ParserAutoInstallInfo**

1.  Allocate a [**PF\_PARSERDLLINFO**](pf-parserdllinfo.md) structure using **HeapAlloc**.
2.  Return memory to the heap using **HeapFree**.
3.  Be aware that this call must also allocate a [**PF\_PARSERINFO**](pf-parserinfo.md) structure for each parser in the DLL.
4.  Specify the number of parsers (typically one) that the DLL contains in the **nParsers** member of [**PF\_PARSERDLLINFO**](pf-parserdllinfo.md).
5.  Specify a name, comment, and optional Help file in the **szProtocolName**, **szComment**, and **szHelpFile** members of each [**PF\_PARSERINFO**](pf-parserinfo.md) structure.
6.  Specify the protocols that precede each DLL protocol. One of the following conditions applies to an incoming handoff set.
    -   If the preceding protocols can determine that your protocol follows from data in the preceding protocols, set the **pWhoHandsOffToMe** member of [**PF\_PARSERINFO**](pf-parserinfo.md). In this case, your protocol is then added to the [*handoff sets*](h.md) of the preceding protocols.
    -   If the preceding protocols cannot determine that your protocol follows from data in the preceding protocols, set **pWhoCanPrecedeMe** member of [**PF\_PARSERINFO**](pf-parserinfo.md). In this case, the your protocol is then added to the [*follow sets*](f.md) of the protocols.
7.  Specify the protocols that follow each DLL protocol. One of the following conditions applies to an outgoing follow-set.
    -   If your protocol can determine which protocols follow based on data in your protocol, set the **pWhoDoIHandOffTo** member of [**PF\_PARSERINFO**](pf-parserinfo.md). In this case, the these protocols are added to the [*handoff set*](h.md) of your protocols.
    -   If your protocol cannot determine which protocols follow based on data in your protocol, set the **pWhoCanFollowMe** member of [**PF\_PARSERINFO**](pf-parserinfo.md). In this case, these protocols are added to the [*follow set*](f.md) of your protocol.
8.  Return the [**PF\_PARSERDLLINFO**](pf-parserdllinfo.md) structure to Network Monitor.

The following is a basic implementation of [**ParserAutoInstallInfo**](parserautoinstallinfo.md). The code example is taken from the generic parser that Network Monitor provides.

``` syntax
#include <windows.h>

PPF_PARSERDLLINFO WINAPI ParserAutoInstallInfo() 
{

  /////////////////////////////////////////////////////////////////
  //
  // Allocate memory for PF_PARSERDLLINFO structure.
  //
  /////////////////////////////////////////////////////////////////
  PPF_PARSERDLLINFO pParserDllInfo; 
  PPF_PARSERINFO    pParserInfo;
  DWORD NumProtocols;
        DWORD NumParsers;
        DWORD NumFollows;
  NumParsers = 1;
  
  pParserDllInfo = (PPF_PARSERDLLINFO)HeapAlloc( GetProcessHeap(),
                                                 HEAP_ZERO_MEMORY,
                                                 sizeof( PF_PARSERDLLINFO ) +
                                                 NumParsers * sizeof( PF_PARSERINFO) );
  if( pParserDllInfo == NULL)
  {
    return NULL;
  }
  

    
  /////////////////////////////////////////////////////////////////
  //
  // Specify the number of parsers in the DLL.
  //
  /////////////////////////////////////////////////////////////////
  
  pParserDllInfo->nParsers = NumParsers;
  

  /////////////////////////////////////////////////////////////////
  // 
  // Specify the name, comment, and Help file for each protocol.
  // 
  /////////////////////////////////////////////////////////////////
  pParserInfo = &(pParserDllInfo->ParserInfo[0]);
  sprintf_s( pParserInfo->szProtocolName, MAX_PROTOCOL_NAME_LEN, 
    "TestProtocol" );
  sprintf_s( pParserInfo->szComment, MAX_PROTOCOL_COMMENT_LEN,
    "Test protocol for SDK" );
  sprintf_s( pParserInfo->szHelpFile, MAX_PATH, "");
  

  
  /////////////////////////////////////////////////////////////////
  //
  // Specify preceding protocols.
  //
  /////////////////////////////////////////////////////////////////
  PPF_HANDOFFSET    pHandoffSet;
  PPF_HANDOFFENTRY  pHandoffEntry;
  
  // Allocate PF_HANDOFFSET structure.
  NumHandoffs = 1;                   
  pHandoffSet = (PPF_HANDOFFSET)HeapAlloc( GetProcessHeap(),
                                           HEAP_ZERO_MEMORY,
                                           sizeof( PF_HANDOFFSET ) +
                                           NumHandoffs * sizeof( PF_HANDOFFENTRY) );
  if( pHandoffSet == NULL )
  {
     return pParserDllInfo;
  }

  // Fill in handoff set
  pParserInfo->pWhoHandsOffToMe = pHandoffSet;
  pHandoffSet->nEntries = NumHandoffs;

  // TCP PORT FFFF
  pHandoffEntry = &(pHandoffSet->Entry[0]);
  sprintf_s( pHandoffEntry->szIniFile, MAX_PATH, "TCPIP.INI" );
  sprintf_s( pHandoffEntry->szIniSection, MAX_PATH, "TCP_HandoffSet" );
  sprintf_s( pHandoffEntry->szProtocol, MAX_PROTOCOL_NAME_LEN, 
    "BLRPLATE" );
  pHandoffEntry->dwHandOffValue =        0xFFFF;
  pHandoffEntry->ValueFormatBase =       HANDOFF_VALUE_FORMAT_BASE_DECIMAL;    
  
  

  /////////////////////////////////////////////////////////////////
  //
  // Specify the following protocols.
  //
  /////////////////////////////////////////////////////////////////
  PPF_FOLLOWSET     pFollowSet;
  PPF_FOLLOWENTRY   pFollowEntry;
 
  // Allocate PF_FOLLOWSET structure
  NumFollows = 1;
  pFollowSet = (PPF_FOLLOWSET)HeapAlloc( GetProcessHeap(),
                                         HEAP_ZERO_MEMORY,
                                         sizeof( PF_FOLLOWSET ) +
                                         NumFollows * sizeof( PF_FOLLOWENTRY) );
  if( pFollowSet == NULL )
  {
    return pParserDllInfo;
  }

  // Fill in the follow set
  pParserInfo->pWhoCanFollowMe = pFollowSet;
  pFollowSet->nEntries = NumFollows;

  // Add SMB
  pFollowEntry = &(pFollowSet->Entry[0]);
  sprintf_s( pFollowEntry->szProtocol, MAX_PROTOCOL_NAME_LEN, "SMB" );
  


  /////////////////////////////////////////////////////////////////
  //
  // Return the PF_PARSERDLLINFO structure.
  //
  /////////////////////////////////////////////////////////////////
  return pParserDllInfo;

}
```

 

 



