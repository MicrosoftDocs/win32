---
description: A TAPI application must call an initialization operation, which prompts a series of actions from TAPI and the service providers that set up the communication environment for the application.
ms.assetid: 10df0fb4-08d6-4ba0-85f7-108cc4e237c1
title: Primary Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Primary Initialization

A TAPI application must call an initialization operation, which prompts a series of actions from TAPI and the service providers that set up the communication environment for the application.

-   Initialization is synchronous and does not return until the operation is complete or has failed.
-   If TAPISRV is not already running, TAPI starts it.
-   TAPI sets up a connection to the TAPISRV process.
-   TAPISVR loads the service providers specified in the registry and prompts them to initialize the devices they support.

**TAPI 2.x:** Applications perform initialization by calling [**lineInitializeEx**](/windows/win32/api/tapi/nf-tapi-lineinitializeexa).

**TAPI 3.x:** Applications call [**ITTAPI::Initialize**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-initialize).

 

 
