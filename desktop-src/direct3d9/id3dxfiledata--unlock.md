---
Description: Ends the lifespan of the ppData pointer returned by ID3DXFileData::Lock.
ms.assetid: 6032ea1f-3c73-4157-ba3f-41ce9e73d64c
title: ID3DXFileData::Unlock method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXFileData::Unlock method

Ends the lifespan of the *ppData* pointer returned by [**ID3DXFileData::Lock**](id3dxfiledata--lock.md).

## Syntax


```C++
BOOL Unlock();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The return value is S\_OK.

## Remarks

You must ensure that the number of [**ID3DXFileData::Lock**](id3dxfiledata--lock.md) calls matches the number of **ID3DXFileData::Unlock** calls. After calling Unlock, the ppData pointer returned by **ID3DXFileData::Lock** should no longer be used.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileData](id3dxfiledata.md)
</dt> </dl>

 

 




