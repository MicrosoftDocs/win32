---
Description: A callback function used to notify the host of information about source files associated with the callstack.
MS-HAID: vspixengine.ISourceFileInfoCallback\_ResultCallback\_DWORD\_SourceFileInfo\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ISourceFileInfoCallback::ResultCallback method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.isourcefileinfocallback_resultcallback_dword_sourcefileinfo_arr"></span>ISourceFileInfoCallback::ResultCallback method

A callback function used to notify the host of information about source files associated with the callstack.

## Syntax


```C++
);
```

## Parameters

*count*   
The number of source files returned.

*count0\_sourceFileInfoBuffer*   
The source files.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ISourceFileInfoCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432802)

 

 



