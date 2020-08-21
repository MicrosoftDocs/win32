---
UID: NF:ntw.EtwEventUnregister
title: EtwEventUnregister function
description: Unregisters an event.
old-location: 
ms.assetid: na
ms.date: 02/20/2018
ms.keywords: EtwEventUnregister
ms.topic: reference
req.header: ntetw.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1803 [desktop apps \| UWP apps]
req.target-min-winversvr: Windows 10, version 1803 [desktop apps \| UWP apps]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- ntetw.h
api_name:
- EtwEventUnregister
targetos: Windows
req.typenames: 
req.redist: 
---

# EtwEventUnregister function


## Description


The 
<b>EtwEventUnregister</b> unregisters an event.
			

Providers can only call this function from their 
<a href="/windows/desktop/ETW/controlcallback">ControlCallback</a> function.


## Parameters




### RegHandle [in]

Handle to an event.


## Returns



Returns an HRESULT.





## Remarks



## See also