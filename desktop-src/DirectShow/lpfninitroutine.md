---
Description: Pointer to a function that gets called from the DLL entry point.
ms.assetid: 30196657-38ab-42ca-b673-b0894999e566
title: LPFNInitRoutine function pointer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LPFNInitRoutine function pointer

Pointer to a function that gets called from the DLL entry point.

## Syntax


```C++
typedef void ( CALLBACK *LPFNInitRoutine)(
         BOOL  bLoading,
   const CLSID *rclsid
);
```



## Parameters

<dl> <dt>

*bLoading* 
</dt> <dd>

**TRUE** when the DLL is loaded, **FALSE** when the DLL is unloaded.

</dd> <dt>

*rclsid* 
</dt> <dd>

Pointer to the object's CLISD, specified in the [**CFactoryTemplate::m\_ClsID**](cfactorytemplate-m-clsid.md) member variable.

</dd> </dl>

## Return value

This function pointer does not return a value.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Combase.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




