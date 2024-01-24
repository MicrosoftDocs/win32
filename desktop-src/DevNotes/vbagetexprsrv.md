---
title: VBAGetExprSrv
description: Loads Visual Basic for Applications and retrieves a pointer to the IExpressionService object.
ms:assetid: ed23be8f-f18e-4098-84b8-81babd85d9d7
ms:mtpsurl: https://msdn.microsoft.com/en-US/library/Aa833132(v=VS.80)
ms.topic: reference
ms.date: 09/04/2009
topic_type: 
- APIRef
- kbSyntax
api_name: 
- VBAGetExprSrv
api_type: 
- DllExport
api_location: 
- vbajet32.dll
---


# VBAGetExprSrv

Loads Visual Basic for Applications and retrieves a pointer to the IExpressionService object.

```cpp
void VBAGetExprSrv(HINSTANCE FAR* lphinstVBA,
                    IExpressionService FAR* FAR* lplpexprsrv,
                    LPBYTE lpStackMin,
                    USHORT usMajVersionExprSrv,
                    USHORT usMinVersionExprSrv,
                    DWORD dwUnused1,
                    DWORD dwUnused2);
 ```

## Parameters

- lphinstVBA  
The location where the instance handle to Visual Basic for Applications is stored.

- lplpexprsrv  
The location where the expression service object pointer is to be stored.

- lpStackMin  
The minimum stack location that Visual Basic for Applications can go to.

- usMajVersionExprSrv  
Major version associated with the expression service DLL.

- usMinVersionExprSrv  
Minor version associated with the expression service DLL.

- dwUnused1  
This argument is reserved for future use.

- dwUnused2  
This argument is reserved for future use.

## Property Value/Return Value

None. Use lphinstVBA and lplpexprsrv to determine whether VBAGetExprSrv succeeded, as indicated in the Remarks section below.

## Remarks

This function is exported from vbajet32.dll.

VBAGetExprSrv calls LoadLibrary() to load the Visual Basic for Applications DLL based on the version numbers that are passed in. The handle returned by LoadLibrary() is stored in the location pointed to by lphinstVBA. If the call is successful, the caller must eventually call FreeLibrary() on this hinstance.

The expression service object pointer is undefined when lphinstVBA points to an invalid hinstance. The expression service object pointer is null if creating the expression service fails.

The value of lpStackMin does not affect the expression service. lpStackMin is required by the Visual Basic for Applications initialization code, and this value must be supplied by the caller.

## See Also

#### Other Resources

[VBA Language References](https://go.microsoft.com/fwlink/?linkid=71507)
