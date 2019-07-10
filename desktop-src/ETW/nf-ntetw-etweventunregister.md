---
UID: NF:ntw.EtwEventUnregister
title: EtwEventUnregister function
author: windows-sdk-content
description: Unregisters an event.
old-location: 
ms.assetid: na
ms.author: windowssdkdev
ms.date: 02/20/2018
ms.keywords: EtwEventUnregister
ms.topic: function
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
product: Windows
targetos: Windows
req.typenames: 
req.redist: 
---

# EtwEventUnregister function


## -description


The 
<b>EtwEventUnregister</b> unregisters an event.
			

Providers can only call this function from their 
<a href="https://docs.microsoft.com/windows/desktop/ETW/controlcallback">ControlCallback</a> function.


## -parameters




### -param RegHandle [in]

Handle to an event.


## -returns



Returns an HRESULT.





## -remarks



## -see-also



