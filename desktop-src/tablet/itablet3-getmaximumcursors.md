---
Description: The GetMaximumCursors method retrieves the maximum number of cursors that a tablet device supports.
ms.assetid: 5a43d792-e64c-4506-9792-31efe0885959
title: ITablet3GetMaximumCursors method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITablet3::GetMaximumCursors method

The **GetMaximumCursors** method retrieves the maximum number of cursors that a tablet device supports.

## Syntax


```C++
HRESULT GetMaximumCursors(
   ULONG *pMaximumCursors
);
```



## Parameters

<dl> <dt>

*pMaximumCursors* 
</dt> <dd>

The maximum number of inputs that the device supports.

</dd> </dl>

## Return value

Returns S\_OK on success; otherwise, returns an error code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITablet3**](itablet3.md)
</dt> </dl>

 

 




