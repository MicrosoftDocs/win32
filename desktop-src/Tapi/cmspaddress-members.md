---
description: The following list contains the CMSP address members.
ms.assetid: ef15adef-1f4d-4bfc-8362-97fe1d118204
title: CMSPAddress Members
ms.topic: article
ms.date: 05/31/2018
---

# CMSPAddress Members



| Member types                    | Name                    | Description                                                                                      |
|---------------------------------|-------------------------|--------------------------------------------------------------------------------------------------|
| Iunknown                        | \*m\_pFTM               | Pointer to the free threaded marshaller.                                                         |
| HANDLE                          | m\_htEvent              | Handle to Tapi3.dll's event, which is used to notify TAPI that the MSP wants to send data to it. |
| LIST\_ENTRY                     | m\_EventList            | List of events.                                                                                  |
| CMSPCritSection                 | m\_EventDataLock        | The lock that protects the data related to event handling with TAPI.                             |
| ITTerminalManager               | \*m\_pITTerminalManager | The pointer to the Terminal Manager object.                                                      |
| CMSPArray <ITTerminal \*> | m\_Terminals            | The list of static terminals that can be used on the address.                                    |
| BOOL                            | m\_fTerminalsUpToDate   | This flag is **TRUE** if the terminal list is up to date.                                        |
| CMSPCritSection                 | m\_TerminalDataLock     | The lock that protects the terminal-related data members.                                        |



 

 

 



