---
title: RendezvousApplication object
description: RendezvousApplication object
ms.assetid: '306efb96-5193-410d-b2f8-e71453828a5e'
keywords: ["RendezvousApplication object Remote Assistance", "RendezvousApplication object Remote Assistance , described"]
topic_type:
- apiref
api_name:
- RendezvousApplication
api_location:
- RendezvousSession.tlb
api_type:
- COM
---

# RendezvousApplication object

## Members

The **RendezvousApplication** object has these types of members:

-   [Interfaces](#interfaces)
-   [Methods](#methods)

### Interfaces

The **RendezvousApplication** object defines these interfaces.



| Interface                                                             | Description                                                                                      |
|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**IRendezvousApplication**](remoteassist-irendezvousapplication.md) | Used by an instant messaging (IM) application to create a remote assistance session. <br/> |



 

### Methods

The **RendezvousApplication** object has these methods.



| Method                                                                                   | Description                                                                                                                                                                              |
|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetRendezvousSession**](remoteassist-irendezvousapplication-setrendezvoussession.md) | Passes [**IRendezvousSession**](remoteassist-irendezvoussession.md) to the Windows Remote Assistance application. This method is used by the instant messaging application. <br/> |



 

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                             |
| Header<br/>                   | <dl> <dt>RendezvousSession.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RendezvousSession.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RendezvousSession.tlb</dt> </dl> |
| IID<br/>                      | CLSID\_RendezvousApplication is defined as 0B7E019A-B5DE-47fa-8966-9082F82FB192<br/>       |



 

 





