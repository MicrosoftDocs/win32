---
Description: Removes the providers registration.
ms.assetid: e52c1ee0-140a-4277-bddd-d93338a512bc
title: CounterCleanup function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CounterCleanup function

Removes the provider's registration.

## Syntax


```C++
void WINAPI CounterCleanup(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

Your provider calls this function. The function calls the [**PerfStopProvider**](/windows/win32/Perflib/nf-perflib-perfstopprovider?branch=master) function to remove the provider's registration.

The [**CTRPP**](ctrpp.md) tool generates this inline function when you specify the **-o** argument. The function's name includes a *prefix* string if you specify the **-prefix** argument (for example, ***prefix*CounterCleanup**.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 




